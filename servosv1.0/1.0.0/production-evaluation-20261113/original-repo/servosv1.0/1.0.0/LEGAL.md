# ServOS licensing, ownership and notices

Effective 2026.11.05. TechE-authored ServOS installer and utility source in
this release is offered under **GNU AGPL-3.0-only**. The exact dated text is
in [LICENSE.txt](LICENSE.txt) and
[LICENSE-2026.11.05.txt](LICENSE-2026.11.05.txt). The corresponding source is
the versioned [SOURCE.zip](README.md#downloads-and-integrity), with its byte
count and SHA-256 in the release manifest. Source modified by a distributor
must be identified and distributed under the applicable license terms.

TechE names, logos, certification and release-signing identity are separate
from the software license; see the [shared IP policy](../../ip/README.md).
Debian GNU/Linux, its installer and netboot components, debootstrap, APT,
Linux, GRUB, OpenSSH, optional ZFS/Btrfs/mdadm/XFS tools and other upstream
software retain their own copyrights and licenses. The AGPL declaration does
not relicense them. Installed package copyright notices are available under
`/usr/share/doc/<package>/copyright`; the ISO and build input include upstream
components whose exact redistribution notice inventory is still under review.
See [QA](QA.md) for that open release control.

The ISO uses a pinned build input and downloads packages from configured
Debian repositories during installation. It does not include a WorkDesk
package, NetBird enrollment key, GitHub credential or customer data. The
selected whole target disks are erased only after the final typed confirmation.

The software is provided **AS IS**, without any express or implied warranty
or guarantee to the extent permitted by applicable law. The full license text
controls the rights and obligations for TechE-authored covered code. Before
deployment, verify backups, disk identity, checksums and the published QA
scope. Contact [sysadmin@teche.works](mailto:sysadmin@teche.works) about
license or attribution concerns.
