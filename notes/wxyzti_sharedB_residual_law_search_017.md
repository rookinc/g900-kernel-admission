# WXYZTI shared_B residual law search 017

Status: wxyzti_sharedB_residual_law_search_recorded

## Output

- sharedB_row_count: `12`
- station_role_counts: `{'IW': 4, 'XY': 4, 'ZT': 4}`
- source_side_roles_with_exact_law: `1`

## Shared_B named laws

- to_C = from_B + 3: matches=3/12, exact=False
- to_C = from_B - 3: matches=3/12, exact=False
- to_C = from_slot + 3: matches=3/12, exact=False
- to_C = from_slot - 3: matches=3/12, exact=False
- to_C = from_A - 2: matches=2/12, exact=False
- to_C = from_B - 2: matches=2/12, exact=False
- to_C = from_slot - 2: matches=2/12, exact=False
- to_C = from_A + 2: matches=1/12, exact=False
- to_C = from_A + 3: matches=1/12, exact=False
- to_C = from_B - 1: matches=1/12, exact=False

## Role results

- IW
  - row_count: `4`
  - source_side_exact_law_count: `6`
  - with_target_side_exact_law_count: `0`
  - rows:
    - `{'station_role': 'IW', 'role_pair': 'IW/YZ', 'role_class': 'shared_B', 'from_A': 2, 'from_B': 13, 'from_C': 1, 'from_slot': 13, 'to_A': 9, 'to_B': 13, 'to_C': 10, 'to_slot': 13, 'integer_C_delta': 9, 'C_delta': 9, 'lift_q': 0}`
    - `{'station_role': 'IW', 'role_pair': 'IW/YZ', 'role_class': 'shared_B', 'from_A': 1, 'from_B': 11, 'from_C': 2, 'from_slot': 11, 'to_A': 7, 'to_B': 11, 'to_C': 14, 'to_slot': 11, 'integer_C_delta': 12, 'C_delta': 12, 'lift_q': 0}`
    - `{'station_role': 'IW', 'role_pair': 'IW/YZ', 'role_class': 'shared_B', 'from_A': 12, 'from_B': 2, 'from_C': 5, 'from_slot': 2, 'to_A': 1, 'to_B': 2, 'to_C': 0, 'to_slot': 2, 'integer_C_delta': -5, 'C_delta': 10, 'lift_q': 3}`
    - `{'station_role': 'IW', 'role_pair': 'IW/YZ', 'role_class': 'shared_B', 'from_A': 10, 'from_B': 4, 'from_C': 5, 'from_slot': 4, 'to_A': 3, 'to_B': 4, 'to_C': 2, 'to_slot': 4, 'integer_C_delta': -3, 'C_delta': 12, 'lift_q': 3}`
  - named laws:
    - to_C = from_B - 2: matches=2/4, exact=False
    - to_C = from_slot - 2: matches=2/4, exact=False
    - to_C = from_A + 3: matches=1/4, exact=False
    - to_C = from_A - 2: matches=1/4, exact=False
    - to_C = from_B + 3: matches=1/4, exact=False
    - to_C = from_B - 3: matches=1/4, exact=False
    - to_C = from_slot + 3: matches=1/4, exact=False
    - to_C = from_slot - 3: matches=1/4, exact=False
  - source-side affine laws:
    - 2*from_A + 12*from_C + 3*from_slot mod 15
    - 2*from_A + 3*from_B + 12*from_C mod 15
    - 2*from_A + 3*from_B + 12*from_fiber_mod15 mod 15
    - 2*from_A + 3*from_B + 12*from_fiber_mod30 mod 15
    - 2*from_A + 3*from_slot + 12*from_fiber_mod15 mod 15
    - 2*from_A + 3*from_slot + 12*from_fiber_mod30 mod 15
  - with-target-side affine laws:
    - none
- XY
  - row_count: `4`
  - source_side_exact_law_count: `0`
  - with_target_side_exact_law_count: `0`
  - rows:
    - `{'station_role': 'XY', 'role_pair': 'TI/XY', 'role_class': 'shared_B', 'from_A': 1, 'from_B': 0, 'from_C': 2, 'from_slot': 0, 'to_A': 10, 'to_B': 0, 'to_C': 5, 'to_slot': 0, 'integer_C_delta': 3, 'C_delta': 3, 'lift_q': 0}`
    - `{'station_role': 'XY', 'role_pair': 'TI/XY', 'role_class': 'shared_B', 'from_A': 3, 'from_B': 2, 'from_C': 4, 'from_slot': 2, 'to_A': 12, 'to_B': 2, 'to_C': 5, 'to_slot': 2, 'integer_C_delta': 1, 'C_delta': 1, 'lift_q': 0}`
    - `{'station_role': 'XY', 'role_pair': 'TI/XY', 'role_class': 'shared_B', 'from_A': 7, 'from_B': 14, 'from_C': 11, 'from_slot': 14, 'to_A': 3, 'to_B': 14, 'to_C': 2, 'to_slot': 14, 'integer_C_delta': -9, 'C_delta': 6, 'lift_q': 3}`
    - `{'station_role': 'XY', 'role_pair': 'TI/XY', 'role_class': 'shared_B', 'from_A': 9, 'from_B': 10, 'from_C': 13, 'from_slot': 10, 'to_A': 0, 'to_B': 10, 'to_C': 1, 'to_slot': 10, 'integer_C_delta': -12, 'C_delta': 3, 'lift_q': 3}`
  - named laws:
    - to_C = from_B + 3: matches=2/4, exact=False
    - to_C = from_slot + 3: matches=2/4, exact=False
    - to_C = from_A + 2: matches=1/4, exact=False
    - to_C = from_A: matches=0/4, exact=False
    - to_C = from_A + 1: matches=0/4, exact=False
    - to_C = from_A + 3: matches=0/4, exact=False
    - to_C = from_A - 1: matches=0/4, exact=False
    - to_C = from_A - 2: matches=0/4, exact=False
  - source-side affine laws:
    - none
  - with-target-side affine laws:
    - none
- ZT
  - row_count: `4`
  - source_side_exact_law_count: `0`
  - with_target_side_exact_law_count: `0`
  - rows:
    - `{'station_role': 'ZT', 'role_pair': 'WX/ZT', 'role_class': 'shared_B', 'from_A': 10, 'from_B': 5, 'from_C': 0, 'from_slot': 5, 'to_A': 12, 'to_B': 5, 'to_C': 2, 'to_slot': 5, 'integer_C_delta': 2, 'C_delta': 2, 'lift_q': 0}`
    - `{'station_role': 'ZT', 'role_pair': 'WX/ZT', 'role_class': 'shared_B', 'from_A': 12, 'from_B': 5, 'from_C': 2, 'from_slot': 5, 'to_A': 10, 'to_B': 5, 'to_C': 4, 'to_slot': 5, 'integer_C_delta': 2, 'C_delta': 2, 'lift_q': 0}`
    - `{'station_role': 'ZT', 'role_pair': 'WX/ZT', 'role_class': 'shared_B', 'from_A': 0, 'from_B': 1, 'from_C': 10, 'from_slot': 1, 'to_A': 2, 'to_B': 1, 'to_C': 13, 'to_slot': 1, 'integer_C_delta': 3, 'C_delta': 3, 'lift_q': 0}`
    - `{'station_role': 'ZT', 'role_pair': 'WX/ZT', 'role_class': 'shared_B', 'from_A': 3, 'from_B': 2, 'from_C': 14, 'from_slot': 2, 'to_A': 1, 'to_B': 2, 'to_C': 11, 'to_slot': 2, 'integer_C_delta': -3, 'C_delta': 12, 'lift_q': 3}`
  - named laws:
    - to_C = from_B - 3: matches=2/4, exact=False
    - to_C = from_slot - 3: matches=2/4, exact=False
    - to_C = from_A - 2: matches=1/4, exact=False
    - to_C = from_B - 1: matches=1/4, exact=False
    - to_C = from_slot - 1: matches=1/4, exact=False
    - to_C = from_A: matches=0/4, exact=False
    - to_C = from_A + 1: matches=0/4, exact=False
    - to_C = from_A + 2: matches=0/4, exact=False
  - source-side affine laws:
    - none
  - with-target-side affine laws:
    - none

## Boundary

This is over realized rows only. Role-specific affine laws may be descriptive or overfit; they do not prove selection from non-realized candidates and do not close Gap A.
