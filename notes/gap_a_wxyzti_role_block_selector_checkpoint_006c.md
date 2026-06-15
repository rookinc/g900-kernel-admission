# Gap A WXYZTI role-block selector checkpoint 006c

Status: gap_a_wxyzti_role_block_selector_checkpoint_recorded

## Result

The WXYZTI overlay now has a coherent local selector chain.

Signed G15 native profile reduces the role-block circulation candidates to 7.

Observed support, q0/q3 inclusion, and shared junction C=2 reduce those 7 to 2.

Directed WXYZTI channel compatibility reduces those 2 to exactly 1.

The selected target is:

    A = [0, 2, 10, 14]
    B = [2, 4, 11, 13]
    C = [1, 2, 5]

with channel order:

    WX/ZT sends A to B.
    TI/XY sends B to C.
    IW/YZ sends C to A.

The target matches all 12 directed C-transitions.

The non-target twin matches 6 of 12 and misses 6.

## Selector chain

1. Signed G15 native profile

    Source:
    artifacts/json/role_block_circulation_native_profile_census_006.v1.json

    Counts:
    total_valid_shape = 25225200
    block_profile_match_count = 195149
    channel_cut_match_count = 135
    full_native_profile_match_count = 7

2. Observed/q0/q3/junction context

    Source:
    artifacts/json/role_block_full_profile_match_inspection_006b.v1.json

    Counts:
    full_match_count_available = 7
    observed_union_match_count = 2
    junction_2_match_count = 2
    q3_subset_union_match_count = 2
    q0_subset_union_match_count = 2

3. Directed WXYZTI channel compatibility

    Source:
    artifacts/json/role_block_directed_transition_selector_006c.v1.json

    Counts:
    candidate_count = 2
    exact_directed_transition_cover_count = 1
    selected_indices = [3]
    target_selected = true
    non_target_selected_count = 0

## Current narrowed statement

The WXYZTI role-block circulation is not uniquely derived from signed G15 profile alone.

However, it has a rare signed-G15 footprint, and when observed support, q0/q3 inclusion, shared junction C=2, and directed WXYZTI channel compatibility are added, the target circulation is selected exactly.

This is a strong local selector chain.

## Boundary

This does not close Gap A.

This does not derive a G60-native generator.

This does not admit full G900.

This does not make WXYZTI edges literal X_sigma or Project16 carrier adjacency.

This does not derive a physical interpretation.

The directed WXYZTI transition table remains upstream.

## Next problem

Derive or independently source the directed WXYZTI transition table from one of the following:

    WXYZTI station constraints
    oriented signed G15 structure
    native G60 structure
    old Hyperxi/G60 involution shadows
    another native object that does not assume the transition table

Compact next question:

    Can the 12 directed C-transitions be generated natively?
