#!/usr/bin/env python3
import csv
import hashlib
import json
import re
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGE_FILE = ROOT / "source/kernel_payload/x_sigma_edges.csv"

OUT_JSON = ROOT / "artifacts/json/connectedness_certificate.json"
OUT_MD = ROOT / "certificates/003_connectedness.md"

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
        if 0 <= a < 900 and 0 <= b < 900:
            return tuple(sorted((a, b)))

    raise ValueError("could not parse edge row: " + str(row))

def sha_edge_ids(edges):
    text = "\n".join(f"{a},{b}" for a, b in sorted(edges)) + "\n"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def main():
    edges = set()
    for row in read_rows(EDGE_FILE):
        a, b = parse_edge_to_ids(row)
        if a == b:
            raise ValueError("loop edge found")
        edges.add((a, b))

    adjacency = {v: [] for v in range(900)}
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)

    root = 0
    parent = {root: None}
    depth = {root: 0}
    q = deque([root])

    while q:
        v = q.popleft()
        for w in sorted(adjacency[v]):
            if w not in parent:
                parent[w] = v
                depth[w] = depth[v] + 1
                q.append(w)

    reached = len(parent)
    tree_edges = [(p, v) for v, p in parent.items() if p is not None]

    parent_edge_ok = True
    bad_parent_edges = []
    edge_lookup = set(edges)

    for p, v in tree_edges:
        e = tuple(sorted((p, v)))
        if e not in edge_lookup:
            parent_edge_ok = False
            bad_parent_edges.append([p, v])

    all_vertices_present = set(parent.keys()) == set(range(900))
    tree_edge_count_ok = len(tree_edges) == 899
    connected = reached == 900
    verification_ok = connected and parent_edge_ok and all_vertices_present and tree_edge_count_ok

    certificate_vertices = []
    for v in range(900):
        certificate_vertices.append({
            "vertex": v,
            "slot": v // 60,
            "local": v % 60,
            "parent": parent.get(v),
            "depth": depth.get(v)
        })

    cert = {
        "certificate": "connectedness",
        "verification_ok": verification_ok,
        "claim": "X_sigma is connected.",
        "method": "BFS spanning tree from root vertex 0 over source/kernel_payload/x_sigma_edges.csv",
        "source_edge_file": str(EDGE_FILE.relative_to(ROOT)),
        "edge_count": len(edges),
        "vertex_count": 900,
        "root": root,
        "reached_vertex_count": reached,
        "tree_edge_count": len(tree_edges),
        "max_bfs_depth_from_root": max(depth.values()) if depth else None,
        "checks": {
            "connected": connected,
            "all_vertices_present": all_vertices_present,
            "tree_edge_count_ok": tree_edge_count_ok,
            "parent_edge_ok": parent_edge_ok,
            "bad_parent_edge_count": len(bad_parent_edges)
        },
        "hashes": {
            "source_edge_id_set_sha256": sha_edge_ids(edges)
        },
        "bfs_parent_certificate": certificate_vertices,
        "boundary": [
            "This certificate proves connectedness from the finite internal edge payload.",
            "It does not prove diameter, radius, uniqueness, census identity, or physical interpretation.",
            "It does not use renderer output or Project 17 at runtime."
        ]
    }

    OUT_JSON.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")

    lines = []
    lines.append("# Connectedness certificate")
    lines.append("")
    lines.append("- verification_ok: " + str(verification_ok))
    lines.append("- claim: X_sigma is connected.")
    lines.append("- method: BFS spanning tree from root vertex 0.")
    lines.append("- source_edge_file: " + str(EDGE_FILE.relative_to(ROOT)))
    lines.append("")
    lines.append("## Counts")
    lines.append("")
    lines.append("- vertex_count: 900")
    lines.append("- edge_count: " + str(len(edges)))
    lines.append("- reached_vertex_count: " + str(reached))
    lines.append("- tree_edge_count: " + str(len(tree_edges)))
    lines.append("- max_bfs_depth_from_root: " + str(cert["max_bfs_depth_from_root"]))
    lines.append("")
    lines.append("## Checks")
    lines.append("")
    for k, v in cert["checks"].items():
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

    print("connectedness_certificate_ok=" + str(verification_ok))
    print("vertex_count=900")
    print("edge_count=" + str(len(edges)))
    print("reached_vertex_count=" + str(reached))
    print("tree_edge_count=" + str(len(tree_edges)))
    print("max_bfs_depth_from_root=" + str(cert["max_bfs_depth_from_root"]))
    print("parent_edge_ok=" + str(parent_edge_ok))
    print("wrote", OUT_JSON)
    print("wrote", OUT_MD)

    if not verification_ok:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
