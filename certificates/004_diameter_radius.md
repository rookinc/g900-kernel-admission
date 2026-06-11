# Diameter and radius certificate

- verification_ok: True
- claim: X_sigma has diameter 8 and radius 6.
- method: all-source BFS over source/kernel_payload/x_sigma_edges.csv

## Metric result

- vertex_count: 900
- edge_count: 3600
- diameter: 8
- radius: 6
- center_count: 349
- first_center_vertex: 1
- diameter_vertex_count: 10
- first_diameter_witness_pair: [198, 623]

## Eccentricity counts

- eccentricity_6: 349
- eccentricity_7: 541
- eccentricity_8: 10

## Distance distribution

- distance_1: 3600
- distance_2: 17710
- distance_3: 60345
- distance_4: 131446
- distance_5: 143177
- distance_6: 45600
- distance_7: 2667
- distance_8: 5

## Checks

- edge_count_is_3600: True
- all_vertices_reached_from_every_source: True
- diameter_is_8: True
- radius_is_6: True
- has_center_vertex: True
- has_diameter_witness: True
- no_eccentricity_below_radius: True
- distance_distribution_pair_count_ok: True

## Hashes

- source_edge_id_set_sha256: 982fa358aa4a6d76000e62a3abde3ff3e2ce06af179ab131030eec923d05877d

## Boundary

- This certificate proves diameter and radius from the finite internal edge payload.
- It also rechecks connected reachability from every source.
- It does not prove uniqueness, census identity, sibling non-switching, or physical interpretation.
- It does not use renderer output or Project 17 at runtime.
