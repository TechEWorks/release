# ServOS v1.0 — rapid 19-gate candidate smoke

**Result after focused retests: 19/19 gates accounted for; 6 gate-level PASS, 11 PARTIAL, 1 FAIL, 1 NOT_APPLICABLE. This is not a production QA pass or a public release.** Each PARTIAL row names the narrow action actually exercised. No PASS from candidate `4513146` is carried into this result.

## Exact candidate and fixtures

| Field | Observed value |
| --- | --- |
| Source commit | `582e026be9f28fed90a9d4c2dccfc4ea164b05a8` |
| Source-transfer ZIP | 417,929 bytes; SHA-256 `d02a804580d1deefc7cac712f79691e13efd874130ebd2c64cd7ae6f061d3fbb` |
| Debian 13.7 base ISO | SHA-256 `7a473b485c3a81406098e2806a6a489b88eb10e44da188db86b92e7a37dfa55a` |
| Built ISO | `TechE-ServOS-13.7-v1.0-CANDIDATE-20261112-582e026.iso`; 71,696,384 bytes; SHA-256 `9269b7641117b963986a4c6f5e157a41486fc84c5283fe8cf4fc96180617c097` |
| One-file ISO ZIP | 71,696,588 bytes; SHA-256 `aa0690860b964ed11de4a09cee7105432deaf9ceff65723bf9dab725461882f7` |
| Build log | SHA-256 `b013cc484d9dca7a592ea086b1afa3a759a546cf846c57bfcc9574265b11b2f9` |
| VM275 | Disposable Debian 13.7 QEMU builder; source syntax, bootstrap equality, frame/screen/message tests and non-destructive simulation passed; simulation reported six injected task failures. |
| VM276 | Disposable x86-64 UEFI QEMU; 8 GiB virtual disk with prior candidate partitions; 4 GiB RAM, 2 vCPU, VLAN 30. Reinstalled from the exact ISO, shut down, detached ISO and cold booted its disk. |
| VM279 | Disposable x86-64 UEFI QEMU; three 8 GiB virtual disks. During this rapid menu phase, **ERASE was not entered**. A later [Btrfs RAID1 installed retest](03%20Btrfs%20RAID1%20installed%20retest.md) used the same VM and ISO after the menu evidence was recorded. |
| VM280 | Disposable x86-64 UEFI QEMU; one blank 8 GiB disk. The same ISO installed XFS, then cold booted with ISO detached; see the [XFS installed retest](04%20XFS%20single-disk%20installed%20retest.md). |

## Rapid gate results

| Gate | Rapid result | Exact observation and limit |
| --- | --- | --- |
| P01 | PASS | VM276 cold boot showed Debian 13.7, ext4 root, SSH address and shared welcome [console](screenshots/servos-s4-qa582276-20261112-21.png). `servadmin` logged in via SSH, belonged to `sudo`; `apt-get update -qq` exited 0. |
| P02 | PASS | Interactive SSH showed the [welcome and four-choice setup menu](SSH%20menu.txt); option 4 disconnected. Noninteractive SSH command returned host, user, version and path data without entering the menu. |
| D01 | PASS | Source-transfer SHA, pinned Debian input, built ISO SHA/size and single-member ZIP SHA were checked in build/transfer; both VMs booted the exact mounted ISO [welcome](screenshots/servos-s4-qa582276-20261112-02.png). Public re-download remains a separate release gate. |
| D02 | PASS | VM276 identified the existing OS, partitions, model, controller and stable by-id path before selection [disk warning](screenshots/servos-s4-qa582276-20261112-07.png); selection required a second Space [selected disk](screenshots/servos-s4-qa582276-20261112-08.png). Final review listed the same disk [review](screenshots/servos-s4-qa582276-20261112-15.png), then required typed `ERASE` [confirmation](screenshots/servos-s4-qa582276-20261112-16.png). |
| D03 | PASS | VM276 installed one-disk ext4 with all six tasks checked [verification](screenshots/servos-s4-qa582276-20261112-19.png), showed [completion](screenshots/servos-s4-qa582276-20261112-20.png), then cold booted the installed disk with the ISO detached [console](screenshots/servos-s4-qa582276-20261112-21.png). |
| D04 | PASS | VM280 installed single-disk XFS with all six tasks complete, detached the ISO and cold booted from disk. The [cold-boot console](screenshots/servos-s4-qa582280-20261112-16.png) and [SSH `findmnt` result](XFS%20root.txt) both reported `xfs /dev/sda3`; [retest and limits](04%20XFS%20single-disk%20installed%20retest.md). |
| D05 | PARTIAL | VM279 offered three-disk ZFS RAIDZ1 [menu](screenshots/servos-s4-qa582279-20261112-07.png). ZFS single, mirror and RAIDZ installation/cold boot were not run. |
| D06 | PARTIAL | VM279 offered three-disk mdadm RAID1 with ext4 [menu](screenshots/servos-s4-qa582279-20261112-09.png). mdadm installation and cold boot were not run. |
| D07 | PARTIAL | VM279 subsequently installed and cold booted three-disk Btrfs RAID1 with separate `/tmp`, `/var`, `/home` subvolumes; [installed retest](03%20Btrfs%20RAID1%20installed%20retest.md). Other Btrfs layouts and recovery remain untested. |
| D08 | PARTIAL | The exact source's non-destructive `simulate.py` exited 0 and reported six injected installation-task failures. No live interrupted-install, failed-boot or failed-member recovery was run. |
| D09 | **FAIL** | On VM276, `sudo /usr/bin/teche get scriptsv1.0` installed its `git` dependency, attempted a public clone, printed `Public scripts failed verification.`, and returned **65**. Full manifest verification, activation, update and rollback could not proceed. The public scripts publication/verification path requires repair and a fresh retest. |
| D10 | PARTIAL | VM276 used DHCP [installer network/storage transition](screenshots/servos-s4-qa582276-20261112-04.png), cold booted with IPv4, SSH and successful `apt-get update -qq`. Static IPv4 and network/mirror failure handling were not run. |
| D11 | PARTIAL | VM276 installed standard directories. VM279 installed and cold booted separate Btrfs `/tmp`, `/var`, `/home` subvolumes; [mount proof](Btrfs%20mounts.txt). Size rejection and other storage-family directory layouts remain untested. |
| D12 | PARTIAL | VM276 used `servos`/`servadmin`, password SSH and sudo. Effective `sshd -T` returned `permitrootlogin no`, `passwordauthentication yes`. Public-key path, explicit denied-root login and credential-log scan were not run. |
| D13 | PARTIAL | VM276 showed live [six-phase progress](screenshots/servos-s4-qa582276-20261112-18.png), all six complete, verification, EFI handoff and completion actions [result](screenshots/servos-s4-qa582276-20261112-19.png). Failed-install diagnostics were only exercised in the source simulation. |
| D14 | PARTIAL | Numbered text screens and keyboard selection worked in both QEMU fixtures; local pre-login [display](screenshots/servos-s4-qa582276-20261112-21.png) and [SSH welcome](SSH%20menu.txt) showed the scripts address. The full 80x24/large-terminal, focus/scroll and GPU-device matrix was not run. |
| D15 | PARTIAL | Installed `/teche.scripts/v1.0/` was root-owned mode 755 and traversable by an unprivileged account; `/usr/bin/teche ver` returned the pre-activation version. The previous dangling `catalog` symlink is absent and the [welcome](screenshots/servos-s4-qa582276-20261112-21.png) has no catalog line. Full timestamps, audit retention and path-permission matrix were not run. |
| D16 | NOT_APPLICABLE | Current Business scope is scripts-only ServOS with no role extension. Installed tree has `config`, `features`, `logs`, `policy` and no bundled role package. A role-extension example is excluded from this release; the acceptance matrix must be amended/approved before final QA closure. |
| H01 | PARTIAL | Exact ISO booted x86-64 UEFI QEMU with virtio network and SCSI disks, including a one-disk installed fixture and three-disk menu fixture. Physical device classes, controllers and GPUs were not tested. |

## Release decision

This rapid smoke is **not a production release pass**. D09 is a reproduced functional failure; the [public fetch diagnosis and retest path](02%20D09%20public%20fetch%20diagnosis.md) records why the published path is absent. The [Btrfs RAID1](03%20Btrfs%20RAID1%20installed%20retest.md) and [XFS](04%20XFS%20single-disk%20installed%20retest.md) installed retests add exact-ISO proof but do not complete the full storage matrix. Recovery, static network, device, rights, independent-review and Business receiving gates remain open. Any fix that changes ISO bytes needs a new exact candidate and fresh affected QA; the results above cannot be transferred to it.
