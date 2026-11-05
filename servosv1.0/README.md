# TechE ServOS (13.7) v1.0

**Put a minimal Debian server on the storage layout you actually need.**
TechE ServOS is a compact network installer for a bootable **DriveOS** disk
or disk set. It installs Debian 13.7 with networking, OpenSSH, sudo and APT;
applications and TechE roles are added later. The installed server runs on
physical hardware or a VM without a Proxmox dependency.

## Why ServOS exists

An administrator may need a server to boot from ZFS, multi-disk Btrfs, or an
mdadm array with ext4 or XFS. Debian Installer provides mdadm and single-disk
Btrfs, but it does not offer all of these boot layouts together in one guided
choice. Assembling the remaining paths by hand, then preparing a consistent
SSH-ready base, takes extra work across machines. ServOS brings disk inspection,
compatible layouts, capacity estimates, an explicit erase review and visible
installation progress into one text workflow.

The ISO starts on a server or remote-management **console**. Once ServOS has
booted, an administrator can provision the next role through SSH on a reachable
network. NetBird or another VPN client can be installed afterward when private
remote access is needed; no VPN account, key or service is bundled into the ISO.
The result is a small foundation for later WorkDesk, infrastructure or custom
server deployments.

[TechE.Works on GitHub](https://github.com/TechEWorks) publishes the release; contact
[sysadmin@teche.works](mailto:sysadmin@teche.works).

## Start here

| What you need | Where to go |
| --- | --- |
| Download the installer ISO | [ServOS v1.0 release](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.0.0) |
| See every storage, network and SSH setup feature | [Full feature path](1.0.0/FEATURES.md) |
| Install on a server or VM | [Install guide](1.0.0/INSTALL.md) |
| Download the code and build your own ISO | [Source and build guide](1.0.0/BUILD.md) |
| Check exact test coverage and limitations | [QA record](1.0.0/QA.md) |
| Read licenses and ownership | [ServOS legal notices](1.0.0/LEGAL.md) |

The installer is text based and works on a local or remote-management console.
It supports DHCP or static IPv4, password or SSH public-key access,
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
3. Follow numbered installation tasks and the live log, then boot TechE ServOS
   from DriveOS.
4. Log in by console or SSH. Interactive SSH offers a setup menu, shell and
   later TechE role installation. Noninteractive SSH commands remain usable
   for automation. The WorkDesk download URL is still pending publication.

## Installer preview

Inspect the model, serial, stable ID and existing partitions before selecting
any disk for erasure.

![Disk identity and existing partitions](1.0.0/screenshots/01-disk-inspection.png)

The available storage layouts follow the number of selected disks. The
installer shows estimated capacity and failure tolerance before final review.

![Eligible six-disk ZFS layouts](1.0.0/screenshots/03-zfs-layout-choices.png)

These real VM captures came from preceding installer candidates. See the
[published ISO QA record](1.0.0/QA.md) for exact release tests and open checks,
or [all three installer captures](1.0.0/README.md#installer-captures).

Debian's own [installer documentation](https://d-i.debian.org/manual/en.amd64/ch06s03.html)
describes optional SSH network-console installation, and its
[Btrfs documentation](https://wiki.debian.org/Btrfs) describes the single-disk
installer path. ServOS does not claim Debian lacks mdadm or remote installation;
its value is a single, storage-focused setup and an SSH-ready server afterward.
