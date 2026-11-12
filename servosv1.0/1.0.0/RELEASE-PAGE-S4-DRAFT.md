# TechE ServOS 1.0.0 — public network installer

**A text-guided installer for a minimal Debian 13.7 server.** It is intended for an administrator evaluating disk layout, network setup and a first boot with SSH, sudo and APT. The buyer, commercial value proposition and supported production scope have **not** been approved by the Business owner. This is the historical public 1.0.0 release; it predates the S4 release packet and is not a new production qualification.

**[Download the deployable ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-amd64-network.iso)** · 71,696,384 bytes · SHA-256 `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf` · [checksums](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/SHA256SUMS.txt) · [manifest](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/RELEASE-MANIFEST.json)

**Start:** [prerequisites and install](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/INSTALL.md) · [feature and SSH guide](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/FEATURES.md) · [full QA and limits](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md) · [source and rebuild](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/BUILD.md)

## What the exact public ISO demonstrated

These are **tested paths on this ISO hash**, not blanket claims for every supported-looking menu choice:

| Observed outcome | Direct QA evidence |
| --- | --- |
| A selected single disk installed and cold-booted Debian with SSH, sudo and APT on ext4, XFS and ZFS paths. | [ext4](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md#L26), [XFS](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md#L42), [ZFS](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md#L54) |
| Two-disk ZFS mirror and mdadm RAID1/XFS installed and cold-booted from either EFI member while both storage members were present. | [ZFS mirror](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md#L69), [mdadm RAID1](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md#L83) |
| One Btrfs RAID1 path installed with static IPv4, SSH key access and separate subvolumes; it booted from either EFI member with both present. | [Btrfs, network and SSH test](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md#L95) |
| The same Btrfs test guest booted with a member missing and was repaired manually after the member returned. | [Degraded boot and repair record](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md#L114) |

The [feature contract](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/FEATURES.md) describes the installer; the [QA report](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md) determines which paths were actually tested. The [new S4 Business scope](https://github.com/TechEWorks/servosv1.0/blob/business/s4-beta-handoff-20261111/Business/07%20Roadmap%20phases%20and%20feature%20scope.md) maps 80 source-derived feature IDs but has no approved customer claims or receiving decision.

## Download, deploy and check

Use an x86-64 UEFI machine or VM with Secure Boot off, a wired network reaching a Debian mirror, and an expendable target disk. Follow the [install and first-boot procedure](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/INSTALL.md); the installer erases only the disk IDs you confirm. The ISO is a **network installer**: it does not include target Debian packages, WorkDesk, NetBird, VPN credentials or a finished desktop.

After downloading, compare the file size and SHA-256 above or use the [checksum asset](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/SHA256SUMS.txt). On Linux, a direct check of the deployable ISO is:

```sh
printf '%s  %s\n' 'b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf' 'TechE-ServOS-13.7-v1.0-amd64-network.iso' | sha256sum -c -
```

After installation, detach the ISO, cold-boot the target and check the console, SSH access and APT as described in the guide. Use a disposable VM for evaluation.

## Source, build and review

[Download the public source ZIP](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-SOURCE.zip) (115,286 bytes; SHA-256 `f63ce9c9dde59ff4e8f5b9260a589f32bfaec224de72f66ee0900001cd526013`) and the [pinned base ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/BUILD-INPUT-Pinned-Base-ISO.iso) (63,307,776 bytes; SHA-256 `7a473b485c3a81406098e2806a6a489b88eb10e44da188db86b92e7a37dfa55a`). **The pinned base is build-only; do not deploy it as ServOS.** The [human build procedure](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/BUILD.md) gives exact commands; an AI operator must use those same pins and checks, stop on any mismatch and record its own build identity. An [independent public-source rebuild](https://github.com/TechEWorks/release/actions/runs/41983978934) produced the published ISO hash. The published source commit is `359909def220ac8b152d4015cecd28f959770ddf`.

**Limits still open:** representative RAIDZ and other storage layouts, broader static/key environments and hardware, interrupted install and additional degraded-member recovery, complete installed/ISO SBOM and upstream notice audit, release signature, and a published pinned WorkDesk package. See the [exact-ISO QA report](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md#L144), [legal information](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/LEGAL.md) and [Business receiving record](https://github.com/TechEWorks/servosv1.0/blob/business/s4-beta-handoff-20261111/Business/Annex%20E%20Commercial%20QA%20and%20handoff.md). The private beta.1 and next S4 candidate have different hashes and cannot inherit this release's test results. No release signature or production-wide approval is claimed.

Support or security reports: [sysadmin@teche.works](mailto:sysadmin@teche.works). Include the ISO hash, storage layout and installer log without credentials or customer data.
