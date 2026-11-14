# TechE ServOS 1.2.0

**A compact network installer for a standalone Debian 13 server.** Choose the boot disks, review the exact erase targets, and install a minimal SSH-ready server on a VM or x86-64 machine.

For homelab operators and infrastructure administrators who want to start with a small server and choose its boot storage up front, one text installer covers single drives and eligible RAID layouts. The installed base is ready for SSH administration and later provisioning.

This public download is available with exact-ISO production qualification open.

[Download ISO ZIP](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.2.0/TechE-ServOS-13.7-v1.2-amd64-network.iso.zip) · [SHA-256 checksums](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.2.0/ServOS-v1.2-SHA256SUMS.txt) · [Release manifest](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.2.0/ServOS-v1.2-RELEASE-MANIFEST.json)

The ZIP is **63.9 MiB** and contains one 75.4 MiB ISO. ZIP SHA-256 `c604bd95a1316c935c01d2bc38297398d5c5eaeba2f8a93eacee09f51ee51da6`.

## What you can configure

- Choose ext4 or XFS for a single drive, or select eligible mdadm, Btrfs or ZFS layouts. [See the ZFS layout dropdown](screenshots/README.md#zfs-layout-dropdown).
- Review grouped drives and inspect model, serial and stable ID before confirming erasure. [See the drive picker](screenshots/README.md#64-drive-inventory-and-scrolling).
- Clear downloaded package indexes and expire temporary files using the Optimize storage option. [See the audited finish option](screenshots/README.md#standalone-storage-cleanup-option-in-the-source-audit).

## Minimum hardware and measured footprint

Allow **2 GiB assigned RAM and at least 2 GiB per target SSD** for a fresh install. An earlier ext4 replica booted and accepted SSH with 512 MiB assigned RAM and a 500 MiB virtual SSD. After cleanup it used 80 MiB RAM and 367 MiB SSD space. These measurements come from the earlier VM trials. [See the four measured layouts](Resource-qualification.md).

[Review all six claims and their evidence](CLAIMS.md)

## Install and verify

Start with an x86-64 machine or VM, a wired IPv4 connection to the Debian mirrors and a verified backup. Disable Secure Boot for UEFI installation. Use an isolated installation network because live SSH opens the shared installer without a password. Installed SSH uses the credentials you configure.

[Install, verify and rebuild](INSTALL.md) · [QA and known limits](QA.md) · [Gallery](screenshots/README.md) · [v1.1 archive and rollback](../1.1.0/README.md)

[Private source commit](https://github.com/TechEWorks/servos/commit/6b2f19e546ca407ef1c315a46549ba64fffe1dd6) · [Debian package sources](https://www.debian.org/distrib/packages) · [OpenZFS source](https://github.com/openzfs/zfs) · [ServOS security contact](https://github.com/TechEWorks/servos/blob/main/SECURITY.md)
