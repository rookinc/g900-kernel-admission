# role-block directed transition selector 006c

Status: role_block_directed_transition_selector_recorded

## Output

- candidate_count: `2`
- exact_directed_transition_cover_count: `1`
- selected_indices: `[3]`
- target_selected: `True`
- non_target_selected_count: `0`

## Candidates

- index 2 target=False exact_directed_transition_cover=False matched=6 missing=6 A=[0, 2, 5, 10] B=[2, 4, 11, 13] C=[1, 2, 14]
  - WX/ZT A->B matched=3 missing=1
  - TI/XY B->C matched=2 missing=2
  - IW/YZ C->A matched=1 missing=3
- index 3 target=True exact_directed_transition_cover=True matched=12 missing=0 A=[0, 2, 10, 14] B=[2, 4, 11, 13] C=[1, 2, 5]
  - WX/ZT A->B matched=4 missing=0
  - TI/XY B->C matched=4 missing=0
  - IW/YZ C->A matched=4 missing=0

## Boundary

This selects by directed WXYZTI transition compatibility. It does not derive the transition table from G60-native structure and does not close Gap A.
