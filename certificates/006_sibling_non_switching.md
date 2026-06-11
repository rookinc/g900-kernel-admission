# Sibling non-switching certificate

- verification_ok: True
- claim: the sibling signing delta is not a switching coboundary over G15.
- interpretation: the sibling signing is not switching-equivalent to the canonical signing.

## Support

- support_edges: [[5, 10], [5, 14], [9, 11], [9, 12], [10, 14], [11, 12]]
- support_triangles: [[5, 10, 14], [9, 11, 12]]
- support_component_count: 2
- support_component_sizes: [3, 3]
- support_cycle_rank: 2

## F2 obstruction

- switching_equation_solvable: False
- rank_coeff: 14
- rank_augmented: 15
- contradiction_count: 16

## Counts

- g15_edges: 30
- canonical_sign_0: 15
- canonical_sign_1: 15
- sibling_sign_0: 15
- sibling_sign_1: 15
- delta_0: 24
- delta_1: 6

## Triangle checks

- triangle [5, 10, 14]: odd_delta_parity=True
- triangle [9, 11, 12]: odd_delta_parity=True

## Checks

- g15_edge_count_is_30: True
- canonical_signing_has_30_edges: True
- canonical_edges_match_g15: True
- support_edge_count_is_6: True
- support_edges_exist_in_g15: True
- support_component_count_is_2: True
- support_component_sizes_are_3_3: True
- support_cycle_rank_is_2: True
- each_support_triangle_has_odd_delta_parity: True
- gf2_system_unsolvable: True
- rank_augmented_exceeds_rank_coeff: True
- assignment_has_contradiction: True

## Boundary

- This certificate proves non-switching-equivalence of the sibling signing delta.
- It does not prove the sibling candidate is invalid.
- It does not prove full graph separation by exact graph invariant.
- It does not prove uniqueness among all possible signed carriers.
- It does not use renderer output, census identity, physical interpretation, or Project 17 at runtime.
