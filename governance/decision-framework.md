# Decision Framework

**Document ID:** AIWA-GOV-02
**Version:** 1.0
**Scope:** Decision logic, authority, and control rules for all decisions made within the AIWA system.

---

## 1. Purpose

1.1. This document defines the decision-making framework for the AIWA system.
1.2. This document defines who may make each type of decision.
1.3. This document defines the allowed decision states.
1.4. This document defines the control rules that apply to all decisions.
1.5. This document defines the escalation path for contested or ambiguous decisions.

---

## 2. Decision Principles

2.1. All decisions must be documented.
2.2. No verbal approvals are permitted.
2.3. No decision may be made outside the allowed decision states.
2.4. No work may be exploited without a recorded approval decision.
2.5. When in doubt, the decision state must be **Held** or **Escalated**.
2.6. The default state for any unresolved decision is **Held**.

---

## 3. Allowed Decision States

3.1. The only allowed decision states are:

| State | Definition |
|-------|------------|
| **Approved** | The work is cleared for the stated scope of use. |
| **Approved with Limits** | The work is cleared with defined restrictions on scope, territory, or use type. |
| **Held** | The work is paused pending further information or review. |
| **Restricted** | The work is blocked from the stated use due to classification or legal grounds. |
| **Rejected** | The work does not meet the requirements for entry into the system. |
| **Escalated** | The decision has been referred to the Governance Board. |

3.2. No additional decision states are permitted.
3.3. Each decision must be recorded with exactly one decision state.
3.4. A decision state may only be changed through a new recorded decision.

---

## 4. Decision Authority

4.1. **Intake Officer** — may set the work status to Unclassified. May return incomplete submissions.
4.2. **Classification Officer** — may set the decision state to Approved (subject to Stage 3), Restricted (folklore or folklore-linked), Held (insufficient information or AI input), or Escalated (ambiguous classification).
4.3. **Legal Officer** — may set the decision state to Held (pending authorization), Restricted (legal non-compliance), Rejected (legal failure), Escalated (unclear jurisdiction), or Legal Clearance (passing to Stage 4).
4.4. **Stewardship Officer** — may set the decision state to Approved or Approved with Limits after Stage 4 completion.
4.5. **Governance Board** — may issue any decision state. The Governance Board has final authority on escalated matters.
4.6. **PRIME Liaison** — does not make classification or approval decisions. The PRIME Liaison confirms and communicates existing decisions only.

---

## 5. Decision Logic

### 5.1. Classification Decision Logic

| Condition | Decision State |
|-----------|---------------|
| Clear modern work with identifiable author | Approved (subject to legal review) |
| Work is Folklore or Folklore-Linked | Restricted (unless explicit authorization exists) |
| Work is an AI Training Input | Held (pending control review) |
| Classification is ambiguous | Escalated |
| Insufficient information to classify | Held |

### 5.2. Legal Review Decision Logic

| Condition | Decision State |
|-----------|---------------|
| Work is legally compliant under Gambian law | Legal clearance — proceed to Stage 4 |
| Government authorization required but not provided | Held |
| Government authorization provided — scope confirmed | Legal clearance (within scope) |
| Work is not legally compliant | Restricted or Rejected |
| Ministry jurisdiction is unclear | Escalated |

### 5.3. Final Approval Decision Logic

| Condition | Decision State |
|-----------|---------------|
| Work has completed all stages with no restrictions | Approved |
| Work has completed all stages with confirmed limits | Approved with Limits |
| Work has not completed all stages | Held |
| Work has failed classification or legal review | Restricted or Rejected |

---

## 6. Control Rules

6.1. No undocumented decisions are permitted at any stage.
6.2. No verbal approvals are permitted at any stage.
6.3. No work may bypass classification.
6.4. No AI training use is automatic. Classification determines eligibility.
6.5. No work may be released before approval.
6.6. No reclassification may occur without a documented record.
6.7. Restricted and folklore-linked works are blocked from AI training use unless explicitly authorized.
6.8. No work may be passed to PRIME without AIWA approval on record.
6.9. No government authorization is effective until verified by the Legal Officer.
6.10. A Held work must not be exploited until the hold is resolved by a new recorded decision.

---

## 7. Escalation Path

7.1. Any role may escalate a decision to the Governance Board.
7.2. Escalation is mandatory when:

- Classification is ambiguous and cannot be resolved by the Classification Officer.
- Ministry jurisdiction is unclear or disputed.
- A legal conflict arises between Gambian law and a contractual term.
- A Submitting Party disputes a classification or decision in writing.
- A work involves AI Training Inputs with no existing authorization.

7.3. The escalating officer must record the reason for escalation in writing before submitting the escalation.
7.4. The Governance Board must issue a decision in one of the allowed decision states defined in Section 3.
7.5. The Governance Board's decision must be recorded and attached to the work record.
7.6. No escalation may be resolved verbally.
7.7. The Governance Board's decision is final unless overturned by a subsequent recorded Governance Board decision.

---

## 8. Record Requirements

8.1. Every decision must include:

- The unique work reference number.
- The decision state assigned.
- The name and role of the officer making the decision.
- The date and time of the decision.
- A written rationale for the decision.
- Any conditions, limits, or restrictions attached to the decision.

8.2. Decision records must be retained and must be accessible for audit.
8.3. No decision record may be altered after the fact without a new recorded decision that references and supersedes the original.

---

## 9. Reclassification Rules

9.1. A work may only be reclassified through a documented AIWA decision.
9.2. Reclassification must be recorded with a rationale.
9.3. The reclassification record must reference the original classification.
9.4. Reclassification to a less restrictive category requires Governance Board approval.
9.5. PRIME may not reclassify a work.
9.6. Government authorization does not constitute reclassification.

---

**End of AIWA-GOV-02**
