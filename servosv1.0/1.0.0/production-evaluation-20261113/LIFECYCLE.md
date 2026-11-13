# ServOS 1.0.0 — operate, recover and supersede

**Exact output:** the unchanged public ISO SHA-256 `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`. Before any operation, identify the installed server, storage layout, disk stable IDs, backup and console access. The [install guide](original-repo/servosv1.0/1.0.0/INSTALL.md) and [safe checks](VERIFICATION.md) define the installation and read-only first-boot path.

## Updates and component refresh

The ISO is a network installer, not an in-place operating-system upgrade image. On an installed server, use Debian's package manager for ordinary package updates after checking the applicable Debian security notices, package changes, available space and backup/restore plan. The original QA demonstrates `apt update` on named VM paths; it does **not** qualify unattended upgrades, major Debian release upgrades or every storage component refresh. Do not infer that an ISO reinstallation preserves data: the selected whole disks are erased.

## Rollback and recovery boundary

For a failed package change, use a known-good backup or snapshot and the procedure approved for that installed host; no universal rollback command is claimed for this ISO. For an interrupted installer, failed network/mirror access, ZFS/mdadm degraded member, new replacement disk or physical-hardware problem, stop destructive actions, preserve the log and storage identity, and use a separately reviewed recovery runbook. The [published exact-ISO QA](QA-CROSSWALK.md) proves one Btrfs RAID1 missing-original-member boot and manual same-member repair. It does not prove automatic repair, new-disk replacement or recovery on other layouts.

## Removal, withdrawal and supersession

There is no safe generic “uninstall ServOS” command for a whole-disk operating system. To retire a server, back up required data, export configuration, confirm service migration, then use an approved data-erasure and reprovisioning procedure for the specific device. If a release asset is suspect, stop using it, retain its hash and URL, and report it through the [support route](CHANGES-SUPPORT.md). A corrected asset receives a new release identity, manifest and QA; do not overwrite shipped bytes under an old identity. The previous public release remains available by default until a separate history decision is executed.

**Expected result of the safe first-boot check:** the chosen root/boot filesystem and members are healthy, SSH is active, the intended administrator has sudo access, `teche -v` reports 1.0.0, and the saved installer log is present. Unexpected results are an investigation, not a PASS. The support record needs ISO hash, disk IDs, layout, boot order, command output and log; do not include secrets.
