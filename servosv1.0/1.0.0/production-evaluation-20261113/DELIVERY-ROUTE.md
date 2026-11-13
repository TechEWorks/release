# ServOS 1.0.0 — current channel and proposed S4 delivery route

This record separates an **observed public release** from an **evaluated local packet**. A local score, copied ISO or page preview does not grant a Production gate.

| Dimension | Existing public 1.0.0 | Current content packet |
|---|---|---|
| Product and audience | ServOS 1.0.0; public administrators | Same intended audience; Business receiving OPEN |
| S4 build stage | Historical public release before this S4 packet; no retroactive 06 approval claimed | **06 Production evaluation proposed**; delivery gate NOT APPROVED |
| Candidate / output | GitHub release ID `434866684`, tag `servosv1.0-v1.0.0` | Local content ZIP; exact digest is in its external ZIP receipt |
| Deployable binary | Original ISO SHA-256 `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf` | Consumes the **same** original ISO bytes; no ISO rebuild |
| Visibility | Public GitHub release, five original assets | Local review only; no public URL, no Pages deployment, no Latest pointer |
| Public page and asset route | [Existing release](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.0.0) | New release ID, version, 128-bit page key and approved site base **UNSET** |
| Approval and readback | Historical publication flags and UTC recorded in [release control](RELEASE-CONTROL.md) | Business, rights, independent delivery decision and H.02–H.04 readback OPEN / NOT_RUN |

## Ordered delivery decisions

1. Preserve the existing release and all five original assets at their current URLs by default. Record an explicit retention/retirement decision if this changes; public history cannot be made secret by renaming a page.
2. Approve the new distribution version and immutable `release_id` for any **new shipped packet bytes**. Do not silently replace an existing 1.0.0 asset under its old name or claim the old tag targets the new packet. Record the exact source commit, unchanged ISO digest, packet digest and one-ISO transport digest in the new manifest.
3. Record stage `06 Production`, candidate/build-run ID, evaluation ID, proposed delivery-pull review ID and actual gate decision as separate records. Stages `04 Public Review` and `05 Pre-production` may be marked `N_A` only with their actual owner-approved reasons. The current content and asset scores are an evaluation, not a gate.
4. After approved Business scope, rights, exact-ISO QA and independent review, generate the S4 versioned page path and random page key; publish the complete approved asset set. Record public route, UTC, visibility, Latest/current pointer and responsible operator. A preview, if used, is labelled public exposure and has its own recorded route.
5. Independently retrieve every new URL and verify bytes, hashes, links, commands and image rendering. Record H.02–H.04 from that actual event. Keep the old release accessible unless a separately approved retirement copy-and-verify procedure is completed.

**Current state:** step 1 retention default applies; steps 2–5 are pending. No release ID, key, gate PASS or publication receipt is invented here. See [Release standards.txt](https://github.com/TechEWorks/standards/blob/d13a8f0b4e564e3453ddde3c9f9300d317bf7af9/Release%20standards.txt) §§05.05–05.11 and S4 §§04.11, 21.12.
