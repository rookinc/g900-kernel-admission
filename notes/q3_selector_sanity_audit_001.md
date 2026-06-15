# q3 selector sanity audit 001

Status: q3_selector_sanity_audit_recorded

## Input

- `/data/data/com.termux/files/home/dev/cori/research/thalean-graph-theory/18-g900-kernel-admission/artifacts/json/q3_candidate_context_fingerprint_search_001.v1.json`

## Result

- candidate_count: `8`
- context_structural_exact_features: `['cut_to_observed', 'cut_to_unobserved']`
- label_dependent_exact_features: `['labelled_neighbor_fingerprint', 'signed_degree_labelled', 'sum', 'sum_mod15']`
- unlabelled_structural_exact_features: `[]`

## Reading

The meaningful selector signal is the context cut:

- `cut_to_observed`
- `cut_to_unobserved`

The following exact selectors are not safe as structural evidence by themselves:

- `sum`
- `sum_mod15`
- `signed_degree_labelled`
- `labelled_neighbor_fingerprint`

## Target q3 summary

```
{
  "candidate": [
    5,
    11,
    13,
    14
  ],
  "cut_to_observed": {
    "edge_count": 8,
    "neg": 4,
    "none": 24,
    "pos": 4
  },
  "cut_to_q0": {
    "edge_count": 8,
    "neg": 4,
    "none": 12,
    "pos": 4
  },
  "cut_to_unobserved": {
    "edge_count": 8,
    "neg": 4,
    "none": 16,
    "pos": 4
  },
  "intersect_observed_count": 4,
  "intersect_q0_count": 0,
  "intersect_unobserved_count": 0,
  "is_target_q3": true,
  "sum": 43,
  "sum_mod15": 13
}
```

## Boundary

This does not close Gap A. It shows that observed/unobserved lift context can select q3 among the 8 rare signed-profile candidates. The next task is to derive or refute the observed/unobserved partition from native oriented G15/G60 or WXYZTI station constraints.
