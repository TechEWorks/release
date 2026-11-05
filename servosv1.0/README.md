# TechE ServOS (13.7) v1.0

**A small, network-installed Debian server foundation.** ServOS prepares a
bootable DriveOS disk or disk set, configures networking and an administrator,
and leaves a working SSH, sudo and APT system. Applications and TechE roles can
be added later. [TechE.Works](https://teche.works) publishes the release;
contact [sysadmin@teche.works](mailto:sysadmin@teche.works).

## Start here

| What you need | Where to go |
| --- | --- |
| Download the installer ISO | [ServOS v1.0 release](1.0.0/README.md#downloads-and-integrity) |
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
