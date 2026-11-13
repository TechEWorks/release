# ServOS 1.0.0 — exact-byte rights decision packet

**Decision target:** unchanged public ISO SHA-256 `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`, original source ZIP SHA-256 `f63ce9c9dde59ff4e8f5b9260a589f32bfaec224de72f66ee0900001cd526013`, and any new transport/outer packet identified by its own manifest. The original [LEGAL.md](original-repo/servosv1.0/1.0.0/LEGAL.md) declares AGPL-3.0-only for TechE-authored source and preserves upstream rights; it expressly says exact upstream ISO/component notice inventory remains under review.

| Component set | Exact available evidence | Remaining review |
|---|---|---|
| TechE source | [39-file source member index](audit/source-file-provenance.tsv), [22-file source-to-initrd reconciliation](audit/source-to-initrd-reconciliation.tsv), original source ZIP and dated licence text | File-level authorship/credits and independent source/mark decision |
| Debian-derived build input | 63,307,776-byte original pinned base ISO, SHA-256 `7a473b485c3a81406098e2806a6a489b88eb10e44da188db86b92e7a37dfa55a` | Supplier/base component inventory, licence texts and notices/source offers |
| Eighteen fetched build components | [Builder input URLs and SHA-256](audit/builder-input-provenance.tsv) transcribed from original `build-iso.sh` | Independent fetched byte counts, licence/notice/source reconciliation |
| Native ISO and installed Debian system | [Exact ISO and initrd inventory](ISO-COMPONENT-INVENTORY.md): 298 regular ISO files, 2,868 initrd entries and 112 initrd package status rows; [original QA](original-repo/servosv1.0/1.0.0/QA.md) | Installed-system package SBOM, upstream copyright/notice coverage, vulnerability and privilege scope |
| One-ISO transport and content packet | [Local packet verification](PACK-VERIFICATION.json) and manifest | Their final release IDs/hashes, inclusion in the rights decision and public readback |

**Origin assurance:** published SHA-256 establishes integrity against the recorded digest. No signature or attestation is claimed in the original release. The rights/security decision must state whether a separately controlled origin signature is required and, if so, provide its trust path and verification/failure/withdrawal instructions. Do not claim one exists because a checksum was published.

**Decision fields:** accountable rights owner; exact source/ISO/ZIP/packet digests; source and trademark terms; upstream licence/notice/source-offer completeness; SBOM and vulnerability review; security claims/exception list; approved distribution audience; decision (APPROVE, BLOCK or APPROVE_WITH_EXCEPTIONS); rationale; UTC; independent technical reviewer. All are **OPEN** until the exact evidence and signed decisions exist. The requester holds the rights decision role; this packet is prepared for one final review rather than asking them to compile component evidence.
