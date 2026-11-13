# ServOS S4 release-content rubric preflight

This is a gap map, **not a score or approval**. Source: `TechEWorks/standards` Release content scoring rubric.txt, revision 2026-11-13. Baseline: the exact public 1.0.0 files inventoried in [baseline-inventory.tsv](baseline-inventory.tsv). Each row states the shortest evidence-backed route to a 9+ review of a **new** scripts-only Production release. A reviewer must score C/E/P/U/L on the actual proposed packet; H.02–H.04 are postpublication checks.

| Rubric subgroup | What the historical release supplies | Work for the new 9+ review |
|---|---|---|
| A.01 Identity/source | Public tag, release ID, source/tree and asset manifest. | Bind the new reviewed commit, tree, tag, release ID and every output to one new manifest. |
| A.02 Classification | Public non-prerelease and current repo catalog. | Record separate stage 06, maturity, distribution, approval, page placement, audience and actual GitHub flags. |
| A.03 Version context | Beta/public distinction is stated. | Exact compare target and no inherited QA; retain old public version by default. |
| A.04 Entry metadata | Release date/title and support email. | Unique new versioned title, page key, owner, target event/UTC and live route after publication. |
| B.01 Who/need | Administrator and minimal server job described. | Match the approved scripts-only Business promise and named buyer/job. |
| B.02 Outcomes/scope | Storage, SSH and source outcomes described. | Three to six included outcomes with Business IDs, exact new-output QA cases and full scope matrix. |
| B.03 Proof/claims | Old QA describes exact old ISO tests. | Link every new claim to exact new ISO case; do not generalize old timings/hardware. |
| B.04 Visual story | Four screenshots; three older illustrative, one exact old ISO. | Version/date/hash/case/caption for each; new exact-output progress/screens and honest historical labels. |
| B.05 Primary action | Direct old ISO and SHA links are prominent. | Direct new original ISO, bytes/hash, one-file ZIP where required, install and safe test adjacent. |
| B.06 Scope/editorial | Several limits are disclosed; product page still names WorkDesk roles. | One scripts-only first-screen path with relevant limitations and issue links, no mixed release identity. |
| C.01 Asset table | Five downloadable assets with sizes/hashes in API; page lists main three. | Complete table for every new asset: role, ID, native format, bytes, hash, URL, access and verification. |
| C.02 Native/transport | Old native ISO downloaded and hash checked. | Build/check new native ISO and required one-file ZIP; verify member and original hashes. |
| C.03 Trust/source/evidence | Source ZIP, manifest, checksums, QA and partial notices. | New complete manifest/checksums, source, QA, SBOM/notices and applicable signature decision. |
| C.04 Reader retrieval | Old assets were independently downloaded for this audit. | Test actual new public URLs and anonymous retrieval; no draft or preview URL called a live release. |
| D.01 Prerequisites/impact | x86-64 UEFI, network mirror, Secure Boot off and disk erasure described. | Recheck new route and exact device/resource/privilege impact. |
| D.02 Install/first boot | Numbered install guide and exact old ISO QA. | New route's numbered download/hash/target/ERASE/log/cold-boot instructions and observed readback. |
| D.03 Safe quick test | Old guide includes basic checks. | Copyable read-only test, expected result, fixture, stop/evidence path on unexpected output. |
| D.04 Lifecycle | Some installation/recovery notes in QA. | Explicit upgrade, rollback, recovery, removal and withdrawal applicability/limits. |
| D.05 Human/AI parity | Human build guide exists. | Matching AI build and deploy instructions with exact observations, hashes and logs. |
| E.01 Business/output trace | General need/output table exists in product page. | Approved Business IDs → requirement → new exact output/case, excluded/deferred decisions and receiver. |
| E.02 Exact-release QA | Detailed old ISO VM225 results and limits. | New ISO's own approved positive/negative/failure/recovery case index and log hashes. |
| E.03 Screens/measurements | Old screenshot set and some timed VM tests. | Case-linked image hashes, new result/fixture/method; no speed claim from one VM. |
| E.04 Scope/issues | Old QA names untested layouts and a progress-label defect. | New support matrix aligned with new QA, stable issue IDs and dispositions. |
| E.05 Rights/decisions | AGPL notice and partial upstream disclosure. | New exact-byte SBOM/notice audit, technical review and Business receiving with digest/UTC. |
| F.01 Complete codebase | Buildable old source ZIP and public rebuild. | Complete reviewed scripts-only source, entry points, dependencies and output map. |
| F.02 Credits/provenance | Dated TechE license and old source identifiers. | File-level authorship/provenance/credit index and preserved upstream notices for new tree. |
| F.03 Build inputs | Pinned old base ISO; build guide lists packages. | Pin/check all new external inputs, toolchain and builder environment/rights. |
| F.04 Human/AI build | Human commands and old byte-identical public rebuild. | Same pinned new recipe for human and AI, ordered commands/logs/failure handling. |
| F.05 Build receipt | Old build/Action and hash record. | New run's actual source/input checks, logs, exit, sizes/hashes and independent reproduction status. |
| G.01 Changes | Old 1.0.0 release notes. | User-facing delta from 1.0.0 with feature/issue/case links; remove unrelated generated notes. |
| G.02 Known Issues and Bugs | QA prose includes a progress-label defect and open paths. | Named section and versioned issue register with stable IDs, severity, impact, workaround, owner, decision and UTC. |
| G.03 Compatibility/migration | Historical release is identified, no upgrade route. | Supported transition from 1.0.0, coexistence and old-release retention. |
| G.04 Help/security | Support mailbox named. | Diagnostic list, owner and verified private security-report route. |
| G.05 Withdrawal/correction | Not a complete reader path. | Document withdrawal, announcement, replacement identity and affected-user recovery. |
| H.01 Before-publication review | No new packet or review yet. | Independent comparison of exact proposed title/body/tag/assets/links/notices, result and UTC. |
| H.02 Independent retrieval | Old assets checked, no new release exists. | After publication, separately fetch every new declared file and check bytes/hashes/ZIP. |
| H.03 Rendered page/links | Old local relative links checked only. | After publication, inspect actual first screen, captions, links, current pointer and screenshot. |
| H.04 Final receipt | Old GitHub release exists, no S4 P06 receipt. | Freeze new URL, manifest digest, reviewer/UTC and append-only publication/readback result. |

**Hard stops:** The old release's open upstream inventory/SBOM, missing formal issue register and Business/independent decisions, absence of a new exact scripts-only ISO and its QA, and no frozen `06-production` release packet prevent a new 9+ Production delivery claim. A signature is only a gate if the adopted trust policy requires it; the old release explicitly claims none.
