**A minimal Debian server on the storage layout you choose.** TechE ServOS installs Debian 13.7 on a selected DriveOS disk or disk set, then boots with networking, OpenSSH, sudo and APT. The installed server runs independently of Proxmox.

## S4 release identity and exact evidence

**Public deployable output:** [TechE-ServOS-13.7-v1.0-amd64-network.iso](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-amd64-network.iso), 71,696,384 bytes, SHA-256 `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`. This is a separate build from the private beta.1 ISO (`1866bd0fbc19be6461ef73227e605c93bb1d7e7edaa05e96ff78e99c5463c342`); **no Beta test result is transferred**. The public release source commit is `359909def220ac8b152d4015cecd28f959770ddf`, with tree `f805c77e945ec6ad0331edda074f3dd08b4b3c9e`.

The [S4 stage 04 catalog](https://github.com/TechEWorks/release/blob/24ea465b992bac76ee11b57c5f953436b377de0c/servosv1.0/04-base-release/README.md) maps this output to its [manifest](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/RELEASE-MANIFEST.json), [source and build guide](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/BUILD.md), [install guide](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/INSTALL.md), [feature contract](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/FEATURES.md), [exact-public-ISO QA and open checks](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md), and [rights notices](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/LEGAL.md). Those public tests were run on the public hash above. A future production-qualified candidate must rerun every required case on its own bytes and resolve its own open hardware, recovery, SBOM/notice and signature gates. This historical 1.0.0 release predates S4; no backdated frozen S4 packet is claimed. The release manifest's QA sentence reflects publication time; the later [QA report](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md) records additional tests on the same ISO hash. The downloadable checksum asset uses CRLF line endings; the repository text copy uses LF with identical entries.


## Why ServOS exists

An administrator may need the OS to boot from ZFS, multi-disk Btrfs or an mdadm array with ext4 or XFS. Debian Installer supports mdadm and an optional SSH network console, but it does not present all these boot layouts together in one compact, guided storage workflow. ServOS lets you inspect disks, choose an eligible layout, review the exact erase target and watch the installation in one text interface.

The ISO starts on a local or remote-management **console**. After first boot, use SSH to configure the next role from a reachable network. NetBird or another VPN client can be installed later for private remote access; the ISO bundles no VPN account, key or service. This makes ServOS a small foundation for WorkDesk, infrastructure roles or a custom server.

## Start here

- [Download the network installer ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-amd64-network.iso)
- [Install and first boot](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/INSTALL.md)
- [Features and remote SSH setup](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/FEATURES.md)
- [Build the ISO from public source](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/BUILD.md)
- [QA results and open checks](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md)
- [License and upstream notices](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/LEGAL.md)
- [ServOS product page and installer screenshots](https://github.com/TechEWorks/release/tree/main/servosv1.0)

## Release files

- **[Installer ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-amd64-network.iso)** — deployable, 71,696,384 bytes. SHA-256: `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`.
- **[Source ZIP](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-SOURCE.zip)** — buildable source, tests, guide and dated license, 115,286 bytes. SHA-256: `f63ce9c9dde59ff4e8f5b9260a589f32bfaec224de72f66ee0900001cd526013`.
- **[Pinned base ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/BUILD-INPUT-Pinned-Base-ISO.iso)** — required for an independent rebuild, 63,307,776 bytes. **Do not deploy this input ISO.**

The release also includes [SHA256SUMS.txt](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/SHA256SUMS.txt) and [RELEASE-MANIFEST.json](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/RELEASE-MANIFEST.json). Verify downloaded assets before use. No release signature is claimed.

## Tested scope

On 5 November 2026, the **exact published ISO** completed live installations on disposable UEFI VM225: single-disk ext4, XFS and ZFS, two-disk ZFS mirror, two-disk mdadm RAID1/XFS, and two-disk Btrfs RAID1. Each two-disk layout cold-booted from both EFI members with both members present. The Btrfs run also checked static IPv4, SSH public-key access and separate `/tmp`, `/var` and `/home` subvolumes; one degraded Btrfs boot and manual recovery path was tested. SSH, sudo and APT update passed on the tested paths. The [QA record](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/QA.md) states exact evidence and the storage, network, recovery and hardware paths still open. A reachable Debian package mirror is required during installation.

## Rebuild and support

An [independent public rebuild](https://github.com/TechEWorks/release/actions/runs/41983978934) verified the release ZIP and pinned base ISO, ran the screen checks, and produced a byte-identical ISO. Follow the [build guide](https://github.com/TechEWorks/release/blob/main/servosv1.0/1.0.0/BUILD.md), including its source-ZIP line-ending step. The optional WorkDesk catalog awaits a published, pinned WorkDesk asset.

Contact [sysadmin@teche.works](mailto:sysadmin@teche.works) · [TechEWorks on GitHub](https://github.com/TechEWorks)