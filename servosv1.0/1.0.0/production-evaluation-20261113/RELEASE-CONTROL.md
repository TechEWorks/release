# ServOS 1.0.0 — release identity and channel record

This record separates the **existing public ISO release** from this **local content packet**. They share the same deployable ISO bytes. The packet is not a second ISO build or a second GitHub release.

| Field | Recorded value | Evidence |
|---|---|---|
| Product and version | TechE ServOS 1.0.0 on Debian 13.7 | [original manifest](assets/RELEASE-MANIFEST.json) |
| Deployable route | x86-64 UEFI network installer; Secure Boot off; wired IPv4 and reachable Debian mirror | [install guide](original-repo/servosv1.0/1.0.0/INSTALL.md) |
| Original release ID and tag | GitHub release `434866684`, `servosv1.0-v1.0.0` | [public release](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.0.0) · [captured API record](publication-record/release-api.json) |
| Tag target | `14602a03b50009df5bfd83862ba946ed17e47665` | Captured API record and locally resolved tag |
| Product source identity | Private source commit `359909def220ac8b152d4015cecd28f959770ddf`; approved tree `f805c77e945ec6ad0331edda074f3dd08b4b3c9e`; public source ZIP SHA-256 `f63ce9c9dde59ff4e8f5b9260a589f32bfaec224de72f66ee0900001cd526013` | [original manifest](assets/RELEASE-MANIFEST.json) · [source ZIP](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-SOURCE.zip) |
| Later documentation snapshot | Public release repository snapshot `d89769b1695c4f4965404ee5317f54303ab6abf8`; it is later than the release tag target | [preserved repository files](original-repo/servosv1.0/1.0.0/README.md) |
| Existing GitHub flags | `draft=false`, `prerelease=false`, `immutable=false` in captured release API | [captured API record](publication-record/release-api.json) |
| Existing publication | `2026-11-05T06:49:58Z`; public by URL | [captured API record](publication-record/release-api.json) |
| ISO | `TechE-ServOS-13.7-v1.0-amd64-network.iso`, 71,696,384 bytes, SHA-256 `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf` | [asset index](ASSET-INDEX.md) |
| Original audience and maturity | Public, non-prerelease GitHub distribution | Captured API record |
| S4 Production delivery approval of this content packet | **NOT RECORDED** | [delivery route](DELIVERY-ROUTE.md) |
| New packet publication URL and UTC | **NOT YET PUBLISHED** | Local [packet verification](PACK-VERIFICATION.json) |

The user's report on 13 November 2026 says Group H passes. The corresponding independent review/readback receipt and exact packet identity have not been supplied in this local packet. This statement records the report; it does not invent a review record. Any new packet publication needs its own versioned URL and readback tied to its actual ZIP hash.

The public release is a historical 1.0.0 output that predates the adopted S4 Production packet. A future S4 decision may consume its unchanged ISO, but must state the release identity, applicable stage gate, Business scope and exact-byte evidence. The original tag, original files and original QA remain attributed to their own identities.
