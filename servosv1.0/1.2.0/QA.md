# Verification and known limits

**Exact published ISO SHA-256** `b9190a6d46884fdcea0ccbd4ecdb9c778ad0f3796642fa48ff2bbbeacbc1c80e`

| Check | Result |
|---|---|
| Standalone ISO build and inspection | Passed. BIOS and UEFI boot entries, the standalone marker and kernel-matched OpenZFS files were present. WorkDesk and Proxmox deployment payloads were absent. |
| ZIP envelope | One member. Its size and hash matched the original ISO. |
| Live installs and cold boots on the exact 1.2 ISO | Deferred at the publisher’s request. Production qualification remains open. |
| Prior v1.2 source audit | 203 captured frames and 6,136 simulated backend installations. [Screen gallery](screenshots/README.md). This work preceded the standalone packaging change. |
| Earlier Proxmox testing | [Resource qualification](Resource-qualification.md) and [v1.1 live QEMU captures](../1.1.0/screenshots/README.md) identify their separate test scope. |

## Known issues and limits

- Live installer SSH opens the shared installer without a password. Use a trusted isolated network.
- The earlier minimum-size RAIDZ2 install fell below the 30% RAM headroom target. The installed-image replica sizes describe measured boot and SSH outcomes.
- The release provides SHA-256 checksums. A detached release signature and exact-image production QA remain open.
