# Install TechE ServOS 1.0.0

## Before booting the ISO

- Use an x86-64 UEFI server or VM with Secure Boot off, wired networking and
  access to a Debian package mirror. The installer needs about 700 MiB RAM;
  provide at least 2 GiB for ZFS. Each selected whole disk must be at least
  8 GiB. More capacity is advisable for applications and updates.
- Download the [installer ISO](README.md#downloads-and-integrity) and verify
  its SHA-256 before attaching or writing it to installation media.
- Back up every selected target disk. The final installation will erase the
  whole disk, including existing partitions. Keep the firmware console or VM
  console accessible until the installed system has booted and SSH works.
- Have an administrator username and password or an OpenSSH **public** key
  ready. Do not paste a private key into the installer.

## Installer sequence

1. Boot **Install TechE ServOS (13.7) v1.0**. Read the welcome and legal pages.
2. Choose the keyboard layout. The minimal server uses UTC; a later role or
   operator can set a local time zone.
3. Use DHCP, or enter static IPv4/prefix, gateway and DNS. Confirm the
   network check succeeds before installation.
4. Inspect the disk list. Current boot disks are separated and unavailable.
   For every target, compare model, serial, controller address, stable ID,
   size and existing partitions. Select the intended whole disk or disks.
5. Choose the storage family and layout that the selected disk count enables.
   A single disk can use ext4, XFS, Btrfs or ZFS. Multiple disks offer valid
   ZFS, mdadm or Btrfs layouts. Select compression and directory options when
   they apply. Larger disks in an array may have unused space.
6. Create a non-root administrator and choose password or public-key SSH
   access. Review the complete network, storage and account summary.
7. Type `ERASE` only after every selected disk is correct. Installation then
   displays numbered tasks and a live log. Keep power and Internet access
   stable while it runs.
8. On completion, remove the ISO or place the new **DriveOS disk** first in
   firmware boot order. Choose Restart or Shut down. Some virtual platforms
   require a shutdown before detaching installation media.

## First boot and operation

The console shows the ServOS system summary and login. Interactive SSH shows
the same summary and setup menu. SSH from a machine that can reach the server:

```sh
ssh YOUR_ADMIN@SERVER_IP
```

Use the password or the private half of the public key selected during setup.
The installed administrator can run:

```sh
sudo apt update && sudo apt upgrade
sudo apt update && sudo apt install PACKAGE
```

The saved installer log is under
`/techev1.0/servosv1.0/logs/install/install.log`. Native Debian logs remain
in their usual locations. If installation fails before a bootable target is
complete, preserve the live log, inspect the failing command and boot the
previous untouched disk if available. Automated interrupted-install recovery
is listed as a post-release QA case; do not rely on it without a backup.

ServOS does not configure Proxmox or alter a host's firmware boot order for
you. Later software can be installed through APT or a TechE role installer.
The optional `teche get wd1.0` catalog requires a separately published and
pinned WorkDesk asset; it is not part of this ISO.
