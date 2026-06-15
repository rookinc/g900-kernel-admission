# WXYZTI station transition feature inspection 009

Status: wxyzti_station_transition_feature_inspection_recorded

## Output

- raw_row_count: `72`
- semantic_pair_role_row_count: `24`
- expected_pair_role_row_count: `24`
- nonexpected_pair_role_row_count: `0`
- role_counts: `{'IW': 4, 'TI': 4, 'WX': 4, 'XY': 4, 'YZ': 4, 'ZT': 4}`
- expected_role_counts: `{'IW': 4, 'TI': 4, 'WX': 4, 'XY': 4, 'YZ': 4, 'ZT': 4}`
- nonexpected_role_counts: `{}`

## Top feature summaries

- from_B: expected_distinct=9, nonexpected_distinct=0, shared=0, expected_only=9, nonexpected_only=0
- from_C: expected_distinct=9, nonexpected_distinct=0, shared=0, expected_only=9, nonexpected_only=0
- from_fiber: expected_distinct=9, nonexpected_distinct=0, shared=0, expected_only=9, nonexpected_only=0
- from_slot: expected_distinct=9, nonexpected_distinct=0, shared=0, expected_only=9, nonexpected_only=0
- to_B: expected_distinct=9, nonexpected_distinct=0, shared=0, expected_only=9, nonexpected_only=0
- to_C: expected_distinct=9, nonexpected_distinct=0, shared=0, expected_only=9, nonexpected_only=0
- to_fiber: expected_distinct=9, nonexpected_distinct=0, shared=0, expected_only=9, nonexpected_only=0
- to_slot: expected_distinct=9, nonexpected_distinct=0, shared=0, expected_only=9, nonexpected_only=0
- from_A: expected_distinct=8, nonexpected_distinct=0, shared=0, expected_only=8, nonexpected_only=0
- to_A: expected_distinct=8, nonexpected_distinct=0, shared=0, expected_only=8, nonexpected_only=0
- edge_role: expected_distinct=6, nonexpected_distinct=0, shared=0, expected_only=6, nonexpected_only=0
- label: expected_distinct=2, nonexpected_distinct=0, shared=0, expected_only=2, nonexpected_only=0

## Boundary

This is a schema/feature inspection. It does not prove a generator and does not close Gap A.

## Reading

This is a schema/provenance inspection, not a selector.

The scanned artifacts only contain realized WXYZTI station-role transition rows. They do not contain a generated universe of nonexpected role-compatible candidate pairs.

Therefore nonexpected_pair_role_row_count = 0 should not be read as a proof that station features select the expected rows from all possible rows.

The useful result is that the 24 realized semantic rows expose station/provenance fields such as from_A, from_B, from_C, from_slot, from_fiber, to_A, to_B, to_C, to_slot, and to_fiber.

The next task is to inspect whether the realized rows obey simple provenance laws by station role, role class, role pair, or source fields.

## Reading

This is a schema/provenance inspection, not a selector.

The scanned artifacts only contain realized WXYZTI station-role transition rows. They do not contain a generated universe of nonexpected role-compatible candidate pairs.

Therefore nonexpected_pair_role_row_count = 0 should not be read as a proof that station features select the expected rows from all possible rows.

The useful result is that the 24 realized semantic rows expose station/provenance fields such as from_A, from_B, from_C, from_slot, from_fiber, to_A, to_B, to_C, to_slot, and to_fiber.

The next task is to inspect whether the realized rows obey simple provenance laws by station role, role class, role pair, or source fields.
