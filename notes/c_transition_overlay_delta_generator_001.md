# C-transition overlay delta generator 001

Status: c_transition_overlay_delta_generator_found

## Purpose

Lift the exact context feature set from_C,to_C into an explicit WXYZTI overlay fiber-delta generator table.

## Summary

- edge_count: 24
- label_counts: {"reverse_partner": 12, "shared_B": 12}
- c_transition_group_count: 12
- c_transition_counts: {"(0, 2)": 2, "(1, 10)": 2, "(10, 13)": 2, "(11, 2)": 2, "(13, 1)": 2, "(14, 11)": 2, "(2, 14)": 2, "(2, 4)": 2, "(2, 5)": 2, "(4, 5)": 2, "(5, 0)": 2, "(5, 2)": 2}
- c_transition_label_counts: {"(0, 2, 'reverse_partner')": 1, "(0, 2, 'shared_B')": 1, "(1, 10, 'reverse_partner')": 1, "(1, 10, 'shared_B')": 1, "(10, 13, 'reverse_partner')": 1, "(10, 13, 'shared_B')": 1, "(11, 2, 'reverse_partner')": 1, "(11, 2, 'shared_B')": 1, "(13, 1, 'reverse_partner')": 1, "(13, 1, 'shared_B')": 1, "(14, 11, 'reverse_partner')": 1, "(14, 11, 'shared_B')": 1, "(2, 14, 'reverse_partner')": 1, "(2, 14, 'shared_B')": 1, "(2, 4, 'reverse_partner')": 1, "(2, 4, 'shared_B')": 1, "(2, 5, 'reverse_partner')": 1, "(2, 5, 'shared_B')": 1, "(4, 5, 'reverse_partner')": 1, "(4, 5, 'shared_B')": 1, "(5, 0, 'reverse_partner')": 1, "(5, 0, 'shared_B')": 1, "(5, 2, 'reverse_partner')": 1, "(5, 2, 'shared_B')": 1}
- delta_counts: {"1": 2, "2": 4, "3": 4, "9": 2, "12": 2, "48": 2, "51": 2, "55": 2, "57": 4}
- ambiguous_c_transition_count: 0
- prediction_match_count: 24
- prediction_exact: true
- c_transition_delta_rule_found: true
- rule_table: {"(0, 2)": 2, "(1, 10)": 9, "(10, 13)": 3, "(11, 2)": 51, "(13, 1)": 48, "(14, 11)": 57, "(2, 14)": 12, "(2, 4)": 2, "(2, 5)": 3, "(4, 5)": 1, "(5, 0)": 55, "(5, 2)": 57}
- gap_a_closed: false
- full_g900_admission_found: false
- next_step: "derive_c_transition_rule_from_native_g60_structure"

## Boundary

- This is an exact overlay delta generator table.
- The rule is expressed in station provenance terms from_C and to_C.
- This is not yet a G60-native derivation of C itself.
- This does not close Gap A.
- This does not prove full G900.

## Checks

- PASS previous_search_loaded: g60_native_overlay_generator_not_found_in_tested_family
- PASS context_search_loaded: context_dependent_overlay_delta_rule_found
- PASS edge_count_24: 24
- PASS label_split_12_12: {'reverse_partner': 12, 'shared_B': 12}
- PASS c_transition_groups_12: 12
- PASS no_ambiguous_c_transitions: {}
- PASS all_predictions_match: {'match_count': 24, 'edge_count': 24}
- PASS no_gap_a_claim_made: C-transition delta table only
