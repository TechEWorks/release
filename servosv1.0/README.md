# TechE ServOS (13.7) v1.0

**A small, network-installed Debian server foundation.** ServOS prepares a
bootable DriveOS disk or disk set, configures networking and an administrator,
and leaves a working SSH, sudo and APT system. Applications and TechE roles can
be added later. [TechE.Works](https://teche.works) publishes the release;
contact [sysadmin@teche.works](mailto:sysadmin@teche.works).

**One installer, the storage you choose.** Inspect every disk and its existing
partitions, choose a supported single-disk or software-array layout, review
the exact erase target, then start a network installation. The result is a
standalone server that can be administered locally or over SSH.

## Start here

| What you need | Where to go |
| --- | --- |
| Download the installer ISO | [ServOS v1.0 release](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.0.0) |
| See every storage, network and SSH setup feature | [Full feature path](1.0.0/FEATURES.md) |
| Install on a server or VM | [Install guide](1.0.0/INSTALL.md) |
| Download the code and build your own ISO | [Source and build guide](1.0.0/BUILD.md) |
| Check exact test coverage and limitations | [QA record](1.0.0/QA.md) |
| Read licenses and ownership | [ServOS legal notices](1.0.0/LEGAL.md) |

The installer is text based and works on a local console or serial-style
terminal. It supports DHCP or static IPv4, password or SSH public-key access,
and single-disk or selected software storage layouts. It shows whole-disk
identity, existing partitions and an explicit erase confirmation before any
selected disk is changed. **DriveOS** is the storage name; **TechE ServOS** is
the product installed on it.

The current public version is **1.0.0**. Its exact artifacts, source identity,
checksums, scope and QA status are recorded in [the version record](1.0.0/README.md)
and [index](index.json). A published checksum, not a moving `latest` URL,
identifies a release.

## From boot to remote setup

1. Boot the compact ISO and connect with DHCP or static IPv4.
2. Inspect disk identities, partitions and eligible ext4, XFS, ZFS, mdadm or
   Btrfs layouts; confirm the target with typed `ERASE`.
3. Follow numbered installation tasks and the live log, then boot DriveOS.
4. Log in by console or SSH. Interactive SSH offers a setup menu, shell and
   later TechE role installation. Noninteractive SSH commands remain usable
   for automation. The WorkDesk download URL is still pending publication.

These real VM QA captures show the text interface. They come from preceding
installer candidates; see [exact release QA](1.0.0/QA.md) for tested scope.

| Inspect before erasing | Choose eligible layouts |
| --- | --- |
| ![Existing OS, partitions and disk ID](1.0.0/screenshots/01-disk-inspection.png) | ![Six-disk ZFS layout choices](1.0.0/screenshots/03-zfs-layout-choices.png) |

[See all three captures](1.0.0/README.md#installer-captures).
