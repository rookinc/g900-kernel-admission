# observed C partition signed G15 census 001

Status: observed_c_partition_signed_g15_census_recorded

## Target partition

- observed: `[0, 1, 2, 4, 5, 10, 11, 13, 14]`
- unobserved: `[3, 6, 7, 8, 9, 12]`
- q0: `[0, 1, 2, 4, 10]`
- q3: `[5, 11, 13, 14]`

## Output

- signed_edge_count: `30`
- total_size9_subsets: `5005`
- full_profile_match_count: `187`
- cut_only_match_count: `389`
- cut_plus_complement_match_count: `187`
- full_profile_plus_q3_relation_match_count: `1`

## Observed profile

```
{
  "complement_size": 6,
  "cut": {
    "edge_count": 14,
    "neg": 9,
    "none": 40,
    "pos": 5
  },
  "induced_complement": {
    "edge_count": 5,
    "neg": 4,
    "none": 10,
    "pos": 1
  },
  "induced_subset": {
    "edge_count": 11,
    "neg": 7,
    "none": 25,
    "pos": 4
  },
  "size": 9
}
```

## Boundary

This does not close Gap A. It does not derive the observed set from G60. It only audits whether the observed/unobserved partition has a native signed-G15 profile.
