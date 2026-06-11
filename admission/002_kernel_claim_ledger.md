# Kernel claim ledger

This ledger classifies the claims attached to the G900 kernel-admission project.

The purpose is to prevent hidden cheating.

Every claim must be one of:

- direct_proof
- certificate_required
- external_boundary
- not_claimed

## Direct proof claims

These claims follow directly from the construction kernel once the source counts are admitted.

### product_register_size

Claim:

    |V(G15) x V(G60)| = 15 * 60 = 900

Status:

    direct_proof

### internal_edge_count

Claim:

    15 copies of 120 G60 edges gives 1800 internal edges

Status:

    direct_proof

### external_edge_count

Claim:

    30 slot edges times 60 carrier states gives 1800 external edges

Status:

    direct_proof

### total_edge_count

Claim:

    1800 internal + 1800 external = 3600 total edges

Status:

    direct_proof

### degree_split

Claim:

    each vertex has 4 internal neighbors and 4 external neighbors

Status:

    direct_proof

### regularity

Claim:

    each vertex has degree 8

Status:

    direct_proof

## Certificate-required claims

These claims are finite, but they require explicit certificates or independent verification.

### connectedness

Claim:

    X_sigma is connected

Status:

    certificate_required

Required certificate:

    spanning tree or BFS reachability certificate

### diameter

Claim:

    diameter(X_sigma) = 8

Status:

    certificate_required

Required certificate:

    upper-bound all-pairs distance witness plus lower-bound pair at distance 8

### radius

Claim:

    radius(X_sigma) = 6

Status:

    certificate_required

Required certificate:

    center eccentricity certificate plus lower-bound proof that no radius below 6 exists

### exact_edge_set_identity

Claim:

    generated X_sigma equals the recorded canonical candidate edge set

Status:

    certificate_required

Required certificate:

    sorted endpoint edge-set equality and hash equality

### sibling_non_switching

Claim:

    sibling signing is not switching-equivalent to canonical signing

Status:

    certificate_required

Required certificate:

    F2 coboundary obstruction certificate

### sibling_full_graph_separation

Claim:

    sibling graph is separated from canonical graph as a full graph

Status:

    certificate_required

Required certificate:

    exact invariant separation, preferably distance distribution or characteristic data

## External boundary claims

These are outside the bounded kernel-admission theorem unless separately proved.

### census_identification

Claim:

    X_sigma has a census identifier

Status:

    external_boundary

Admission rule:

    do not claim unless independently established

### uniqueness

Claim:

    X_sigma is the unique G900 ring

Status:

    external_boundary

Admission rule:

    do not claim unless a uniqueness theorem is proved

### physical_interpretation

Claim:

    X_sigma has direct physical interpretation

Status:

    external_boundary

Admission rule:

    do not claim inside the finite theorem

## Not claimed

The kernel-admission theorem does not claim:

- census identification
- uniqueness
- physical interpretation
- invalidity of sibling candidates
- final public theorem status without admission certificates

## Admission principle

A bounded QED theorem is possible only when every load-bearing claim is either directly proved from the kernel or supported by an explicit finite certificate.
