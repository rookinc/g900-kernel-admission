# Algebraic kernel

This note defines the algebraic form of the G900 construction kernel.

The set-theoretic construction gives the graph. The algebraic kernel gives the matrix language for QED admission.

## Matrices

Let:

    A15 = adjacency matrix of G15
    A60 = adjacency matrix of G60
    I15 = 15 x 15 identity matrix
    I60 = 60 x 60 identity matrix
    H   = 60 x 60 half-flip permutation matrix

The half-flip matrix H is defined by:

    H[x, y] = 1 if y = x + 30 mod 60
    H[x, y] = 0 otherwise

Let sigma be the carrier signing:

    sigma: E15 -> F2

where:

    sigma(t,u) = 0 means identity carrier
    sigma(t,u) = 1 means half-flip carrier

## Internal adjacency

The internal adjacency matrix is:

    A_internal = I15 kron A60

This is one copy of A60 over each slot.

## Carrier adjacency

The carrier adjacency matrix is a 15 by 15 block matrix with 60 by 60 blocks.

For slots t and u:

    block(t,u) = I60 if {t,u} in E15 and sigma(t,u) = 0
    block(t,u) = H   if {t,u} in E15 and sigma(t,u) = 1
    block(t,u) = 0   otherwise

The full carrier matrix is called:

    A_carrier

## Generated adjacency

The generated adjacency matrix is:

    AX = A_internal + A_carrier

where ordinary integer addition is used, and the construction is valid because the internal and carrier layers are disjoint.

## Direct algebraic consequences

From the admitted source counts:

    vertex_count = 15 * 60 = 900

From edge counts:

    internal_edges = 15 * 120 = 1800
    carrier_edges = 30 * 60 = 1800
    total_edges = 3600

From row sums:

    row_sum(A60) = 4
    row_sum(A15) = 4
    row_sum(each carrier block per adjacent slot) = 1

Therefore:

    row_sum(AX) = 8

So the graph is 8-regular.

## Boolean reachability target

Metric claims can be expressed by Boolean matrix powers.

Let Boolean multiplication use AND for multiplication and OR for addition.

Define:

    R_k = I OR AX OR AX^[2] OR ... OR AX^[k]

Then:

    connectedness means R_k has no zero off-diagonal entries for some finite k
    diameter <= 8 means R_8 is all ones
    diameter > 7 means R_7 is not all ones
    diameter = 8 means both conditions hold

Radius can be certified by row reachability and eccentricity extracted from Boolean powers.

## F2 switching target

Sibling switching equivalence is algebra over F2.

Let B be the incidence/coboundary matrix of G15 over F2.

Let delta be the difference between the canonical signing and sibling signing.

Switching equivalence means:

    B^T g = delta

has a solution over F2.

Non-switching equivalence means this system has no solution.

## Algebraic QED target

A purely algebraic QED package should reduce every load-bearing claim to:

- integer arithmetic,
- matrix equality,
- Boolean reachability,
- F2 row reduction,
- exact invariant comparison.

No visual rendering is needed.
