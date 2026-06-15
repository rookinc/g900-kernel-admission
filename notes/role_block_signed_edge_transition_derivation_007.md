# role-block signed-edge transition derivation 007

Status: role_block_signed_edge_transition_derivation_recorded

## Output

- candidate_count: `2`
- exact_signed_edge_derivation_count: `0`
- selected_indices: `[]`
- target_selected: `False`
- non_target_selected_count: `0`

## Candidates

- index 2 target=False exact_signed_edge_derivation=False derived=13 expected=12 missing=11 extra=12 A=[0, 2, 5, 10] B=[2, 4, 11, 13] C=[1, 2, 14]
  - WX/ZT A->B exact=False derived=5 expected=4 sign_counts={-1: 4, 1: 1}
  - TI/XY B->C exact=False derived=5 expected=4 sign_counts={-1: 3, 1: 2}
  - IW/YZ C->A exact=False derived=3 expected=4 sign_counts={-1: 2, 1: 1}
- index 3 target=True exact_signed_edge_derivation=False derived=13 expected=12 missing=9 extra=10 A=[0, 2, 10, 14] B=[2, 4, 11, 13] C=[1, 2, 5]
  - WX/ZT A->B exact=False derived=5 expected=4 sign_counts={-1: 4, 1: 1}
  - TI/XY B->C exact=False derived=5 expected=4 sign_counts={-1: 3, 1: 2}
  - IW/YZ C->A exact=False derived=3 expected=4 sign_counts={-1: 2, 1: 1}

## Boundary

If exact for the target, this derives the 12 directed C-transition pairs from signed-G15 adjacency plus the selected A/B/C block circulation and channel order. It still does not derive the A/B/C blocks or channel order from G60-native structure, and it does not close Gap A.

## Reading

This is a negative result.

The 12 directed C-transitions are not recovered as the raw signed-G15 cut edges between consecutive A/B/C blocks.

For the target circulation, the raw signed cuts produce 13 directed block-cut edges, but only partially overlap the expected 12 directed C-transitions. The target has missing=9 and extra=10.

So the directed WXYZTI transition table is not simply signed-G15 adjacency oriented along the A/B/C circulation.

This is consistent with the current boundary: WXYZTI is a source-native transport overlay, not literal signed-G15 or X_sigma carrier adjacency.

## Updated next problem

Do not try to derive the C-transition table from raw signed-G15 cut adjacency alone.

Next candidates:

    station-role constraints inside WXYZTI rows
    oriented station order around W-X-Y-Z-T-I
    old Hyperxi/G60 involution shadows
    source-native provenance fields A/B/C/slot/fiber
