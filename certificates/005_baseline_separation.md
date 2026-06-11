# Baseline separation certificate

- verification_ok: True
- claim: X_sigma is separated from the untwisted product baseline by exact metric invariants.

## Source counts

- vertex_count: 900
- g15_slot_edges: 30
- g60_local_edges: 120
- baseline_edges: 3600

## Metric comparison

- x_sigma_diameter: 8
- x_sigma_radius: 6
- baseline_diameter: 9
- baseline_radius: 9
- diameter_separates: True
- radius_separates: True

## Baseline details

- baseline_center_count: 900
- baseline_first_center_vertex: 0
- baseline_diameter_vertex_count: 900
- baseline_first_diameter_witness_pair: [0, 520]

## Baseline eccentricity counts

- eccentricity_9: 900

## Baseline distance distribution

- distance_1: 3600
- distance_2: 14400
- distance_3: 36900
- distance_4: 72000
- distance_5: 110700
- distance_6: 112050
- distance_7: 45000
- distance_8: 9000
- distance_9: 900

## Checks

- g15_edge_count_is_30: True
- g60_edge_count_is_120: True
- baseline_edge_count_is_3600: True
- baseline_connected: True
- baseline_diameter_is_9: True
- baseline_radius_is_9: True
- x_sigma_diameter_is_8: True
- x_sigma_radius_is_6: True
- diameter_separates: True
- radius_separates: True
- distance_distribution_pair_count_ok: True

## Hashes

- baseline_edge_id_set_sha256: c347b81a3e663db7104b277a148802b67049e041dd80b153d45c8052f24dba66

## Boundary

- This certificate proves separation from the untwisted product baseline by exact metric invariants.
- It does not prove uniqueness among all possible signed carriers.
- It does not prove sibling non-switching or sibling full-graph separation.
- It does not use renderer output, census identity, physical interpretation, or Project 17 at runtime.
