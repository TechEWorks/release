# Install and verify ServOS 1.2.0

Download the [ISO ZIP](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.2.0/TechE-ServOS-13.7-v1.2-amd64-network.iso.zip) and [checksums](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.2.0/ServOS-v1.2-SHA256SUMS.txt) into the same folder. On Linux, verify the ZIP and its extracted ISO:

```sh
unzip TechE-ServOS-13.7-v1.2-amd64-network.iso.zip
sha256sum -c ServOS-v1.2-SHA256SUMS.txt
```

Attach the ISO as virtual optical media or write the extracted ISO to a dedicated boot USB. Boot x86-64 BIOS or UEFI with Secure Boot disabled. At Welcome press Enter, read to the end of the legal notice, and choose the network adapter and target storage. Review each selected disk before typing ERASE. On the finish screen, choose shutdown or remove the media and restart. On first boot, confirm the server name and address on the console, then connect to the installed SSH service using the administrator credentials configured during setup.

Use a trusted isolated installation network for the live SSH stage. Back up the target first. For recovery or rollback, restore the verified backup or use the [v1.1 archive](https://github.com/TechEWorks/release/releases/tag/servosv1.0-v1.1.0) to reinstall after preserving needed data.

## Rebuild

The [tagged source](https://github.com/TechEWorks/servos/tree/v1.2.0) and kernel-matched storage asset bundle are available through TechEWorks. On an amd64 Debian build host with root privileges, extract the standalone source bundle and run:

```sh
SERVOS_STANDALONE=1 sh installer/build-iso.sh /path/to/pinned-base.iso /path/to/TechE-ServOS-13.7-v1.2-amd64-network.iso
```

The builder checks the [pinned Debian base ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/BUILD-INPUT-Pinned-Base-ISO.iso) and storage bundle. Automated rebuilds use the same inputs and record the output SHA-256, byte count, and BIOS/UEFI boot catalog.
