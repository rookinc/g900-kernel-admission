# Kernel claim ledger verification

- verification_ok: True
- checked_ledger: artifacts/json/kernel_claim_ledger.json
- checked_note: admission/002_kernel_claim_ledger.md

## Checks

- ledger_exists: True
- note_exists: True
- claim_classes_ok: True
- direct_claims_complete: True
- certificate_claims_complete: True
- boundary_claims_complete: True
- has_not_claimed_list: True
- has_admission_principle: True

## Counts

- direct_proof_count: 6
- certificate_required_count: 6
- external_boundary_count: 3
- not_claimed_count: 5
