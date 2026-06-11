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
CANONICAL_EDGES = PAYLOAD / "x_sigma_edges.csv"
SIBLING_SIGNING = PAYLOAD / "sibling_candidate_signing_table.csv"
CANONICAL_METRIC = ROOT / "artifacts/json/metric_certificate.json"

OUT_SIBLING_EDGES = PAYLOAD / "sibling_x_sigma_edges.csv"
OUT_JSON = ROOT / "artifacts/json/sibling_full_graph_separation_certificate.json"
OUT_MD = ROOT / "certificates/007_sibling_full_graph_separation.md"

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

def edge_pair(a, b):
    return tuple(sorted((int(a), int(b))))

def vid(slot, local):
    return int(slot) * 60 + int(local)

def slot_local(v):
    return v // 60, v % 60

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
        edges.add(edge_pair(a, b))
    return edges

def parse_recorded_edge(row):
    keys = {str(k).lower(): k for k in row.keys()}

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
            return edge_pair(vid(vals[0], vals[1]), vid(vals[2], vals[3]))

    xs = ints_from_row(row)

    if len(xs) >= 4:
        a_slot, a_local, b_slot, b_local = xs[:4]
        if 0 <= a_slot < 15 and 0 <= b_slot < 15 and 0 <= a_local < 60 and 0 <= b_local < 60:
            return edge_pair(vid(a_slot, a_local), vid(b_slot, b_local))

    if len(xs) >= 2:
        a, b = xs[:2]
        if 0 <= a < N and 0 <= b < N:
            return edge_pair(a, b)

    raise ValueError("could not parse recorded edge row: " + str(row))

def read_recorded_edges(path):
    edges = set()
    for row in read_rows(path):
        a, b = parse_recorded_edge(row)
        if a == b:
            raise ValueError("loop edge in " + str(path) + ": " + str(row))
        edges.add((a, b))
    return edges

def read_sibling_signing(path):
    signs = {}
    for row in read_rows(path):
        keys = {str(k).lower(): k for k in row.keys()}

        if "slot_a" in keys and "slot_b" in keys and "sibling_sign" in keys:
            a = int(row[keys["slot_a"]])
            b = int(row[keys["slot_b"]])
            sign = int(row[keys["sibling_sign"]])
        else:
            xs = ints_from_row(row)
            if len(xs) < 3:
                raise ValueError("could not parse sibling signing row: " + str(row))
            a, b = xs[0], xs[1]
            sign = xs[-1]

        if sign not in (0, 1):
            raise ValueError("sibling sign must be 0 or 1: " + str(row))

        signs[edge_pair(a, b)] = sign

    return signs

def build_signed_graph_edges(g15_edges, g60_edges, signs):
    edges = set()

    for t in range(15):
        for x, y in g60_edges:
            edges.add(edge_pair(vid(t, x), vid(t, y)))

    for t, u in g15_edges:
        sign = signs[edge_pair(t, u)]
        for x in range(60):
            y = x if sign == 0 else (x + 30) % 60
            edges.add(edge_pair(vid(t, x), vid(u, y)))

    return edges

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

def all_source_metrics(edges, label):
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

    print("running all-source BFS over " + label + " 900 vertices")
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
        "center_count": len(center_vertices),
        "first_center_vertex": center_vertices[0] if center_vertices else None,
        "diameter_vertex_count": len(diameter_vertices),
        "first_diameter_witness_pair": first_diameter_witness,
        "eccentricity_counts": {str(k): eccentricity_counts[k] for k in sorted(eccentricity_counts)},
        "distance_distribution": {str(k): distance_distribution[k] for k in sorted(distance_distribution)},
        "distance_pair_count": sum(distance_distribution.values())
    }

def write_sibling_edges(path, edges):
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["slot_a", "local_a", "slot_b", "local_b"])
        writer.writeheader()
        for a, b in sorted(edges):
            sa, la = slot_local(a)
            sb, lb = slot_local(b)
            writer.writerow({
                "slot_a": sa,
                "local_a": la,
                "slot_b": sb,
                "local_b": lb
            })

def main():
    if not SIBLING_SIGNING.exists():
        raise FileNotFoundError("missing sibling signing table: " + str(SIBLING_SIGNING))

    if not CANONICAL_METRIC.exists():
        raise FileNotFoundError("missing canonical metric certificate: " + str(CANONICAL_METRIC))

    g15_edges = read_simple_edges(G15)
    g60_edges = read_simple_edges(G60)
    sibling_signs = read_sibling_signing(SIBLING_SIGNING)

    canonical_edges = read_recorded_edges(CANONICAL_EDGES)
    sibling_edges = build_signed_graph_edges(g15_edges, g60_edges, sibling_signs)

    write_sibling_edges(OUT_SIBLING_EDGES, sibling_edges)

    canonical_metric = json.loads(CANONICAL_METRIC.read_text())
    sibling_metric = all_source_metrics(sibling_edges, "sibling")

    canonical_distance_distribution = canonical_metric.get("distance_distribution")
    canonical_eccentricity_counts = canonical_metric.get("eccentricity_counts")

    sibling_distance_distribution = sibling_metric["distance_distribution"]
    sibling_eccentricity_counts = sibling_metric["eccentricity_counts"]

    canonical_only = canonical_edges - sibling_edges
    sibling_only = sibling_edges - canonical_edges
    intersection = canonical_edges & sibling_edges

    distance_distribution_separates = canonical_distance_distribution != sibling_distance_distribution
    eccentricity_counts_separates = canonical_eccentricity_counts != sibling_eccentricity_counts
    diameter_separates = canonical_metric.get("diameter") != sibling_metric["diameter"]
    radius_separates = canonical_metric.get("radius") != sibling_metric["radius"]

    exact_graph_invariant_separates = (
        distance_distribution_separates or
        eccentricity_counts_separates or
        diameter_separates or
        radius_separates
    )

    checks = {
        "g15_edge_count_is_30": len(g15_edges) == 30,
        "g60_edge_count_is_120": len(g60_edges) == 120,
        "sibling_signing_has_30_edges": len(sibling_signs) == 30,
        "sibling_signing_edges_match_g15": set(sibling_signs.keys()) == set(g15_edges),
        "canonical_edge_count_is_3600": len(canonical_edges) == 3600,
        "sibling_edge_count_is_3600": len(sibling_edges) == 3600,
        "sibling_connected": sibling_metric["all_reached"] is True,
        "sibling_distance_pair_count_ok": sibling_metric["distance_pair_count"] == (N * (N - 1)) // 2,
        "canonical_and_sibling_label_distinct": len(canonical_only) > 0 and len(sibling_only) > 0,
        "exact_graph_invariant_separates": exact_graph_invariant_separates,
        "distance_distribution_separates": distance_distribution_separates
    }

    verification_ok = all(checks.values())

    cert = {
        "certificate": "sibling_full_graph_separation",
        "verification_ok": verification_ok,
        "claim": "The sibling graph is separated from canonical X_sigma by an exact graph invariant.",
        "method": "Build sibling graph from the sibling signing table, compute all-source BFS invariants, and compare against canonical X_sigma invariants.",
        "source_files": {
            "g15_slot_edges": str(G15.relative_to(ROOT)),
            "g60_local_edges": str(G60.relative_to(ROOT)),
            "canonical_x_sigma_edges": str(CANONICAL_EDGES.relative_to(ROOT)),
            "sibling_signing_table": str(SIBLING_SIGNING.relative_to(ROOT)),
            "sibling_x_sigma_edges": str(OUT_SIBLING_EDGES.relative_to(ROOT)),
            "canonical_metric_certificate": str(CANONICAL_METRIC.relative_to(ROOT))
        },
        "edge_set_comparison": {
            "canonical_edges": len(canonical_edges),
            "sibling_edges": len(sibling_edges),
            "intersection_edges": len(intersection),
            "canonical_only_edges": len(canonical_only),
            "sibling_only_edges": len(sibling_only),
            "symmetric_difference_edges": len(canonical_only) + len(sibling_only)
        },
        "canonical_metric": {
            "diameter": canonical_metric.get("diameter"),
            "radius": canonical_metric.get("radius"),
            "eccentricity_counts": canonical_eccentricity_counts,
            "distance_distribution": canonical_distance_distribution
        },
        "sibling_metric": {
            "diameter": sibling_metric["diameter"],
            "radius": sibling_metric["radius"],
            "center_count": sibling_metric["center_count"],
            "first_center_vertex": sibling_metric["first_center_vertex"],
            "diameter_vertex_count": sibling_metric["diameter_vertex_count"],
            "first_diameter_witness_pair": sibling_metric["first_diameter_witness_pair"],
            "eccentricity_counts": sibling_eccentricity_counts,
            "distance_distribution": sibling_distance_distribution
        },
        "separation_flags": {
            "diameter_separates": diameter_separates,
            "radius_separates": radius_separates,
            "eccentricity_counts_separates": eccentricity_counts_separates,
            "distance_distribution_separates": distance_distribution_separates,
            "exact_graph_invariant_separates": exact_graph_invariant_separates
        },
        "checks": checks,
        "hashes": {
            "canonical_edge_id_set_sha256": sha_edge_ids(canonical_edges),
            "sibling_edge_id_set_sha256": sha_edge_ids(sibling_edges)
        },
        "boundary": [
            "This certificate proves canonical X_sigma and the sibling graph are separated by an exact graph invariant.",
            "Unequal distance distributions are graph invariants, so this also certifies non-isomorphism for this sibling graph.",
            "It does not prove the sibling candidate is invalid.",
            "It does not prove uniqueness among all possible signed carriers.",
            "It does not use renderer output, census identity, physical interpretation, or Project 17 at runtime."
        ]
    }

    OUT_JSON.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")

    lines = []
    lines.append("# Sibling full graph separation certificate")
    lines.append("")
    lines.append("- verification_ok: " + str(verification_ok))
    lines.append("- claim: the sibling graph is separated from canonical X_sigma by an exact graph invariant.")
    lines.append("")
    lines.append("## Edge-set comparison")
    lines.append("")
    for k, v in cert["edge_set_comparison"].items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")
    lines.append("## Canonical metric")
    lines.append("")
    lines.append("- diameter: " + str(canonical_metric.get("diameter")))
    lines.append("- radius: " + str(canonical_metric.get("radius")))
    lines.append("- eccentricity_counts: " + str(canonical_eccentricity_counts))
    lines.append("- distance_distribution: " + str(canonical_distance_distribution))
    lines.append("")
    lines.append("## Sibling metric")
    lines.append("")
    lines.append("- diameter: " + str(sibling_metric["diameter"]))
    lines.append("- radius: " + str(sibling_metric["radius"]))
    lines.append("- center_count: " + str(sibling_metric["center_count"]))
    lines.append("- first_center_vertex: " + str(sibling_metric["first_center_vertex"]))
    lines.append("- diameter_vertex_count: " + str(sibling_metric["diameter_vertex_count"]))
    lines.append("- first_diameter_witness_pair: " + str(sibling_metric["first_diameter_witness_pair"]))
    lines.append("- eccentricity_counts: " + str(sibling_eccentricity_counts))
    lines.append("- distance_distribution: " + str(sibling_distance_distribution))
    lines.append("")
    lines.append("## Separation flags")
    lines.append("")
    for k, v in cert["separation_flags"].items():
        lines.append("- " + k + ": " + str(v))
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    for k, v in checks.items():
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

    print("sibling_full_graph_separation_ok=" + str(verification_ok))
    print("canonical_edges=" + str(len(canonical_edges)))
    print("sibling_edges=" + str(len(sibling_edges)))
    print("intersection_edges=" + str(len(intersection)))
    print("canonical_only_edges=" + str(len(canonical_only)))
    print("sibling_only_edges=" + str(len(sibling_only)))
    print("symmetric_difference_edges=" + str(len(canonical_only) + len(sibling_only)))
    print("canonical_diameter=" + str(canonical_metric.get("diameter")))
    print("canonical_radius=" + str(canonical_metric.get("radius")))
    print("sibling_diameter=" + str(sibling_metric["diameter"]))
    print("sibling_radius=" + str(sibling_metric["radius"]))
    print("distance_distribution_separates=" + str(distance_distribution_separates))
    print("eccentricity_counts_separates=" + str(eccentricity_counts_separates))
    print("exact_graph_invariant_separates=" + str(exact_graph_invariant_separates))
    print("wrote", OUT_SIBLING_EDGES)
    print("wrote", OUT_JSON)
    print("wrote", OUT_MD)

    if not verification_ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
