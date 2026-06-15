# Lift q context rules 001

Status: lift_q_context_rule_found

## Purpose

Search which small context features determine the Z4 lift choice q in the C-transition overlay delta decomposition.

## Summary

- row_count: 24
- q_counts: {"0": 14, "3": 10}
- tested_feature_sets: 9108
- exact_feature_set_count: 3239
- least_exact_feature_sets: [{"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["c_transition_key"], "group_count": 12}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["a_delta_mod15", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["b_delta_mod15", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_A", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_B", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "from_columns_key"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "same_A"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "same_B"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "same_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "same_columns"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "same_slot"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "to_columns_key"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_slot", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["slot_delta_mod15", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["to_A", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["to_B", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["to_slot", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["a_delta_mod15", "c_transition_key"], "group_count": 12}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["b_delta_mod15", "c_transition_key"], "group_count": 12}]
- best_near_miss_feature_sets: [{"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["c_transition_key"], "group_count": 12}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["a_delta_mod15", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["b_delta_mod15", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_A", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_B", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "from_columns_key"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "same_A"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "same_B"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "same_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "same_columns"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "same_slot"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_C", "to_columns_key"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["from_slot", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["slot_delta_mod15", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["to_A", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["to_B", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["to_slot", "from_C"], "group_count": 9}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["a_delta_mod15", "c_transition_key"], "group_count": 12}, {"ambiguous_group_count": 0, "ambiguous_groups_sample": {}, "exact": true, "features": ["b_delta_mod15", "c_transition_key"], "group_count": 12}]
- q_by_label: {"reverse_partner": {"0": 7, "3": 5}, "shared_B": {"0": 7, "3": 5}}
- q_by_role: {"IW": {"0": 2, "3": 2}, "TI": {"0": 2, "3": 2}, "WX": {"0": 3, "3": 1}, "XY": {"0": 2, "3": 2}, "YZ": {"0": 2, "3": 2}, "ZT": {"0": 3, "3": 1}}
- q_by_c_transition: {"(0, 2)": {"0": 2}, "(1, 10)": {"0": 2}, "(10, 13)": {"0": 2}, "(11, 2)": {"3": 2}, "(13, 1)": {"3": 2}, "(14, 11)": {"3": 2}, "(2, 14)": {"0": 2}, "(2, 4)": {"0": 2}, "(2, 5)": {"0": 2}, "(4, 5)": {"0": 2}, "(5, 0)": {"3": 2}, "(5, 2)": {"3": 2}}
- q_by_c_delta: {"1": {"0": 2}, "10": {"3": 2}, "12": {"0": 2, "3": 4}, "2": {"0": 4}, "3": {"0": 4, "3": 2}, "6": {"3": 2}, "9": {"0": 2}}
- q_by_from_C: {"0": {"0": 2}, "1": {"0": 2}, "10": {"0": 2}, "11": {"3": 2}, "13": {"3": 2}, "14": {"3": 2}, "2": {"0": 6}, "4": {"0": 2}, "5": {"3": 4}}
- q_by_to_C: {"0": {"3": 2}, "1": {"3": 2}, "10": {"0": 2}, "11": {"3": 2}, "13": {"0": 2}, "14": {"0": 2}, "2": {"0": 2, "3": 4}, "4": {"0": 2}, "5": {"0": 4}}
- lift_q_context_rule_found: true
- gap_a_closed: false
- full_g900_admission_found: false
- next_step: "lift_q_rule_to_native_g60_quotient_context"

## Boundary

- This searches the lift q context rule only.
- A found rule is not yet a G60-native derivation.
- This does not close Gap A.
- This does not prove full G900.

## Checks

- PASS source_loaded: c_transition_delta_lift_decomposition_found
- PASS row_count_24: 24
- PASS q_values_only_0_3: {3: 10, 0: 14}
- PASS feature_tests_ran: 9108
- PASS no_gap_a_claim_made: lift-q context search only
