# C-transition role-channel grammar audit 004

Status: c_transition_role_channel_grammar_audit_recorded

## Output

- transition_count: `12`
- support: `[0, 1, 2, 4, 5, 10, 11, 13, 14]`
- complement: `[3, 6, 7, 8, 9, 12]`
- support_equals_observed: `True`
- complement_equals_unobserved: `True`
- role_pair_count: `3`
- from_deterministic_q: `True`
- role_pair_plus_from_determines_to: `False`
- role_pair_plus_from_determines_delta: `False`

## Role-pair channels

- IW/YZ: transitions=4, from=[1, 2, 5], to=[0, 2, 10, 14], q_counts={0: 2, 3: 2}
- TI/XY: transitions=4, from=[2, 4, 11, 13], to=[1, 2, 5], q_counts={0: 2, 3: 2}
- WX/ZT: transitions=4, from=[0, 2, 10, 14], to=[2, 4, 11, 13], q_counts={0: 3, 3: 1}

## From-C rows

- from_C 0: count=1, to=[2], role_pairs=['WX/ZT'], q=[0]
- from_C 1: count=1, to=[10], role_pairs=['IW/YZ'], q=[0]
- from_C 2: count=3, to=[4, 5, 14], role_pairs=['IW/YZ', 'TI/XY', 'WX/ZT'], q=[0]
- from_C 4: count=1, to=[5], role_pairs=['TI/XY'], q=[0]
- from_C 5: count=2, to=[0, 2], role_pairs=['IW/YZ'], q=[3]
- from_C 10: count=1, to=[13], role_pairs=['WX/ZT'], q=[0]
- from_C 11: count=1, to=[2], role_pairs=['TI/XY'], q=[3]
- from_C 13: count=1, to=[1], role_pairs=['TI/XY'], q=[3]
- from_C 14: count=1, to=[11], role_pairs=['WX/ZT'], q=[3]

## Boundary

This is still a channel-grammar audit over the WXYZTI overlay. It does not derive the role-pair channels from G60-native structure and does not close Gap A.
