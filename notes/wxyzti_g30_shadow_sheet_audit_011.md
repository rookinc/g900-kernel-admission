# WXYZTI G30 shadow sheet audit 011

Status: wxyzti_g30_shadow_sheet_audit_recorded

## Output

- row_count: `24`
- all_from_fiber_mod15_equals_from_C: `True`
- all_to_fiber_mod15_equals_to_C: `True`
- all_fiber_mod15_delta_equals_C_delta: `True`
- all_fiber_sheet15_delta_equals_lift_q: `False`
- all_q3_sheet30_rule: `False`
- exact_deterministic_test_count: `50`

## lift_q summary

- lift_q 0: count=14, sheet30_delta_counts={0: 14}, mod30_delta_counts={1: 2, 2: 4, 3: 4, 9: 2, 12: 2}, sheet15_delta_counts={0: 14}, mod15_delta_counts={1: 2, 2: 4, 3: 4, 9: 2, 12: 2}, sheet15_equals_q=14/14, q3_sheet30_rule=14/14
- lift_q 3: count=10, sheet30_delta_counts={0: 10}, mod30_delta_counts={18: 2, 21: 2, 25: 2, 27: 4}, sheet15_delta_counts={0: 10}, mod15_delta_counts={3: 2, 6: 2, 10: 2, 12: 4}, sheet15_equals_q=0/10, q3_sheet30_rule=0/10

## role_pair summary

- IW/YZ: count=8, lift_q_counts={0: 4, 3: 4}, sheet30_delta_counts={0: 8}, mod30_delta_counts={9: 2, 12: 2, 25: 2, 27: 2}
- TI/XY: count=8, lift_q_counts={0: 4, 3: 4}, sheet30_delta_counts={0: 8}, mod30_delta_counts={1: 2, 3: 2, 18: 2, 21: 2}
- WX/ZT: count=8, lift_q_counts={0: 6, 3: 2}, sheet30_delta_counts={0: 8}, mod30_delta_counts={2: 4, 3: 2, 27: 2}

## Reading

If the mod15 and sheet15 checks are all true, the clean structure is G60 as four G15 sheets. If all_q3_sheet30_rule is also true, then the same data has a clean 2xG30 shadow. If not, the G30 interpretation is only partial.

## Boundary

This is a coordinate-shadow audit over realized WXYZTI rows only. It does not prove a complete generator, does not derive G60-native structure, and does not close Gap A.

## Reading update

This refutes the naive 2xG30 sheet-flip interpretation.

All realized rows preserve the 30-sheet and the 15-sheet. Both q=0 and q=3 rows have sheet30_delta=0 and sheet15_delta=0.

Therefore q=3 is not a G30 sheet flip and not a G15 sheet change.

The better interpretation is same-sheet modular wrap:

    q = 0 when the C-coordinate moves forward without wrap.
    q = 3 when the C-coordinate wraps backward inside the same G60 fiber sheet.

The next audit should test whether q=3 is exactly equivalent to to_C < from_C.
