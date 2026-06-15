# C-transition schema inspection 003a

Status: c_transition_schema_inspection_recorded

## Output

- scanned_file_count: `9`
- candidate_row_count: `190`
- with_from_to_count: `142`
- canonical_pair_row_count: `142`
- exact_delta_row_count: `84`

## Canonical pair summary

- (0, 2) expected=2 rows=11 deltas={'base_delta_mod15=2': 3, 'fiber_delta=2': 2, 'predicted_delta=2': 4} roles={'WX': 4, 'ZT': 4, 'none': 3}
- (1, 10) expected=9 rows=12 deltas={'base_delta_mod15=9': 4, 'fiber_delta=2': 1, 'fiber_delta=9': 2, 'predicted_delta=9': 4} roles={'IW': 4, 'YZ': 4, 'none': 4}
- (2, 4) expected=2 rows=11 deltas={'base_delta_mod15=2': 3, 'fiber_delta=2': 2, 'predicted_delta=2': 4} roles={'WX': 4, 'ZT': 4, 'none': 3}
- (2, 5) expected=3 rows=12 deltas={'base_delta_mod15=3': 4, 'fiber_delta=2': 1, 'fiber_delta=3': 2, 'predicted_delta=3': 4} roles={'TI': 4, 'XY': 4, 'none': 4}
- (2, 14) expected=12 rows=12 deltas={'base_delta_mod15=12': 4, 'fiber_delta=12': 2, 'fiber_delta=2': 1, 'predicted_delta=12': 4} roles={'IW': 4, 'YZ': 4, 'none': 4}
- (4, 5) expected=1 rows=12 deltas={'base_delta_mod15=1': 4, 'fiber_delta=1': 2, 'fiber_delta=2': 1, 'predicted_delta=1': 4} roles={'TI': 4, 'XY': 4, 'none': 4}
- (5, 0) expected=55 rows=12 deltas={'base_delta_mod15=10': 4, 'fiber_delta=2': 1, 'fiber_delta=55': 2, 'predicted_delta=55': 4} roles={'IW': 4, 'YZ': 4, 'none': 4}
- (5, 2) expected=57 rows=12 deltas={'base_delta_mod15=12': 4, 'fiber_delta=2': 1, 'fiber_delta=57': 2, 'predicted_delta=57': 4} roles={'IW': 4, 'YZ': 4, 'none': 4}
- (10, 13) expected=3 rows=12 deltas={'base_delta_mod15=3': 4, 'fiber_delta=2': 1, 'fiber_delta=3': 2, 'predicted_delta=3': 4} roles={'WX': 4, 'ZT': 4, 'none': 4}
- (11, 2) expected=51 rows=12 deltas={'base_delta_mod15=6': 4, 'fiber_delta=2': 1, 'fiber_delta=51': 2, 'predicted_delta=51': 4} roles={'TI': 4, 'XY': 4, 'none': 4}
- (13, 1) expected=48 rows=12 deltas={'base_delta_mod15=3': 4, 'fiber_delta=2': 1, 'fiber_delta=48': 2, 'predicted_delta=48': 4} roles={'TI': 4, 'XY': 4, 'none': 4}
- (14, 11) expected=57 rows=12 deltas={'base_delta_mod15=12': 4, 'fiber_delta=2': 1, 'fiber_delta=57': 2, 'predicted_delta=57': 4} roles={'WX': 4, 'ZT': 4, 'none': 4}

## Reading

Use this before the two-cover audit. If exact_delta_row_count is 0, the previous audit failed because the expected fiber delta is not stored beside the C pair in the scanned artifacts.
