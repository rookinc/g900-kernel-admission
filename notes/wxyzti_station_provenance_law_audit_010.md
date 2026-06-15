# WXYZTI station provenance law audit 010

Status: wxyzti_station_provenance_law_audit_recorded

## Output

- semantic_row_count: `24`
- role_counts: `{'IW': 4, 'TI': 4, 'WX': 4, 'XY': 4, 'YZ': 4, 'ZT': 4}`
- role_class_counts: `{'reverse_partner': 12, 'shared_B': 12}`
- role_pair_counts: `{'IW/YZ': 8, 'TI/XY': 8, 'WX/ZT': 8}`
- deterministic_test_count: `96`
- exact_deterministic_test_count: `23`

## Role-pair summary

- IW/YZ: count=8, from_C=[1, 2, 5], to_C=[0, 2, 10, 14], C_delta_counts={9: 2, 10: 2, 12: 4}, lift_q_counts={0: 4, 3: 4}, fiber_delta_matches=8/8
- TI/XY: count=8, from_C=[2, 4, 11, 13], to_C=[1, 2, 5], C_delta_counts={1: 2, 3: 4, 6: 2}, lift_q_counts={0: 4, 3: 4}, fiber_delta_matches=8/8
- WX/ZT: count=8, from_C=[0, 2, 10, 14], to_C=[2, 4, 11, 13], C_delta_counts={2: 4, 3: 2, 12: 2}, lift_q_counts={0: 6, 3: 2}, fiber_delta_matches=8/8

## First exact deterministic tests

- keys=['from_C'] -> lift_q, groups=9
- keys=['role_pair', 'from_C'] -> lift_q, groups=11
- keys=['from_slot', 'from_fiber'] -> lift_q, groups=22
- keys=['station_role', 'from_C'] -> lift_q, groups=22
- keys=['from_A', 'from_B', 'from_C'] -> lift_q, groups=22
- keys=['role_pair', 'from_slot', 'from_fiber'] -> lift_q, groups=23
- keys=['station_role', 'from_slot', 'from_fiber'] -> C_delta, groups=24
- keys=['station_role', 'from_slot', 'from_fiber'] -> fiber_delta, groups=24
- keys=['station_role', 'from_slot', 'from_fiber'] -> fiber_delta_from_fields, groups=24
- keys=['station_role', 'from_slot', 'from_fiber'] -> lift_q, groups=24
- keys=['station_role', 'from_slot', 'from_fiber'] -> slot_delta, groups=24
- keys=['station_role', 'from_slot', 'from_fiber'] -> to_C, groups=24
- keys=['station_role', 'from_slot', 'from_fiber'] -> to_fiber, groups=24
- keys=['station_role', 'from_slot', 'from_fiber'] -> to_slot, groups=24
- keys=['role_pair', 'from_A', 'from_B', 'from_C'] -> lift_q, groups=23
- keys=['station_role', 'from_A', 'from_B', 'from_C'] -> C_delta, groups=24
- keys=['station_role', 'from_A', 'from_B', 'from_C'] -> fiber_delta, groups=24
- keys=['station_role', 'from_A', 'from_B', 'from_C'] -> fiber_delta_from_fields, groups=24
- keys=['station_role', 'from_A', 'from_B', 'from_C'] -> lift_q, groups=24
- keys=['station_role', 'from_A', 'from_B', 'from_C'] -> slot_delta, groups=24

## Boundary

This audits only realized station rows. It does not compare against non-realized candidate rows, does not prove a complete generator, and does not close Gap A.
