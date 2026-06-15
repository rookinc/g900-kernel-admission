# role-block full profile match inspection 006b

Status: role_block_full_profile_match_inspection_recorded

## Output

- full_match_count_available: `7`
- reported_full_native_profile_match_count: `7`
- target_match_count: `1`
- observed_union_match_count: `2`
- junction_2_match_count: `2`
- q3_subset_union_match_count: `2`
- q0_subset_union_match_count: `2`
- junction_counts: `{1: 2, 2: 2, 7: 1, 9: 2}`

## Matches

- index 0 target=False junction=1 union=[1, 2, 3, 4, 5, 8, 11, 12, 14] observed=False q3_subset=False q0_subset=False
- index 1 target=False junction=1 union=[1, 2, 4, 5, 8, 10, 11, 12, 14] observed=False q3_subset=False q0_subset=False
- index 2 target=False junction=2 union=[0, 1, 2, 4, 5, 10, 11, 13, 14] observed=True q3_subset=True q0_subset=True
- index 3 target=True junction=2 union=[0, 1, 2, 4, 5, 10, 11, 13, 14] observed=True q3_subset=True q0_subset=True
- index 4 target=False junction=7 union=[3, 4, 5, 7, 8, 9, 12, 13, 14] observed=False q3_subset=False q0_subset=False
- index 5 target=False junction=9 union=[0, 1, 2, 5, 7, 8, 9, 10, 12] observed=False q3_subset=False q0_subset=False
- index 6 target=False junction=9 union=[0, 1, 3, 7, 8, 9, 10, 11, 13] observed=False q3_subset=False q0_subset=False

## Boundary

This is an inspection of the 7 signed-G15 profile matches. It does not derive the role-block circulation from G60-native structure and does not close Gap A.
