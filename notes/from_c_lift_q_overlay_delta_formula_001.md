# from_C lift-q overlay delta formula 001

Status: from_c_lift_q_overlay_delta_formula_found

## Formula

fiber_delta = (to_C - from_C) mod 15 + 15*q(from_C) mod 60

## Summary

- row_count: 24
- from_c_group_count: 9
- from_c_counts: {"0": 2, "1": 2, "10": 2, "11": 2, "13": 2, "14": 2, "2": 6, "4": 2, "5": 4}
- from_c_to_q_rule: {"0": 0, "1": 0, "10": 0, "11": 3, "13": 3, "14": 3, "2": 0, "4": 0, "5": 3}
- rule_q_counts: {"0": 5, "3": 4}
- row_q_counts: {"0": 14, "3": 10}
- ambiguous_from_c_count: 0
- prediction_match_count: 24
- prediction_exact: true
- formula: "fiber_delta = (to_C - from_C) mod 15 + 15*q(from_C) mod 60"
- interpretation: "In the observed WXYZTI overlay rows, the Z4 lift choice q is determined by from_C alone."
- gap_a_closed: false
- full_g900_admission_found: false
- next_step: "derive_from_c_lift_partition_from_native_g60_structure"

## Boundary

- This records an exact formula over station C coordinates.
- It does not yet derive the from_C partition from native G60 structure.
- It does not close Gap A.
- It does not prove full G900.

## Checks

- PASS decomposition_loaded: c_transition_delta_lift_decomposition_found
- PASS context_loaded: lift_q_context_rule_found
- PASS row_count_24: 24
- PASS from_c_rule_unambiguous: {}
- PASS from_c_rule_nonempty: {'0': 0, '1': 0, '2': 0, '4': 0, '5': 3, '10': 0, '11': 3, '13': 3, '14': 3}
- PASS formula_predicts_all_rows: {'match_count': 24, 'row_count': 24}
- PASS q_values_only_0_3: {3: 10, 0: 14}
- PASS no_gap_a_claim_made: formula rule only
