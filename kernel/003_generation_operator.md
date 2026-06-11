# Generation operator

## Purpose

This note defines the operator that turns the construction kernel into the generated graph.

The construction kernel is

    K_900 = (G15, G60, sigma, h)

where:

- G15 is the slot graph.
- G60 is the thalion fiber.
- sigma is the F2-valued signing on E(G15).
- h is the half-flip involution h(x) = x + 30 mod 60.

The generation operator is written:

    Gen(K_900) = X_sigma

## Input data

The operator requires exactly four finite inputs:

1. G15 slot edges.
2. G60 local edges.
3. Carrier signing sigma on every slot edge.
4. Half-flip rule h(x) = x + 30 mod 60.

No rendering data is an input.

No visual ring geometry is an input.

No Aletheos surface coordinates are an input.

## Vertex generation

The vertex set is the product register:

    V(X_sigma) = V(G15) x V(G60)

A generated vertex is written:

    (t, x)

where:

- t is a slot in V(G15),
- x is a local state in V(G60).

Since |V(G15)| = 15 and |V(G60)| = 60, the generated vertex count is:

    15 * 60 = 900

## Internal edge generation

For every slot t in V(G15), and for every local edge {x,y} in E(G60), add:

    (t,x) ~ (t,y)

These are internal thalion-copy edges.

Since there are 15 slots and 120 local G60 edges, this creates:

    15 * 120 = 1800

internal edges.

## Carrier edge generation

For every slot edge {t,u} in E(G15), and for every local state x in V(G60), add:

    (t,x) ~ (u, phi_sigma({t,u})(x))

where:

    phi_0(x) = x
    phi_1(x) = h(x) = x + 30 mod 60

These are external signed-carrier edges.

Since there are 30 slot edges and 60 local states, this creates:

    30 * 60 = 1800

external edges.

## Generated edge set

The full edge set is:

    E(X_sigma) = E_internal union E_carrier

The generated graph therefore has:

    900 vertices
    3600 edges

provided the source counts are admitted.

## Determinism

The operator Gen is deterministic.

Given the same G15 edge list, G60 edge list, carrier signing sigma, and half-flip rule h, it returns the same endpoint edge set.

Therefore any difference between generated candidates must come from a difference in at least one kernel component.

## Kernel admission meaning

The statement

    X_sigma = Gen(K_900)

means that the graph is generated from the kernel only.

It does not mean that every invariant of X_sigma has been proved.

The kernel generates the graph. The proof kernel certifies the claims made about the graph.
