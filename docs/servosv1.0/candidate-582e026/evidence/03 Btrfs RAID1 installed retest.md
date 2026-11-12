# Exact-ISO Btrfs RAID1 installed retest — VM279

**Path result: PASS for this one installed layout. D07 and D11 remain PARTIAL as full release gates.** This follow-up uses the same ISO as the [rapid 19-gate report](01%20Rapid%2019-gate%20smoke.md): `TechE-ServOS-13.7-v1.0-CANDIDATE-20261112-582e026.iso`, 71,696,384 bytes, SHA-256 `9269b7641117b963986a4c6f5e157a41486fc84c5283fe8cf4fc96180617c097`, source commit `582e026be9f28fed90a9d4c2dccfc4ea164b05a8`.

## Fixture and action

Disposable x86-64 UEFI QEMU VM279 (`teche-servos-s4-smoke-279`) had three 8 GiB `DriveDATA` SCSI disks, 4 GiB RAM, 2 vCPU and VLAN 30. The [full review](screenshots/servos-s4-qa582279-20261112-19.png) and its [last lines](screenshots/servos-s4-qa582279-20261112-21.png) identified all three stable by-id disk paths, Btrfs RAID1, zstd level 4, and separate `/tmp`, `/var`, `/home` Btrfs subvolumes. All disks were blank before this test. The installer required typed [ERASE for three disks](screenshots/servos-s4-qa582279-20261112-22.png). ERASE was entered only after review, on this disposable VM.

The [six-phase install](screenshots/servos-s4-qa582279-20261112-24.png) completed with all six tasks checked and verification complete at elapsed 4:22 [result](screenshots/servos-s4-qa582279-20261112-27.png). The [completion screen](screenshots/servos-s4-qa582279-20261112-28.png) reported Btrfs RAID1. The VM shut down; the ISO was detached (`ide2=none,media=cdrom`) and boot order changed to installed `scsi0`. The installed system [cold booted](screenshots/servos-s4-qa582279-20261112-29.png) to Debian 13.7 and SSH at its DHCP address.

## Installed evidence after cold boot

| Check | Observed result | Raw evidence |
| --- | --- | --- |
| Btrfs device set | One filesystem UUID with 3 devices: `/dev/sda3`, `/dev/sdb3`, `/dev/sdc3`, each 6.50 GiB; command exit 0 | [Btrfs devices](Btrfs%20devices.txt) |
| Redundancy profile | Data, System and Metadata all reported `RAID1`; command exit 0 | [Btrfs profile](Btrfs%20profile.txt) |
| Separate directories | `/tmp`, `/var`, `/home` mounted from `@tmp`, `@var`, `@home` Btrfs subvolumes after cold boot; command exit 0 | [Btrfs mounts](Btrfs%20mounts.txt) |
| Boot and pre-login display | Local banner reported Btrfs root and all three physical virtual drives, with `/teche.scripts/v1.0/` address | [Cold-boot console](screenshots/servos-s4-qa582279-20261112-29.png) |

The mount options include `degraded` because the installer intentionally configures multi-disk Btrfs root and separate subvolumes to permit a degraded boot (`backend.py` fstab and GRUB generation). The observed filesystem still listed **all three devices** and a RAID1 profile. This test did **not** remove a disk, prove failed-member recovery, scrub/repair, or qualify another Btrfs layout. It does not close D08 or the remaining D07 device/recovery matrix. Separate subvolume mount state is proven; D11 capacity rejection and other storage-family directory layouts remain untested.
