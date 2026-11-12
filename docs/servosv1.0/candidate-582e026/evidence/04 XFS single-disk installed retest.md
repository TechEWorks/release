# Exact-ISO single-disk XFS installed retest — VM280

**Path result: PASS for this one installed layout. This is candidate smoke evidence, not full release qualification.** The tested artifact was `TechE-ServOS-13.7-v1.0-CANDIDATE-20261112-582e026.iso`, 71,696,384 bytes, SHA-256 `9269b7641117b963986a4c6f5e157a41486fc84c5283fe8cf4fc96180617c097`, from source commit `582e026be9f28fed90a9d4c2dccfc4ea164b05a8`. The [rapid 19-gate report](01%20Rapid%2019-gate%20smoke.md) remains the overall candidate status.

## Fixture and installation

Disposable x86-64 UEFI QEMU VM280 (`teche-servos-s4-xfs-280`) had one blank 8 GiB `DriveDATA` SCSI disk, 4 GiB RAM, 2 vCPU and VLAN 30. The [installer review](screenshots/servos-s4-qa582280-20261112-09.png) showed one selected disk, XFS single-disk root, standard directories, DHCP, SSH and the chosen administrator. The [typed ERASE gate](screenshots/servos-s4-qa582280-20261112-10.png) was entered only on this verified disposable disk; the [confirmation](screenshots/servos-s4-qa582280-20261112-11.png) preceded installation.

All [six installation tasks completed](screenshots/servos-s4-qa582280-20261112-14.png), including verification and cleanup, in 3:04. The [completion screen](screenshots/servos-s4-qa582280-20261112-15.png) reported `XFS / single`. The VM shut down; its ISO was detached (`ide2=none,media=cdrom`) and boot order changed to installed `scsi0` on the same 8 GiB disk. The [cold-boot console](screenshots/servos-s4-qa582280-20261112-16.png) reported Debian 13.7, root `xfs | /dev/sda3`, SSH at `10.64.2.49` and the login prompt. An SSH command after cold boot independently returned [`xfs /dev/sda3`, exit 0](XFS%20root.txt) from `findmnt -no FSTYPE,SOURCE /`.

## Boundaries

This closes the **single-disk XFS install and cold-boot path** behind rapid gate D04. It does not qualify other disk sizes, boot modes, storage layouts, recovery, or the full release matrix. D09 public scripts fetch still fails on this candidate because the public package is absent. Publication rights, independent review and Business receiving remain open. No result from another ISO or an earlier release is transferred here.
