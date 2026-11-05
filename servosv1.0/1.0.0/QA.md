# ServOS 1.0.0 verification and open checks

Release artifact: `TechE-ServOS-13.7-v1.0-amd64-network.iso`, 71,696,384
bytes, SHA-256
`b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`.
The private source commit is `359909def220ac8b152d4015cecd28f959770ddf`;
the approved tree and build tree are both
`f805c77e945ec6ad0331edda074f3dd08b4b3c9e`.

## Verified checks

- The pinned 63,307,776-byte build input matched its SHA-256. The Debian 13.7
  CI build completed, reported BIOS and UEFI El Torito entries, and uploaded
  the exact ISO and build manifest. A downloaded copy matched the manifest's
  ISO SHA-256 and byte count.
- The source QA and release build checks passed, including screen framing,
  screen walkthrough, activity copy and the product/DriveOS naming scan.
- A separate [public-source rebuild](https://github.com/TechEWorks/release/actions/runs/41983978934)
  downloaded the immutable release ZIP and base ISO without private source
  access, verified both against `SHA256SUMS.txt`, ran the three public screen
  checks, and rebuilt an ISO with SHA-256
  `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`—
  **byte-identical to the published ISO**. `xorriso` reported BIOS and UEFI
  El Torito entries. The first run exposed source-ZIP CRLF line endings; the
  public guide now normalizes text to LF after verifying the archive.
- **Published-ISO live smoke test, 2026.11.05:** the exact 71,696,384-byte
  release ISO (`b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`)
  booted on disposable UEFI PVE VM225. With DHCP on VirtIO `ens18`, the installer
  selected only the 8 GiB disk with stable ID
  `/dev/disk/by-id/scsi-0QEMU_QEMU_HARDDISK_drive-scsi0`, reviewed its existing
  partitions, and required typed `ERASE`. The single-disk ext4 installation
  completed all six displayed tasks and saved a 201,413-byte install log under
  `/techev1.0/servosv1.0/logs/install/install.log`. After shutdown, the ISO
  was detached and firmware boot order set to `scsi0`; the guest cold-booted
  to the ServOS console. The guest reported Debian 13.7, kernel
  `6.12.115+deb13.1-amd64`, ext4 root on the selected stable disk, active and
  enabled OpenSSH, and a working `servadmin` SSH login with sudo membership.
  `sudo apt update` reached the Debian main, updates and security repositories
  and exited successfully. The installed `teche -v` reported utility 1.0.0.
  This proves one ext4/DHCP/password path on the published bytes; it does not
  qualify other storage or network choices.
- **Published-ISO ZFS mirror test, 2026.11.05:** the same release ISO installed
  ZFS with `lz4` compression on two separate 8 GiB VM225 scratch disks, stable
  IDs ending `drive-scsi1` and `drive-scsi2`. The final review listed both IDs
  and their existing partitions before typed `ERASE`. All six install tasks
  completed, and the installed log was 400,952 bytes. After detaching the ISO,
  firmware boot order was set to `scsi1`, then in a separate cold boot to
  `scsi2`. Both boots reached the ServOS console and SSH. The guest mounted its
  root and `/boot` from ZFS datasets; `zpool status -P` showed both boot and
  root pools `ONLINE` with both selected members and no known data errors.
  SSH, sudo and `apt update` succeeded on the first boot; the second boot
  reported active SSH and `zpool status -x` said all pools were healthy. The
  earlier ext4 disk was not selected or erased. This proves boot from either
  EFI member while both mirror disks are present; degraded-member boot and
  repair remain untested.
- An earlier exact ISO from the same installer backend, SHA-256
  `7f0d27d40eac5dd1dd861ecf3afe610388a560d408702005cbe5045a2f4c4a5e`,
  passed on disposable PVE VM225: ext4 single-disk boot; ZFS two-disk mirror
  boot from each EFI member; mdadm RAID1 with XFS boot from each EFI member;
  and Btrfs RAID1 boot from each EFI member. Those runs also checked SSH,
  sudo, APT update, mount state and saved installation logs. The new ISO
  changes product wording, footer date and utility version/help. These
  earlier live results are evidence about the backend, **not exact-byte live
  QA of the published ISO**.

## Post-release acceptance work

The public source ZIP has Windows CRLF line endings. The
[public build guide](BUILD.md) includes a text-only LF normalization step
after archive verification and before shell execution. The ZIP, ISO and their
published checksums remain immutable; the corrected public rebuild passed.

The following paths are not claimed as passed for the published ISO:
single-disk XFS and ZFS; representative ZFS RAIDZ, mdadm ext4 and other Btrfs
layouts; static IPv4; SSH public-key access; separate physical directory
partitions; degraded-member boot and repair; interrupted-install recovery;
failed network/mirror handling; and broader non-VirtIO hardware. The optional
WorkDesk catalog requires a
published pinned HTTPS ZIP and its matching SHA-256. A complete installed and
ISO component SBOM, upstream notice audit and release signature are also
post-release controls. They must be closed before claiming a mission-critical
production qualification.

The live ZFS test exposed a progress-label defect: task 1/6 still read
"Check network" while the activity pane installed ZFS storage tools. The
installation continued and booted, but the label needs correction in a future
build so long package operations are accurately identified.

For an incident, preserve the ISO SHA-256, selected disk stable IDs, storage
layout, boot order and installer log. Send the details privately to
[sysadmin@teche.works](mailto:sysadmin@teche.works). Do not send passwords,
private keys or customer data in a public issue.
