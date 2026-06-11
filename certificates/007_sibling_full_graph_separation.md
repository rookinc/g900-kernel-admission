# Sibling full graph separation certificate

- verification_ok: True
- claim: the sibling graph is separated from canonical X_sigma by an exact graph invariant.

## Edge-set comparison

- canonical_edges: 3600
- sibling_edges: 3600
- intersection_edges: 3240
- canonical_only_edges: 360
- sibling_only_edges: 360
- symmetric_difference_edges: 720

## Canonical metric

- diameter: 8
- radius: 6
- eccentricity_counts: {'6': 349, '7': 541, '8': 10}
- distance_distribution: {'1': 3600, '2': 17710, '3': 60345, '4': 131446, '5': 143177, '6': 45600, '7': 2667, '8': 5}

## Sibling metric

- diameter: 8
- radius: 6
- center_count: 327
- first_center_vertex: 1
- diameter_vertex_count: 48
- first_diameter_witness_pair: [18, 683]
- eccentricity_counts: {'6': 327, '7': 525, '8': 48}
- distance_distribution: {'1': 3600, '2': 17700, '3': 60642, '4': 130810, '5': 142395, '6': 46225, '7': 3144, '8': 34}

## Separation flags

- diameter_separates: False
- radius_separates: False
- eccentricity_counts_separates: True
- distance_distribution_separates: True
- exact_graph_invariant_separates: True

## Checks

- g15_edge_count_is_30: True
- g60_edge_count_is_120: True
- sibling_signing_has_30_edges: True
- sibling_signing_edges_match_g15: True
- canonical_edge_count_is_3600: True
- sibling_edge_count_is_3600: True
- sibling_connected: True
- sibling_distance_pair_count_ok: True
- canonical_and_sibling_label_distinct: True
- exact_graph_invariant_separates: True
- distance_distribution_separates: True

## Hashes

- canonical_edge_id_set_sha256: e261704922e6aa218126561bbf0d0b488d9eecd79b34fbeb08e66311e42bbd60
- sibling_edge_id_set_sha256: b7951eac5c82e49faeed6f3be342e2f0d546ae1bca90a22b4fc73edb79ed983c

## Boundary

- This certificate proves canonical X_sigma and the sibling graph are separated by an exact graph invariant.
- Unequal distance distributions are graph invariants, so this also certifies non-isomorphism for this sibling graph.
- It does not prove the sibling candidate is invalid.
- It does not prove uniqueness among all possible signed carriers.
- It does not use renderer output, census identity, physical interpretation, or Project 17 at runtime.
