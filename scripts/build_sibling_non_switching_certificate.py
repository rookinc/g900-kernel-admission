#!/usr/bin/env python3
import csv
import json
import re
from collections import Counter, defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAYLOAD = ROOT / "source/kernel_payload"

G15 = PAYLOAD / "g15_slot_edges.csv"
CARRIER = PAYLOAD / "carrier_signing_table.csv"

OUT_DELTA = PAYLOAD / "sibling_signing_delta.csv"
OUT_SIBLING = PAYLOAD / "sibling_candidate_signing_table.csv"
OUT_JSON = ROOT / "artifacts/json/sibling_non_switching_certificate.json"
OUT_MD = ROOT / "certificates/006_sibling_non_switching.md"

INT_RE = re.compile(r"-?\d+")

SUPPORT_TRIANGLES = [
    [5, 10, 14],
    [9, 11, 12],
]

SUPPORT_EDGES = [
    (5, 10),
    (5, 14),
    (10, 14),
    (9, 11),
    (9, 12),
    (11, 12),
]

def edge(a, b):
    return tuple(sorted((int(a), int(b))))

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

def read_g15_edges(path):
    edges = set()
    for row in read_rows(path):
        a, b = first_two_ints(row, path)
        if a == b:
            raise ValueError("loop edge in " + str(path) + ": " + str(row))
        edges.add(edge(a, b))
    return edges

def read_carrier_signs(path):
    signs = {}
    for row in read_rows(path):
        lower = {str(k).lower(): v for k, v in row.items()}
        xs = ints_from_row(row)

        sign = None
        for k, v in lower.items():
            if "sign" in k:
                found = INT_RE.findall(str(v))
                if found:
                    sign = int(found[0])
                    break

        if len(xs) < 2:
            raise ValueError("could not parse carrier edge: " + str(row))

        a, b = xs[0], xs[1]

        if sign is None:
            if len(xs) < 3:
                raise ValueError("could not parse carrier sign: " + str(row))
            sign = xs[2]

        if sign not in (0, 1):
            raise ValueError("carrier sign must be 0 or 1: " + str(row))

        signs[edge(a, b)] = sign

    return signs

def gf2_rank(matrix, ncols):
    rows = [r[:] for r in matrix]
    rank = 0

    for col in range(ncols):
        pivot = None
        for i in range(rank, len(rows)):
            if rows[i][col] & 1:
                pivot = i
                break

        if pivot is None:
            continue

        rows[rank], rows[pivot] = rows[pivot], rows[rank]

        for i in range(len(rows)):
            if i != rank and (rows[i][col] & 1):
                rows[i] = [(a ^ b) for a, b in zip(rows[i], rows[rank])]

        rank += 1

    return rank

def switching_solvable(g15_edges, delta_map):
    coeff = []
    aug = []

    for a, b in sorted(g15_edges):
        rhs = delta_map.get(edge(a, b), 0)
        row = [0] * 15
        row[a] = 1
        row[b] = 1
        coeff.append(row)
        aug.append(row + [rhs])

    rank_coeff = gf2_rank(coeff, 15)
    rank_aug = gf2_rank(aug, 16)

    return {
        "solvable": rank_coeff == rank_aug,
        "rank_coeff": rank_coeff,
        "rank_augmented": rank_aug
    }

def assignment_contradiction(g15_edges, delta_map):
    adj = defaultdict(list)
    for a, b in g15_edges:
        d = delta_map.get(edge(a, b), 0)
        adj[a].append((b, d))
        adj[b].append((a, d))

    value = {}
    contradictions = []

    for start in range(15):
        if start in value:
            continue
        value[start] = 0
        q = deque([start])

        while q:
            v = q.popleft()
            for w, d in adj[v]:
                expected = value[v] ^ d
                if w not in value:
                    value[w] = expected
                    q.append(w)
                elif value[w] != expected:
                    contradictions.append({
                        "edge": [v, w],
                        "delta": d,
                        "value_v": value[v],
                        "value_w": value[w],
                        "expected_value_w": expected
                    })

    return value, contradictions

def support_components(support_edges):
    adj = defaultdict(list)
    vertices = set()
    for a, b in support_edges:
        vertices.add(a)
        vertices.add(b)
        adj[a].append(b)
        adj[b].append(a)

    seen = set()
    comps = []

    for start in sorted(vertices):
        if start in seen:
            continue
        q = deque([start])
        seen.add(start)
        comp = []
        while q:
            v = q.popleft()
            comp.append(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    q.append(w)
        comps.append(sorted(comp))

    degree_counts = Counter(len(adj[v]) for v in vertices)
    cycle_rank = len(support_edges) - len(vertices) + len(comps)

    return {
        "vertices": sorted(vertices),
        "components": comps,
        "component_count": len(comps),
        "component_sizes": [len(c) for c in comps],
        "degree_counts": {str(k): degree_counts[k] for k in sorted(degree_counts)},
        "cycle_rank": cycle_rank
    }

def triangle_edges(tri):
    a, b, c = tri
    return [edge(a, b), edge(a, c), edge(b, c)]

def main():
    g15_edges = read_g15_edges(G15)
    canonical_signs = read_carrier_signs(CARRIER)

    support_edges = [edge(a, b) for a, b in SUPPORT_EDGES]
    delta_map = {e: 1 for e in support_edges}

    support_edges_exist = all(e in g15_edges for e in support_edges)
    canonical_edges_match_g15 = set(canonical_signs.keys()) == set(g15_edges)

    sibling_signs = {}
    for e in sorted(g15_edges):
        sibling_signs[e] = canonical_signs[e] ^ delta_map.get(e, 0)

    linear = switching_solvable(g15_edges, delta_map)
    assignment, contradictions = assignment_contradiction(g15_edges, delta_map)
    support = support_components(support_edges)

    triangle_checks = []
    for tri in SUPPORT_TRIANGLES:
        tes = triangle_edges(tri)
        exists = all(e in g15_edges for e in tes)
        parity = sum(delta_map.get(e, 0) for e in tes) % 2
        triangle_checks.append({
            "triangle": tri,
            "edges": [[a, b] for a, b in tes],
            "all_edges_exist": exists,
            "delta_parity": parity,
            "odd_delta_parity": parity == 1
        })

    with OUT_DELTA.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["slot_a", "slot_b", "delta", "support_role"])
        writer.writeheader()
        for e in sorted(g15_edges):
            writer.writerow({
                "slot_a": e[0],
                "slot_b": e[1],
                "delta": delta_map.get(e, 0),
                "support_role": "sibling_delta_support" if e in delta_map else "unchanged"
            })

    with OUT_SIBLING.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["slot_a", "slot_b", "canonical_sign", "delta", "sibling_sign"]
        )
        writer.writeheader()
        for e in sorted(g15_edges):
            writer.writerow({
                "slot_a": e[0],
                "slot_b": e[1],
                "canonical_sign": canonical_signs[e],
                "delta": delta_map.get(e, 0),
                "sibling_sign": sibling_signs[e]
            })

    canonical_sign_counts = Counter(canonical_signs.values())
    sibling_sign_counts = Counter(sibling_signs.values())
    delta_counts = Counter(delta_map.get(e, 0) for e in g15_edges)

    checks = {
        "g15_edge_count_is_30": len(g15_edges) == 30,
        "canonical_signing_has_30_edges": len(canonical_signs) == 30,
        "canonical_edges_match_g15": canonical_edges_match_g15,
        "support_edge_count_is_6": len(support_edges) == 6,
        "support_edges_exist_in_g15": support_edges_exist,
        "support_component_count_is_2": support["component_count"] == 2,
        "support_component_sizes_are_3_3": support["component_sizes"] == [3, 3],
        "support_cycle_rank_is_2": support["cycle_rank"] == 2,
        "each_support_triangle_has_odd_delta_parity": all(t["odd_delta_parity"] for t in triangle_checks),
        "gf2_system_unsolvable": linear["solvable"] is False,
        "rank_augmented_exceeds_rank_coeff": linear["rank_augmented"] > linear["rank_coeff"],
        "assignment_has_contradiction": len(contradictions) > 0
    }

    verification_ok = all(checks.values())

    cert = {
        "certificate": "sibling_non_switching",
        "verification_ok": verification_ok,
        "claim": "The sibling signing delta is not a switching coboundary over the G15 slot graph.",
        "interpretation": "The sibling signing is not switching-equivalent to the canonical signing.",
        "method": "Solve the F2 switching equation g_u + g_v = delta_uv over the G15 edge set and verify inconsistency.",
        "source_files": {
            "g15_slot_edges": str(G15.relative_to(ROOT)),
            "canonical_carrier_signing": str(CARRIER.relative_to(ROOT)),
            "sibling_delta": str(OUT_DELTA.relative_to(ROOT)),
            "sibling_candidate_signing": str(OUT_SIBLING.relative_to(ROOT))
        },
        "support": {
            "support_edges": [[a, b] for a, b in sorted(support_edges)],
            "support_triangles": SUPPORT_TRIANGLES,
            "support_graph": support,
            "triangle_checks": triangle_checks
        },
        "linear_obstruction": linear,
        "assignment_contradictions_sample": contradictions[:10],
        "counts": {
            "g15_edges": len(g15_edges),
            "canonical_sign_0": canonical_sign_counts.get(0, 0),
            "canonical_sign_1": canonical_sign_counts.get(1, 0),
            "sibling_sign_0": sibling_sign_counts.get(0, 0),
            "sibling_sign_1": sibling_sign_counts.get(1, 0),
            "delta_0": delta_counts.get(0, 0),
            "delta_1": delta_counts.get(1, 0)
        },
        "checks": checks,
        "boundary": [
            "This certificate proves non-switching-equivalence of the sibling signing delta.",
            "It does not prove the sibling candidate is invalid.",
            "It does not prove full graph separation by exact graph invariant.",
            "It does not prove uniqueness among all possible signed carriers.",
            "It does not use renderer output, census identity, physical interpretation, or Project 17 at runtime."
        ]
    }

    OUT_JSON.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")

    lines = []
    lines.append("# Sibling non-switching certificate")
    lines.append("")
    lines.append("- verification_ok: " + str(verification_ok))
    lines.append("- claim: the sibling signing delta is not a switching coboundary over G15.")
    lines.append("- interpretation: the sibling signing is not switching-equivalent to the canonical signing.")
    lines.append("")
    lines.append("## Support")
    lines.append("")
    lines.append("- support_edges: " + str([[a, b] for a, b in sorted(support_edges)]))
    lines.append("- support_triangles: " + str(SUPPORT_TRIANGLES))
    lines.append("- support_component_count: " + str(support["component_count"]))
    lines.append("- support_component_sizes: " + str(support["component_sizes"]))
    lines.append("- support_cycle_rank: " + str(support["cycle_rank"]))
    lines.append("")
    lines.append("## F2 obstruction")
    lines.append("")
    lines.append("- switching_equation_solvable: " + str(linear["solvable"]))
    lines.append("- rank_coeff: " + str(linear["rank_coeff"]))
    lines.append("- rank_augmented: " + str(linear["rank_augmented"]))
    lines.append("- contradiction_count: " + str(len(contradictions)))
    lines.append("")
    lines.append("## Counts")
    lines.append("")
    for k, v in cert["counts"].items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")
    lines.append("## Triangle checks")
    lines.append("")
    for t in triangle_checks:
        lines.append("- triangle " + str(t["triangle"]) + ": odd_delta_parity=" + str(t["odd_delta_parity"]))
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    for k, v in checks.items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")
    lines.append("## Boundary")
    lines.append("")
    for b in cert["boundary"]:
        lines.append("- " + b)
    lines.append("")

    OUT_MD.write_text("\n".join(lines))

    print("sibling_non_switching_ok=" + str(verification_ok))
    print("support_edges=" + str([[a, b] for a, b in sorted(support_edges)]))
    print("support_component_count=" + str(support["component_count"]))
    print("support_component_sizes=" + str(support["component_sizes"]))
    print("support_cycle_rank=" + str(support["cycle_rank"]))
    print("switching_equation_solvable=" + str(linear["solvable"]))
    print("rank_coeff=" + str(linear["rank_coeff"]))
    print("rank_augmented=" + str(linear["rank_augmented"]))
    print("contradiction_count=" + str(len(contradictions)))
    print("wrote", OUT_DELTA)
    print("wrote", OUT_SIBLING)
    print("wrote", OUT_JSON)
    print("wrote", OUT_MD)

    if not verification_ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
