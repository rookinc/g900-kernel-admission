# QED status ledger

- ledger_ok: True
- direct_kernel_claims_proved: 6
- certificate_claims_certified: 7
- remaining_planned_claims: 0
- not_certified_claims: 0
- qed_complete: True

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
- sibling_non_switching
- sibling_full_graph_separation

## Planned

- none

## Not certified

- none

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
- sibling_non_switching: certified
  - support: artifacts/json/sibling_non_switching_certificate.json
- sibling_full_graph_separation: certified
  - support: artifacts/json/sibling_full_graph_separation_certificate.json

## Boundary

- This closes the bounded Project 18 QED ledger for the listed claim set.
- This does not claim uniqueness among all possible signed carriers.
- This does not claim census identity.
- This does not claim physical interpretation.
- This does not claim sibling invalidity.
- The result is a finite kernel-admission theorem package for the explicit generated candidate and listed separations.
