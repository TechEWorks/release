# ServOS 1.0.0 — Business claim and receiving sheet

This is the explicit handoff for the **unchanged published ISO**, not a claim that every installer menu choice has passed Production acceptance. Each proposed reader-facing outcome below names its technical behavior and exact-ISO observation. Business receiving is recorded as **OPEN** until the accountable owner approves this exact scope and output digest.

| Claim ID | Business outcome and user | Technical behavior | Exact-ISO proof | Boundary |
|---|---|---|---|---|
| SVO-CL-01 | An administrator can inspect the target before installing a minimal Debian server. | Show stable disk ID, previous partitions and final review; require typed `ERASE`. | [Ext4 case](QA-CROSSWALK.md) · [original QA](original-repo/servosv1.0/1.0.0/QA.md) | Only named tested VM paths; whole selected disks are erased. |
| SVO-CL-02 | The administrator can choose a tested single-disk root format and reach SSH after disk-only boot. | Install ext4, XFS or ZFS on one selected disk, then cold boot with OpenSSH, sudo and APT. | [Exact-ISO cases](QA-CROSSWALK.md) | Single-disk Btrfs and wider hardware are not in this claim. |
| SVO-CL-03 | The administrator can use tested two-disk storage paths. | ZFS mirror, mdadm RAID1/XFS and Btrfs RAID1 installed; each healthy two-disk system cold-booted from either EFI member. | [Exact-ISO cases](QA-CROSSWALK.md) | Both disks were present for the two EFI-source checks; other RAID levels are not claimed. |
| SVO-CL-04 | The administrator can inspect one tested degraded Btrfs recovery case. | Boot with one original Btrfs member missing, restore that same member, scrub and manually re-add the stale `/boot` mdadm member. | [Btrfs recovery case](QA-CROSSWALK.md) | Not a general recovery promise or new-disk replacement procedure. |
| SVO-CL-05 | A human or AI operator can obtain, verify and use the same published output. | Check the original ISO SHA-256, follow numbered installation steps and observe first-boot health. | [Verification](VERIFICATION.md) · [human and AI install](INSTALL-HUMAN-AI.md) · [human and AI build](BUILD-HUMAN-AI.md) | AI installation observation record and independent user run remain to be reviewed. |

The [feature scope matrix](SCOPE-MATRIX.md) covers all sixteen source groups and marks offered but unverified choices. Those choices are **not** included in the five claims above. No WorkDesk package, VPN enrollment or general physical-hardware qualification is claimed. Images in the [capability gallery](gallery/index.html) illustrate the workflow; the exact public-ISO report above carries the release acceptance claims.

## Receiving decision fields

| Required field | State |
|---|---|
| Accountable Business owner and named approver | OPEN |
| Exact output accepted | ISO SHA-256 `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf` |
| Included claims | SVO-CL-01 through SVO-CL-05 proposed |
| Excluded/deferred choices | [Scope matrix](SCOPE-MATRIX.md) and [known issues](KNOWN-ISSUES-AND-LIMITS.md); approval OPEN |
| Receiving decision, rationale and UTC | OPEN |

An approval must identify this exact ISO digest and state which claims and exclusions are accepted. The receiving decision does not replace QA, legal rights review or publication readback.
