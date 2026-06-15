# WXYZTI reverse_partner vs shared_B audit 016

Status: wxyzti_reverse_partner_vs_sharedB_audit_recorded

## Output

- row_count: `24`

## reverse_partner

- row_count: `12`
- station_role_counts: `{'TI': 4, 'WX': 4, 'YZ': 4}`
- from_C_values: `[0, 1, 2, 4, 5, 10, 11, 13, 14]`
- to_C_values: `[0, 1, 2, 4, 5, 10, 11, 13, 14]`
- best laws:
  - from_B: matches=12/12, exact=True
  - from_slot: matches=12/12, exact=True
  - from_A: matches=0/12, exact=False
  - from_A_minus_9: matches=0/12, exact=False
  - from_A_plus_3: matches=0/12, exact=False
  - from_B_minus_2: matches=0/12, exact=False
  - from_B_plus_2: matches=0/12, exact=False
  - from_C: matches=0/12, exact=False
  - from_slot_minus_2: matches=0/12, exact=False
  - from_slot_plus_2: matches=0/12, exact=False

## shared_B

- row_count: `12`
- station_role_counts: `{'IW': 4, 'XY': 4, 'ZT': 4}`
- from_C_values: `[0, 1, 2, 4, 5, 10, 11, 13, 14]`
- to_C_values: `[0, 1, 2, 4, 5, 10, 11, 13, 14]`
- best laws:
  - from_B_minus_2: matches=2/12, exact=False
  - from_slot_minus_2: matches=2/12, exact=False
  - from_A_plus_3: matches=1/12, exact=False
  - from_A: matches=0/12, exact=False
  - from_A_minus_9: matches=0/12, exact=False
  - from_B: matches=0/12, exact=False
  - from_B_plus_2: matches=0/12, exact=False
  - from_C: matches=0/12, exact=False
  - from_slot: matches=0/12, exact=False
  - from_slot_plus_2: matches=0/12, exact=False

## Station summaries

- IW:
  - from_B_minus_2: matches=2/4, exact=False
  - from_slot_minus_2: matches=2/4, exact=False
  - from_A_plus_3: matches=1/4, exact=False
  - from_A: matches=0/4, exact=False
  - from_A_minus_9: matches=0/4, exact=False
- TI:
  - from_B: matches=4/4, exact=True
  - from_slot: matches=4/4, exact=True
  - from_A: matches=0/4, exact=False
  - from_A_minus_9: matches=0/4, exact=False
  - from_A_plus_3: matches=0/4, exact=False
- WX:
  - from_B: matches=4/4, exact=True
  - from_slot: matches=4/4, exact=True
  - from_A: matches=0/4, exact=False
  - from_A_minus_9: matches=0/4, exact=False
  - from_A_plus_3: matches=0/4, exact=False
- XY:
  - from_A: matches=0/4, exact=False
  - from_A_minus_9: matches=0/4, exact=False
  - from_A_plus_3: matches=0/4, exact=False
  - from_B: matches=0/4, exact=False
  - from_B_minus_2: matches=0/4, exact=False
- YZ:
  - from_B: matches=4/4, exact=True
  - from_slot: matches=4/4, exact=True
  - from_A: matches=0/4, exact=False
  - from_A_minus_9: matches=0/4, exact=False
  - from_A_plus_3: matches=0/4, exact=False
- ZT:
  - from_A: matches=0/4, exact=False
  - from_A_minus_9: matches=0/4, exact=False
  - from_A_plus_3: matches=0/4, exact=False
  - from_B: matches=0/4, exact=False
  - from_B_minus_2: matches=0/4, exact=False

## Boundary

This audits realized rows only. It does not prove selection from non-realized candidates and does not close Gap A.
