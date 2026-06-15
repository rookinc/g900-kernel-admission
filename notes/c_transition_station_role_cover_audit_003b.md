# C-transition station-role cover audit 003b

Status: c_transition_station_role_cover_audit_recorded

## Output

- raw_station_role_row_count: `72`
- semantic_station_role_row_count: `24`
- canonical_transition_count: `12`
- station_role_counts: `{'IW': 4, 'TI': 4, 'WX': 4, 'XY': 4, 'YZ': 4, 'ZT': 4}`
- role_class_counts: `{'reverse_partner': 12, 'shared_B': 12}`
- q_counts_by_transition_type: `{0: 7, 3: 5}`
- all_pairs_have_two_station_roles: `True`
- all_pairs_have_one_diad_one_coupler: `True`
- all_pairs_have_expected_delta_somewhere: `True`
- station_role_cover_confirmed: `True`

## Role-class rule

- reverse_partner: `['TI', 'WX', 'YZ']`
- shared_B: `['IW', 'XY', 'ZT']`

## Pair rows

- (0, 2) -> 2 q=0 station_roles=['WX', 'ZT'] role_classes=['reverse_partner', 'shared_B'] exact_delta_roles=2
- (1, 10) -> 9 q=0 station_roles=['IW', 'YZ'] role_classes=['reverse_partner', 'shared_B'] exact_delta_roles=2
- (2, 4) -> 2 q=0 station_roles=['WX', 'ZT'] role_classes=['reverse_partner', 'shared_B'] exact_delta_roles=2
- (2, 5) -> 3 q=0 station_roles=['TI', 'XY'] role_classes=['reverse_partner', 'shared_B'] exact_delta_roles=2
- (2, 14) -> 12 q=0 station_roles=['IW', 'YZ'] role_classes=['reverse_partner', 'shared_B'] exact_delta_roles=2
- (4, 5) -> 1 q=0 station_roles=['TI', 'XY'] role_classes=['reverse_partner', 'shared_B'] exact_delta_roles=2
- (5, 0) -> 55 q=3 station_roles=['IW', 'YZ'] role_classes=['reverse_partner', 'shared_B'] exact_delta_roles=2
- (5, 2) -> 57 q=3 station_roles=['IW', 'YZ'] role_classes=['reverse_partner', 'shared_B'] exact_delta_roles=2
- (10, 13) -> 3 q=0 station_roles=['WX', 'ZT'] role_classes=['reverse_partner', 'shared_B'] exact_delta_roles=2
- (11, 2) -> 51 q=3 station_roles=['TI', 'XY'] role_classes=['reverse_partner', 'shared_B'] exact_delta_roles=2
- (13, 1) -> 48 q=3 station_roles=['TI', 'XY'] role_classes=['reverse_partner', 'shared_B'] exact_delta_roles=2
- (14, 11) -> 57 q=3 station_roles=['WX', 'ZT'] role_classes=['reverse_partner', 'shared_B'] exact_delta_roles=2

## Boundary

This clarifies WXYZTI overlay multiplicity. It does not derive the 12 C-transitions from native G60 structure and does not close Gap A.
