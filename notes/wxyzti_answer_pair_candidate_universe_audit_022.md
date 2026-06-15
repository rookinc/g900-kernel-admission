# WXYZTI answer-pair candidate universe audit 022

Status: wxyzti_answer_pair_candidate_universe_audit_recorded

## Candidate universe

All shared_B rows crossed with all reverse_partner rows having the same role_pair.

- shared_row_count: `12`
- reverse_row_count: `12`
- candidate_count: `48`
- expected_pair_count: `12`
- candidate_role_pair_counts: `{'IW/YZ': 16, 'TI/XY': 16, 'WX/ZT': 16}`
- expected_role_pair_counts: `{'IW/YZ': 4, 'TI/XY': 4, 'WX/ZT': 4}`

## Selector scores

- same_role_pair: accepted=48, false_positive=36, miss=0, exact=False
- same_from_C: accepted=14, false_positive=2, miss=0, exact=False
- same_to_C: accepted=14, false_positive=2, miss=0, exact=False
- same_C_delta: accepted=18, false_positive=6, miss=0, exact=False
- same_integer_C_delta: accepted=14, false_positive=2, miss=0, exact=False
- same_lift_q: accepted=26, false_positive=14, miss=0, exact=False
- answer_R_from_B_to_S_to_C: accepted=14, false_positive=2, miss=0, exact=False
- answer_R_from_slot_to_S_to_C: accepted=14, false_positive=2, miss=0, exact=False
- return_R_to_B_to_S_from_C: accepted=14, false_positive=2, miss=0, exact=False
- return_R_to_slot_to_S_from_C: accepted=14, false_positive=2, miss=0, exact=False
- reciprocal_answer_pair: accepted=12, false_positive=0, miss=0, exact=True
- strict_pair_grammar: accepted=12, false_positive=0, miss=0, exact=True

## Exact selectors

- reciprocal_answer_pair
- strict_pair_grammar

## Reading

The strict pair grammar is exact when it accepts exactly the 12 expected reciprocal pairs with no false positives and no misses.

Strict pair grammar means:

    same role_pair
    same from_C
    same to_C
    same C_delta
    same integer_C_delta
    same lift_q
    shared_B preserves B/slot
    reverse_partner preserves A and swaps B/C
    reverse_partner.from_B supplies shared_B.to_C
    reverse_partner.to_B returns shared_B.from_C

## Boundary

This is still a row-pair candidate universe built from realized WXYZTI rows. It is stronger than a realized-pair audit, but it is not a native G60 generator and does not close Gap A.
