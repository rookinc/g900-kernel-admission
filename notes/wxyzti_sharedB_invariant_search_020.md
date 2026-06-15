# WXYZTI shared_B invariant search 020

Status: wxyzti_sharedB_invariant_search_recorded

## Output

- sharedB_row_count: `12`
- global_invariant_count: `14`
- global_constant_delta_count: `14`

## Global invariants

- B mod 15
- 2*B mod 15
- 3*B mod 15
- 4*B mod 15
- 5*B mod 15
- 6*B mod 15
- 7*B mod 15
- 8*B mod 15
- 9*B mod 15
- 10*B mod 15
- 11*B mod 15
- 12*B mod 15
- 13*B mod 15
- 14*B mod 15

## Global constant deltas

- B mod 15 delta=0
- 2*B mod 15 delta=0
- 3*B mod 15 delta=0
- 4*B mod 15 delta=0
- 5*B mod 15 delta=0
- 6*B mod 15 delta=0
- 7*B mod 15 delta=0
- 8*B mod 15 delta=0
- 9*B mod 15 delta=0
- 10*B mod 15 delta=0
- 11*B mod 15 delta=0
- 12*B mod 15 delta=0
- 13*B mod 15 delta=0
- 14*B mod 15 delta=0

## By station role

- IW
  - row_count: `4`
  - invariant_count: `14`
  - constant_delta_count: `14`
  - invariants:
    - B mod 15
    - 2*B mod 15
    - 3*B mod 15
    - 4*B mod 15
    - 5*B mod 15
    - 6*B mod 15
    - 7*B mod 15
    - 8*B mod 15
    - 9*B mod 15
    - 10*B mod 15
  - constant deltas:
    - B mod 15 delta=0
    - 2*B mod 15 delta=0
    - 3*B mod 15 delta=0
    - 4*B mod 15 delta=0
    - 5*B mod 15 delta=0
    - 6*B mod 15 delta=0
    - 7*B mod 15 delta=0
    - 8*B mod 15 delta=0
    - 9*B mod 15 delta=0
    - 10*B mod 15 delta=0
- XY
  - row_count: `4`
  - invariant_count: `14`
  - constant_delta_count: `14`
  - invariants:
    - B mod 15
    - 2*B mod 15
    - 3*B mod 15
    - 4*B mod 15
    - 5*B mod 15
    - 6*B mod 15
    - 7*B mod 15
    - 8*B mod 15
    - 9*B mod 15
    - 10*B mod 15
  - constant deltas:
    - B mod 15 delta=0
    - 2*B mod 15 delta=0
    - 3*B mod 15 delta=0
    - 4*B mod 15 delta=0
    - 5*B mod 15 delta=0
    - 6*B mod 15 delta=0
    - 7*B mod 15 delta=0
    - 8*B mod 15 delta=0
    - 9*B mod 15 delta=0
    - 10*B mod 15 delta=0
- ZT
  - row_count: `4`
  - invariant_count: `14`
  - constant_delta_count: `14`
  - invariants:
    - B mod 15
    - 2*B mod 15
    - 3*B mod 15
    - 4*B mod 15
    - 5*B mod 15
    - 6*B mod 15
    - 7*B mod 15
    - 8*B mod 15
    - 9*B mod 15
    - 10*B mod 15
  - constant deltas:
    - B mod 15 delta=0
    - 2*B mod 15 delta=0
    - 3*B mod 15 delta=0
    - 4*B mod 15 delta=0
    - 5*B mod 15 delta=0
    - 6*B mod 15 delta=0
    - 7*B mod 15 delta=0
    - 8*B mod 15 delta=0
    - 9*B mod 15 delta=0
    - 10*B mod 15 delta=0

## Boundary

This audits realized shared_B rows only. It does not generate the shared_B candidate set and does not close Gap A.

## Reading

The 14 global invariants are one substantive invariant repeated by multiplication:

    B is preserved.

No additional global linear invariant involving A and C was found.

So shared_B should be read as a B-preserving coupler with residual A/C motion, not as a map preserving a second simple linear quantity in the tested family.
