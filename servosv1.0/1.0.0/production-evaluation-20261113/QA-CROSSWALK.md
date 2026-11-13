# Exact ISO QA crosswalk

**Published ISO:** `TechE-ServOS-13.7-v1.0-amd64-network.iso`, 71,696,384 bytes, SHA-256 `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`. Source: [original public QA report](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md). These are recorded results on the exact published ISO, not tests newly performed by this content revision.

| Case | Reported observed result | Precise source |
|---|---|---|
| Ext4, DHCP, password | Single 8 GiB disk; typed `ERASE`; six install tasks; ISO detached; cold boot; SSH, sudo, APT and `teche -v`. | [QA lines 26–41](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L26-L41) |
| XFS single disk | Existing partitions reviewed; XFS root/ext4 boot; disk-only cold boot; SSH and APT. | [QA lines 42–53](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L42-L53) |
| ZFS single disk | ZFS root/boot, `lz4` and separate datasets; healthy pool; disk-only cold boot; SSH and APT. | [QA lines 54–68](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L54-L68) |
| ZFS mirror | Two selected 8 GiB disks; healthy boot/root pools; cold boot from both EFI members **with both disks present**. | [QA lines 69–82](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L69-L82) |
| mdadm RAID1/XFS | Two selected disks; root/boot arrays `[2/2] [UU]`; cold boot from both EFI members **with both disks present**. | [QA lines 83–94](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L83-L94) |
| Btrfs RAID1, static/key | Two disks, RAID1 data/metadata, separate subvolumes, one static IPv4 and Ed25519-key setup; both EFI sources with healthy members. | [QA lines 95–113](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L95-L113) |
| Btrfs degraded/repair | One original member detached, booted on remaining member, restored same member, scrubbed and manually re-added stale mdadm `/boot` member. New-disk replacement and automatic recovery were not tested. | [QA lines 114–138](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L114-L138) |

The [capture manifest](gallery/capture-manifest.tsv) binds each image to its recorded build identity. The public ISO's own report separately records the exact public-ISO tests above; no other build's results are transferred to it.

The [original post-release acceptance section](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#post-release-acceptance-work) names unverified layouts, network and key environments, hardware, interrupted installation, failure paths, other degraded recovery, SBOM/notices and signature. These remain visible in [Known issues and limits](KNOWN-ISSUES-AND-LIMITS.md).
