# G60 native overlay generator family search 001

Status: g60_native_overlay_generator_not_found_in_tested_family

## Purpose

Test a bounded family of simple native G60 maps as candidate generators for WXYZTI overlay edges.

## Summary

- forms_key: "wxyzti_admitted_forms"
- form_count: 4
- edge_record_count: 24
- label_counts: {"reverse_partner": 12, "shared_B": 12}
- role_counts: {"IW": 4, "TI": 4, "WX": 4, "XY": 4, "YZ": 4, "ZT": 4}
- candidate_count: 10
- candidate_names: ["identity", "minus_15_mod60", "minus_30_mod60", "old_g60_pair_involution_relabelled", "old_hyperxi_a_relabelled", "old_hyperxi_ab_relabelled", "old_hyperxi_b_relabelled", "old_hyperxi_ba_relabelled", "plus_15_mod60", "plus_30_mod60"]
- best_single_candidate: {"candidate": "old_hyperxi_ab_relabelled", "exact_all": false, "exact_reverse_partner": false, "exact_shared_B": false, "is_permutation": true, "matched_by_label": {"reverse_partner": 2, "shared_B": 2}, "matched_edges": 4, "missed_by_label": {"reverse_partner": 10, "shared_B": 10}}
- two_map_exact_hit_count: 0
- strict_native_two_map_generator_found: false
- fiber_delta_by_label: {"reverse_partner": {"1": 1, "2": 2, "3": 2, "9": 1, "12": 1, "48": 1, "51": 1, "55": 1, "57": 2}, "shared_B": {"1": 1, "2": 2, "3": 2, "9": 1, "12": 1, "48": 1, "51": 1, "55": 1, "57": 2}}
- slot_delta_by_label: {"reverse_partner": {"3": 3, "5": 1, "6": 1, "9": 1, "12": 3, "13": 2, "14": 1}, "shared_B": {"0": 12}}
- gap_a_closed: false
- full_g900_admission_found: false
- next_step: "expand_to_context_dependent_g60_native_generator_family"

## Best single candidates

- old_hyperxi_ab_relabelled: matched_edges=4, matched_by_label={"reverse_partner": 2, "shared_B": 2}
- old_hyperxi_ba_relabelled: matched_edges=4, matched_by_label={"reverse_partner": 2, "shared_B": 2}
- identity: matched_edges=0, matched_by_label={}
- minus_15_mod60: matched_edges=0, matched_by_label={}
- minus_30_mod60: matched_edges=0, matched_by_label={}
- old_g60_pair_involution_relabelled: matched_edges=0, matched_by_label={}
- old_hyperxi_a_relabelled: matched_edges=0, matched_by_label={}
- old_hyperxi_b_relabelled: matched_edges=0, matched_by_label={}
- plus_15_mod60: matched_edges=0, matched_by_label={}
- plus_30_mod60: matched_edges=0, matched_by_label={}

## Boundary

- This searches a first bounded family of simple native G60 maps.
- Failure refutes only this tested family.
- Success would identify a candidate generator family, not full Gap A closure.
- This does not prove full G900.

## Checks

- PASS bundle_loaded: g60_native_generator_input_bundle_built
- PASS wxyzti_forms_loaded: 4
- PASS edge_records_24: 24
- PASS no_missing_endpoints: []
- PASS label_split_12_12: {'reverse_partner': 12, 'shared_B': 12}
- PASS overlay_loaded_classified: True
- PASS candidate_family_nonempty: ['identity', 'minus_15_mod60', 'minus_30_mod60', 'old_g60_pair_involution_relabelled', 'old_hyperxi_a_relabelled', 'old_hyperxi_ab_relabelled', 'old_hyperxi_b_relabelled', 'old_hyperxi_ba_relabelled', 'plus_15_mod60', 'plus_30_mod60']
- PASS no_gap_a_claim_made: search family only
