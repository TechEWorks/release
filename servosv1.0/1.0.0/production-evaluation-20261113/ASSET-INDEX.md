# ServOS 1.0.0 — exact public release files

The five rows below are the **unchanged assets of the latest published ServOS ISO release**, tag [`servosv1.0-v1.0.0`](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.0.0). The local copies were independently downloaded and checked against GitHub sizes and SHA-256 values on 13 November 2026. The [asset verification record](audit/asset-audit.json) contains GitHub asset IDs and the full digest check. No asset is called signed; SHA-256 alone is an integrity check.

| Role | Original file / direct download | Bytes | SHA-256 |
|---|---|---:|---|
| **Deployable network installer** | [TechE-ServOS-13.7-v1.0-amd64-network.iso](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-amd64-network.iso) | 71,696,384 | `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf` |
| **Complete buildable source** | [TechE-ServOS-13.7-v1.0-SOURCE.zip](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-SOURCE.zip) | 115,286 | `f63ce9c9dde59ff4e8f5b9260a589f32bfaec224de72f66ee0900001cd526013` |
| **Build-only input; do not install** | [BUILD-INPUT-Pinned-Base-ISO.iso](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/BUILD-INPUT-Pinned-Base-ISO.iso) | 63,307,776 | `7a473b485c3a81406098e2806a6a489b88eb10e44da188db86b92e7a37dfa55a` |
| Release metadata | [RELEASE-MANIFEST.json](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/RELEASE-MANIFEST.json) | 1,588 | `d5f6b0577449092f6b6e01479edd8df7f433c31daaefcc90eef22924e518d058` |
| Original checksum list | [SHA256SUMS.txt](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/SHA256SUMS.txt) | 397 | `f454454c22d9389abe1433e6532ac2eb74f3e7b21de9ba21fc19325055ff65d8` |

The original checksum list has four entries for the ISO, source ZIP, build-only base ISO and manifest. The checksum list itself is recorded by the GitHub asset hash above. The repository copy of the list uses LF (393 bytes); the downloadable asset uses CRLF (397 bytes) with the same four entries. Always identify which file is being checked.

**Local packet addition:** one-ISO transport ZIP, 71,696,582 bytes, SHA-256 `ffa059186659f92b8528a74e5c30fdc0c526c3cdd10b3237a240f13687548cba`. Its only member is the original ISO above; extraction and member SHA-256 were checked. The packet manifest and checksum list cover every included file. The outer release-content ZIP is recorded by the external `ZIP-RECEIPT.json`. These additions are local review files, not public downloads.
