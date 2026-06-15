# WXYZTI allowed-pair rule search 013

Status: wxyzti_allowed_pair_rule_search_recorded

## Output

- row_count: `24`
- exact_rule_count: `2804`
- exact_base_only_rule_count: `1761`
- non_row_exact_base_rule_count: `522`
- low_group_exact_base_rule_count: `91`

## Tests of interest

- keys=['role_pair'] -> to_C: deterministic=False, groups=3, ambiguous=3, group_sizes={8: 3}
- keys=['role_pair', 'from_C'] -> to_C: deterministic=False, groups=11, ambiguous=1, group_sizes={2: 10, 4: 1}
- keys=['station_role', 'from_C'] -> to_C: deterministic=False, groups=22, ambiguous=2, group_sizes={1: 20, 2: 2}
- keys=['from_C'] -> to_C: deterministic=False, groups=9, ambiguous=2, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_C'] -> lift_q: deterministic=True, groups=9, ambiguous=0, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_C'] -> C_wrap_flag: deterministic=True, groups=9, ambiguous=0, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['role_pair', 'from_C'] -> integer_C_delta: deterministic=False, groups=11, ambiguous=1, group_sizes={2: 10, 4: 1}
- keys=['station_role', 'from_C'] -> integer_C_delta: deterministic=False, groups=22, ambiguous=2, group_sizes={1: 20, 2: 2}
- keys=['role_pair', 'from_C'] -> C_delta: deterministic=False, groups=11, ambiguous=1, group_sizes={2: 10, 4: 1}
- keys=['station_role', 'from_C'] -> C_delta: deterministic=False, groups=22, ambiguous=2, group_sizes={1: 20, 2: 2}
- keys=['role_pair', 'from_A', 'from_B', 'from_C'] -> to_C: deterministic=False, groups=23, ambiguous=1, group_sizes={1: 22, 2: 1}
- keys=['station_role', 'from_A', 'from_B', 'from_C'] -> to_C: deterministic=True, groups=24, ambiguous=0, group_sizes={1: 24}

## Source summary by role_pair/from_C

- IW/YZ from_C=1: rows=2, to_C=[10]
- IW/YZ from_C=2: rows=2, to_C=[14]
- IW/YZ from_C=5: rows=4, to_C=[0, 2]
- TI/XY from_C=11: rows=2, to_C=[2]
- TI/XY from_C=13: rows=2, to_C=[1]
- TI/XY from_C=2: rows=2, to_C=[5]
- TI/XY from_C=4: rows=2, to_C=[5]
- WX/ZT from_C=0: rows=2, to_C=[2]
- WX/ZT from_C=10: rows=2, to_C=[13]
- WX/ZT from_C=14: rows=2, to_C=[11]
- WX/ZT from_C=2: rows=2, to_C=[4]

## First non-row exact base rules

- keys=['from_C'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_fiber'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_fiber_mod15'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_fiber_mod30'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_C', 'from_fiber'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_C', 'from_fiber_mod15'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_C', 'from_fiber_mod30'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_C', 'from_fiber_sheet15'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_C', 'from_fiber_sheet30'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_fiber', 'from_fiber_mod15'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_fiber', 'from_fiber_mod30'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_fiber', 'from_fiber_sheet15'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_fiber', 'from_fiber_sheet30'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_fiber_mod15', 'from_fiber_mod30'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_fiber_mod15', 'from_fiber_sheet15'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_fiber_mod15', 'from_fiber_sheet30'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_fiber_mod30', 'from_fiber_sheet30'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['from_fiber_sheet15', 'from_fiber_mod30'] -> predicted_lift_q_from_wrap, groups=9, group_sizes={2: 7, 4: 1, 6: 1}
- keys=['role_pair', 'from_C'] -> predicted_lift_q_from_wrap, groups=11, group_sizes={2: 10, 4: 1}
- keys=['role_pair', 'from_fiber'] -> predicted_lift_q_from_wrap, groups=11, group_sizes={2: 10, 4: 1}
- keys=['role_pair', 'from_fiber_mod15'] -> predicted_lift_q_from_wrap, groups=11, group_sizes={2: 10, 4: 1}
- keys=['role_pair', 'from_fiber_mod30'] -> predicted_lift_q_from_wrap, groups=11, group_sizes={2: 10, 4: 1}
- keys=['role_class', 'from_C'] -> predicted_lift_q_from_wrap, groups=18, group_sizes={1: 14, 2: 2, 3: 2}
- keys=['role_class', 'from_fiber'] -> predicted_lift_q_from_wrap, groups=18, group_sizes={1: 14, 2: 2, 3: 2}
- keys=['role_class', 'from_fiber_mod15'] -> predicted_lift_q_from_wrap, groups=18, group_sizes={1: 14, 2: 2, 3: 2}
- keys=['role_class', 'from_fiber_mod30'] -> predicted_lift_q_from_wrap, groups=18, group_sizes={1: 14, 2: 2, 3: 2}
- keys=['from_A', 'from_C'] -> predicted_lift_q_from_wrap, groups=19, group_sizes={1: 14, 2: 5}
- keys=['from_A', 'from_fiber'] -> predicted_lift_q_from_wrap, groups=19, group_sizes={1: 14, 2: 5}
- keys=['from_A', 'from_fiber_mod15'] -> predicted_lift_q_from_wrap, groups=19, group_sizes={1: 14, 2: 5}
- keys=['from_A', 'from_fiber_mod30'] -> predicted_lift_q_from_wrap, groups=19, group_sizes={1: 14, 2: 5}

## Boundary

This audits realized rows only. Exact rules here do not prove selection from non-realized candidate rows and do not close Gap A.
