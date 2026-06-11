#!/usr/bin/env python3
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAYLOAD = ROOT / "source/kernel_payload"

G15 = PAYLOAD / "g15_slot_edges.csv"
G60 = PAYLOAD / "g60_local_edges.csv"
CARRIER = PAYLOAD / "carrier_signing_table.csv"
RECORDED = PAYLOAD / "x_sigma_edges.csv"

OUT_JSON = ROOT / "artifacts/json/exact_edge_set_identity_certificate.json"
OUT_MD = ROOT / "certificates/002_exact_edge_set_identity.md"

INT_RE = re.compile(r"-?\d+")

def read_rows(path):
    with path.open(newline="") as f:
        return list(csv.DictReader(f))

def ints_from_row(row):
    vals = []
    for v in row.values():
        if v is None:
            continue
        for m in INT_RE.findall(str(v)):
            vals.append(int(m))
    return vals

def first_two_ints(row, path):
    xs = ints_from_row(row)
    if len(xs) < 2:
        raise ValueError("could not parse two integers from " + str(path) + ": " + str(row))
    return xs[0], xs[1]

def read_simple_edges(path):
    edges = set()
    for row in read_rows(path):
        a, b = first_two_ints(row, path)
        if a == b:
            raise ValueError("loop edge in " + str(path) + ": " + str(row))
        edges.add(tuple(sorted((a, b))))
    return edges

def read_carrier_rows(path):
    rows = []
    for row in read_rows(path):
        lower = {k.lower(): v for k, v in row.items()}
        sign = None
        for key, val in lower.items():
            if "sign" in key:
                sign = int(INT_RE.findall(str(val))[0])
                break

        xs = ints_from_row(row)
        if len(xs) < 3 and sign is None:
            raise ValueError("could not parse carrier row: " + str(row))

        a, b = xs[0], xs[1]
        if sign is None:
            sign = xs[2]

        if sign not in (0, 1):
            raise ValueError("carrier sign must be 0 or 1: " + str(row))

        rows.append((min(a, b), max(a, b), sign))
    return rows

def normalize_edge(v1, v2):
    return tuple(sorted((tuple(v1), tuple(v2))))

def edge_to_row(edge):
    a, b = edge
    return {
        "slot_a": a[0],
        "local_a": a[1],
        "slot_b": b[0],
        "local_b": b[1],
    }

def parse_recorded_edge(row):
    keys = {k.lower(): k for k in row.keys()}

    four_key_sets = [
        ("slot_a", "local_a", "slot_b", "local_b"),
        ("slot_u", "local_u", "slot_v", "local_v"),
        ("a_slot", "a_local", "b_slot", "b_local"),
        ("u_slot", "u_local", "v_slot", "v_local"),
        ("t1", "x1", "t2", "x2"),
        ("t_a", "x_a", "t_b", "x_b"),
    ]

    for wanted in four_key_sets:
        if all(k in keys for k in wanted):
            vals = [int(row[keys[k]]) for k in wanted]
            return normalize_edge((vals[0], vals[1]), (vals[2], vals[3]))

    xs = ints_from_row(row)

    if len(xs) >= 4:
        vals = xs[:4]
        if 0 <= vals[0] < 15 and 0 <= vals[2] < 15 and 0 <= vals[1] < 60 and 0 <= vals[3] < 60:
            return normalize_edge((vals[0], vals[1]), (vals[2], vals[3]))

    if len(xs) >= 2:
        a, b = xs[0], xs[1]
        if 0 <= a < 900 and 0 <= b < 900:
            return normalize_edge((a // 60, a % 60), (b // 60, b % 60))

    raise ValueError("could not parse recorded edge row: " + str(row))

def read_recorded_edges(path):
    edges = set()
    for row in read_rows(path):
        edges.add(parse_recorded_edge(row))
    return edges

def sha_edges(edges):
    lines = []
    for edge in sorted(edges):
        a, b = edge
        lines.append(f"{a[0]},{a[1]},{b[0]},{b[1]}")
    text = "\n".join(lines) + "\n"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def main():
    g15_edges = read_simple_edges(G15)
    g60_edges = read_simple_edges(G60)
    carrier_rows = read_carrier_rows(CARRIER)
    recorded_edges = read_recorded_edges(RECORDED)

    generated = set()

    for t in range(15):
        for x, y in g60_edges:
            generated.add(normalize_edge((t, x), (t, y)))

    for t, u, sign in carrier_rows:
        for x in range(60):
            y = x if sign == 0 else (x + 30) % 60
            generated.add(normalize_edge((t, x), (u, y)))

    missing_from_generated = sorted(recorded_edges - generated)
    extra_in_generated = sorted(generated - recorded_edges)

    ok = (
        len(g15_edges) == 30 and
        len(g60_edges) == 120 and
        len(carrier_rows) == 30 and
        len(generated) == 3600 and
        len(recorded_edges) == 3600 and
        not missing_from_generated and
        not extra_in_generated
    )

    cert = {
        "certificate": "exact_edge_set_identity",
        "verification_ok": ok,
        "claim": "Gen(K_900) equals the recorded canonical X_sigma edge set.",
        "source_files": {
            "g15_slot_edges": str(G15.relative_to(ROOT)),
            "g60_local_edges": str(G60.relative_to(ROOT)),
            "carrier_signing_table": str(CARRIER.relative_to(ROOT)),
            "recorded_x_sigma_edges": str(RECORDED.relative_to(ROOT)),
        },
        "counts": {
            "g15_slot_edges": len(g15_edges),
            "g60_local_edges": len(g60_edges),
            "carrier_rows": len(carrier_rows),
            "generated_edges": len(generated),
            "recorded_edges": len(recorded_edges),
            "missing_from_generated": len(missing_from_generated),
            "extra_in_generated": len(extra_in_generated),
        },
        "hashes": {
            "generated_edge_set_sha256": sha_edges(generated),
            "recorded_edge_set_sha256": sha_edges(recorded_edges),
        },
        "boundary": [
            "This certificate proves edge-set equality from the finite kernel payload.",
            "It does not prove connectedness, diameter, radius, or uniqueness.",
            "It does not use renderer output, visual geometry, census identity, or physical interpretation."
        ],
    }

    OUT_JSON.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")

    lines = []
    lines.append("# Exact edge-set identity certificate")
    lines.append("")
    lines.append("- verification_ok: " + str(ok))
    lines.append("- claim: Gen(K_900) equals the recorded canonical X_sigma edge set.")
    lines.append("")
    lines.append("## Counts")
    lines.append("")
    for k, v in cert["counts"].items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")
    lines.append("## Hashes")
    lines.append("")
    for k, v in cert["hashes"].items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")
    lines.append("## Boundary")
    lines.append("")
    for b in cert["boundary"]:
        lines.append("- " + b)
    lines.append("")

    OUT_MD.write_text("\n".join(lines))

    print("exact_edge_set_identity_ok=" + str(ok))
    print("generated_edges=" + str(len(generated)))
    print("recorded_edges=" + str(len(recorded_edges)))
    print("missing_from_generated=" + str(len(missing_from_generated)))
    print("extra_in_generated=" + str(len(extra_in_generated)))
    print("generated_edge_set_sha256=" + cert["hashes"]["generated_edge_set_sha256"])
    print("recorded_edge_set_sha256=" + cert["hashes"]["recorded_edge_set_sha256"])
    print("wrote", OUT_JSON)
    print("wrote", OUT_MD)

    if not ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
