# Diameter and radius certificate

- verification_ok: True
- claim: X_sigma has diameter 8 and radius 6.
- method: all-source BFS over source/kernel_payload/x_sigma_edges.csv

## Metric result

- vertex_count: 900
- edge_count: 3600
- diameter: 8
- radius: 6
- center_count: 342
- first_center_vertex: 1
- diameter_vertex_count: 32
- first_diameter_witness_pair: [18, 683]

## Eccentricity counts

- eccentricity_6: 342
- eccentricity_7: 526
- eccentricity_8: 32

## Distance distribution

- distance_1: 3600
- distance_2: 17700
- distance_3: 59941
- distance_4: 129877
- distance_5: 142712
- distance_6: 47600
- distance_7: 3100
- distance_8: 20

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

- source_edge_id_set_sha256: e261704922e6aa218126561bbf0d0b488d9eecd79b34fbeb08e66311e42bbd60

## Boundary

- This certificate proves diameter and radius from the finite internal edge payload.
- It also rechecks connected reachability from every source.
- It does not prove uniqueness, census identity, sibling non-switching, or physical interpretation.
- It does not use renderer output or Project 17 at runtime.
