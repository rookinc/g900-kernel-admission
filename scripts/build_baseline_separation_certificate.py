#!/usr/bin/env python3
import csv
import hashlib
import json
import re
from collections import Counter, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAYLOAD = ROOT / "source/kernel_payload"

G15 = PAYLOAD / "g15_slot_edges.csv"
G60 = PAYLOAD / "g60_local_edges.csv"
X_METRIC = ROOT / "artifacts/json/metric_certificate.json"

OUT_JSON = ROOT / "artifacts/json/baseline_separation_certificate.json"
OUT_MD = ROOT / "certificates/005_baseline_separation.md"

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

def vid(slot, local):
    return slot * 60 + local

def edge_id_pair(a, b):
    return tuple(sorted((a, b)))

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

def all_source_metrics(edges):
    adjacency = [[] for _ in range(N)]
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)

    for v in range(N):
        adjacency[v].sort()

    all_reached = True
    eccentricities = []
    distance_distribution = Counter()
    diameter = -1
    radius = None
    first_diameter_witness = None

    print("running all-source BFS over baseline 900 vertices")
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
            farthest = [i for i, d in enumerate(dist) if d == ecc]
            first_diameter_witness = [s, farthest[0]] if farthest else None

        for t in range(s + 1, N):
            distance_distribution[dist[t]] += 1

    center_vertices = [i for i, ecc in enumerate(eccentricities) if ecc == radius]
    diameter_vertices = [i for i, ecc in enumerate(eccentricities) if ecc == diameter]
    eccentricity_counts = Counter(eccentricities)

    return {
        "all_reached": all_reached,
        "diameter": diameter,
        "radius": radius,
        "center_vertices": center_vertices,
        "diameter_vertices": diameter_vertices,
        "first_diameter_witness_pair": first_diameter_witness,
        "eccentricity_counts": {str(k): eccentricity_counts[k] for k in sorted(eccentricity_counts)},
        "distance_distribution": {str(k): distance_distribution[k] for k in sorted(distance_distribution)},
        "distance_pair_count": sum(distance_distribution.values())
    }

def main():
    g15_edges = read_simple_edges(G15)
    g60_edges = read_simple_edges(G60)

    baseline_edges = set()

    # Internal fiber edges: 15 copies of G60.
    for t in range(15):
        for x, y in g60_edges:
            baseline_edges.add(edge_id_pair(vid(t, x), vid(t, y)))

    # Untwisted product carrier edges: identity transport across each G15 edge.
    for t, u in g15_edges:
        for x in range(60):
            baseline_edges.add(edge_id_pair(vid(t, x), vid(u, x)))

    metrics = all_source_metrics(baseline_edges)

    if not X_METRIC.exists():
        raise FileNotFoundError("missing X_sigma metric certificate: " + str(X_METRIC))

    x_metric = json.loads(X_METRIC.read_text())
    x_diameter = x_metric.get("diameter")
    x_radius = x_metric.get("radius")

    baseline_diameter = metrics["diameter"]
    baseline_radius = metrics["radius"]

    checks = {
        "g15_edge_count_is_30": len(g15_edges) == 30,
        "g60_edge_count_is_120": len(g60_edges) == 120,
        "baseline_edge_count_is_3600": len(baseline_edges) == 3600,
        "baseline_connected": metrics["all_reached"] is True,
        "baseline_diameter_is_9": baseline_diameter == 9,
        "baseline_radius_is_9": baseline_radius == 9,
        "x_sigma_diameter_is_8": x_diameter == 8,
        "x_sigma_radius_is_6": x_radius == 6,
        "diameter_separates": baseline_diameter != x_diameter,
        "radius_separates": baseline_radius != x_radius,
        "distance_distribution_pair_count_ok": metrics["distance_pair_count"] == (N * (N - 1)) // 2
    }

    verification_ok = all(checks.values())

    cert = {
        "certificate": "baseline_separation",
        "verification_ok": verification_ok,
        "claim": "The canonical X_sigma graph is separated from the untwisted product baseline by exact metric invariants.",
        "method": "Build untwisted baseline from G15 and G60 with identity carriers, then compare exact diameter and radius against X_sigma metric certificate.",
        "source_files": {
            "g15_slot_edges": str(G15.relative_to(ROOT)),
            "g60_local_edges": str(G60.relative_to(ROOT)),
            "x_sigma_metric_certificate": str(X_METRIC.relative_to(ROOT))
        },
        "counts": {
            "vertex_count": N,
            "g15_slot_edges": len(g15_edges),
            "g60_local_edges": len(g60_edges),
            "baseline_edges": len(baseline_edges)
        },
        "x_sigma": {
            "diameter": x_diameter,
            "radius": x_radius
        },
        "untwisted_baseline": {
            "diameter": baseline_diameter,
            "radius": baseline_radius,
            "center_count": len(metrics["center_vertices"]),
            "first_center_vertex": metrics["center_vertices"][0] if metrics["center_vertices"] else None,
            "diameter_vertex_count": len(metrics["diameter_vertices"]),
            "first_diameter_witness_pair": metrics["first_diameter_witness_pair"],
            "eccentricity_counts": metrics["eccentricity_counts"],
            "distance_distribution": metrics["distance_distribution"]
        },
        "checks": checks,
        "hashes": {
            "baseline_edge_id_set_sha256": sha_edge_ids(baseline_edges)
        },
        "boundary": [
            "This certificate proves separation from the untwisted product baseline by exact metric invariants.",
            "It does not prove uniqueness among all possible signed carriers.",
            "It does not prove sibling non-switching or sibling full-graph separation.",
            "It does not use renderer output, census identity, physical interpretation, or Project 17 at runtime."
        ]
    }

    OUT_JSON.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")

    lines = []
    lines.append("# Baseline separation certificate")
    lines.append("")
    lines.append("- verification_ok: " + str(verification_ok))
    lines.append("- claim: X_sigma is separated from the untwisted product baseline by exact metric invariants.")
    lines.append("")
    lines.append("## Source counts")
    lines.append("")
    lines.append("- vertex_count: " + str(N))
    lines.append("- g15_slot_edges: " + str(len(g15_edges)))
    lines.append("- g60_local_edges: " + str(len(g60_edges)))
    lines.append("- baseline_edges: " + str(len(baseline_edges)))
    lines.append("")
    lines.append("## Metric comparison")
    lines.append("")
    lines.append("- x_sigma_diameter: " + str(x_diameter))
    lines.append("- x_sigma_radius: " + str(x_radius))
    lines.append("- baseline_diameter: " + str(baseline_diameter))
    lines.append("- baseline_radius: " + str(baseline_radius))
    lines.append("- diameter_separates: " + str(checks["diameter_separates"]))
    lines.append("- radius_separates: " + str(checks["radius_separates"]))
    lines.append("")
    lines.append("## Baseline details")
    lines.append("")
    lines.append("- baseline_center_count: " + str(len(metrics["center_vertices"])))
    lines.append("- baseline_first_center_vertex: " + str(metrics["center_vertices"][0] if metrics["center_vertices"] else None))
    lines.append("- baseline_diameter_vertex_count: " + str(len(metrics["diameter_vertices"])))
    lines.append("- baseline_first_diameter_witness_pair: " + str(metrics["first_diameter_witness_pair"]))
    lines.append("")
    lines.append("## Baseline eccentricity counts")
    lines.append("")
    for k, v in metrics["eccentricity_counts"].items():
        lines.append("- eccentricity_" + k + ": " + str(v))
    lines.append("")
    lines.append("## Baseline distance distribution")
    lines.append("")
    for k, v in metrics["distance_distribution"].items():
        lines.append("- distance_" + k + ": " + str(v))
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    for k, v in checks.items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")
    lines.append("## Hashes")
    lines.append("")
    lines.append("- baseline_edge_id_set_sha256: " + cert["hashes"]["baseline_edge_id_set_sha256"])
    lines.append("")
    lines.append("## Boundary")
    lines.append("")
    for b in cert["boundary"]:
        lines.append("- " + b)
    lines.append("")

    OUT_MD.write_text("\n".join(lines))

    print("baseline_separation_ok=" + str(verification_ok))
    print("baseline_edges=" + str(len(baseline_edges)))
    print("x_sigma_diameter=" + str(x_diameter))
    print("x_sigma_radius=" + str(x_radius))
    print("baseline_diameter=" + str(baseline_diameter))
    print("baseline_radius=" + str(baseline_radius))
    print("diameter_separates=" + str(checks["diameter_separates"]))
    print("radius_separates=" + str(checks["radius_separates"]))
    print("baseline_eccentricity_counts=" + json.dumps(metrics["eccentricity_counts"], sort_keys=True))
    print("baseline_distance_distribution=" + json.dumps(metrics["distance_distribution"], sort_keys=True))
    print("wrote", OUT_JSON)
    print("wrote", OUT_MD)

    if not verification_ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
