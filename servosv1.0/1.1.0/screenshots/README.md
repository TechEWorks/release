# ServOS 1.1 installer gallery

These QEMU captures show the v1.1 release-candidate installation on Proxmox VM 102.
The BIOS and UEFI runs each used four 64 GiB virtual SSDs, a ZFS RAIDZ2 root pool and a mirrored boot pool.
The [QA record](../QA.md) identifies the captured build and the checks performed on the published ISO.

## ZFS RAID and disk selection

![Four 64 GiB virtual SSDs selected for ZFS RAIDZ2. The installer estimates about 125 GiB of root capacity and tolerance of up to two disk failures.](01-zfs-raidz2.png)

Four 64 GiB virtual SSDs selected for ZFS RAIDZ2. The installer estimates about 125 GiB of root capacity and tolerance of up to two disk failures. (UEFI)

![ZFS layouts available for the selected disk count, including mirror, stripe, RAIDZ1, RAIDZ2 and mirror pairs.](02-zfs-layouts.png)

ZFS layouts available for the selected disk count, including mirror, stripe, RAIDZ1, RAIDZ2 and mirror pairs. (UEFI)

![Storage family picker with ZFS, mdadm and Btrfs for this four-drive selection.](03-storage-families.png)

Storage family picker with ZFS, mdadm and Btrfs for this four-drive selection. (UEFI)

![Drive Info shows the QEMU disk model, stable ID and existing BIOS, boot and root partitions.](04-drive-info.png)

Drive Info shows the QEMU disk model, stable ID and existing BIOS, boot and root partitions. (BIOS)

![Separate /tmp, /var and /home can use datasets or subvolumes that share root pool capacity.](05-zfs-directory-layout.png)

Separate /tmp, /var and /home can use datasets or subvolumes that share root pool capacity. (UEFI)

![The BIOS install review shows the ZFS RAIDZ2 selection, estimated root size and disk-erasure warning.](06-zfs-install-review.png)

The BIOS install review shows the ZFS RAIDZ2 selection, estimated root size and disk-erasure warning. (BIOS)

## Boot and preparation

![The BIOS installer boot menu.](07-bios-boot-menu.png)

The BIOS installer boot menu. (BIOS)

![The UEFI installer boot menu.](08-uefi-boot-menu.png)

The UEFI installer boot menu. (UEFI)

![Seven preparation tasks, network status and elapsed time.](09-seven-preparation-tasks.png)

Seven preparation tasks, network status and elapsed time. (BIOS)

![Keyboard selection explains which layout applies to the local console and SSH.](10-keyboard-layout.png)

Keyboard selection explains which layout applies to the local console and SSH. (UEFI)

## Keyboard and remote access

![F1 opens keyboard help from the installer.](11-keyboard-help.png)

F1 opens keyboard help from the installer. (BIOS)

![F3 shows the version history and changes.](12-release-history.png)

F3 shows the version history and changes. (BIOS)

![The installer prefills the detected host name and lets the operator edit it.](13-hostname-default.png)

The installer prefills the detected host name and lets the operator edit it. (BIOS)

![The installed server can use an SSH public key or an administrator password.](14-ssh-access.png)

The installed server can use an SSH public key or an administrator password. (UEFI)

![The empty public-key entry screen.](15-ssh-public-key.png)

The empty public-key entry screen. (UEFI)

![The password and confirmation stage before any password was entered.](16-password-entry.png)

The password and confirmation stage before any password was entered. (UEFI)

## Confirmation, installation and boot

![Typed confirmation gates erasure of the selected virtual disks.](17-erase-confirmation.png)

Typed confirmation gates erasure of the selected virtual disks. (UEFI)

![Six installation tasks with the running activity log.](18-install-progress.png)

Six installation tasks with the running activity log. (BIOS)

![UEFI installation configuring the target bootloader.](19-uefi-bootloader-progress.png)

UEFI installation configuring the target bootloader. (UEFI)

![The BIOS RAIDZ2 install completed with restart and shutdown available.](20-bios-install-complete.png)

The BIOS RAIDZ2 install completed with restart and shutdown available. (BIOS)

![The UEFI RAIDZ2 install completed on the same four-drive layout.](21-uefi-install-complete.png)

The UEFI RAIDZ2 install completed on the same four-drive layout. (UEFI)

![The installed system's GRUB menu after the ISO was ejected.](22-installed-grub.png)

The installed system's GRUB menu after the ISO was ejected. (UEFI)
