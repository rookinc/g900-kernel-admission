# WXYZTI shared/reverse pair coupling audit 021

Status: wxyzti_shared_reverse_pair_coupling_audit_recorded

## Output

- pair_count: `12`
- bad_bucket_count: `0`
- shared_role_counts: `{'IW': 4, 'XY': 4, 'ZT': 4}`
- reverse_role_counts: `{'TI': 4, 'WX': 4, 'YZ': 4}`
- exact_true_flag_count: `16`

## Exact true flags

- R_preserves_A
- R_swaps_BC
- R_to_B_eq_S_from_C
- R_to_slot_eq_S_from_C
- S_from_C_eq_R_from_C
- S_preserves_B
- S_preserves_slot
- S_to_C_eq_R_from_B
- S_to_C_eq_R_from_slot
- S_to_C_eq_R_to_C
- same_C_delta
- same_from_C
- same_integer_C_delta
- same_lift_q
- same_role_pair
- same_to_C

## Partial flags


## Pair records

- key=('IW/YZ', 1, 10) shared=IW reverse=YZ
  - shared: `{'station_role': 'IW', 'role_pair': 'IW/YZ', 'role_class': 'shared_B', 'from_A': 2, 'from_B': 13, 'from_C': 1, 'from_slot': 13, 'to_A': 9, 'to_B': 13, 'to_C': 10, 'to_slot': 13, 'integer_C_delta': 9, 'C_delta': 9, 'fiber_delta': 9, 'lift_q': 0}`
  - reverse: `{'station_role': 'YZ', 'role_pair': 'IW/YZ', 'role_class': 'reverse_partner', 'from_A': 0, 'from_B': 10, 'from_C': 1, 'from_slot': 10, 'to_A': 0, 'to_B': 1, 'to_C': 10, 'to_slot': 1, 'integer_C_delta': 9, 'C_delta': 9, 'fiber_delta': 9, 'lift_q': 0}`
- key=('IW/YZ', 2, 14) shared=IW reverse=YZ
  - shared: `{'station_role': 'IW', 'role_pair': 'IW/YZ', 'role_class': 'shared_B', 'from_A': 1, 'from_B': 11, 'from_C': 2, 'from_slot': 11, 'to_A': 7, 'to_B': 11, 'to_C': 14, 'to_slot': 11, 'integer_C_delta': 12, 'C_delta': 12, 'fiber_delta': 12, 'lift_q': 0}`
  - reverse: `{'station_role': 'YZ', 'role_pair': 'IW/YZ', 'role_class': 'reverse_partner', 'from_A': 3, 'from_B': 14, 'from_C': 2, 'from_slot': 14, 'to_A': 3, 'to_B': 2, 'to_C': 14, 'to_slot': 2, 'integer_C_delta': 12, 'C_delta': 12, 'fiber_delta': 12, 'lift_q': 0}`
- key=('IW/YZ', 5, 0) shared=IW reverse=YZ
  - shared: `{'station_role': 'IW', 'role_pair': 'IW/YZ', 'role_class': 'shared_B', 'from_A': 12, 'from_B': 2, 'from_C': 5, 'from_slot': 2, 'to_A': 1, 'to_B': 2, 'to_C': 0, 'to_slot': 2, 'integer_C_delta': -5, 'C_delta': 10, 'fiber_delta': 55, 'lift_q': 3}`
  - reverse: `{'station_role': 'YZ', 'role_pair': 'IW/YZ', 'role_class': 'reverse_partner', 'from_A': 10, 'from_B': 0, 'from_C': 5, 'from_slot': 0, 'to_A': 10, 'to_B': 5, 'to_C': 0, 'to_slot': 5, 'integer_C_delta': -5, 'C_delta': 10, 'fiber_delta': 55, 'lift_q': 3}`
- key=('IW/YZ', 5, 2) shared=IW reverse=YZ
  - shared: `{'station_role': 'IW', 'role_pair': 'IW/YZ', 'role_class': 'shared_B', 'from_A': 10, 'from_B': 4, 'from_C': 5, 'from_slot': 4, 'to_A': 3, 'to_B': 4, 'to_C': 2, 'to_slot': 4, 'integer_C_delta': -3, 'C_delta': 12, 'fiber_delta': 57, 'lift_q': 3}`
  - reverse: `{'station_role': 'YZ', 'role_pair': 'IW/YZ', 'role_class': 'reverse_partner', 'from_A': 12, 'from_B': 2, 'from_C': 5, 'from_slot': 2, 'to_A': 12, 'to_B': 5, 'to_C': 2, 'to_slot': 5, 'integer_C_delta': -3, 'C_delta': 12, 'fiber_delta': 57, 'lift_q': 3}`
- key=('TI/XY', 11, 2) shared=XY reverse=TI
  - shared: `{'station_role': 'XY', 'role_pair': 'TI/XY', 'role_class': 'shared_B', 'from_A': 7, 'from_B': 14, 'from_C': 11, 'from_slot': 14, 'to_A': 3, 'to_B': 14, 'to_C': 2, 'to_slot': 14, 'integer_C_delta': -9, 'C_delta': 6, 'fiber_delta': 51, 'lift_q': 3}`
  - reverse: `{'station_role': 'TI', 'role_pair': 'TI/XY', 'role_class': 'reverse_partner', 'from_A': 1, 'from_B': 2, 'from_C': 11, 'from_slot': 2, 'to_A': 1, 'to_B': 11, 'to_C': 2, 'to_slot': 11, 'integer_C_delta': -9, 'C_delta': 6, 'fiber_delta': 51, 'lift_q': 3}`
- key=('TI/XY', 13, 1) shared=XY reverse=TI
  - shared: `{'station_role': 'XY', 'role_pair': 'TI/XY', 'role_class': 'shared_B', 'from_A': 9, 'from_B': 10, 'from_C': 13, 'from_slot': 10, 'to_A': 0, 'to_B': 10, 'to_C': 1, 'to_slot': 10, 'integer_C_delta': -12, 'C_delta': 3, 'fiber_delta': 48, 'lift_q': 3}`
  - reverse: `{'station_role': 'TI', 'role_pair': 'TI/XY', 'role_class': 'reverse_partner', 'from_A': 2, 'from_B': 1, 'from_C': 13, 'from_slot': 1, 'to_A': 2, 'to_B': 13, 'to_C': 1, 'to_slot': 13, 'integer_C_delta': -12, 'C_delta': 3, 'fiber_delta': 48, 'lift_q': 3}`
- key=('TI/XY', 2, 5) shared=XY reverse=TI
  - shared: `{'station_role': 'XY', 'role_pair': 'TI/XY', 'role_class': 'shared_B', 'from_A': 1, 'from_B': 0, 'from_C': 2, 'from_slot': 0, 'to_A': 10, 'to_B': 0, 'to_C': 5, 'to_slot': 0, 'integer_C_delta': 3, 'C_delta': 3, 'fiber_delta': 3, 'lift_q': 0}`
  - reverse: `{'station_role': 'TI', 'role_pair': 'TI/XY', 'role_class': 'reverse_partner', 'from_A': 12, 'from_B': 5, 'from_C': 2, 'from_slot': 5, 'to_A': 12, 'to_B': 2, 'to_C': 5, 'to_slot': 2, 'integer_C_delta': 3, 'C_delta': 3, 'fiber_delta': 3, 'lift_q': 0}`
- key=('TI/XY', 4, 5) shared=XY reverse=TI
  - shared: `{'station_role': 'XY', 'role_pair': 'TI/XY', 'role_class': 'shared_B', 'from_A': 3, 'from_B': 2, 'from_C': 4, 'from_slot': 2, 'to_A': 12, 'to_B': 2, 'to_C': 5, 'to_slot': 2, 'integer_C_delta': 1, 'C_delta': 1, 'fiber_delta': 1, 'lift_q': 0}`
  - reverse: `{'station_role': 'TI', 'role_pair': 'TI/XY', 'role_class': 'reverse_partner', 'from_A': 10, 'from_B': 5, 'from_C': 4, 'from_slot': 5, 'to_A': 10, 'to_B': 4, 'to_C': 5, 'to_slot': 4, 'integer_C_delta': 1, 'C_delta': 1, 'fiber_delta': 1, 'lift_q': 0}`
- key=('WX/ZT', 0, 2) shared=ZT reverse=WX
  - shared: `{'station_role': 'ZT', 'role_pair': 'WX/ZT', 'role_class': 'shared_B', 'from_A': 10, 'from_B': 5, 'from_C': 0, 'from_slot': 5, 'to_A': 12, 'to_B': 5, 'to_C': 2, 'to_slot': 5, 'integer_C_delta': 2, 'C_delta': 2, 'fiber_delta': 2, 'lift_q': 0}`
  - reverse: `{'station_role': 'WX', 'role_pair': 'WX/ZT', 'role_class': 'reverse_partner', 'from_A': 1, 'from_B': 2, 'from_C': 0, 'from_slot': 2, 'to_A': 1, 'to_B': 0, 'to_C': 2, 'to_slot': 0, 'integer_C_delta': 2, 'C_delta': 2, 'fiber_delta': 2, 'lift_q': 0}`
- key=('WX/ZT', 10, 13) shared=ZT reverse=WX
  - shared: `{'station_role': 'ZT', 'role_pair': 'WX/ZT', 'role_class': 'shared_B', 'from_A': 0, 'from_B': 1, 'from_C': 10, 'from_slot': 1, 'to_A': 2, 'to_B': 1, 'to_C': 13, 'to_slot': 1, 'integer_C_delta': 3, 'C_delta': 3, 'fiber_delta': 3, 'lift_q': 0}`
  - reverse: `{'station_role': 'WX', 'role_pair': 'WX/ZT', 'role_class': 'reverse_partner', 'from_A': 9, 'from_B': 13, 'from_C': 10, 'from_slot': 13, 'to_A': 9, 'to_B': 10, 'to_C': 13, 'to_slot': 10, 'integer_C_delta': 3, 'C_delta': 3, 'fiber_delta': 3, 'lift_q': 0}`
- key=('WX/ZT', 14, 11) shared=ZT reverse=WX
  - shared: `{'station_role': 'ZT', 'role_pair': 'WX/ZT', 'role_class': 'shared_B', 'from_A': 3, 'from_B': 2, 'from_C': 14, 'from_slot': 2, 'to_A': 1, 'to_B': 2, 'to_C': 11, 'to_slot': 2, 'integer_C_delta': -3, 'C_delta': 12, 'fiber_delta': 57, 'lift_q': 3}`
  - reverse: `{'station_role': 'WX', 'role_pair': 'WX/ZT', 'role_class': 'reverse_partner', 'from_A': 7, 'from_B': 11, 'from_C': 14, 'from_slot': 11, 'to_A': 7, 'to_B': 14, 'to_C': 11, 'to_slot': 14, 'integer_C_delta': -3, 'C_delta': 12, 'fiber_delta': 57, 'lift_q': 3}`
- key=('WX/ZT', 2, 4) shared=ZT reverse=WX
  - shared: `{'station_role': 'ZT', 'role_pair': 'WX/ZT', 'role_class': 'shared_B', 'from_A': 12, 'from_B': 5, 'from_C': 2, 'from_slot': 5, 'to_A': 10, 'to_B': 5, 'to_C': 4, 'to_slot': 5, 'integer_C_delta': 2, 'C_delta': 2, 'fiber_delta': 2, 'lift_q': 0}`
  - reverse: `{'station_role': 'WX', 'role_pair': 'WX/ZT', 'role_class': 'reverse_partner', 'from_A': 3, 'from_B': 4, 'from_C': 2, 'from_slot': 4, 'to_A': 3, 'to_B': 2, 'to_C': 4, 'to_slot': 2, 'integer_C_delta': 2, 'C_delta': 2, 'fiber_delta': 2, 'lift_q': 0}`

## Boundary

This audits realized reciprocal pairs only. It does not generate the pair set from a non-realized candidate universe and does not close Gap A.
