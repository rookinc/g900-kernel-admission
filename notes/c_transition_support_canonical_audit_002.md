# C-transition support canonical audit 002

Status: c_transition_support_canonical_audit_recorded

## Output

- source: `locked_12_row_c_transition_table`
- canonical_transition_count: `12`
- canonical_support: `[0, 1, 2, 4, 5, 10, 11, 13, 14]`
- canonical_complement: `[3, 6, 7, 8, 9, 12]`
- support_equals_observed: `True`
- complement_equals_unobserved: `True`
- q0_subset_of_support: `True`
- q3_subset_of_support: `True`
- unobserved_disjoint_from_support: `True`
- q_counts: `{0: 7, 3: 5}`

## Canonical transitions

- (0, 2) -> fiber_delta 2, base_delta_mod15 2, lift_q 0
- (1, 10) -> fiber_delta 9, base_delta_mod15 9, lift_q 0
- (2, 4) -> fiber_delta 2, base_delta_mod15 2, lift_q 0
- (2, 5) -> fiber_delta 3, base_delta_mod15 3, lift_q 0
- (2, 14) -> fiber_delta 12, base_delta_mod15 12, lift_q 0
- (4, 5) -> fiber_delta 1, base_delta_mod15 1, lift_q 0
- (5, 0) -> fiber_delta 55, base_delta_mod15 10, lift_q 3
- (5, 2) -> fiber_delta 57, base_delta_mod15 12, lift_q 3
- (10, 13) -> fiber_delta 3, base_delta_mod15 3, lift_q 0
- (11, 2) -> fiber_delta 51, base_delta_mod15 6, lift_q 3
- (13, 1) -> fiber_delta 48, base_delta_mod15 3, lift_q 3
- (14, 11) -> fiber_delta 57, base_delta_mod15 12, lift_q 3

## Reading

The observed C set is exactly the support of the canonical 12 C-transitions. The unobserved C set is exactly the complement.

## Boundary

This does not close Gap A. It does not derive the 12 C-transitions from G60-native structure. It only canonicalizes the WXYZTI transition support and its lift-q decomposition.
