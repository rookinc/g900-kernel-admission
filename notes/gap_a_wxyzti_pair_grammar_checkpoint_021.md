# Gap A WXYZTI pair grammar checkpoint 021

Status: gap_a_wxyzti_pair_grammar_checkpoint_recorded

## Result

The realized WXYZTI overlay now has a paired local grammar.

Each directed C-transition has exactly two station rows:

    one shared_B row
    one reciprocal reverse_partner row

The pair is keyed by:

    role_pair
    from_C
    to_C

The audit found:

    pair_count = 12
    bad_bucket_count = 0

## reverse_partner law

Roles:

    TI
    WX
    YZ

Exact transform:

    (A, B, C) -> (A, C, B)

Meaning:

    reverse_partner preserves A.
    reverse_partner sends to_C = from_B = from_slot.
    reverse_partner sends to_B = from_C.
    reverse_partner sends to_slot = from_C.

This was exact over all 12 reverse_partner rows.

## shared_B law

Roles:

    IW
    XY
    ZT

Exact structure:

    shared_B preserves B.
    shared_B preserves slot.
    from_slot = from_B.
    to_slot = from_B = to_B.

The shared_B invariant search found no additional global linear invariant involving A/C in the tested family. The 14 listed invariants were all multiples of the same substantive invariant:

    B is preserved.

## pair coupling law

For all 12 realized reciprocal pairs:

    S and R share role_pair.
    S and R share from_C.
    S and R share to_C.
    S and R share C_delta.
    S and R share integer_C_delta.
    S and R share lift_q.

The key cross-coupling is:

    S.to_C = R.from_B
    S.to_C = R.from_slot
    R.to_B = S.from_C
    R.to_slot = S.from_C

So shared_B does not answer alone.

The shared_B row preserves B/slot.

The paired reverse_partner row supplies the answer.

## Compact statement

The witness is the nearest neighbor that answers back.

The shared_B carrier preserves B/slot, while the paired reverse_partner row supplies the returned C value by swapping B and C.

## Boundary

This does not close Gap A.

This does not derive a G60-native generator.

This does not admit full G900.

This does not generate the non-realized candidate universe.

This audits realized reciprocal WXYZTI station pairs only.

## Next problem

Generate the 12 reciprocal shared_B/reverse_partner pairs from a native candidate universe, rather than merely auditing realized WXYZTI rows.

Compact next question:

    What native rule generates exactly these 12 reciprocal answer-pairs?
