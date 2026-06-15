# WXYZTI station transform map audit 019

Status: wxyzti_station_transform_map_audit_recorded

## Output

- row_count: `24`
- reverse_partner_row_count: `12`
- shared_B_row_count: `12`
- reverse_partner_swap_BC_match_count: `12`
- reverse_partner_swap_BC_miss_count: `0`
- reverse_partner_swap_BC_exact: `True`

## reverse_partner transform

reverse_partner realizes:

    (A, B, C) -> (A, C, B)

## shared_B by role

- IW
  - row_count: `4`
  - B_preserved_count: `4/4`
  - slot_preserved_count: `4/4`
  - delta_ABC_counts: `{'(4, 0, 10)': 1, '(6, 0, 12)': 1, '(7, 0, 9)': 1, '(8, 0, 12)': 1}`
  - transitions:
    - `(2, 13, 1) -> (9, 13, 10), delta=(7, 0, 9)`
    - `(1, 11, 2) -> (7, 11, 14), delta=(6, 0, 12)`
    - `(12, 2, 5) -> (1, 2, 0), delta=(4, 0, 10)`
    - `(10, 4, 5) -> (3, 4, 2), delta=(8, 0, 12)`
- XY
  - row_count: `4`
  - B_preserved_count: `4/4`
  - slot_preserved_count: `4/4`
  - delta_ABC_counts: `{'(11, 0, 6)': 1, '(6, 0, 3)': 1, '(9, 0, 1)': 1, '(9, 0, 3)': 1}`
  - transitions:
    - `(1, 0, 2) -> (10, 0, 5), delta=(9, 0, 3)`
    - `(3, 2, 4) -> (12, 2, 5), delta=(9, 0, 1)`
    - `(7, 14, 11) -> (3, 14, 2), delta=(11, 0, 6)`
    - `(9, 10, 13) -> (0, 10, 1), delta=(6, 0, 3)`
- ZT
  - row_count: `4`
  - B_preserved_count: `4/4`
  - slot_preserved_count: `4/4`
  - delta_ABC_counts: `{'(13, 0, 12)': 1, '(13, 0, 2)': 1, '(2, 0, 2)': 1, '(2, 0, 3)': 1}`
  - transitions:
    - `(10, 5, 0) -> (12, 5, 2), delta=(2, 0, 2)`
    - `(12, 5, 2) -> (10, 5, 4), delta=(13, 0, 2)`
    - `(0, 1, 10) -> (2, 1, 13), delta=(2, 0, 3)`
    - `(3, 2, 14) -> (1, 2, 11), delta=(13, 0, 12)`

## Boundary

This audits realized station rows only. It does not generate shared_B from a non-realized candidate universe and does not close Gap A.
