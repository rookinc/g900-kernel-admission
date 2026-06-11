# Connectedness certificate

- verification_ok: True
- claim: X_sigma is connected.
- method: BFS spanning tree from root vertex 0.
- source_edge_file: source/kernel_payload/x_sigma_edges.csv

## Counts

- vertex_count: 900
- edge_count: 3600
- reached_vertex_count: 900
- tree_edge_count: 899
- max_bfs_depth_from_root: 7

## Checks

- connected: True
- all_vertices_present: True
- tree_edge_count_ok: True
- parent_edge_ok: True
- bad_parent_edge_count: 0

## Hashes

- source_edge_id_set_sha256: 982fa358aa4a6d76000e62a3abde3ff3e2ce06af179ab131030eec923d05877d

## Boundary

- This certificate proves connectedness from the finite internal edge payload.
- It does not prove diameter, radius, uniqueness, census identity, or physical interpretation.
- It does not use renderer output or Project 17 at runtime.
