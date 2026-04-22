# Process & Procedures for All Works

**Document ID:** AIWA-DOC-03
**Version:** 1.0
**Scope:** System flow, stages, roles, escalation, and government approval handling.
**Restrictions:** This document is procedural and stage-based.

---

## 1. Purpose

1.1. This document defines the end-to-end process for all works entering and managed within the AIWA system.
1.2. This document defines stages, roles, and outputs for each step.
1.3. This document defines escalation rules.
1.4. This document defines how government approvals are handled.

---

## 2. Roles

2.1. **Intake Officer** — receives and logs incoming works.
2.2. **Classification Officer** — performs and records all classification decisions.
2.3. **Legal Officer** — confirms legal compliance and ministry alignment.
2.4. **Stewardship Officer** — manages ongoing rights, records, and payout.
2.5. **Governance Board** — holds final authority on escalated decisions.
2.6. **PRIME Liaison** — manages communication with PRIME for offshore exploitation.
2.7. **Submitting Party** — the creator, rights holder, or authorized representative submitting a work.

---

## 3. Allowed Decision States

3.1. The only allowed decision states are:

- **Approved** — the work is cleared for the stated scope of use.
- **Approved with Limits** — the work is cleared with defined restrictions on scope, territory, or use type.
- **Held** — the work is paused pending further information or review.
- **Restricted** — the work is blocked from the stated use due to classification or legal grounds.
- **Rejected** — the work does not meet the requirements for entry into the system.
- **Escalated** — the decision has been referred to the Governance Board.

3.2. No additional decision states are permitted.
3.3. Every decision must be recorded with a decision state.
3.4. No undocumented decisions are permitted.
3.5. No verbal approvals are permitted.

---

## 4. Stage 1 — Submission and Intake

### 4.1. What

The Submitting Party submits the work to AIWA for registration and classification.

### 4.2. Why

All works must enter the system through a controlled intake point. No work may be classified or exploited without a formal submission record.

### 4.3. Who

- **Submitting Party** — submits the work and supporting documentation.
- **Intake Officer** — receives, logs, and validates the submission.

### 4.4. When

At the point of first submission to the AIWA system.

### 4.5. Where

Through the AIWA intake channel (physical or digital, as defined by AIWA operational rules).

### 4.6. How

1. The Submitting Party provides the work and all required documentation.
2. The Intake Officer assigns a unique submission reference number.
3. The Intake Officer logs the work type, submitting party, date, and medium.
4. The Intake Officer confirms the completeness of the submission.
5. If the submission is incomplete, the Intake Officer returns it to the Submitting Party with a written explanation.
6. If the submission is complete, the Intake Officer passes the record to the Classification Officer.

### 4.7. Output

A complete submission record with a unique reference number. The work status is set to **Unclassified**.

---

## 5. Stage 2 — Classification

### 5.1. What

The Classification Officer assigns a primary classification to the work.

### 5.2. Why

No work may be released, licensed, or exploited without a valid classification. Classification determines all downstream decisions.

### 5.3. Who

- **Classification Officer** — performs and records the classification decision.
- **Legal Officer** — is consulted when classification has legal implications.

### 5.4. When

After a complete submission record has been received from Stage 1.

### 5.5. Where

Within the AIWA classification system.

### 5.6. How

1. The Classification Officer reviews the work and supporting documentation.
2. The Classification Officer applies the classification logic defined in AIWA-DOC-01.
3. The Classification Officer determines the primary classification category.
4. If the work involves AI training inputs, the Classification Officer must flag the record for additional control review.
5. If the work is Folklore or Folklore-Linked, the Classification Officer must set the decision state to **Restricted** unless explicit authorization exists.
6. The Classification Officer records the classification decision with a written rationale.
7. The Classification Officer sets the decision state based on the classification outcome:
   - Clear modern work → **Approved** (subject to Stage 3).
   - Folklore or Folklore-Linked → **Restricted** unless authorization is confirmed.
   - AI Training Input → **Held** pending control review.
   - Ambiguous classification → **Escalated** to the Governance Board.
   - Insufficient information → **Held** pending additional documentation.

### 5.7. Output

A classification record with a primary classification category, decision state, and written rationale.

---

## 6. Stage 3 — Legal and Ministry Review

### 6.1. What

The Legal Officer confirms that the classification and intended use comply with Gambian law and applicable ministry jurisdiction.

### 6.2. Why

Gambian law governs first. All works must be confirmed as legally compliant before any exploitation decision is made.

### 6.3. Who

- **Legal Officer** — performs the legal and ministry review.
- **Classification Officer** — provides the classification record from Stage 2.
- **Governance Board** — is consulted when ministry jurisdiction is unclear or disputed.

### 6.4. When

After a classification decision has been recorded in Stage 2.

### 6.5. Where

Within the AIWA legal review function.

### 6.6. How

1. The Legal Officer receives the classification record from Stage 2.
2. The Legal Officer identifies the applicable Gambian laws for the work type and classification.
3. The Legal Officer identifies all ministries with applicable jurisdiction.
4. If ministry jurisdiction is unclear, the Legal Officer sets the decision state to **Escalated** and refers to the Governance Board.
5. The Legal Officer confirms whether any government authorization is required.
6. If government authorization is required and has been provided, the Legal Officer verifies its scope and validity.
7. If government authorization is required and has not been provided, the Legal Officer sets the decision state to **Held**.
8. If the work is legally compliant, the Legal Officer records a legal clearance.
9. If the work is not legally compliant, the Legal Officer sets the decision state to **Restricted** or **Rejected** with a written reason.

### 6.7. Output

A legal review record confirming applicable law, ministry jurisdiction, and legal clearance status. The decision state is updated accordingly.

---

## 7. Stage 4 — Stewardship Assignment

### 7.1. What

The Stewardship Officer assigns formal stewardship responsibilities to AIWA and records the creator's ownership details.

### 7.2. Why

AIWA is the mandatory local steward for all works in this system. Stewardship must be formally recorded before any exploitation.

### 7.3. Who

- **Stewardship Officer** — performs the assignment and recording.
- **Submitting Party** — confirms ownership details.

### 7.4. When

After legal clearance has been confirmed in Stage 3.

### 7.5. Where

Within the AIWA stewardship registry.

### 7.6. How

1. The Stewardship Officer receives the legal clearance record from Stage 3.
2. The Stewardship Officer confirms the creator's ownership details with the Submitting Party.
3. The Stewardship Officer records AIWA as the local steward in the stewardship registry.
4. The Stewardship Officer records the creator's retained ownership.
5. The Stewardship Officer records any payout terms agreed with the Submitting Party.
6. The Stewardship Officer sets the work status to **Approved** or **Approved with Limits** as applicable.

### 7.7. Output

A stewardship record confirming AIWA as local steward, creator ownership, and payout terms.

---

## 8. Stage 5 — Offshore Referral to PRIME (Where Applicable)

### 8.1. What

The PRIME Liaison refers an approved work to PRIME for offshore exploitation.

### 8.2. Why

PRIME is the non-exclusive offshore exploitation partner. Works may only be referred to PRIME after AIWA approval. PRIME must not exploit a work that AIWA has not approved.

### 8.3. Who

- **PRIME Liaison** — manages the referral.
- **Stewardship Officer** — confirms the work's approval status before referral.
- **PRIME** — receives the referral for offshore exploitation.

### 8.4. When

After stewardship has been recorded in Stage 4 and only when offshore exploitation has been requested or authorized.

### 8.5. Where

Through the AIWA-PRIME contractual channel.

### 8.6. How

1. The PRIME Liaison confirms that the work holds a status of **Approved** or **Approved with Limits** in the AIWA system.
2. The PRIME Liaison confirms the scope of any limits applied.
3. The PRIME Liaison prepares a referral record including classification, approved scope, and any restrictions.
4. The PRIME Liaison transmits the referral to PRIME through the designated contractual channel.
5. PRIME must not exceed the approved scope defined in the referral record.
6. PRIME must not reclassify the work.
7. PRIME must not remove or override any restriction applied by AIWA.

### 8.7. Output

A PRIME referral record confirming approved scope, classification, and any applicable restrictions.

---

## 9. Stage 6 — Ongoing Stewardship, Records, and Payout

### 9.1. What

The Stewardship Officer maintains the work record, manages rights, and administers payout.

### 9.2. Why

AIWA is the stewardship and payout system for all registered works. Records must be maintained for auditability and compliance.

### 9.3. Who

- **Stewardship Officer** — maintains records and manages payout.
- **Submitting Party / Creator** — receives payout under agreed terms.
- **PRIME Liaison** — reports offshore exploitation activity to the Stewardship Officer.

### 9.4. When

On an ongoing basis after Stage 4 completion, and whenever an exploitation event is reported.

### 9.5. Where

Within the AIWA stewardship registry and payout system.

### 9.6. How

1. The Stewardship Officer maintains an up-to-date record for each work.
2. The Stewardship Officer records all exploitation events reported by the PRIME Liaison or other licensed parties.
3. The Stewardship Officer calculates payout due to the creator under agreed terms.
4. The Stewardship Officer executes payout within the period defined in the payout agreement.
5. The Stewardship Officer records each payout with a reference to the triggering exploitation event.
6. No payout may be made without a corresponding exploitation record.

### 9.7. Output

Updated work records and documented payout events in the AIWA stewardship registry.

---

## 10. Escalation Rules

10.1. Any stage may trigger an escalation to the Governance Board.
10.2. Escalation is mandatory when:

- Classification is ambiguous and cannot be resolved by the Classification Officer.
- Ministry jurisdiction is unclear or disputed.
- A legal conflict arises between Gambian law and a contractual term.
- A Submitting Party disputes a classification or decision.
- A work involves AI Training Inputs with no existing authorization.

10.3. The escalating officer must record the reason for escalation in writing.
10.4. The Governance Board must issue a decision in one of the allowed decision states defined in Section 3.
10.5. The Governance Board's decision must be recorded and attached to the work record.
10.6. No escalation may be resolved verbally.

---

## 11. Government Approval Handling

11.1. Government authorization does not constitute AIWA approval.
11.2. Government authorization must be verified by the Legal Officer in Stage 3.
11.3. Government authorization is scope-limited. It applies only to the use explicitly stated.
11.4. Government authorization does not remove the classification assigned by AIWA.
11.5. Government authorization does not authorize AI training use unless AI training use is explicitly stated.
11.6. A work with government authorization must still complete all stages of this process.
11.7. The Legal Officer must record the scope and validity period of any government authorization.

---

## 12. Control Rules

12.1. No undocumented decisions are permitted at any stage.
12.2. No verbal approvals are permitted at any stage.
12.3. No work may bypass classification.
12.4. No AI training use is automatic. Classification determines eligibility.
12.5. No work may be released before approval.
12.6. No reclassification may occur without a documented record.
12.7. Restricted and folklore-linked works are blocked from AI training use unless explicitly authorized.
12.8. No work may be passed to PRIME without AIWA approval on record.

---

**End of AIWA-DOC-03**
