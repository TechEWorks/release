# TechE WorkDesk v1.0

WorkDesk is the TechE.Works desktop system. Three installer formats are planned; each delivers the same WorkDesk product through a different setup route.

| Installer | Status | What it does |
| --- | --- | --- |
| **WD(txt) network** | [QA preview 23 prepared; download pending](previews/qa23/README.md) | Boots a text installer and downloads its pinned WorkDesk assets and Debian packages over the network. |
| **WD(gui) network** | Coming soon | Graphical installer with network delivery. |
| **WD(gui) offline** | Coming soon | Graphical installer with the required payload on the installation media. |

## WD(txt) network QA preview

**The ISO download has not been published yet.** The prepared preview is for an isolated, disposable UEFI virtual machine, not an approved production release. The ISO erases disks selected during installation. Read the [preview record, setup steps and known issues](previews/qa23/README.md) before booting it once available.

1. Once publication is approved, download the ISO from the QA preview release linked here.
2. Verify its SHA-256 against the [exact preview manifest](previews/qa23/RELEASE-MANIFEST.json) or [checksums](previews/qa23/SHA256SUMS.txt).
3. Attach it to a **disposable** UEFI VM with a blank test disk and working internet. The observed QA profile used 4 logical CPUs, 8 GiB RAM and a 64 GiB disk.
4. Follow the installer, inspect the selected disk and erasure warning, and finish setup. Detach the ISO before booting the installed disk.

The preview ISO is **74,842,112 bytes** (about 71.4 MiB). It is small because the installation downloads its pinned content. Installation speed depends on the network and host; the observed QA install stage exceeded 12 minutes. The linked record identifies what passed, what failed and what remains untested.

The [approved release index](index.json) remains empty until WorkDesk passes its release gates. The QA preview is deliberately excluded from that index. Source and build-input publication is pending an explicit decision; TechE and upstream component licences remain applicable.
