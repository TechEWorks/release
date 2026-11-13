# ServOS 1.0 feature and setup path

ServOS is a small Debian 13.7 server foundation. It installs the OS on the
selected **DriveOS** disk or disk set, then exposes the resulting server by
console and SSH. The storage, network, access and boot path below is the
product scope; [QA](QA.md) states which combinations have been live-tested.

## From ISO to an SSH-ready server

1. **Boot and verify:** boot the x86-64 UEFI network ISO after checking its
   SHA-256. The installer detects wired NICs and whole disks. Secure Boot is
   off for this release.
2. **Connect:** choose DHCP, which is the default, or enter static IPv4,
   prefix, gateway and DNS. The installer checks the package mirror before
   proceeding.
3. **Inspect disks:** view media type, capacity, vendor, model, serial when
   reported by hardware, stable ID, controller address and existing
   partitions. Disks mounted or in use by the running installer are blocked.
   An existing OS on an unmounted disk is flagged, but remains selectable
   after a second Space press and the final typed `ERASE` review. Up to 64
   disks can be enumerated; only selected whole disks are erased.
4. **Choose DriveOS:** one disk offers ext4, XFS, Btrfs or ZFS. Valid
   multi-disk ZFS, mdadm or Btrfs layouts appear as the disk count permits.
   The interface gives usable-capacity and failure-tolerance estimates.
   ZFS compression and Btrfs options appear only where applicable. mdadm
   installs an ext4 or XFS root filesystem over the array.
5. **Choose directories and access:** use default `/tmp`, `/var`, `/home`,
   or configure eligible separate directories. Set a server name and non-root
   sudo administrator with either a password or an SSH public key. The
   installer never asks for an SSH private key.
6. **Review and install:** inspect the complete network, disk, layout and
   access summary, then type `ERASE`. Numbered installation tasks and ongoing
   logs show disk preparation, minimal base, network and SSH, kernel and boot,
   verification and cleanup. The target receives the persistent install log.
7. **Boot and administer:** remove the ISO or move DriveOS first in firmware
   boot order, then restart or shut down. Console and interactive SSH show
   the same system summary: Debian base and kernel, CPU, IP and SSH command,
   memory, DriveOS usage, boot/storage inventory, GPU when present, and APT
   commands.

## DriveOS choices by selected drive count

The installer can enumerate and select up to 64 whole drives. It recalculates
the eligible storage menu when the selection changes; RAID1 is one of several
choices. This is menu availability, while [QA](QA.md) records which choices
have cold-booted on the published ISO.

| Selected drives | Storage choices offered |
| --- | --- |
| 1 | ext4, XFS, Btrfs or ZFS |
| 2–64, ZFS | Mirror or stripe; RAIDZ1 at 3+, RAIDZ2 at 4+, RAIDZ3 at 5+, mirror pairs at even counts of 4+ |
| 2–64, mdadm | RAID0, RAID1 or RAID10; RAID5 at 3+, RAID6 at 4+; ext4 or XFS root filesystem |
| 2–64, Btrfs | Single, RAID0 or RAID1; RAID1C3 at 3+, RAID10 and RAID1C4 at 4+ |

Mixed drive capacities are selectable with a warning. USB is a single-drive
target only. The interface shows estimated usable capacity and failure
tolerance for the selected layout; the administrator makes the final choice.
See [practical examples](../README.md#choose-the-driveos-layout).

## Remote setup over SSH

After ServOS has booted and joined the network, an administrator can SSH into
it with the access method chosen during installation. An **interactive SSH
login** presents the shared system display and a text setup menu:

1. Open the administrator shell.
2. Set up WorkDesk through `sudo teche install wd1.0` once its pinned public
   download URL and SHA-256 are configured.
3. Show system and network details.
4. Disconnect.

The menu also accepts `shell` immediately. Noninteractive SSH commands run
normally, so automation is not trapped in a menu. The console keeps its normal
login behavior. SSH setup is **post-boot role configuration**; the ServOS ISO
itself is initially run on the server or VM console. The WorkDesk download URL
is not published yet, so that menu choice currently explains the missing
catalog configuration rather than installing WorkDesk.

## Operator paths and logs

`/usr/bin/teche` is the CLI entry point; scripts live in `/usr/lib/teche/`,
and the package catalog is `/etc/teche/packages.d/`. TechE-specific policy,
features, state and append-only operational records live below
`/techev1.0/servosv1.0/`. Native Debian logs remain in their normal locations.
Root privileges are required for system-changing `teche` operations. Run
`teche -v`, `teche v` or `teche --help` for utility information.

The installed server does not need Proxmox. Docker, NetBird, WorkDesk and other
roles are optional subsequent installations. The network ISO is small because
the selected target packages are downloaded during setup.
