# C-transition support partition audit 001

Status: c_transition_support_partition_audit_recorded

## Output

- transition_count: `34`
- transition_support: `[0, 1, 2, 4, 5, 10, 11, 13, 14]`
- transition_complement: `[3, 6, 7, 8, 9, 12]`
- support_equals_observed: `True`
- complement_equals_unobserved: `True`
- q3_subset_of_transition_support: `True`
- q0_subset_of_transition_support: `True`
- unobserved_disjoint_from_transition_support: `True`

## q3 / q0 cuts to transition support

- q3_cut_to_transition_support: `{'edge_count': 8, 'neg': 4, 'pos': 4, 'none': 24}`
- q3_cut_to_transition_complement: `{'edge_count': 8, 'neg': 4, 'pos': 4, 'none': 16}`
- q0_cut_to_transition_support: `{'edge_count': 14, 'neg': 10, 'pos': 4, 'none': 26}`
- q0_cut_to_transition_complement: `{'edge_count': 6, 'neg': 5, 'pos': 1, 'none': 24}`

## Boundary

This does not close Gap A. It may derive observed support from WXYZTI transition rows, but not from G60-native structure. If support_equals_observed is true, the next task is to derive the transition support itself from station constraints or native oriented structure.
