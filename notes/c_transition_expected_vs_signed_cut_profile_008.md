# C-transition expected vs signed-cut profile 008

Status: c_transition_expected_vs_signed_cut_profile_recorded

## Output

- candidate_count: `2`
- target_possible_pair_count: `37`
- target_expected_pair_count: `12`
- target_total_expected_relation_counts: `{'no_edge': 9, 'signed_neg': 2, 'signed_pos': 1}`
- target_total_nonexpected_relation_counts: `{'no_edge': 15, 'signed_neg': 7, 'signed_pos': 3}`
- target_total_possible_relation_counts: `{'no_edge': 24, 'signed_neg': 9, 'signed_pos': 4}`
- target_total_expected_signed_pair_count: `3`
- target_total_expected_no_edge_pair_count: `9`
- target_total_nonexpected_signed_pair_count: `10`

## Target channel rows

- WX/ZT A->B possible=15 expected=4 expected_rel={'no_edge': 4} nonexpected_rel={'no_edge': 6, 'signed_neg': 4, 'signed_pos': 1}
  - expected_signed_pairs: `[]`
  - expected_no_edge_pairs: `[[0, 2], [2, 4], [10, 13], [14, 11]]`
- TI/XY B->C possible=11 expected=4 expected_rel={'no_edge': 2, 'signed_neg': 2} nonexpected_rel={'no_edge': 4, 'signed_neg': 1, 'signed_pos': 2}
  - expected_signed_pairs: `[[4, 5], [11, 2]]`
  - expected_no_edge_pairs: `[[2, 5], [13, 1]]`
- IW/YZ C->A possible=11 expected=4 expected_rel={'no_edge': 3, 'signed_pos': 1} nonexpected_rel={'no_edge': 5, 'signed_neg': 2}
  - expected_signed_pairs: `[[5, 0]]`
  - expected_no_edge_pairs: `[[1, 10], [2, 14], [5, 2]]`

## Boundary

This does not derive the C-transition table. It only profiles the relation between the overlay transition table and signed-G15 cut adjacency.
