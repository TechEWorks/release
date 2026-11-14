# ServOS v1.2 assets

This index records the assets selected for ServOS v1.2.0. Each dependency retains its own version and is identified by its exact SHA-256 checksum where a binary is pinned.

## Published standalone release

The [ServOS v1.2.0 release](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.2.0) contains the standalone ISO ZIP, checksum file, and release manifest. The ISO inside the ZIP has its own checksum. See the [published artifact index](../../servosv1.0/1.2.0/Artifact%20index.tsv) for exact sizes and checksums.

## Verified public inputs for the multi-form installer

| Asset | Version | SHA-256 | Download |
| --- | --- | --- | --- |
| Base installer ISO | ServOS v1.0 build input | `7a473b485c3a81406098e2806a6a489b88eb10e44da188db86b92e7a37dfa55a` | [Pinned base ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/BUILD-INPUT-Pinned-Base-ISO.iso) |
| WorkDesk visual pack | WorkDesk v1.0 visual assets, snapshot 2026-11-05 | `2757577dec9301249b8b84c47e323d5c219c081853a207cabec08aa602775dda` | [Visual pack](https://raw.githubusercontent.com/TechEWorks/release/6c5bd161b280ec5b1fe124986d36e22da9200e20/workdeskv1.0/qa-assets/2026-11-05/WorkDesk-v1.0-visual-assets.zip) |
| Mattermost Desktop | 6.3.1-1 amd64 | `62ad18cf1b85023ce8992d83b207a74f17ac0d58281cf479db5b0aba4e088a3b` | [Debian package](https://releases.mattermost.com/desktop/6.3.1/mattermost-desktop_6.3.1-1_amd64.deb) |
| ONLYOFFICE Desktop Editors | 10.0.0 amd64 | `2190edb4022a2ac2f6eee0f78815520f0e4ece1e8a1097c645a6f9b225c8b59c` | [Debian package](https://download.onlyoffice.com/repo/debian/pool/main/o/onlyoffice-desktopeditors/onlyoffice-desktopeditors_10.0.0_amd64.deb) |
| Proxmox archive keyring | Debian 13 (Trixie) | `136673be77aba35dcce385b28737689ad64fd785a797e57897589aed08db6e45` | [Archive keyring](https://enterprise.proxmox.com/debian/proxmox-archive-keyring-trixie.gpg) |

The 19 pinned Debian build packages passed download and SHA-256 verification on 2026-11-14. The seven pinned Proxmox VE package versions and both pinned Debian Docker package versions were present in the upstream package indexes on the same date.

## Pending download locations

| Asset | Version | Status |
| --- | --- | --- |
| ServOS storage build bundle | Kernel ABI `6.12.107+deb13-amd64` | Local archive and 11 manifest entries verified. CI download location pending. |
| WorkDesk deployment core | WorkDesk v1.1 | Local archive and 183 manifest entries verified. Installer download location pending. |
