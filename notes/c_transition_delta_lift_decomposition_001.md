# C-transition delta lift decomposition 001

Status: c_transition_delta_lift_decomposition_found

## Purpose

Decompose the exact C-transition overlay delta rule into base C motion modulo 15 plus a four-sheet lift choice.

## Summary

- row_count: 24
- transition_group_count: 12
- all_deltas_match_c_delta_mod15: true
- bad_mod15_count: 0
- lift_q_counts: {"0": 14, "3": 10}
- lift_q_by_label: {"reverse_partner": {"0": 7, "3": 5}, "shared_B": {"0": 7, "3": 5}}
- lift_q_by_role: {"IW": {"0": 2, "3": 2}, "TI": {"0": 2, "3": 2}, "WX": {"0": 3, "3": 1}, "XY": {"0": 2, "3": 2}, "YZ": {"0": 2, "3": 2}, "ZT": {"0": 3, "3": 1}}
- lift_q_by_c_delta: {"1": {"0": 2}, "10": {"3": 2}, "12": {"0": 2, "3": 4}, "2": {"0": 4}, "3": {"0": 4, "3": 2}, "6": {"3": 2}, "9": {"0": 2}}
- transition_table: {"(0, 2)": {"c_delta_mod15": 2, "fiber_delta_mod60": 2, "lift_q_mod4": 0}, "(1, 10)": {"c_delta_mod15": 9, "fiber_delta_mod60": 9, "lift_q_mod4": 0}, "(10, 13)": {"c_delta_mod15": 3, "fiber_delta_mod60": 3, "lift_q_mod4": 0}, "(11, 2)": {"c_delta_mod15": 6, "fiber_delta_mod60": 51, "lift_q_mod4": 3}, "(13, 1)": {"c_delta_mod15": 3, "fiber_delta_mod60": 48, "lift_q_mod4": 3}, "(14, 11)": {"c_delta_mod15": 12, "fiber_delta_mod60": 57, "lift_q_mod4": 3}, "(2, 14)": {"c_delta_mod15": 12, "fiber_delta_mod60": 12, "lift_q_mod4": 0}, "(2, 4)": {"c_delta_mod15": 2, "fiber_delta_mod60": 2, "lift_q_mod4": 0}, "(2, 5)": {"c_delta_mod15": 3, "fiber_delta_mod60": 3, "lift_q_mod4": 0}, "(4, 5)": {"c_delta_mod15": 1, "fiber_delta_mod60": 1, "lift_q_mod4": 0}, "(5, 0)": {"c_delta_mod15": 10, "fiber_delta_mod60": 55, "lift_q_mod4": 3}, "(5, 2)": {"c_delta_mod15": 12, "fiber_delta_mod60": 57, "lift_q_mod4": 3}}
- interpretation: "Each WXYZTI overlay fiber delta decomposes as base C motion modulo 15 plus a Z4 lift sheet choice."
- gap_a_closed: false
- full_g900_admission_found: false
- next_step: "derive_lift_q_from_native_g60_context"

## Boundary

- This decomposes the overlay delta rule.
- It does not yet derive the Z4 lift choice from native G60 structure.
- It does not close Gap A.
- It does not prove full G900.

## Checks

- PASS source_loaded: c_transition_overlay_delta_generator_found
- PASS row_count_24: 24
- PASS all_predictions_match: all prediction rows match
- PASS all_deltas_match_c_delta_mod15: []
- PASS transition_group_count_12: 12
- PASS no_gap_a_claim_made: decomposition only
