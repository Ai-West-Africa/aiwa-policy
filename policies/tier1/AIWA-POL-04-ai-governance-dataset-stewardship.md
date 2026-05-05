# AI Governance & Dataset Stewardship Policy

**Document ID:** AIWA-POL-04
**Version:** 1.0
**Status:** Active
**Tier:** 1 — Foundational Governance
**Scope:** Governance of AI-processable materials, dataset intake, provenance, consent, downstream licensing, and restrictions on AI use within the AIWA system.
**Restrictions:** This document does not contain process or workflow. Those are contained in AIWA-DOC-03.
**Cross-Reference:** AIWA-DOC-01 (Classification), AIWA-DOC-02 (Legal Alignment), AIWA-POL-01 (Rights Administration), AIWA-POL-03 (Cultural Heritage), AIWA-POL-05 (Rights Verification), AIWA-POL-12 (AI Dataset Licensing)

---

## 1. Purpose

1.1. This document defines AIWA's governance framework for AI-processable materials and datasets.

1.2. This document establishes standards for dataset intake, provenance tracking, consent verification, AI processing permissions, and restrictions on AI use.

1.3. This document governs AIWA's obligations as a steward of materials that may be processed by AI systems, including obligations to rights holders and to the communities whose cultural materials are involved.

1.4. AIWA administers rights on behalf of rights holders and does not acquire ownership of copyrights, communal heritage, languages, or cultural identity except where expressly agreed in writing.

---

## 2. AI Governance Principles

2.1. AIWA applies the following principles to all AI governance decisions:

- **Consent-first:** No work may be processed by an AI system without documented consent from the rights holder.
- **Provenance integrity:** Every AI-processable work must carry verified provenance records before processing is authorized.
- **Non-extraction:** AIWA does not aggregate or deliver cultural materials to AI systems for the benefit of those systems at the expense of rights holders or communities.
- **Cultural protection:** Cultural heritage materials and TCEs are subject to heightened AI restrictions under AIWA-POL-03.
- **Accountability:** Every AI processing authorization is documented and auditable.
- **Reversibility:** AIWA must have mechanisms to withdraw AI processing authorizations and require dataset deletion where rights are revoked.

2.2. These principles apply to all AI-related activities within the AIWA system, including internal operations, sublicensing, and partner arrangements.

---

## 3. Dataset Intake Standards

3.1. A dataset enters the AIWA system only through the intake process governed by AIWA-DOC-03.

3.2. Before a dataset is accepted, AIWA must verify:

- the submitting party's authority to submit;
- the rights status of all works included in the dataset;
- the consent status for AI processing for each work included; and
- the provenance of the dataset's component works.

3.3. Mixed datasets — datasets containing works with different consent statuses — must be segregated. Works without AI processing consent must be removed from AI-eligible dataset pools.

3.4. No dataset may be processed for AI use before classification under AIWA-DOC-01.

3.5. AIWA must maintain a dataset registry recording each dataset's composition, rights status, consent status, and processing history.

---

## 4. Provenance Tracking

4.1. Provenance tracking is mandatory for all AI-processable materials in the AIWA system.

4.2. Provenance records must include:

- the original creator and creation date;
- the submission chain from creator to AIWA;
- all prior uses, assignments, or licenses of the work;
- cultural origin and community affiliation where applicable;
- classification status under AIWA-DOC-01;
- consent documentation for AI processing; and
- any restrictions or conditions attached to the work.

4.3. Provenance records must be maintained for the life of the work's presence in the AIWA system and for a minimum of seven years after termination of administration.

4.4. Incomplete provenance is grounds for restricting a work from AI processing.

4.5. AIWA must not deliver a work to an AI processing partner without complete provenance documentation.

---

## 5. Consent Verification

5.1. Consent for AI processing must be:

- express and documented in writing;
- given by the rights holder or an authorized representative;
- specific to the type of AI processing authorized; and
- separate from general submission consent.

5.2. Consent for AI processing is not implied by:

- submission of the work to AIWA;
- consent to DSP distribution;
- consent to educational use; or
- any other consent not expressly covering AI processing.

5.3. Consent may be withdrawn at any time by the rights holder.

5.4. Upon withdrawal of consent, AIWA must:

- remove the work from all AI-eligible dataset pools;
- notify active AI processing partners of the withdrawal;
- prohibit the work from inclusion in any future AI training runs or dataset releases from the date of withdrawal;
- require deletion of the work from datasets and active AI processing pipelines where technically feasible; and
- document the withdrawal and the actions taken.

5.5. Where deletion from a trained AI model or integrated model weights is not technically feasible, AIWA must:

- document the technical limitation in writing;
- require the AI processing partner to confirm in writing that the work will not be used in future processing, training, or dataset inclusion;
- apply commercially reasonable efforts to limit ongoing exposure to the work; and
- record all steps taken in the consent withdrawal register.

5.6. AIWA must not warrant to rights holders that selective model retraining or weight-level removal is achievable. AIWA's deletion obligation applies to datasets and active processing pipelines. Model-level removal is subject to commercially reasonable technical limitations, and AIWA must document those limitations when invoked.

5.7. AIWA must maintain a consent register for all AI-processable works.

---

## 6. Rights Verification

6.1. AIWA must verify that the party granting AI processing consent is the legitimate rights holder before accepting consent.

6.2. Rights verification for AI-processable works must include:

- confirmation of authorship or ownership;
- confirmation that no conflicting rights claims exist;
- confirmation of the chain of title for the work; and
- confirmation that any co-owners have also provided consent where required.

6.3. Split ownership works require all co-owners to provide consent for AI processing unless the co-ownership agreement expressly grants a single party authority to consent.

6.4. Rights verification for AI-processable works is governed by AIWA-POL-05.

---

## 7. AI Processing Permissions

7.1. AI processing permissions in the AIWA system are categorized as follows:

| Permission Level | Permitted Uses |
|---|---|
| Full AI Processing | Linguistic analysis, educational indexing, language resource development, dataset inclusion |
| Limited AI Processing | Educational archiving only; no commercial dataset inclusion |
| No AI Processing | No AI use of any kind permitted |

7.2. The applicable permission level is determined by:

- the classification decision under AIWA-DOC-01;
- the rights holder's consent; and
- any cultural restrictions under AIWA-POL-03.

7.3. The default permission level is No AI Processing unless Full or Limited AI Processing has been expressly authorized.

7.4. Cultural heritage materials and TCEs are subject to the AI restrictions in AIWA-POL-03, which may not be overridden by a commercial agreement.

---

## 8. Restricted AI Uses

8.1. The following AI uses are prohibited for all works in the AIWA system without exception:

- creation of synthetic voice replicas of identifiable individuals without express written consent;
- creation of deepfake audiovisual content;
- impersonation of living or recently deceased creators;
- deceptive synthetic reconstruction of cultural heritage or TCEs;
- use in systems designed to circumvent copyright detection;
- use in systems producing content to compete commercially with the original work without authorization; and
- use for surveillance, profiling, or tracking of creators or communities.

8.2. The following AI uses are restricted and require elevated authorization from the Governance Board:

- commercial AI training datasets derived from heritage or community-linked materials;
- cross-border delivery of cultural datasets to jurisdictions with inadequate data protections; and
- AI use of works under active legal holds or disputed ownership.

8.3. Restricted and prohibited uses may not be authorized by a sublicensee, platform partner, or AI processing partner without AIWA's written authorization.

---

## 9. AI Output Rules

9.1. AI systems operating under an AIWA license must:

- maintain attribution traceability to the source works used in their training or processing;
- not produce outputs that are designed to substitute for the source works commercially;
- not obscure the cultural origin of works incorporated into their training; and
- comply with AIWA's anti-reconstruction standards under Section 15.

9.2. AIWA must include AI output rules in all AI processing licensing agreements.

9.3. AI output rules are enforceable against sublicensees.

---

## 10. Synthetic Voice and Likeness Restrictions

10.1. Synthetic voice replication of any rights holder in the AIWA system requires:

- express written consent from the rights holder;
- documentation of the intended use scope;
- a time-limited authorization; and
- the right of the rights holder to revoke consent at any time.

10.2. Synthetic voice or likeness of a deceased rights holder requires:

- consent of the estate or authorized beneficiary;
- cultural review if the individual was a community cultural figure; and
- Governance Board approval.

10.3. Synthetic voice or likeness may not be used to:

- misrepresent the rights holder's statements, beliefs, or identity;
- produce content the rights holder would reasonably object to;
- commercially exploit the rights holder's identity without compensation; or
- impersonate a community or cultural authority.

---

## 11. Cultural Dataset Safeguards

11.1. Cultural datasets — datasets consisting of or substantially incorporating cultural heritage or community-linked materials — require:

- Cultural Review Unit clearance before any AI processing;
- documented community consultation where practicable;
- restricted delivery to AI partners with demonstrated cultural governance standards; and
- prohibition of commercial AI training use unless specifically authorized.

11.2. AIWA must not deliver cultural datasets to any AI partner operating under a framework that does not include cultural governance protections equivalent to those in this policy.

11.3. Cultural dataset safeguards may not be waived by a commercial licensing agreement.

---

## 12. Dataset Retention and Deletion

12.1. AIWA must specify retention and deletion terms in all AI processing licensing agreements.

12.2. Retention periods must be proportionate to the processing purpose and must not extend beyond what is necessary for that purpose.

12.3. AIWA must require AI processing partners to:

- delete datasets upon termination of the licensing agreement;
- provide written confirmation of deletion;
- retain deletion records for a minimum of three years; and
- submit to audit of deletion compliance where requested.

12.4. AIWA must maintain a deletion register recording all deletion events, including partner confirmations.

---

## 13. International AI Licensing

13.1. AI processing licensing for international partners is governed by AIWA-POL-12.

13.2. International AI licensing must comply with:

- applicable Gambian law;
- AIWA-POL-10 (Compliance & International Licensing); and
- the data protection and privacy standards in AIWA-POL-09.

13.3. AI processing licenses must not be granted to entities in restricted jurisdictions under AIWA-POL-10.

---

## 14. Model Auditability

14.1. AIWA must require AI processing partners to maintain model auditability for models trained on AIWA-administered works.

14.2. Auditability requirements include:

- documentation of training datasets used;
- version control for models trained on AIWA materials;
- the ability to identify which AIWA-administered works contributed to a model; and
- the ability to remove contributions where required by law or by AIWA's rights governance decisions.

14.3. AIWA may conduct or commission an audit of an AI partner's use of AIWA-administered materials at any time during an active licensing agreement.

14.4. AI partners must cooperate with AIWA audit requests within thirty days.

---

## 15. Anti-Reconstruction Standards

15.1. AI systems operating under AIWA licenses must not use AIWA-administered materials to reconstruct or replicate:

- the full content of a work in a form that substitutes for the original;
- protected cultural expressions in a form that replicates their cultural integrity without authorization;
- individual creative identities or creative styles at a level that causes market substitution; or
- restricted or folklore-designated materials in any form.

15.2. Anti-reconstruction obligations are included in all AI processing licensing agreements.

15.3. Violation of anti-reconstruction standards is grounds for immediate termination of the AI processing license and referral to the Governance Board.

15.4. Anti-reconstruction standards apply to sublicensees. AIWA must pass these obligations through all sublicensing chains.

---

## 16. Governance and Compliance

16.1. This policy operates within the legal hierarchy established in AIWA-DOC-02.

16.2. AI governance decisions are subject to oversight by the Governance Board.

16.3. All AI processing authorizations must be documented.

16.4. No AI processing authorization may be issued verbally.

16.5. AI governance decisions follow the decision states established in AIWA-GOV-02.

---

**End of AIWA-POL-04**

---

*AI West Africa is a Busumbla Born, Gambian Grown Company.*

*Copyright (c) 2026 AI West Africa. All rights reserved.*
