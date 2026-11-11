# ServOS S4 stage 04 — base release

**Catalog status: AVAILABLE.** The existing [public 1.0.0 release](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.0.0) was published 2026-11-05. This is a retrospective S4 catalog pointer; it is not a newly built ISO or a backdated S4 frozen packet.

| Deliverable or record | Location and exact identity |
| --- | --- |
| **Deployable network ISO** | [TechE-ServOS-13.7-v1.0-amd64-network.iso](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-amd64-network.iso), 71,696,384 bytes, SHA-256 `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf` |
| Buildable source | [SOURCE.zip](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-SOURCE.zip), 115,286 bytes, SHA-256 `f63ce9c9dde59ff4e8f5b9260a589f32bfaec224de72f66ee0900001cd526013` |
| Build-only input | [Pinned base ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/BUILD-INPUT-Pinned-Base-ISO.iso), 63,307,776 bytes, SHA-256 `7a473b485c3a81406098e2806a6a489b88eb10e44da188db86b92e7a37dfa55a`; do not deploy |
| Integrity/provenance | [SHA256SUMS](../1.0.0/SHA256SUMS.txt), [release manifest](../1.0.0/RELEASE-MANIFEST.json), source commit `359909def220ac8b152d4015cecd28f959770ddf` |
| Human build/install | [Build guide](../1.0.0/BUILD.md), [install guide](../1.0.0/INSTALL.md) |
| Feature and QA | [Features](../1.0.0/FEATURES.md), [exact public ISO QA and open checks](../1.0.0/QA.md) |
| Rights | [Legal notices](../1.0.0/LEGAL.md) |

The public ISO's exact-ISO QA includes VM225 installs, cold boots, SSH/APT and selected storage/recovery paths; [QA.md](../1.0.0/QA.md) names each result and remaining hardware, recovery, SBOM/notice and signature gaps. The private beta.1 hash is different; its results are never inherited. A future production-qualified candidate starts NOT_RUN for every required case and must retest its exact bytes.

## Retrieve and verify the deployable ISO

On a Debian/Linux machine, download the exact public release assets and check the published checksum and original byte count before deployment:

```sh
base='https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0'
curl -fL -o TechE-ServOS-13.7-v1.0-amd64-network.iso "$base/TechE-ServOS-13.7-v1.0-amd64-network.iso"
curl -fL -o SHA256SUMS.txt "$base/SHA256SUMS.txt"
sha256sum -c SHA256SUMS.txt --ignore-missing
test "$(stat -c %s TechE-ServOS-13.7-v1.0-amd64-network.iso)" -eq 71696384
```

Use the [install guide](../1.0.0/INSTALL.md) and [exact-ISO QA scope](../1.0.0/QA.md). The base ISO is a build input only. The existing 1.0.0 release used direct assets before S4; `LEGACY_PREVIEW` in [index.json](index.json) describes that transport history, not the stable release maturity. No one-file transport ZIP, signing proof or S4 frozen packet is claimed for 2026.11.05. New releases must meet the current S4 transfer and trust rules.
