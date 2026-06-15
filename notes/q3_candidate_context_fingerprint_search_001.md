# q3 candidate context fingerprint search 001

Status: q3_candidate_context_fingerprint_search_recorded

## Inputs

- signed automorphism artifact: `/data/data/com.termux/files/home/dev/cori/research/thalean-graph-theory/18-g900-kernel-admission/artifacts/json/signed_g15_q3_automorphism_search_001.v1.json`
- native context artifact: `/data/data/com.termux/files/home/dev/cori/research/thalean-graph-theory/18-g900-kernel-admission/artifacts/json/from_c_lift_partition_native_context_001.v1.json`
- formula artifact: `/data/data/com.termux/files/home/dev/cori/research/thalean-graph-theory/18-g900-kernel-admission/artifacts/json/from_c_lift_q_overlay_delta_formula_001.v1.json`

## Output

- signed_edge_count: `30`
- candidate_count: `8`
- exact_single_feature_count: `6`
- least_exact_feature_set_count: `6`
- observed: `[0, 1, 2, 4, 5, 10, 11, 13, 14]`
- unobserved: `[3, 6, 7, 8, 9, 12]`
- q0: `[0, 1, 2, 4, 10]`
- q3: `[5, 11, 13, 14]`

## Exact single features

- `cut_to_observed`
- `cut_to_unobserved`
- `labelled_neighbor_fingerprint`
- `signed_degree_labelled`
- `sum`
- `sum_mod15`

## Least exact feature sets

- `['cut_to_observed']`
- `['cut_to_unobserved']`
- `['labelled_neighbor_fingerprint']`
- `['signed_degree_labelled']`
- `['sum']`
- `['sum_mod15']`

## Boundary

This is a context-fingerprint selector test over the 8 q3-profile candidates. It does not close Gap A and does not prove a G60-native generator.

