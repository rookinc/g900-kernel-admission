# WXYZTI role-class invariant audit 018

Status: wxyzti_role_class_invariant_audit_recorded

## Output

- row_count: `24`

## reverse_partner

- row_count: `12`
- station_role_counts: `{'TI': 4, 'WX': 4, 'YZ': 4}`
- exact_true_flags: `['A_preserved', 'to_C_equals_from_B', 'to_C_equals_from_slot', 'to_slot_equals_from_C', 'from_slot_equals_from_B', 'to_slot_equals_to_B']`
- exact_false_flags: `['B_preserved', 'C_preserved', 'slot_preserved', 'fiber_preserved', 'to_C_equals_from_A', 'to_C_equals_from_C', 'to_slot_equals_from_A', 'to_slot_equals_from_B', 'to_slot_equals_from_slot']`
- boolean_counts:
  - A_preserved: `{True: 12}`
  - B_preserved: `{False: 12}`
  - C_preserved: `{False: 12}`
  - slot_preserved: `{False: 12}`
  - fiber_preserved: `{False: 12}`
  - to_C_equals_from_A: `{False: 12}`
  - to_C_equals_from_B: `{True: 12}`
  - to_C_equals_from_C: `{False: 12}`
  - to_C_equals_from_slot: `{True: 12}`
  - to_slot_equals_from_A: `{False: 12}`
  - to_slot_equals_from_B: `{False: 12}`
  - to_slot_equals_from_C: `{True: 12}`
  - to_slot_equals_from_slot: `{False: 12}`
  - from_slot_equals_from_B: `{True: 12}`
  - to_slot_equals_to_B: `{True: 12}`

## shared_B

- row_count: `12`
- station_role_counts: `{'IW': 4, 'XY': 4, 'ZT': 4}`
- exact_true_flags: `['B_preserved', 'slot_preserved', 'to_slot_equals_from_B', 'to_slot_equals_from_slot', 'from_slot_equals_from_B', 'to_slot_equals_to_B']`
- exact_false_flags: `['A_preserved', 'C_preserved', 'fiber_preserved', 'to_C_equals_from_A', 'to_C_equals_from_B', 'to_C_equals_from_C', 'to_C_equals_from_slot', 'to_slot_equals_from_A', 'to_slot_equals_from_C']`
- boolean_counts:
  - A_preserved: `{False: 12}`
  - B_preserved: `{True: 12}`
  - C_preserved: `{False: 12}`
  - slot_preserved: `{True: 12}`
  - fiber_preserved: `{False: 12}`
  - to_C_equals_from_A: `{False: 12}`
  - to_C_equals_from_B: `{False: 12}`
  - to_C_equals_from_C: `{False: 12}`
  - to_C_equals_from_slot: `{False: 12}`
  - to_slot_equals_from_A: `{False: 12}`
  - to_slot_equals_from_B: `{True: 12}`
  - to_slot_equals_from_C: `{False: 12}`
  - to_slot_equals_from_slot: `{True: 12}`
  - from_slot_equals_from_B: `{True: 12}`
  - to_slot_equals_to_B: `{True: 12}`

## Station summaries

- IW: exact_true=['B_preserved', 'slot_preserved', 'to_slot_equals_from_B', 'to_slot_equals_from_slot', 'from_slot_equals_from_B', 'to_slot_equals_to_B'], exact_false=['A_preserved', 'C_preserved', 'fiber_preserved', 'to_C_equals_from_A', 'to_C_equals_from_B', 'to_C_equals_from_C', 'to_C_equals_from_slot', 'to_slot_equals_from_A', 'to_slot_equals_from_C']
- TI: exact_true=['A_preserved', 'to_C_equals_from_B', 'to_C_equals_from_slot', 'to_slot_equals_from_C', 'from_slot_equals_from_B', 'to_slot_equals_to_B'], exact_false=['B_preserved', 'C_preserved', 'slot_preserved', 'fiber_preserved', 'to_C_equals_from_A', 'to_C_equals_from_C', 'to_slot_equals_from_A', 'to_slot_equals_from_B', 'to_slot_equals_from_slot']
- WX: exact_true=['A_preserved', 'to_C_equals_from_B', 'to_C_equals_from_slot', 'to_slot_equals_from_C', 'from_slot_equals_from_B', 'to_slot_equals_to_B'], exact_false=['B_preserved', 'C_preserved', 'slot_preserved', 'fiber_preserved', 'to_C_equals_from_A', 'to_C_equals_from_C', 'to_slot_equals_from_A', 'to_slot_equals_from_B', 'to_slot_equals_from_slot']
- XY: exact_true=['B_preserved', 'slot_preserved', 'to_slot_equals_from_B', 'to_slot_equals_from_slot', 'from_slot_equals_from_B', 'to_slot_equals_to_B'], exact_false=['A_preserved', 'C_preserved', 'fiber_preserved', 'to_C_equals_from_A', 'to_C_equals_from_B', 'to_C_equals_from_C', 'to_C_equals_from_slot', 'to_slot_equals_from_A', 'to_slot_equals_from_C']
- YZ: exact_true=['A_preserved', 'to_C_equals_from_B', 'to_C_equals_from_slot', 'to_slot_equals_from_C', 'from_slot_equals_from_B', 'to_slot_equals_to_B'], exact_false=['B_preserved', 'C_preserved', 'slot_preserved', 'fiber_preserved', 'to_C_equals_from_A', 'to_C_equals_from_C', 'to_slot_equals_from_A', 'to_slot_equals_from_B', 'to_slot_equals_from_slot']
- ZT: exact_true=['B_preserved', 'slot_preserved', 'to_slot_equals_from_B', 'to_slot_equals_from_slot', 'from_slot_equals_from_B', 'to_slot_equals_to_B'], exact_false=['A_preserved', 'C_preserved', 'fiber_preserved', 'to_C_equals_from_A', 'to_C_equals_from_B', 'to_C_equals_from_C', 'to_C_equals_from_slot', 'to_slot_equals_from_A', 'to_slot_equals_from_C']

## Boundary

This is an invariant audit over realized station rows only. It does not generate the allowed transitions from a non-realized candidate universe and does not close Gap A.
