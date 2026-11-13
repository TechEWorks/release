# Verify the published ISO and use the installed server safely

The original ISO and its published checksum can be verified now. This public documentation mirror does not contain the separate local content packet or its one-ISO transport ZIP.

## Verify the published ISO now

Download the [official ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-amd64-network.iso) and [official SHA256SUMS.txt](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/SHA256SUMS.txt) into the same directory. On Debian or another system with `sha256sum`:

```sh
sha256sum -c SHA256SUMS.txt --ignore-missing
```

Expect `TechE-ServOS-13.7-v1.0-amd64-network.iso: OK`. On Windows PowerShell:

```powershell
(Get-FileHash -Algorithm SHA256 .\TechE-ServOS-13.7-v1.0-amd64-network.iso).Hash.ToLowerInvariant()
```

Expect `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`. Stop if either check differs. The [five-asset index](ASSET-INDEX.md) gives every published file's exact size and hash.

The original release checksum file covers its four named historical files. A checksum detects changes relative to a recorded digest; it does not establish publisher identity. Compare the ISO hash to the [official GitHub release](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.0.0) through your trusted access path before use.

## Safe first-boot checks

After following the [install guide](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/INSTALL.md), detaching the ISO and cold booting the selected disk, run these **read-only** checks on the installed server:

```sh
cat /etc/os-release
findmnt -no SOURCE,FSTYPE,TARGET /
findmnt -no SOURCE,FSTYPE,TARGET /boot
findmnt -no SOURCE,FSTYPE,TARGET /boot/efi
systemctl is-active ssh
id
teche -v
```

Expect Debian 13.7 for the historical ISO, the storage mounts chosen at installation, `active` for SSH, the intended non-root administrator and TechE utility version 1.0.0. For ZFS, additionally inspect `zpool status -x`; for mdadm, inspect `cat /proc/mdstat`; for Btrfs, inspect `sudo btrfs filesystem show /` and `sudo btrfs filesystem df /`. The exact expected topology depends on the layout. The [public QA case record](QA-CROSSWALK.md) provides tested examples, not a substitute for inspecting the actual machine.

If identity, mounts, SSH or storage health differ from the reviewed target, stop deployment and preserve the ISO hash, selected disk stable IDs, boot order, `/techev1.0/servosv1.0/logs/install/install.log` and command output. Do not run repair or `ERASE` on an uncertain device. Contact [sysadmin@teche.works](mailto:sysadmin@teche.works) privately with non-secret diagnostics.
