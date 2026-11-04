# TechEWorks releases

This is the public release catalog for TechEWorks products. Product source code, build workspaces, and QA scripts live in their private product repositories. Publication is controlled by the TechEWorks release maintainers.

| Product | Public release record |
| --- | --- |
| WorkDesk v1.0 | [workdeskv1.0/index.json](workdeskv1.0/index.json) |
| ServOS v1.0 | [servosv1.0/index.json](servosv1.0/index.json) |
| Fleet RMM v1.0 | [fleetrmmv1.0/index.json](fleetrmmv1.0/index.json) |
| UCP v1.0 | [ucpv1.0/index.json](ucpv1.0/index.json) |
| Maestro v1.0 | [maestrov1.0/index.json](maestrov1.0/index.json) |

Each index lists **published** releases only. Each entry must identify the product version, release channel, UTC approval/publication time, source commit, supported upgrade path, asset names and byte sizes, SHA-256 hashes, signature, QA result, release notes, and rollback path. An empty index means no release has been published.

Binaries belong on GitHub Releases attached to this repository, not in Git history. Tags must be unique across all products, for example `workdeskv1.0-v1.0.0-beta.1` and `servosv1.0-v1.0.0`. Asset filenames include product, version, architecture, and purpose. Installer and updater consumers pin the exact tag, asset name, byte count, and SHA-256; they do not use a moving `latest` URL.

WorkDesk's graphical and text installers use the same approved core image and hash. Their installer ISOs may be separate release assets. Update records are separate from installer assets and must state whether installation is automatic under policy or requires an administrator.
