# 18-g900-kernel-admission

This project begins the kernel-admission phase for the G900 theorem program.

Project 17 produced the release-candidate theorem proof package:

- finite construction note
- signed half-flip carrier construction
- reproducibility spine
- admission boundary
- no census claim
- no uniqueness claim
- no physical interpretation claim

Project 18 does not change the object.

Project 18 asks:

What is the smallest finite kernel that generates the candidate, and what certificate bundle is required for bounded QED admission?

## Core distinction

17 = theorem proof package / rc1 note

18 = kernel admission

## Construction kernel

The construction kernel is

    K_900 = (G15, G60, sigma, h)

where:

- G15 is the 15-slot graph.
- G60 is the 60-state thalion fiber.
- sigma is the F2-valued carrier signing on E(G15).
- h is the half-flip involution h(x) = x + 30 mod 60.

The generated graph is

    X_sigma = Gen(K_900)

## Proof kernel

The proof kernel is

    P_900 = (K_900, C)

where C is the finite certificate bundle needed to admit the bounded theorem.

## Boundary

This project does not claim:

- uniqueness of the G900 ring
- census identification
- physical interpretation
- invalidity of sibling candidates
- final public theorem status until admission criteria are met

## Current goal

Convert the project-17 computational theorem package into a bounded finite theorem admission by defining:

1. the construction kernel,
2. the proof kernel,
3. certificate requirements,
4. admissibility criteria,
5. one clean verification target.
