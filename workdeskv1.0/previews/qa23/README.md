# WorkDesk v1.0 — WD(txt) network QA preview 23

This public prerelease exposes the exact ISO that was tested in disposable VMs on 6 November 2026. It is a **QA preview**, not a passed product release. Use an isolated, disposable UEFI VM and blank test disks only. Do not deploy it on a production machine or a network where open SSH/RDP listeners are unacceptable.

## Download and verify

Download `TechE-WDtxt-Network-v1.0-d358c44-QA23.iso` from the [GitHub prerelease](https://github.com/TechEWorks/release/releases/tag/workdeskv1.0-v1.0.0-qa.23). Its exact size is **74,842,112 bytes** and SHA-256 is `33e876edc0a2397f64c02ef176e4be7b7248827d3dfb3c6096493c6c1d181738`. The [checksums](SHA256SUMS.txt) and [manifest](RELEASE-MANIFEST.json) also cover the source archive, pinned ServOS base and visual asset pack. No release signature is claimed.

On Linux or macOS, run `sha256sum TechE-WDtxt-Network-v1.0-d358c44-QA23.iso`. On Windows PowerShell, run `Get-FileHash .\TechE-WDtxt-Network-v1.0-d358c44-QA23.iso -Algorithm SHA256`. Compare the entire digest before booting.

## Test installation

1. Create a **disposable** UEFI VM with a blank 64 GiB test disk, 4 logical CPUs, 8 GiB RAM and internet access. This is the profile observed in QA, not a general hardware certification.
2. Attach the ISO as virtual optical media and boot it. The network route downloads Debian packages and a pinned WorkDesk visual archive. Its pinned visual URL was anonymously reachable at the time of publication.
3. Select only the blank test disk. Review the disk list and erasure summary before confirming. **Selected disks are wiped.** The single-disk ext4 and single-disk ZFS paths have installation and installed-disk boot evidence; other storage modes are not approved by this preview.
4. Create the separate maintenance and daily-use accounts, complete the installer, detach the ISO and boot the installed disk.

## Known failures and unverified areas

- A two-disk ZFS mirror booted from either surviving member, but one degraded-member configuration did **not** mount its surviving EFI partition. Kernel and bootloader updates on that degraded member are therefore unsafe. Do not use the mirror route for this preview.
- The installed guest had no enforced inbound firewall policy; SSH and RDP listened on all interfaces in the QA network. Keep the VM isolated.
- The measured ext4 installation stage took at least **12 minutes 21 seconds**, exceeding the five-minute target.
- The exact installed package/licence inventory, customer terms, component notices, wallpaper rights record and release signature are not complete for this candidate.
- Physical hardware, legacy BIOS, alternate storage layouts, static/Wi-Fi configuration, full desktop/app workflows, multiuser RDP and VM211 visual parity have not passed this candidate's release checks.

The approved [WorkDesk release index](../../index.json) remains empty. This preview does not change the product release decision. [TechE licensing information](../../../license/README.md) and [IP information](../../../ip/README.md) apply alongside the licences of Debian and other included components.

## Rebuild inputs

The prerelease includes the tested ISO, its exact source ZIP, the pinned ServOS base ISO, the WorkDesk visual ZIP, `SHA256SUMS.txt` and `RELEASE-MANIFEST.json`. The source archive corresponds to private WorkDesk commit `d358c44b59b6055758d0ce48a5fc918b8efa9e73`. The visual archive is also pinned at a public GitHub URL in the core pack. These files document the candidate; no fully reproducible rebuild or signed supply-chain claim is made.
