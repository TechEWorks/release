# TechE Works ServOS 1.0.0 | 06 Production review

**State: public 06 Production review prerelease; gates open.** [Download the four verified release assets](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.0.0-06-production-review.1). Release ID `444202627`, tag `servosv1.0-v1.0.0-06-production-review.1`. The [original public 1.0.0 release](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.0.0) remains live.

ServOS is a text installer for an administrator preparing a minimal Debian 13.7 server. It puts disk identity, storage and network choices, the typed erase decision, and installation progress in one console workflow. [See the 17-screen capability gallery](../1.0.0/production-evaluation-20261113/gallery/README.md). The [original exact-ISO QA report](../1.0.0/QA.md) records tested VM paths and their limits; other-build images illustrate capabilities without transferring a QA pass.

## Download and verify

| Asset | Role | Bytes | SHA-256 |
|---|---|---:|---|
| `TechE-ServOS-13.7-v1.0-amd64-network.iso` | **Deployable ISO** | 71,696,384 | `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf` |
| `TechE-ServOS-13.7-v1.0-amd64-network.one-file.zip` | One-file ZIP containing that exact ISO | 71,696,562 | `8e99031d820ec1c225e429f7c939dad8f5d89246f0419b388251e5b450d4f6d7` |
| `TechE-ServOS-13.7-v1.0-SOURCE.zip` | Original 1.0.0 source ZIP | 115,286 | `f63ce9c9dde59ff4e8f5b9260a589f32bfaec224de72f66ee0900001cd526013` |
| `TechE-ServOS-1.0.0-06-production-review-pack-20261113.zip` | 57-file 06 review packet | 207,608,872 | `3b69180f76f7045bd3cb5594fbc2cccebde08dc495fad6bdb5fa3306e7171516` |

The [exact asset index](Asset%20index.tsv) supplies GitHub asset IDs. The review packet contains the ISO, its transport, original release assets, 17 curated screenshots, human and AI install/build instructions, source and scope records, issues, and its own manifest/checksums. Its GitHub upload was downloaded again and matched the complete ZIP SHA-256. The ISO was also downloaded directly from the original public release and independently matched its byte count and SHA-256.

For immediate public use of the unchanged ISO, use its [original public download](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-amd64-network.iso), verify the hash above, then follow the [numbered install guide](../1.0.0/INSTALL.md) and [human and AI verification path](../1.0.0/production-evaluation-20261113/INSTALL-HUMAN-AI.md). Whole selected disks are erased only after review and typed `ERASE`; use a disposable VM for a safe first trial.

## Scope and release control

The [feature boundary](../1.0.0/production-evaluation-20261113/SCOPE-MATRIX.md), [known issues](../1.0.0/production-evaluation-20261113/KNOWN-ISSUES-AND-LIMITS.md), [human and AI build instructions](../1.0.0/production-evaluation-20261113/BUILD-HUMAN-AI.md), and [rights packet](../1.0.0/production-evaluation-20261113/RIGHTS-DECISION-PACKET.md) show the current evidence and limits. The requester approved a [documented S4 exception](https://github.com/TechEWorks/servosv1.0/blob/main/06-production/release-engineering/decisions/EXC-001%20existing%20ISO%20build%20route.md) to keep this exact already published ISO instead of making a new clean ISO build. That exception does not pass the other gates.

**Still open:** digest-bound Business receiving and rights decisions, remaining exact-ISO QA evidence and issue disposition, independent delivery review, and final page review. All four public assets were anonymously downloaded and independently hash-verified. No new ISO build, new QA pass, or 06 Production gate approval is claimed here.
