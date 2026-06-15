# C-transition role-block circulation audit 005

Status: c_transition_role_block_circulation_audit_recorded

## Output

- role_pair_order: `['WX/ZT', 'TI/XY', 'IW/YZ']`
- all_circulation_matches: `True`
- block_union: `[0, 1, 2, 4, 5, 10, 11, 13, 14]`
- block_union_equals_observed: `True`
- block_complement: `[3, 6, 7, 8, 9, 12]`
- block_complement_equals_unobserved: `True`
- triple_from_block_intersection: `[2]`
- shared_junction_is_2: `True`

## Blocks

- WX/ZT: from=[0, 2, 10, 14] to=[2, 4, 11, 13] transitions=4 q_counts={'0': 3, '3': 1}
- TI/XY: from=[2, 4, 11, 13] to=[1, 2, 5] transitions=4 q_counts={'0': 2, '3': 2}
- IW/YZ: from=[1, 2, 5] to=[0, 2, 10, 14] transitions=4 q_counts={'0': 2, '3': 2}

## Circulation checks

- WX/ZT to-block -> TI/XY from-block: `True`
- TI/XY to-block -> IW/YZ from-block: `True`
- IW/YZ to-block -> WX/ZT from-block: `True`

## Boundary

This is a WXYZTI role-channel circulation result. It does not derive the circulation from G60-native structure and does not close Gap A.
