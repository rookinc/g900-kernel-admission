# Finite set-theoretic floor

Project 18 is rooted in finite set theory.

The G900 construction does not require infinite choice, visual geometry, a graph census, or physical interpretation.

It requires only finite sets, finite relations, and finite verification.

## Basic graph form

A graph is treated as an ordered pair:

    G = (V, E)

where:

- V is a finite set,
- E is a finite set of unordered pairs from V.

## Source sets

The slot graph is:

    G15 = (V15, E15)

with:

    |V15| = 15
    |E15| = 30

The thalion fiber is:

    G60 = (V60, E60)

with:

    |V60| = 60
    |E60| = 120

## Product register

The generated vertex set is the Cartesian product:

    V900 = V15 x V60

A generated vertex is an ordered pair:

    (t, x)

where:

    t in V15
    x in V60

Therefore:

    |V900| = |V15| * |V60| = 15 * 60 = 900

## Internal relation

The internal edge relation is:

    E_internal = { {(t,x),(t,y)} : t in V15 and {x,y} in E60 }

This places one copy of the G60 relation over each slot.

## Carrier relation

The carrier relation is:

    E_carrier = { {(t,x),(u,phi_s(t,u)(x))} : {t,u} in E15 and x in V60 }

where:

    phi_0(x) = x
    phi_1(x) = x + 30 mod 60

## Generated graph

The generated graph is:

    X_sigma = (V900, E_internal union E_carrier)

## Foundation claim

The construction is finite-set-theoretic.

All later matrix forms, graph invariants, and certificates are representations or checks of this finite relation.

The renderer is not foundational.

The graph census is not foundational.

Physical interpretation is not foundational.

Project memory is not foundational.

The foundation is finite membership:

    vertex in V
    edge in E
    relation holds
    certificate verifies
