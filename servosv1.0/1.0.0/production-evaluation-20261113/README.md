# TechE ServOS 1.0.0 — release content draft

**Repository mirror:** [Read publication and asset status first](PUBLIC-STATUS.md). This directory omits large binaries included in the complete local packet; its S4 Production evaluation remains open.

**Content state:** prepared for the unchanged latest published ISO. This local content ZIP and one-file ISO transport have been packaged and verified. The GitHub release still serves its original five assets; links to this new local packet are not public until separately published and read back.

**For:** an administrator installing a minimal Debian 13.7 server on a selected disk or disk set. **Job:** inspect the target, choose supported storage and network settings, confirm the erase operation, and reach an SSH-ready system after boot. ServOS brings those decisions into one text installer. [Install instructions](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/INSTALL.md) · [exact public-ISO QA](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md).

**Identity:** This draft is bound to the public [ServOS 1.0.0 release](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.0.0), published 5 November 2026. Its ISO is **unchanged**: 71,696,384 bytes, SHA-256 `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`. It is not a new ISO build, a new GitHub release or a retroactive S4 Production approval.

## Get, check and install

1. **Download the deployable ISO:** [official GitHub asset](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-amd64-network.iso). This packet also contains the [one-ISO transport ZIP](assets/TechE-ServOS-13.7-v1.0-amd64-network.one-file.zip) (71,696,582 bytes; SHA-256 `ffa059186659f92b8528a74e5c30fdc0c526c3cdd10b3237a240f13687548cba`).
2. **Verify before use:** compare the ISO with the [original SHA256SUMS](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/SHA256SUMS.txt). The [packet verification procedure](VERIFICATION.md) checks its transport member against the original ISO. A checksum detects changes; the original release does not claim a cryptographic signature.
3. **Install:** x86-64 UEFI, Secure Boot off, wired IPv4, a reachable Debian mirror, at least 8 GiB per selected disk and a console are required. The selected whole disks are erased only after the review and typed `ERASE`. Follow the [numbered install guide](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/INSTALL.md), detach the ISO, cold boot from the installed disk, then run the [safe first-boot checks](VERIFICATION.md#safe-first-boot-checks).

## What the exact public ISO has shown

These are observed **VM225 UEFI paths on the published ISO hash above**, not a blanket hardware or layout qualification. [Case-by-case QA crosswalk](QA-CROSSWALK.md) links each claim to the public report.

| Delivered outcome | Exact public-ISO evidence |
|---|---|
| Inspect the selected disk and confirm whole-disk erasure; install single-disk ext4 and reach console/SSH. | [Ext4 live test](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L26) |
| Install single-disk XFS or ZFS and cold boot with SSH, sudo and APT. | [XFS case](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L42) · [ZFS case](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L54) |
| Install two-disk ZFS mirror or mdadm RAID1/XFS; cold boot from either EFI member while both members are present. | [ZFS mirror case](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L69) · [mdadm/XFS case](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L83) |
| Install two-disk Btrfs RAID1 using one static IPv4 and SSH-key path; cold boot from both EFI members, then test one missing-member boot and manual recovery. | [Btrfs install case](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L95) · [degraded recovery case](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L114) |

Explore the [wide capability gallery](gallery/index.html): 26 full-size screens covering disk inspection, ZFS and mdadm choices, typed erasure, installation progress, ext4, XFS and Btrfs completion, and first boot. The [capture manifest](gallery/capture-manifest.tsv) identifies each image once; the exact public-ISO report above supports the release claims.

## Source, limits and support

[All five release assets and hashes](ASSET-INDEX.md) · [channel and delivery route](DELIVERY-ROUTE.md) · [release identity](RELEASE-CONTROL.md) · [Business claim and receiving sheet](BUSINESS-RECEIVING.md) · [Feature and tested-scope matrix](SCOPE-MATRIX.md) · [exact-ISO case matrix](RELEASE-QA-MATRIX.tsv) · [original release source ZIP](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-SOURCE.zip) · [human and AI install path](INSTALL-HUMAN-AI.md) · [human and AI build path](BUILD-HUMAN-AI.md) · [exact ISO component inventory](ISO-COMPONENT-INVENTORY.md) · [rights decision packet](RIGHTS-DECISION-PACKET.md) · [lifecycle and recovery boundary](LIFECYCLE.md) · [known issues and unverified paths](KNOWN-ISSUES-AND-LIMITS.md) · [issue register](KNOWN-ISSUES-REGISTER.tsv) · [support and correction route](CHANGES-SUPPORT.md).

The ISO installs a minimal Debian base with OpenSSH, sudo and APT. It does not include a WorkDesk package. **Historical 1.0.0 source does include an optional, unconfigured WorkDesk menu/catalog path**; that is not part of the requested scripts-only scope for a future release. A new scripts-only ISO needs its own identity and QA.

Full upstream ISO/installed-system SBOM and notice inventory, a release signature, broad hardware testing and several recovery cases are not established for 1.0.0. See the [original QA limitations](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#post-release-acceptance-work) and [rubric status](RUBRIC-STATUS.md). For an incident, preserve the ISO hash, disk IDs, layout, boot order and installer log; contact [sysadmin@teche.works](mailto:sysadmin@teche.works). Do not post passwords, private keys or customer data in a public issue.
