# Kernel admission standard

A G900 kernel admission must satisfy the following requirements.

## 1. Source admission

The source objects must be explicit:

- G15 slot edge list,
- G60 local edge list,
- carrier signing table,
- half-flip rule.

## 2. Construction admission

The graph X_sigma must be regenerated from the kernel only:

    X_sigma = Gen(G15, G60, sigma, h)

No renderer data may be required.

## 3. Invariant admission

Every claimed invariant must be either:

- proved directly from the kernel,
- certified by a finite witness,
- checked by an independent verifier.

## 4. Separation admission

The proof must retain nearby alternatives:

- untwisted Cartesian product baseline,
- sibling candidate.

The canonical candidate must be separated from these by explicit invariants or finite algebra.

## 5. Boundary admission

The admission must state what is not claimed:

- no uniqueness unless proved,
- no census identification unless independently established,
- no physical interpretation unless separately justified,
- no dismissal of sibling candidates unless proved.

## 6. QED target

The QED target is a bounded finite theorem:

Given K_900 and certificate bundle C, the generated graph X_sigma has the stated finite invariants and separations.

Nothing broader is admitted by this theorem.
