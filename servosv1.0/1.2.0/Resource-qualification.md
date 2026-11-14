# ServOS v1.2 resource qualification

## Fresh installation minimum

**2 GiB of assigned RAM and at least 2 GiB per target SSD.** Fresh installs below use BIOS on VM 102 with Debian 13.7. Usage was measured after boot and cleanup.

| VM 102 BIOS layout | Install RAM | Install SSDs | Result | RAM used after cleanup | Root + boot used after cleanup | SSD used across members after cleanup¹ |
|---|---:|---:|---|---:|---:|---:|
| ext4 single | 2 GiB | 1 × 2 GiB | Installed and booted | 173 MiB | 424 MiB | 424 MiB |
| md RAID1 (ext4) | 2 GiB | 2 × 2 GiB | Installed and booted | 180 MiB | 427 MiB | 853 MiB |
| Btrfs RAID1 | 2 GiB | 2 × 2 GiB | Installed and booted | 207 MiB | 427 MiB | 843 MiB |
| ZFS RAIDZ2 | 2 GiB | 4 × 2 GiB | Installed and booted | 258 MiB | 716 MiB | 1,420 MiB |

¹ Includes RAID redundancy. Excludes the separate diagnostics SSD and unused capacity.

## Installed-image replicas tested at 512 MiB RAM

| VM 102 BIOS replica | Assigned RAM | Verified virtual SSDs | Boot + SSH | RAM used after cleanup | SSD used after cleanup | Root space available |
|---|---:|---:|---|---:|---:|---:|
| ext4 single | 512 MiB | 1 × 500 MiB | Passed | 80 MiB | 367 MiB | 60 MiB |
| md RAID1 (ext4) | 512 MiB | 2 × 480 MiB | Passed | 84 MiB | 734 MiB | 5 MiB |
| Btrfs RAID1 | 512 MiB | 2 × 460 MiB | Passed | 88 MiB | 536 MiB | 109 MiB |
| ZFS RAIDZ2 | 512 MiB | 4 × 540 MiB | Passed | 148 MiB | 1,323 MiB | 57 MiB |

SSD usage includes root, boot, and RAID redundancy. It excludes the diagnostics
SSD and unused capacity. Root space available is the guest-reported figure.

The ext4 replica used a hardware-specific 11.7 MiB initramfs, down from 36.2 MiB,
and retained the installed kernel module tree. The ZFS replica used a 64 MiB ARC
cap. Cleanup omitted temporary files, downloaded APT packages and indexes,
manual-page cache, and old system journals. Original disks remained available.
Boot and SSH were verified. Workload, package upgrade capacity, and 30% free-space
headroom remain separate qualification checks.

## Other installation trials

| VM 102 BIOS layout | RAM assigned | SSDs assigned | Observed result | RAM used after cleanup | SSD used after cleanup |
|---|---:|---:|---|---:|---:|
| ext4 single | 512 MiB | 1 × 1 GiB | Failed preparing the Debian runtime | — | — |
| ext4 single | 2 GiB | 1 × 1 GiB | Rejected at storage selection. No room for root. | — | — |
| ext4 single | 2 GiB | 1 × 1,792 MiB | Failed during initramfs generation. Target filesystem full. | — | — |
| ext4 single | 2 GiB | 1 × 2 GiB | Installed and booted | 173 MiB | 424 MiB across root and boot |
| md RAID1 / Btrfs RAID1, shared preparation | 512 MiB | 2 × 1 GiB | Failed preparing the Debian runtime | — | — |
| md RAID1 / Btrfs RAID1, shared preparation | 1 GiB | 2 × 1 GiB | Failed loading installer tools | — | — |
| md RAID1 | 2 GiB | 2 × 1 GiB | Rejected at storage selection. No room for root. | — | — |
| md RAID1 | 2 GiB | 2 × 2 GiB | Initial build failed formatting /boot. The named md device did not appear. | — | — |
| Btrfs RAID1 | 2 GiB | 2 × 1 GiB | Rejected at storage selection. No room for root. | — | — |
| Btrfs RAID1 | 2 GiB | 2 × 2 GiB | Initial build failed formatting /boot. The named md device did not appear. | — | — |
| ZFS RAIDZ2, shared preparation | 512 MiB | 4 × 1 GiB | Failed preparing the Debian runtime | — | — |
| ZFS RAIDZ2, shared preparation | 1 GiB | 4 × 2 GiB | Failed loading installer tools | — | — |
| ZFS RAIDZ2 | 2 GiB | 4 × 2 GiB | Installed and booted. Minimum observed RAM headroom was 149 MiB, below 30%. | 258 MiB | 1,420 MiB allocated across both pools, including redundancy |
