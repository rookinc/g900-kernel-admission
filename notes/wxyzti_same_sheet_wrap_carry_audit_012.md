# WXYZTI same-sheet wrap-carry audit 012

Status: wxyzti_same_sheet_wrap_carry_audit_recorded

## Output

- row_count: `24`
- all_same_sheet15: `True`
- all_same_sheet30: `True`
- all_predicted_lift_q_matches: `True`
- all_predicted_fiber_delta_matches: `True`
- wrap_flag_counts: `{False: 14, True: 10}`
- lift_q_counts: `{0: 14, 3: 10}`
- integer_C_delta_counts: `{-12: 2, -9: 2, -5: 2, -3: 4, 1: 2, 2: 4, 3: 4, 9: 2, 12: 2}`

## Law

For realized WXYZTI rows, endpoints preserve the same 15-sheet and 30-sheet. The lift q is determined by ordinary integer C wrap: q=0 when to_C-from_C >= 0, q=3 when to_C-from_C < 0. The fiber delta is (to_C-from_C) mod 60.

## Role-pair summary

- IW/YZ: count=8, lift_q_counts={0: 4, 3: 4}, wrap_flag_counts={False: 4, True: 4}, predicted_q_match=8/8, predicted_delta_match=8/8
- TI/XY: count=8, lift_q_counts={0: 4, 3: 4}, wrap_flag_counts={False: 4, True: 4}, predicted_q_match=8/8, predicted_delta_match=8/8
- WX/ZT: count=8, lift_q_counts={0: 6, 3: 2}, wrap_flag_counts={False: 6, True: 2}, predicted_q_match=8/8, predicted_delta_match=8/8

## Boundary

This is an exact law over realized WXYZTI station rows. It does not generate the allowed transitions from a larger candidate universe, does not derive G60-native structure, and does not close Gap A.
