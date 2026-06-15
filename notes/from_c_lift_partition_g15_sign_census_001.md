# from_C lift partition G15 sign census 001

Status: from_c_lift_partition_g15_sign_census_recorded

## Key counts

- q3_profile_match_count_size4: 8
- q0_profile_match_count_size5: 103
- independent_4_count: 90
- independent_4_balanced_boundary_count: 8
- automorphism_report: {"networkx_available": true, "q0_profile_matches_in_unsigned_orbit": 15, "q0_unsigned_orbit_sample": [[0, 1, 2, 3, 6], [0, 1, 2, 3, 9], [0, 1, 2, 4, 6], [0, 1, 2, 4, 10], [0, 1, 3, 4, 7], [0, 1, 3, 4, 10], [0, 1, 5, 9, 12], [0, 1, 5, 11, 13], [0, 1, 5, 11, 14], [0, 1, 5, 12, 13], [0, 1, 7, 11, 12], [0, 1, 11, 12, 14], [0, 2, 3, 4, 7], [0, 2, 3, 4, 12], [0, 2, 5, 6, 7], [0, 2, 5, 6, 8], [0, 2, 6, 11, 13], [0, 2, 6, 12, 13], [0, 2, 8, 9, 14], [0, 2, 10, 11, 14]], "q0_unsigned_orbit_size": 120, "q3_profile_matches_in_unsigned_orbit": 5, "q3_unsigned_orbit_sample": [[0, 2, 7, 12], [0, 2, 7, 14], [0, 2, 12, 14], [0, 3, 6, 9], [0, 3, 6, 11], [0, 3, 9, 11], [0, 6, 9, 11], [0, 7, 12, 14], [1, 3, 5, 7], [1, 3, 5, 10], [1, 3, 7, 10], [1, 4, 9, 12], [1, 4, 9, 13], [1, 4, 12, 13], [1, 5, 7, 10], [1, 9, 12, 13], [2, 4, 6, 8], [2, 4, 6, 10], [2, 4, 8, 10], [2, 6, 8, 10]], "q3_unsigned_orbit_size": 30, "unsigned_automorphism_count": 120}

## q3 profile

{
  "nodes": [
    5,
    11,
    13,
    14
  ],
  "size": 4,
  "induced_edge_count": 0,
  "boundary_edge_count": 16,
  "induced_sign_profile": {},
  "boundary_sign_profile": {
    "-1": 8,
    "1": 8
  },
  "degree_inside": {
    "5": 0,
    "11": 0,
    "13": 0,
    "14": 0
  },
  "degree_outside": {
    "5": 4,
    "11": 4,
    "13": 4,
    "14": 4
  }
}

## q0 profile

{
  "nodes": [
    0,
    1,
    2,
    4,
    10
  ],
  "size": 5,
  "induced_edge_count": 3,
  "boundary_edge_count": 14,
  "induced_sign_profile": {
    "-1": 3
  },
  "boundary_sign_profile": {
    "-1": 9,
    "1": 5
  },
  "degree_inside": {
    "0": 2,
    "1": 2,
    "2": 1,
    "4": 1,
    "10": 0
  },
  "degree_outside": {
    "0": 2,
    "1": 2,
    "2": 3,
    "4": 3,
    "10": 4
  }
}

## Boundary

- This is a signed G15 subset census.
- It does not derive the partition from native G60.
- Automorphism data is unsigned unless otherwise stated.
- This does not close Gap A.
- This does not prove full G900.

## Checks

- PASS partition_loaded: from_c_lift_partition_native_context_recorded
- PASS bundle_loaded: g60_native_generator_input_bundle_built
- PASS g15_edge_count_30: 30
- PASS q3_size_4: [5, 11, 13, 14]
- PASS q0_size_5: [0, 1, 2, 4, 10]
- PASS q3_profile_found_in_census: 8
- PASS q0_profile_found_in_census: 103
- PASS no_gap_a_claim_made: subset census only
