# Third-party components and attribution

Revision: 2026.11.05.

This release includes a Debian-derived network boot environment and pinned
Debian build input. The installed system obtains Debian packages from the
selected package mirror. Debian GNU/Linux, the Linux kernel, GRUB,
debootstrap, APT, OpenSSH, ZFS, mdadm, Btrfs, XFS tools and their dependencies
retain their respective upstream copyrights and licenses. TechE's AGPL grant
in [LICENSE.txt](LICENSE.txt) applies only to TechE-authored code in the
public source snapshot; it does not change any upstream license.

Installed packages expose their package-specific notices under
`/usr/share/doc/<package>/copyright`. The build input and ISO component
inventory has not yet been published as a complete SBOM. See [QA](QA.md) for
that open release control. Contact
[sysadmin@teche.works](mailto:sysadmin@teche.works) about attribution.
