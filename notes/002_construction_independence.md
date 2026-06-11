# Construction independence

Project 18 now contains the finite construction payload required to regenerate the canonical G900 candidate without reading Project 17 at runtime.

## Status

Project 18 is construction-independent of Project 17.

Project 17 remains the frozen provenance checkpoint:

    17-g900-theorem-proof
    tag: g900-theorem-proof-v1.0.0-rc1

Project 18 now contains its own kernel payload:

    source/kernel_payload/g15_slot_edges.csv
    source/kernel_payload/g60_local_edges.csv
    source/kernel_payload/carrier_signing_table.csv
    source/kernel_payload/x_sigma_edges.csv

## Meaning

Construction independence means:

- G15 slot edges are internal to Project 18.
- G60 local edges are internal to Project 18.
- The carrier signing table is internal to Project 18.
- The generated X_sigma edge list is internal to Project 18.
- The generation operator is defined inside Project 18.
- Project 17 is no longer needed to state the construction kernel.

## Non-meaning

Construction independence does not yet mean full QED independence.

The proof-kernel certificate bundle is still planned.

The remaining certificate targets are:

- connectedness,
- diameter,
- radius,
- exact edge-set identity,
- sibling non-switching,
- sibling full-graph separation,
- baseline separation.

## Boundary

Project 18 does not modify Project 17.

Project 18 does not claim uniqueness, census identification, physical interpretation, or final public theorem status.

The current status is:

    construction-independent kernel admission project

not yet:

    fully admitted bounded QED theorem
