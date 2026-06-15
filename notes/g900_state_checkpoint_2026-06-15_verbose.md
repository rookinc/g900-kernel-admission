# G900 State Checkpoint - 2026-06-15

Status: bounded progress checkpoint
Project: Thalean / G900 / Gap A / Registered Boundary Flux
Primary local area: 18-g900-kernel-admission
Purpose: preserve the current state so later work does not drift away from the findings.

## 1. Reason for this checkpoint

This checkpoint records the current state of the G900 line after a sequence of linked results involving:

- the old Hyperxi G60 archive
- the current canonical G60 payload
- Project 16's twisted G900 carrier candidate
- the current Registered Boundary Flux lab channel-aware join
- the WXYZTI witness form
- the admission-blind nearest-neighbor reciprocal witness

The purpose of this note is not to claim completion. It is to prevent drift.

The current result is strong, but bounded. We have not closed Gap A. We have not proven full G900. We have, however, narrowed the live problem substantially.

The current best reading is:

G900 stands as a canonical twisted 900-state carrier candidate whose edge law is now provenance-aligned across Project 16 and the current lab, and whose local reciprocal witness layer has been found, classified, and tied to an admission-blind exact selector. The remaining open problem is to derive the WXYZTI / NRC witness from a genuinely G60-native generator.

## 2. Current one-line status

G900 is not yet admitted, but it now has a verified carrier law, a classified source-native witness overlay, and an exact admission-blind reciprocal witness tied to that overlay.

Keeper line:

Admission is witnessed by an admission-blind nearest-neighbor return, and the return is carried by a classified source-native WXYZTI overlay.

## 3. What is now locked

### 3.1 Canonical G60 has multiple provenance sources

The old Hyperxi archive contains a machine-readable G60 definition at:

../../../../zarchive/zarchive/hyperxi_lab/reports/true_quotients/export_thalean_graph_definition.json

That archive payload records the canonical Thalean G60 identity profile:

- vertices = 60
- edges = 120
- degree set = [4]
- triangles = 40
- diameter = 6
- shell profile = [1, 4, 8, 16, 24, 6, 1]
- automorphism count = 480
- graph6 string present
- adjacency table present
- edge list present
- involutions a and b present
- V4 orbit structure present
- quotient summary present

The accompanying text report records the same identity profile and adjacency table.

This matches the canonical Thalean G60 identity already associated with:

- GraphSym AT4val[60,6]
- House of Graphs Graph52002

The current lab payload lives at:

../../aletheos.ai/public_html/labs/registered_boundary_flux/data/canonical_g60_local_edges.v1.csv

Direct edge-label comparison between the old archive G60 and the current lab G60 showed:

- old_edges = 120
- current_edges = 120
- intersection = 7
- old_only = 113
- current_only = 113
- exact edge-label match = false

This initially looked like a mismatch, but both graphs had the same canonical identity profile:

- 60 vertices
- 120 edges
- degree 4
- 40 triangles
- shell profile [1, 4, 8, 16, 24, 6, 1] at every root

A NetworkX isomorphism test then confirmed:

- isomorphic = true
- mapped_exact_match = true

Therefore:

The old Hyperxi G60 archive and the current lab G60 payload are the same canonical G60 graph under vertex relabeling.

The old-to-current vertex map was saved as:

18-g900-kernel-admission/artifacts/json/old_g60_to_current_g60_vertex_map_001.json

This makes the old Hyperxi archive a second provenance source for the same canonical G60.

### 3.2 Important caution about similarly named archive objects

Some old archive files use names such as "true_g60" for a different 60-vertex object with:

- vertices = 60
- edges = 90
- degree set = [3]
- shell profile similar to [1, 3, 6, 11, 15, 18, 6]

That object is not the canonical 120-edge tetravalent Thalean G60 used here.

Current terminology for avoiding drift:

- canonical chamber/scaffold G60 = 60 vertices, 120 edges, degree 4
- incidence quotient / alternate 60-object = 60 vertices, 90 edges, degree 3

Do not confuse these in later generator work.

### 3.3 Project 16 and the current lab share the same G900 twisted carrier law

Project 16, located at:

16-fifteen-thalion-ring

contains the earlier computational spine for the twisted G900 candidate.

The current lab channel-aware join was compared against the Project 16 canonical twisted candidate edge list. The match was exact.

Result profile:

- Project 16 rows = 3600
- Project 16 parsed edges = 3600
- lab edges = 3600
- intersection = 3600
- lab_only = 0
- project16_only = 0
- exact edge match = true
- normalized kind match = true

The edge kind counts matched exactly:

- internal_thalion_copy = 1800
- external_signed_carrier = 1800

The external signed carrier profile matched exactly:

- slot edge count = 30
- each slot edge contributes 60 rows
- delta counts = {0: 900, 30: 900}
- identity count = 900
- half_flip count = 900
- other delta count = 0

Interpretation:

The current lab channel-aware join is the same canonical twisted G900 carrier edge law already present in Project 16.

This means the current lab object is not a new visual approximation. It is edge-law aligned with the Project 16 twisted candidate.

### 3.4 WXYZTI is not literal X_sigma adjacency

The WXYZTI witness form was tested against the Project 16 / current lab carrier edge law using several endpoint wiring interpretations.

Tested modes included:

- key-based wiring
- role-based wiring
- edge_role-based wiring
- index-order wiring

All modes resolved station endpoints, but none resolved the WXYZTI witness edges as literal carrier edges.

Result:

- WXYZTI witness edges = 24
- literal carrier matches = 0
- reverse_partner not found in channel join = 12
- shared_B not found in channel join = 12

Interpretation:

WXYZTI should not be read as a literal path in the Project 16 / X_sigma carrier adjacency graph.

This is not a failure of the G900 carrier law. The carrier law had already been matched exactly against Project 16.

Instead, it means WXYZTI belongs to a different relation layer.

### 3.5 WXYZTI classifies as a source-native transport overlay

The not-found edge deltas were inspected.

The 24 WXYZTI witness edges split cleanly into two source-native transport relation families:

- reverse_partner = 12
- shared_B = 12

The pattern split was exact:

- reverse_partner: same_A + same_edge_columns + same_station_columns
- shared_B: same_B + same_slot

The overlay classification passed:

- edge_count = 24
- reverse_partner = 12
- shared_B = 12
- bad_edge_count = 0
- overlay_classified = true

Overlay rules:

1. reverse_partner preserves A and columns.
2. shared_B preserves B and slot.

Interpretation:

WXYZTI is a source-native reciprocal transport overlay over station provenance fields, not literal adjacency in the Project 16 / X_sigma carrier.

This is a structural correction. The witness was not lost. It was sitting one layer above the carrier adjacency.

### 3.6 The WXYZTI overlay is consistent with the admission-blind NRC witness

The first overlay/NRC consistency check found the core profile but missed the exactness boolean because the script searched the wrong schema paths.

That v1 result should be kept as a schema-miss diagnostic.

The schema-aware v2 check passed.

Result:

- status = overlay_consistent_with_admission_blind_nrc_witness
- nrc_exact_resolved = true
- nrc_exactness_source = explicit_boolean
- accepted = 4
- false_pos = 0
- miss = 0
- WXYZTI forms = 4
- WXYZTI edges = 24
- WXYZTI labels = reverse_partner 12, shared_B 12
- overlay_nrc_consistent = true
- failed checks = 0

Interpretation:

The admission-blind nearest-neighbor reciprocal witness and the classified WXYZTI source-native overlay agree on the admitted-four structure.

This strengthens the witness result without claiming Gap A.

## 4. The current provenance chain

Current strongest bounded chain:

old Hyperxi canonical G60 source
-> old-to-current G60 vertex relabeling
-> current canonical G60 lab payload
-> 15-slot G900 register
-> signed half-flip carrier over G15
-> Project 16 twisted G900 candidate
-> current lab channel-aware join
-> WXYZTI source-native transport overlay
-> admission-blind nearest-neighbor reciprocal exact witness

This is the chain to preserve.

## 5. What G900 currently is

G900 is currently best described as:

A canonical twisted 900-state carrier candidate built from 15 copies of the canonical G60 thalion body, with external signed half-flip transport over the G15 slot graph, whose carrier law is verified against Project 16 and whose local reciprocal witness overlay is classified and consistent with an admission-blind exact NRC witness.

Shorter version:

G900 is a verified carrier candidate with a classified witness layer, not yet a fully admitted theorem object.

## 6. What has been crossed

The following thresholds have been crossed:

1. G60 provenance strengthened

The canonical G60 payload is no longer supported only by the current lab file. It is linked to an older independent Hyperxi archive definition by graph isomorphism and an explicit vertex relabeling map.

2. G900 carrier law stabilized

The current lab channel join is exactly the Project 16 twisted G900 candidate edge law.

3. WXYZTI misinterpretation corrected

The WXYZTI witness is not literal carrier adjacency. This is now known, not guessed.

4. WXYZTI relation layer classified

The witness relation is a source-native transport overlay with two clean rule families.

5. Overlay tied back to NRC

The overlay is consistent with the admission-blind nearest-neighbor reciprocal witness.

## 7. What remains open

The following are not yet solved:

- no G60-native generator has been found for the WXYZTI / NRC witness
- Gap A remains open
- full G900 admission remains open
- no uniqueness claim is made
- no census identity claim is made for G900
- no physical interpretation is claimed
- no claim is made that WXYZTI edges are literal carrier adjacency
- no claim is made that the current witness overlay exhausts all possible witness layers

## 8. Current Gap A formulation

Gap A is now sharper than before.

Old broad version:

Can we explain the admitted four?

Current sharper version:

Can the classified WXYZTI / NRC witness overlay be generated natively from canonical G60 structure, rather than reconstructed from the 120-record witness surface?

Even sharper:

Find or refute a lawful G60-native generator whose output gives the source-native WXYZTI transport overlay rules:

- reverse_partner preserves A and columns
- shared_B preserves B and slot

and whose selected forms match the admission-blind NRC exact profile:

- accepted = 4
- false_pos = 0
- miss = 0

## 9. Language discipline going forward

Use this language:

- G900 carrier candidate
- Project 16 twisted carrier law
- current lab channel-aware join
- WXYZTI source-native transport overlay
- admission-blind NRC witness
- local reciprocal return
- classified witness layer
- Gap A remains open

Avoid this language unless later proved:

- G900 is solved
- G900 is fully admitted
- WXYZTI is a literal G900 path
- WXYZTI edges are carrier edges
- the G60-native generator has been found
- the witness is external
- the witness is independent in a global/external sense
- physical force derivation

## 10. Keeper lines

The witness is not outside the system. The witness is the nearest neighbor that answers back.

The witness path is chosen without knowing admission. Only afterward does the sharp reciprocal trace select the admitted four.

Admission is witnessed by local reciprocal return.

The WXYZTI witness is not carrier adjacency. It is a source-native transport overlay.

G900 does not yet say "I am." It asks whether "I am" is allowed to return true.

Current G900 status:

G900 is a verified canonical carrier candidate whose local reciprocal witness layer has been found, classified, and tied to an admission-blind exact selector, but whose source-native generator is still open.

## 11. Immediate next research target

Next target:

derive or refute a genuine G60-native generator for the source-native WXYZTI / NRC witness form.

The next search should not try to force WXYZTI into literal X_sigma adjacency. That interpretation has been tested and rejected.

Instead, search for a native rule over canonical G60, old/current relabeling, involutions, slot/fiber provenance, and quotient structure that produces the WXYZTI overlay rules.

Candidate inputs to inspect:

- old Hyperxi adjacency table
- old-to-current G60 vertex map
- involutions a and b
- V4 orbits
- g60_involution_pairs.json
- g15_edge_sign_table.json
- G15 slot graph
- Project 16 half-flip law
- station provenance fields A, B, C, columns, slot, fiber
- reverse_partner and shared_B overlay constraints

## 12. Final boundary statement

This checkpoint records a strong bounded state.

It does not close G900.

It does show that the G900 carrier, the WXYZTI witness overlay, and the admission-blind NRC exact selector now form a coherent audited chain.

The live problem is no longer whether the pieces are merely visual or accidental. The live problem is whether the witness overlay can be generated natively from G60.
