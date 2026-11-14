# ServOS 1.1.0 verification scope

| Build | Evidence |
| --- | --- |
| Published ISO `6cda5cb36b162980f3309cbb7edef90f948dea9fbe45fcf11ac322789d6c3678` | Public download matched the published SHA-256. BIOS and UEFI boot entries and the installer payload were checked. Full installs and cold boots on these exact bytes remain open. |
| Release candidate `e1fabdaee26613505b2223bd9f172ebbade9ca09680787d8c702187fac5c3e54` | Full four-drive RAIDZ2 installations and cold boots passed in BIOS and UEFI on Proxmox VM 102. This build supplied the [gallery](screenshots/README.md). |
| CI candidate `fb566c5c4634ac6799fe22959554124fa96a61bcaee6911094ff0fde8f60601d` | The [GitHub build](https://github.com/TechEWorks/servos/actions/runs/43531086133) matched the local rebuild. Boot entries and installer payload were checked. [Source QA](https://github.com/TechEWorks/servos/actions/runs/43531086165) passed seven checks, 6,136 simulated installs and 17,936 screen checks. |

Potential RAID Summary can display the prior filesystem briefly when returning to DriveOS. Recheck the selected family and final review before confirming erasure. Use an isolated installation network because live SSH can open the shared installer without authentication. Release signing and exact-ISO production qualification remain open.
