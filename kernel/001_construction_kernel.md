# Construction kernel

## Definition

The G900 construction kernel is

    K_900 = (G15, G60, sigma, h)

where:

- G15 is the 15-vertex slot graph.
- G60 is the 60-vertex thalion fiber.
- sigma: E(G15) -> F2 is the carrier signing.
- h is the half-flip involution on local states:

    h(x) = x + 30 mod 60

## Generated object

The generated graph is

    X_sigma = Gen(K_900)

with vertex set

    V(X_sigma) = V(G15) x V(G60)

and edge set

    E(X_sigma) = E_int union E_car

## Internal edges

For each slot t in V(G15), include one copy of the G60 edge law:

    (t,x) ~ (t,y)

whenever

    {x,y} in E(G60)

## Carrier edges

For each slot edge {t,u} in E(G15), include carrier edges

    (t,x) ~ (u, phi_sigma(t,u)(x))

where

    phi_0(x) = x
    phi_1(x) = h(x) = x + 30 mod 60

## Important boundary

The construction kernel generates the candidate.

It does not by itself prove every graph invariant.

The 900 vertices and 3600 edges follow directly from the kernel and source counts.

Connectedness, diameter, radius, exact match, and sibling separation require proof-kernel certificates.
