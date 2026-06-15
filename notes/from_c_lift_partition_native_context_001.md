# from_C lift partition native context 001

Status: from_c_lift_partition_native_context_recorded

## Summary

- observed_from_C_values: [0, 1, 2, 4, 5, 10, 11, 13, 14]
- unobserved_C_values: [3, 6, 7, 8, 9, 12]
- q0_values: [0, 1, 2, 4, 10]
- q3_values: [5, 11, 13, 14]
- q0_size: 5
- q3_size: 4
- g15_edge_count: 30
- interpretation: "Inspects whether the observed from_C lift partition has a native G15/Petersen/sign profile."
- gap_a_closed: false
- full_g900_admission_found: false
- next_step: "compare_from_c_partition_against_g15_sign_orbits_and_old_hyperxi_involutions"

## Subset reports

### q0

- nodes: [0, 1, 2, 4, 10]
- induced_edge_count: 3
- induced_sign_profile: {"-1": 3}
- boundary_edge_count: 14
- boundary_sign_profile: {"-1": 9, "1": 5}

### q3

- nodes: [5, 11, 13, 14]
- induced_edge_count: 0
- induced_sign_profile: {}
- boundary_edge_count: 16
- boundary_sign_profile: {"-1": 8, "1": 8}

### observed

- nodes: [0, 1, 2, 4, 5, 10, 11, 13, 14]
- induced_edge_count: 11
- induced_sign_profile: {"-1": 7, "1": 4}
- boundary_edge_count: 14
- boundary_sign_profile: {"-1": 9, "1": 5}

### unobserved

- nodes: [3, 6, 7, 8, 9, 12]
- induced_edge_count: 5
- induced_sign_profile: {"-1": 4, "1": 1}
- boundary_edge_count: 14
- boundary_sign_profile: {"-1": 9, "1": 5}

## Boundary

- This is an inspection of the observed from_C partition.
- Only 9 of 15 C values appear in the WXYZTI overlay rows.
- Candidate Petersen decoding is provisional unless independently aligned.
- This does not close Gap A.
- This does not prove full G900.

## Checks

- PASS formula_loaded: from_c_lift_q_overlay_delta_formula_found
- PASS bundle_loaded: g60_native_generator_input_bundle_built
- PASS g15_edges_30: 30
- PASS rule_observed_9: 9
- PASS q_values_0_3: {0: 0, 1: 0, 2: 0, 4: 0, 5: 3, 10: 0, 11: 3, 13: 3, 14: 3}
- PASS no_gap_a_claim_made: partition context inspection only
