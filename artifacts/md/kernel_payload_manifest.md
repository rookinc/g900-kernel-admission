# Kernel payload manifest

- project: 18-g900-kernel-admission
- source_project: 17-g900-theorem-proof
- kernel_payload_independent_of_project17: True
- missing_count: 0

## Boundary

- This payload makes the construction kernel data available inside Project 18.
- Project 17 remains provenance, not a runtime dependency, after this import.
- This does not yet create the full proof-kernel certificate bundle.

## Payload files

- G15 slot edge list
  - payload_path: source/kernel_payload/g15_slot_edges.csv
  - source_path: support/admission/admitted_g15_slot_edges.csv
  - row_count: 30
  - expected_rows: 30
  - row_count_ok: True
  - sha256: 7b94834d507cf2995ec6faf73e2e227a685d831894aa98f2647556d8b922b8f6
  - bytes: 185
- G60 local edge list
  - payload_path: source/kernel_payload/g60_local_edges.csv
  - source_path: support/admission/admitted_g60_local_edges.csv
  - row_count: 120
  - expected_rows: 120
  - row_count_ok: True
  - sha256: c700a185fab6a5f434da09b7acb716b96c76170774bee946af8ea907e4fe7f9f
  - bytes: 817
- carrier signing table
  - payload_path: source/kernel_payload/carrier_signing_table.csv
  - source_path: support/admission/carrier_signing_table.csv
  - row_count: 30
  - expected_rows: 30
  - row_count_ok: True
  - sha256: 9b3cf812cc0f6d7b065666c81fa6d16fd3e3b8a98955c264709337c7f3e7efb7
  - bytes: 942
- regenerated X_sigma edge list
  - payload_path: source/kernel_payload/x_sigma_edges.csv
  - source_path: support/admission/regenerated_x_sigma_edges.csv
  - row_count: 3600
  - expected_rows: 3600
  - row_count_ok: True
  - sha256: ea2679662f4322a9ea021fba1143c804ef73b1fae95f50c77ba76b7fe1092230
  - bytes: 151574
