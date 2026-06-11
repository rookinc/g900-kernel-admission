# QED status ledger

- ledger_ok: True
- direct_kernel_claims_proved: 6
- certificate_claims_certified: 5
- remaining_planned_claims: 2
- qed_complete: False

## Proved by kernel

- product_register_size
- internal_edge_count
- external_edge_count
- total_edge_count
- degree_split
- regularity

## Certified

- exact_edge_set_identity
- connectedness
- diameter
- radius
- baseline_separation

## Planned

- sibling_non_switching
- sibling_full_graph_separation

## Claim table

- product_register_size: proved_by_kernel
  - support: finite product count |V15| * |V60| = 15 * 60 = 900
- internal_edge_count: proved_by_kernel
  - support: 15 copies of 120 G60 edges gives 1800 internal edges
- external_edge_count: proved_by_kernel
  - support: 30 slot edges times 60 carrier states gives 1800 external edges
- total_edge_count: proved_by_kernel
  - support: 1800 internal + 1800 external = 3600 total edges
- degree_split: proved_by_kernel
  - support: 4 internal neighbors plus 4 external carrier neighbors
- regularity: proved_by_kernel
  - support: degree split gives 8-regularity
- exact_edge_set_identity: certified
  - support: artifacts/json/exact_edge_set_identity_certificate.json
- connectedness: certified
  - support: artifacts/json/connectedness_certificate.json
- diameter: certified
  - support: artifacts/json/metric_certificate.json
  - value: 8
- radius: certified
  - support: artifacts/json/metric_certificate.json
  - value: 6
- baseline_separation: certified
  - support: artifacts/json/baseline_separation_certificate.json
- sibling_non_switching: planned
  - support: needs F2 coboundary obstruction certificate internal to Project 18
- sibling_full_graph_separation: planned
  - support: needs exact invariant separation certificate internal to Project 18

## Boundary

- This is a status overlay, not a replacement for the claim ledger.
- QED is not complete until the remaining planned claims are certified or removed from the theorem.
- No uniqueness, census identity, physical interpretation, or sibling invalidity is claimed.
