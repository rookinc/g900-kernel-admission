#!/usr/bin/env python3
import csv
import hashlib
import json
import re
from collections import Counter, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGE_FILE = ROOT / "source/kernel_payload/x_sigma_edges.csv"

OUT_JSON = ROOT / "artifacts/json/metric_certificate.json"
OUT_MD = ROOT / "certificates/004_diameter_radius.md"

INT_RE = re.compile(r"-?\d+")
N = 900

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

def parse_edge_to_ids(row):
    xs = ints_from_row(row)

    if len(xs) >= 4:
        a_slot, a_local, b_slot, b_local = xs[:4]
        if 0 <= a_slot < 15 and 0 <= b_slot < 15 and 0 <= a_local < 60 and 0 <= b_local < 60:
            a = a_slot * 60 + a_local
            b = b_slot * 60 + b_local
            return tuple(sorted((a, b)))

    if len(xs) >= 2:
        a, b = xs[:2]
        if 0 <= a < N and 0 <= b < N:
            return tuple(sorted((a, b)))

    raise ValueError("could not parse edge row: " + str(row))

def sha_edge_ids(edges):
    text = "\n".join(f"{a},{b}" for a, b in sorted(edges)) + "\n"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def bfs(source, adjacency):
    dist = [-1] * N
    dist[source] = 0
    q = deque([source])

    while q:
        v = q.popleft()
        nd = dist[v] + 1
        for w in adjacency[v]:
            if dist[w] == -1:
                dist[w] = nd
                q.append(w)

    return dist

def main():
    edges = set()
    for row in read_rows(EDGE_FILE):
        a, b = parse_edge_to_ids(row)
        if a == b:
            raise ValueError("loop edge found")
        edges.add((a, b))

    adjacency = [[] for _ in range(N)]
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)

    for v in range(N):
        adjacency[v].sort()

    eccentricities = []
    all_reached = True
    distance_distribution = Counter()
    diameter = -1
    radius = None
    diameter_witnesses = []
    first_diameter_witness = None

    print("running all-source BFS over 900 vertices")
    for s in range(N):
        if s % 100 == 0:
            print("progress source=" + str(s))

        dist = bfs(s, adjacency)

        if any(d < 0 for d in dist):
            all_reached = False

        ecc = max(dist)
        eccentricities.append(ecc)

        if radius is None or ecc < radius:
            radius = ecc

        if ecc > diameter:
            diameter = ecc
            diameter_witnesses = []
            first_diameter_witness = None

        if ecc == diameter:
            farthest = [i for i, d in enumerate(dist) if d == ecc]
            if farthest:
                pair = [s, farthest[0]]
                diameter_witnesses.append(pair)
                if first_diameter_witness is None:
                    first_diameter_witness = pair

        for t in range(s + 1, N):
            distance_distribution[dist[t]] += 1

    center_vertices = [i for i, ecc in enumerate(eccentricities) if ecc == radius]
    diameter_vertices = [i for i, ecc in enumerate(eccentricities) if ecc == diameter]
    eccentricity_counts = Counter(eccentricities)

    distance_distribution_json = {
        str(k): distance_distribution[k]
        for k in sorted(distance_distribution)
    }

    eccentricity_counts_json = {
        str(k): eccentricity_counts[k]
        for k in sorted(eccentricity_counts)
    }

    checks = {
        "edge_count_is_3600": len(edges) == 3600,
        "all_vertices_reached_from_every_source": all_reached,
        "diameter_is_8": diameter == 8,
        "radius_is_6": radius == 6,
        "has_center_vertex": len(center_vertices) > 0,
        "has_diameter_witness": first_diameter_witness is not None,
        "no_eccentricity_below_radius": min(eccentricities) == radius,
        "distance_distribution_pair_count_ok": sum(distance_distribution.values()) == (N * (N - 1)) // 2
    }

    verification_ok = all(checks.values())

    cert = {
        "certificate": "diameter_radius_metric_certificate",
        "verification_ok": verification_ok,
        "claim": "X_sigma has diameter 8 and radius 6.",
        "method": "All-source BFS over source/kernel_payload/x_sigma_edges.csv",
        "source_edge_file": str(EDGE_FILE.relative_to(ROOT)),
        "vertex_count": N,
        "edge_count": len(edges),
        "diameter": diameter,
        "radius": radius,
        "center_count": len(center_vertices),
        "center_vertices": center_vertices,
        "diameter_vertex_count": len(diameter_vertices),
        "diameter_vertices": diameter_vertices,
        "first_diameter_witness_pair": first_diameter_witness,
        "sample_diameter_witness_pairs": diameter_witnesses[:20],
        "eccentricity_counts": eccentricity_counts_json,
        "distance_distribution": distance_distribution_json,
        "checks": checks,
        "hashes": {
            "source_edge_id_set_sha256": sha_edge_ids(edges)
        },
        "eccentricity_table": [
            {
                "vertex": v,
                "slot": v // 60,
                "local": v % 60,
                "eccentricity": eccentricities[v]
            }
            for v in range(N)
        ],
        "boundary": [
            "This certificate proves diameter and radius from the finite internal edge payload.",
            "It also rechecks connected reachability from every source.",
            "It does not prove uniqueness, census identity, sibling non-switching, or physical interpretation.",
            "It does not use renderer output or Project 17 at runtime."
        ]
    }

    OUT_JSON.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")

    lines = []
    lines.append("# Diameter and radius certificate")
    lines.append("")
    lines.append("- verification_ok: " + str(verification_ok))
    lines.append("- claim: X_sigma has diameter 8 and radius 6.")
    lines.append("- method: all-source BFS over source/kernel_payload/x_sigma_edges.csv")
    lines.append("")
    lines.append("## Metric result")
    lines.append("")
    lines.append("- vertex_count: " + str(N))
    lines.append("- edge_count: " + str(len(edges)))
    lines.append("- diameter: " + str(diameter))
    lines.append("- radius: " + str(radius))
    lines.append("- center_count: " + str(len(center_vertices)))
    lines.append("- first_center_vertex: " + str(center_vertices[0] if center_vertices else None))
    lines.append("- diameter_vertex_count: " + str(len(diameter_vertices)))
    lines.append("- first_diameter_witness_pair: " + str(first_diameter_witness))
    lines.append("")
    lines.append("## Eccentricity counts")
    lines.append("")
    for k, v in eccentricity_counts_json.items():
        lines.append("- eccentricity_" + k + ": " + str(v))
    lines.append("")
    lines.append("## Distance distribution")
    lines.append("")
    for k, v in distance_distribution_json.items():
        lines.append("- distance_" + k + ": " + str(v))
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    for k, v in checks.items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")
    lines.append("## Hashes")
    lines.append("")
    lines.append("- source_edge_id_set_sha256: " + cert["hashes"]["source_edge_id_set_sha256"])
    lines.append("")
    lines.append("## Boundary")
    lines.append("")
    for b in cert["boundary"]:
        lines.append("- " + b)
    lines.append("")

    OUT_MD.write_text("\n".join(lines))

    print("metric_certificate_ok=" + str(verification_ok))
    print("vertex_count=" + str(N))
    print("edge_count=" + str(len(edges)))
    print("diameter=" + str(diameter))
    print("radius=" + str(radius))
    print("center_count=" + str(len(center_vertices)))
    print("first_center_vertex=" + str(center_vertices[0] if center_vertices else None))
    print("first_diameter_witness_pair=" + str(first_diameter_witness))
    print("eccentricity_counts=" + json.dumps(eccentricity_counts_json, sort_keys=True))
    print("distance_distribution=" + json.dumps(distance_distribution_json, sort_keys=True))
    print("wrote", OUT_JSON)
    print("wrote", OUT_MD)

    if not verification_ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
