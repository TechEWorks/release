# Changes, support and correction route

## What changed in this content draft

The latest published ISO, source ZIP, base input, manifest and original checksums are unchanged. This public documentation mirror adds a direct reader path, [complete five-asset index](ASSET-INDEX.md), [feature boundary matrix](SCOPE-MATRIX.md), [exact-ISO case matrix](RELEASE-QA-MATRIX.tsv), [17-screen capability gallery](gallery/README.md), [known-issue register](KNOWN-ISSUES-REGISTER.tsv), [human/AI installation](INSTALL-HUMAN-AI.md) and [build instructions](BUILD-HUMAN-AI.md), [lifecycle boundary](LIFECYCLE.md), and [exact ISO component and source reconciliation](ISO-COMPONENT-INVENTORY.md). It is a documentation and presentation proposal, not a software update or public release event. There is no earlier public ServOS version identified in the 1.0.0 release record to compare against.

## Support and private reporting

For an installation problem, preserve the exact ISO SHA-256, selected disk stable IDs, storage layout, firmware boot order, network mode, installer log at `/techev1.0/servosv1.0/logs/install/install.log` and the observed command/error text. Send non-secret diagnostics to [sysadmin@teche.works](mailto:sysadmin@teche.works). Do not include passwords, private keys or customer data in a public issue. The release record does not establish a response-time promise or independently verified security-report handling route.

## If an asset or installation is suspect

Stop using a file whose bytes differ from the [published asset index](ASSET-INDEX.md). Preserve the file, computed hash, download URL and timestamp, then report them privately. A corrected binary requires a separately identified release with its own manifest, checksums, tested scope, notice and independent reader retrieval; changing shipped bytes under the old identity would make existing verification records ambiguous. For an already installed server, do not perform unreviewed disk repair. Retain backups and console access, collect the health checks in [Verification](VERIFICATION.md), and select a recovery path for the actual storage layout. The [known issues register](KNOWN-ISSUES-AND-LIMITS.md) identifies recovery paths not yet qualified on public 1.0.0.
