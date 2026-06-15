# WXYZTI ambiguous source split audit 014

Status: wxyzti_ambiguous_source_split_audit_recorded

## Base tests

- keys=['role_pair', 'from_C'] -> to_C: deterministic=False, groups=11, ambiguous=1
- keys=['station_role', 'from_C'] -> to_C: deterministic=False, groups=22, ambiguous=2
- keys=['role_pair', 'from_C'] -> integer_C_delta: deterministic=False, groups=11, ambiguous=1
- keys=['station_role', 'from_C'] -> integer_C_delta: deterministic=False, groups=22, ambiguous=2
- keys=['role_pair', 'from_C'] -> C_delta: deterministic=False, groups=11, ambiguous=1
- keys=['station_role', 'from_C'] -> C_delta: deterministic=False, groups=22, ambiguous=2

## Focus groups

- role_pair_IW_YZ_from_C_5
  - row_count: `4`
  - to_C_values: `[0, 2]`
  - station_role_counts: `{'IW': 2, 'YZ': 2}`
  - from_A_counts: `{10: 2, 12: 2}`
  - from_B_counts: `{0: 1, 2: 2, 4: 1}`
  - to_A_counts: `{1: 1, 3: 1, 10: 1, 12: 1}`
  - to_B_counts: `{2: 1, 4: 1, 5: 2}`
  - integer_C_delta_counts: `{-5: 2, -3: 2}`
  - rows:
    - `{'station_role': 'IW', 'role_class': 'shared_B', 'role_pair': 'IW/YZ', 'from_A': 12, 'from_B': 2, 'from_C': 5, 'to_A': 1, 'to_B': 2, 'to_C': 0, 'from_slot': 2, 'to_slot': 2, 'from_fiber': 5, 'to_fiber': 0, 'integer_C_delta': -5, 'C_delta': 10, 'fiber_delta': 55, 'C_wrap_flag': True, 'lift_q': 3}`
    - `{'station_role': 'IW', 'role_class': 'shared_B', 'role_pair': 'IW/YZ', 'from_A': 10, 'from_B': 4, 'from_C': 5, 'to_A': 3, 'to_B': 4, 'to_C': 2, 'from_slot': 4, 'to_slot': 4, 'from_fiber': 5, 'to_fiber': 2, 'integer_C_delta': -3, 'C_delta': 12, 'fiber_delta': 57, 'C_wrap_flag': True, 'lift_q': 3}`
    - `{'station_role': 'YZ', 'role_class': 'reverse_partner', 'role_pair': 'IW/YZ', 'from_A': 10, 'from_B': 0, 'from_C': 5, 'to_A': 10, 'to_B': 5, 'to_C': 0, 'from_slot': 0, 'to_slot': 5, 'from_fiber': 5, 'to_fiber': 0, 'integer_C_delta': -5, 'C_delta': 10, 'fiber_delta': 55, 'C_wrap_flag': True, 'lift_q': 3}`
    - `{'station_role': 'YZ', 'role_class': 'reverse_partner', 'role_pair': 'IW/YZ', 'from_A': 12, 'from_B': 2, 'from_C': 5, 'to_A': 12, 'to_B': 5, 'to_C': 2, 'from_slot': 2, 'to_slot': 5, 'from_fiber': 5, 'to_fiber': 2, 'integer_C_delta': -3, 'C_delta': 12, 'fiber_delta': 57, 'C_wrap_flag': True, 'lift_q': 3}`
  - minimal splitters to to_C:
    - keys=['C_delta'], groups=2, group_sizes={2: 2}
    - keys=['integer_C_delta'], groups=2, group_sizes={2: 2}
    - keys=['to_fiber'], groups=2, group_sizes={2: 2}
    - keys=['to_A'], groups=4, group_sizes={1: 4}

## Ambiguous station_role/from_C sources

- station_role=IW, from_C=5, rows=2, to_C=[0, 2]
  - `{'station_role': 'IW', 'role_class': 'shared_B', 'role_pair': 'IW/YZ', 'from_A': 12, 'from_B': 2, 'from_C': 5, 'to_A': 1, 'to_B': 2, 'to_C': 0, 'from_slot': 2, 'to_slot': 2, 'from_fiber': 5, 'to_fiber': 0, 'integer_C_delta': -5, 'C_delta': 10, 'fiber_delta': 55, 'C_wrap_flag': True, 'lift_q': 3}`
  - `{'station_role': 'IW', 'role_class': 'shared_B', 'role_pair': 'IW/YZ', 'from_A': 10, 'from_B': 4, 'from_C': 5, 'to_A': 3, 'to_B': 4, 'to_C': 2, 'from_slot': 4, 'to_slot': 4, 'from_fiber': 5, 'to_fiber': 2, 'integer_C_delta': -3, 'C_delta': 12, 'fiber_delta': 57, 'C_wrap_flag': True, 'lift_q': 3}`
  - splitter keys=['C_delta'], groups=2
  - splitter keys=['from_A'], groups=2
  - splitter keys=['from_B'], groups=2
  - splitter keys=['from_slot'], groups=2
  - splitter keys=['integer_C_delta'], groups=2
- station_role=YZ, from_C=5, rows=2, to_C=[0, 2]
  - `{'station_role': 'YZ', 'role_class': 'reverse_partner', 'role_pair': 'IW/YZ', 'from_A': 10, 'from_B': 0, 'from_C': 5, 'to_A': 10, 'to_B': 5, 'to_C': 0, 'from_slot': 0, 'to_slot': 5, 'from_fiber': 5, 'to_fiber': 0, 'integer_C_delta': -5, 'C_delta': 10, 'fiber_delta': 55, 'C_wrap_flag': True, 'lift_q': 3}`
  - `{'station_role': 'YZ', 'role_class': 'reverse_partner', 'role_pair': 'IW/YZ', 'from_A': 12, 'from_B': 2, 'from_C': 5, 'to_A': 12, 'to_B': 5, 'to_C': 2, 'from_slot': 2, 'to_slot': 5, 'from_fiber': 5, 'to_fiber': 2, 'integer_C_delta': -3, 'C_delta': 12, 'fiber_delta': 57, 'C_wrap_flag': True, 'lift_q': 3}`
  - splitter keys=['C_delta'], groups=2
  - splitter keys=['from_A'], groups=2
  - splitter keys=['from_B'], groups=2
  - splitter keys=['from_slot'], groups=2
  - splitter keys=['integer_C_delta'], groups=2

## Boundary

This is still over realized rows only. A splitter here explains a realized ambiguity but does not prove selection from a non-realized candidate universe or close Gap A.
