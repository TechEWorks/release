# TechE ServOS (13.7) v1.0

**A minimal Debian foundation for remotely provisioning the next system.**

Built on **Debian GNU/Linux 13.7**, ServOS turns a blank physical server or VM
into a bootable, networked base with OpenSSH, sudo and APT. From there, an
administrator can connect over SSH and install the role that machine actually
needs: a Docker Engine host, WorkDesk, a hypervisor base, or a GPU and LLM
workload. ServOS installs none of those larger roles by default.

The network installer is about **68.4 MiB**. It is designed for administrators
bringing provider hardware, rack servers and VMs online from a consistent
starting point, while downloading the packages needed for the selected
storage layout.

**DriveOS** is the name of the boot disk or disk set; **TechE ServOS** is the
system installed on it.

[Download the installer ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-amd64-network.iso) ·
[See how installation works](1.0.0/INSTALL.md) ·
[Build it from public source](1.0.0/BUILD.md)

## One small base, many possible systems

| Build next | Start with ServOS, then add |
| --- | --- |
| Container host | Docker Engine and the services that host will run |
| WorkDesk system | The WorkDesk desktop and application layer |
| Hypervisor base | The chosen virtualization stack and its management layer |
| GPU or LLM node | Hardware drivers, model runtime and workloads suited to that GPU |
| Custom server | Only the packages, network access and services that role requires |

The same minimal base can be installed on a single disk or on a supported ZFS,
Btrfs or mdadm layout. The installer enumerates **up to 64 drives** and offers
storage choices compatible with the selected count. ext4 and XFS are available
on one disk or as filesystems over supported mdadm arrays; ZFS and Btrfs have
their own eligible single- and multi-disk layouts. USB is limited to a
single-disk target. Inspect identities, capacity and existing partitions
before the typed erase confirmation.

Once booted, the machine is reachable by SSH on a connected network. Use the
administrator shell, APT or a later role installer to provision the next
system remotely. Interactive SSH displays the same system summary as the
console and offers a text setup menu; ordinary noninteractive SSH commands
remain available for automation.

## Why this exists

Remote provisioning needs a predictable first layer: a bootable OS on the
intended storage, working IPv4, an administrator account and SSH. Preparing that
layer by hand on different servers consumes time before the actual application
installation can even begin. ServOS prepares it in one guided text workflow
with disk inspection, layout selection, erase review and live progress.
Debian Installer already supports mdadm and an optional SSH network console;
ServOS brings the broader ZFS, multi-disk Btrfs and mdadm choices together as
the foundation for the next installation.

This matters when a machine is in a rack, at a provider or inside a VM:
prepare it through its console, then use SSH for the next setup steps. Install
NetBird or another VPN client afterward if the server needs private remote
reachability. The initial ISO setup still needs a local or remote-management
console; it does not bundle a VPN account, key or client.

## From blank machine to remote provisioning

1. **Connect.** Use DHCP by default or enter static IPv4, gateway and DNS.
   The network installer checks the package mirror.
2. **Inspect and choose.** Review disk size, model, serial, stable ID and
   existing partitions. The selected disk count determines which layouts
   appear, with estimated capacity and failure tolerance.
3. **Confirm and install.** Type `ERASE` to confirm the selected whole disks.
   Follow numbered tasks and a live installation log.
4. **Boot and extend.** Boot TechE ServOS from DriveOS. Sign in on the console
   or through SSH and install only the packages needed for this machine.

## The SSH handoff

The published ISO's first-boot console displays the installed Debian base,
kernel, network address, SSH command, boot storage, capacity and hardware.
An interactive SSH login uses the same system display, then offers the
administrator a remote setup menu or an ordinary shell.

![Published ServOS ISO first-boot system display](1.0.0/screenshots/04-published-iso-first-boot-console.png)

The interactive SSH choice follows the system display:

```text
Press Enter to open setup, type shell for a shell, or exit to disconnect:

Remote setup

  1  Open administrator shell
  2  Set up WorkDesk
  3  Show system and network details
  4  Disconnect
```

The WorkDesk action requires a separately published, pinned WorkDesk package.
For other roles, open the shell or use noninteractive SSH commands to run
your own provisioning scripts.

## See the decisions before erasure

The disk view shows identity and existing partitions before selection. Mounted
or active disks are blocked. An unmounted disk with an existing OS is marked
and needs an extra selection step before the final erase confirmation.

![Disk identity and existing partitions in the ServOS installer](1.0.0/screenshots/01-disk-inspection.png)

Available layouts follow the number of selected disks. This six-disk example
shows ZFS choices with estimated usable capacity and failure tolerance.

![Eligible six-disk ZFS layouts in the ServOS installer](1.0.0/screenshots/03-zfs-layout-choices.png)

These captures are from preceding installer candidates. The
[published ISO QA record](1.0.0/QA.md) identifies exact-release tests and open
checks; [all three captures](1.0.0/README.md#installer-captures) are in the
version record.

## Download, verify or build

The **1.0.0** release includes a 71,696,384-byte network installer ISO, its
source ZIP, pinned base ISO, manifest and SHA-256 checksums. The exact release
ISO has live VM installation and cold-boot evidence for single-disk ext4, XFS
and ZFS; ZFS mirror; mdadm RAID1 with XFS; and Btrfs RAID1. The QA record
states the limits of those tests and the storage, recovery and hardware paths
still open.

| Start with | Link |
| --- | --- |
| Installer ISO, source and checksums | [ServOS 1.0.0 release](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.0.0) |
| Installation and first boot | [Install guide](1.0.0/INSTALL.md) |
| Full storage, network and access path | [Feature guide](1.0.0/FEATURES.md) |
| Public-source rebuild | [Build guide](1.0.0/BUILD.md) |
| Exact tests and open checks | [QA record](1.0.0/QA.md) |
| License and upstream notices | [Legal notices](1.0.0/LEGAL.md) |

**Requirements:** x86-64 UEFI, Secure Boot off, wired IPv4 and Internet access
to a Debian package mirror. Verify the release checksum before deployment.
The [version record](1.0.0/README.md) and [release index](index.json) identify
the artifacts. Contact [sysadmin@teche.works](mailto:sysadmin@teche.works).
