# Known Issues and Bugs — ServOS public 1.0.0

This is a **content-draft reading index** of the [published 1.0.0 QA record](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md), not a replacement for a reviewed issue tracker. A stable public bug ticket, severity/owner decision and fix target were not found in the release record; those fields remain open under the S4 rubric.

| Pack reference | Classification | Trigger and observed user impact | Workaround / status |
|---|---|---|---|
| OBS-01 (local reference, not tracker ID) | Confirmed presentation defect | During the exact public ISO's ZFS install, task 1/6 still says “Check network” while the activity pane installs ZFS storage tools. The install continued and booted. [Original QA observation](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md#L163). | Read the live activity log; label correction belongs in a future build. No verified fix is claimed. |
| LIM-01 (local reference) | Not qualified | ZFS RAIDZ, mdadm ext4 and other Btrfs layouts are offered but not shown as installed/cold-booted on the public ISO in the cited QA report. | Select a reported tested layout when its constraints fit; otherwise qualify the chosen layout independently before relying on it. |
| LIM-02 (local reference) | Not qualified | Other static IPv4/key setups, broader physical hardware, interrupted install, failed mirror/network, degraded ZFS/mdadm and new-disk Btrfs recovery lack public-ISO acceptance evidence. | Keep backups and console access; do not infer recovery behavior from the tested Btrfs same-member path. |
| CTRL-01 (local reference) | Release control open | Complete ISO and installed-system SBOM, upstream notice audit and release signature are not published as complete controls. | Review [original legal notice](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/LEGAL.md) and [original QA](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/QA.md); no signature is claimed. |

The optional `wd1.0` menu/catalog code is present in the historical source but its pinned package URL was not configured for the public release. No WorkDesk package is bundled or promised by this ISO. The next requested scripts-only scope is a separate new-build decision.

For support, record the exact ISO hash, disk stable IDs, storage layout, boot order, installer log and observed error. Send those privately to [sysadmin@teche.works](mailto:sysadmin@teche.works), without credentials or customer data. The pack does not establish a separate verified security response SLA or an approved release-risk acceptance.
