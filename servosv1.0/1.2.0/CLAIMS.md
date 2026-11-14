# ServOS 1.2.0 release claims

| Claim | Published wording | Evidence and scope |
|---|---|---|
| SV12-01 | A 63.9 MiB download for a standalone Debian 13 AMD64 server. | [Published manifest](RELEASE-MANIFEST.json) records ZIP and ISO sizes. [Publication receipt](PUBLICATION.md) records public retrieval and hashes. |
| SV12-02 | One network ISO with BIOS and UEFI boot entries. | [Build inspection](QA.md#verification-and-known-limits) verified both entries on the published ISO. Exact-image installs and cold boots remain open. |
| SV12-03 | Choose an eligible single-disk, mdadm, Btrfs or ZFS layout, including four-drive RAIDZ2. Review each erase target. | [Saved v1.2 terminal simulation](screenshots/README.md#zfs-layout-dropdown) and [earlier live QEMU gallery](../1.1.0/screenshots/README.md). |
| SV12-04 | Opt to clear downloaded APT indexes and expire temporary files during finish. | [Saved v1.2 source audit frame](screenshots/README.md#standalone-storage-cleanup-option-in-the-source-audit). |
| SV12-05 | Fresh installation calls for 2 GiB of assigned RAM and 2 GiB per target SSD. | [Resource qualification](Resource-qualification.md#fresh-installation-minimum) records the prior BIOS trials and their headroom limits. |
| SV12-06 | An ext4 replica used 80 MiB of RAM and 367 MiB of disk after cleanup in the VM 102 trial. | [Earlier installed-image measurements](Resource-qualification.md#installed-image-replicas-tested-at-512-mib-ram). That replica had 512 MiB assigned RAM and a 500 MiB virtual SSD. |

The standalone download excludes WorkDesk and Proxmox deployment. [Known limits](QA.md#known-issues-and-limits).
