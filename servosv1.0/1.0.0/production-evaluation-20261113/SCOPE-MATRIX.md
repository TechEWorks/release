# ServOS 1.0.0 — declared feature scope and observed boundary

This matrix maps the original source's numbered [feature register](source-feature-register.txt) to the [published ISO's exact-hash case record](QA-CROSSWALK.md). An offered menu choice is **not** an installed-system pass. These F IDs are source-side engineering identifiers; the public release does not contain an approved Business feature/claim decision for each ID. No Business approval is inferred here.

| Source group | Declared capability in 1.0.0 | Exact public-ISO observation and boundary |
|---|---|---|
| F01 Boot/platform | x86-64 UEFI network installer; Secure Boot off. | Published ISO booted in disposable UEFI VM225. Broader firmware/NIC/storage hardware remains open. |
| F02 Network | DHCP or static IPv4, gateway, DNS and mirror check. | DHCP observed on multiple installs; one static IPv4 path with Btrfs/SSH key. Other static, failure and mirror-outage paths remain open. |
| F03 Disk safety | Stable IDs, existing partitions, occupied-disk warning and typed `ERASE`. | Named tested paths reviewed selected disk IDs and existing partitions before typed confirmation. Other negative/change-race cases remain open. |
| F04 Single disk | ext4, XFS, Btrfs and ZFS menu paths. | Single-disk ext4, XFS and ZFS installed and cold-booted. Single-disk Btrfs remains unverified on published bytes. |
| F05 Multi-disk ZFS | Mirror, stripe, RAIDZ and mirror-pair choices subject to disk count. | Two-disk mirror installed; both EFI sources cold-booted with healthy members. RAIDZ, stripe, mirror pairs and degraded-member recovery remain unverified. |
| F06 mdadm root | RAID families with ext4 or XFS root. | Two-disk mdadm RAID1/XFS installed; both EFI sources booted with healthy members. mdadm ext4, other RAID levels and degraded recovery remain unverified. |
| F07 Multi-disk Btrfs | RAID1 and other eligible data/metadata profiles. | Two-disk RAID1 installed and both EFI sources booted with healthy members; one missing-member boot and manual same-member recovery recorded. Other profiles and new-disk replacement remain unverified. |
| F08 Directories | Default directories or eligible separate datasets/subvolumes. | ZFS datasets and Btrfs subvolumes observed. Separate physical directory partitions remain open. |
| F09 Identity/SSH | Non-root sudo admin, password or public-key access; root SSH disabled. | Password and one SSH-key path recorded; broader key/network environments remain open. |
| F10 Install/boot handoff | Numbered tasks, logs, EFI/GRUB and completion actions. | Six tasks completed on tested routes with log and disk-only cold boot. Interrupted-install recovery remains open; one ZFS progress label was inaccurate. |
| F11 Post-boot server | Console/interactive SSH summary, storage/network/capacity and APT. | Console, SSH, sudo, APT and selected storage states recorded on tested routes. Wider hardware detail coverage is not established. |
| F12 TechE utility | Version/help and optional package catalog behavior. | Installed `teche -v` reported 1.0.0 on tested routes. Historical source includes optional unconfigured WorkDesk catalog/menu code; no WorkDesk package is bundled or claimed installed. |
| F13 Policy/logs | ServOS-specific paths and persistent install/operations records. | Installed log existence and selected permissions recorded in test cases. Full policy and event matrix is not established by the public report. |
| F14 Text UI | Consistent text screens, keyboard behavior and progress. | Source screen checks and published-ISO install path are recorded. The ZFS task label defect remains open. |
| F15 Release/rebuild | Pinned source/input, ISO and checksum checks. | Source/build checks and a byte-identical public rebuild recorded. Full upstream SBOM/notice audit and release signature remain open. |
| F16 Extension contract | Future role packages may extend the base. | No role package is part of the ISO. This is a boundary, not an installed capability claim. |

## Requested scripts-only handoff

The requested `TechE.ScriptsV1.0` root folder, installed `/teche.scripts/v1.0/` path, script-loading command, account-wide PATH setup and login/SSH script address are **not evidenced** in the exact published [source ZIP](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-SOURCE.zip) or the [ISO/initrd file inventory](ISO-COMPONENT-INVENTORY.md). The source ZIP does contain an installer `bootstrap.sh` and the `teche` utility; the published QA record reports `teche -v` on a tested path. This source/inventory check does not replace an installed-system check. Do not treat the requested scripts handoff as a delivered feature of the unchanged 1.0.0 ISO without a separate exact-output observation and Business decision.

**Release decision boundary:** The matrix tells a reader what is declared, what was observed on the exact public ISO and what remains unverified. It does not promote a Beta result to the published ISO, expand tested hardware, or approve a future scripts-only release.
