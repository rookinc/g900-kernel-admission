# Certificate plan

This plan defines the finite certificates needed to promote Project 18 from kernel definition to bounded theorem admission.

No heavy certificate is created here. This file only defines the target shape of each certificate.

## Certificate 1: connectedness

Claim:

    X_sigma is connected.

Certificate target:

    A spanning tree or BFS parent map on all 900 vertices.

Verifier requirements:

- all 900 vertices appear,
- root has no parent,
- every non-root vertex has exactly one parent,
- every parent edge exists in X_sigma,
- the parent relation reaches every vertex,
- the tree has 899 edges.

## Certificate 2: diameter

Claim:

    diameter(X_sigma) = 8.

Certificate target:

    A distance certificate proving both an upper bound and a lower bound.

Verifier requirements:

- upper bound: every pair of vertices has distance at most 8,
- lower bound: at least one vertex pair has distance exactly 8,
- all distances are checked against the generated edge set.

Acceptable implementation:

- all-source BFS distance summary,
- eccentricity table,
- witness pair at distance 8.

## Certificate 3: radius

Claim:

    radius(X_sigma) = 6.

Certificate target:

    An eccentricity certificate.

Verifier requirements:

- at least one vertex has eccentricity 6,
- no vertex has eccentricity less than 6,
- all eccentricities are checked against the generated edge set.

Acceptable implementation:

- eccentricity table,
- center set,
- radius witness.

## Certificate 4: exact edge-set identity

Claim:

    Gen(K_900) equals the recorded canonical candidate edge set.

Certificate target:

    Sorted endpoint edge-set equality.

Verifier requirements:

- regenerate X_sigma from K_900,
- normalize every edge endpoint,
- sort generated edge list,
- sort recorded candidate edge list,
- prove row-by-row equality,
- record missing edge count 0,
- record extra edge count 0,
- record identical hash.

## Certificate 5: sibling non-switching

Claim:

    The sibling signing is not switching-equivalent to the canonical signing.

Certificate target:

    F2 coboundary obstruction.

Verifier requirements:

- construct the slot graph incidence/coboundary matrix,
- encode the signing difference vector,
- attempt to solve the coboundary equation over F2,
- certify no solution exists,
- record the two-triangle support.

## Certificate 6: sibling full-graph separation

Claim:

    The sibling graph is separated from the canonical graph as a full graph.

Certificate target:

    Exact invariant difference.

Preferred verifier requirements:

- compute exact distance distribution for canonical graph,
- compute exact distance distribution for sibling graph,
- show the distributions differ.

Alternative:

- exact characteristic polynomial or another exact graph invariant.

Avoid relying only on floating-point spectra.

## Certificate 7: baseline separation

Claim:

    X_sigma is not isomorphic to the untwisted product baseline.

Certificate target:

    Metric invariant separation.

Verifier requirements:

- record baseline diameter and radius,
- record X_sigma diameter and radius,
- show at least one of diameter or radius differs,
- cite graph-isomorphism invariance of distance.

## Admission rule

A certificate is admissible only if it can be checked from finite data without relying on:

- renderer output,
- visual geometry,
- screen coordinates,
- census identity,
- physical interpretation,
- project memory.

## Minimal bounded QED package

A bounded QED package requires:

1. construction kernel,
2. generation operator,
3. claim ledger,
4. certificate plan,
5. finite certificates,
6. independent verifier,
7. final theorem prose.
