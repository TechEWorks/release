# ServOS 1.0.0 verification and open checks

Release artifact: `TechE-ServOS-13.7-v1.0-amd64-network.iso`, 71,696,384
bytes, SHA-256
`b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`.
The private source commit is `359909def220ac8b152d4015cecd28f959770ddf`;
the approved tree and build tree are both
`f805c77e945ec6ad0331edda074f3dd08b4b3c9e`.

## Verified before publication

- The pinned 63,307,776-byte build input matched its SHA-256. The Debian 13.7
  CI build completed, reported BIOS and UEFI El Torito entries, and uploaded
  the exact ISO and build manifest. A downloaded copy matched the manifest's
  ISO SHA-256 and byte count.
- The source QA and release build checks passed, including screen framing,
  screen walkthrough, activity copy and the product/DriveOS naming scan.
- An earlier exact ISO from the same installer backend, SHA-256
  `7f0d27d40eac5dd1dd861ecf3afe610388a560d408702005cbe5045a2f4c4a5e`,
  passed on disposable PVE VM225: ext4 single-disk boot; ZFS two-disk mirror
  boot from each EFI member; mdadm RAID1 with XFS boot from each EFI member;
  and Btrfs RAID1 boot from each EFI member. Those runs also checked SSH,
  sudo, APT update, mount state and saved installation logs. The new ISO
  changes product wording, footer date and utility version/help. These
  earlier live results are evidence about the backend, **not exact-byte live
  QA of the published ISO**.

## Post-release acceptance work

The first independent public-source rebuild detected CRLF line endings in the
source ZIP. The [public build guide](BUILD.md) now includes an explicit
text-only LF normalization step before executing shell scripts. The source
ZIP, ISO and their published checksums have not changed. The independent
rebuild is being rerun against that corrected procedure.

The following paths are not claimed as passed for the published ISO: a fresh
end-to-end install and cold boot of the published bytes; single-disk XFS and
ZFS; representative ZFS RAIDZ, mdadm ext4 and other Btrfs layouts; static IPv4;
SSH public-key access; separate physical directory partitions; degraded-member
boot and repair; interrupted-install recovery; failed network/mirror handling;
and broader non-VirtIO hardware. The optional WorkDesk catalog requires a
published pinned HTTPS ZIP and its matching SHA-256. A complete installed and
ISO component SBOM, upstream notice audit and release signature are also
post-release controls. They must be closed before claiming a mission-critical
production qualification.

For an incident, preserve the ISO SHA-256, selected disk stable IDs, storage
layout, boot order and installer log. Send the details privately to
[sysadmin@teche.works](mailto:sysadmin@teche.works). Do not send passwords,
private keys or customer data in a public issue.
