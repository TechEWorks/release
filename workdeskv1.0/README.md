# WorkDesk v1.0 releases

This folder is the public WorkDesk release record. The private product workspace is [TechEWorks/workdeskv1.0](https://github.com/TechEWorks/workdeskv1.0). The [index](index.json) lists approved published releases only.

A published release can contain these asset types:

- **GUI installer ISO:** graphical live environment and installation flow.
- **Text installer ISO:** network or offline text installation flow.
- **Shared WorkDesk core image:** the exact same approved bytes and SHA-256 must be used by both installer paths for the same release.
- **Update artifacts:** versioned packages or images for an approved upgrade path.
- **Release manifest, checksums, and signature:** asset names, byte counts, SHA-256 values, UTC release time, source commit, channel, compatibility, QA result, and rollback instructions.

Large binaries are attached to a GitHub Release in the public `TechEWorks/release` repository. The Git tag must include the product name and version, for example `workdeskv1.0-v1.0.0-beta.1`. File paths under this folder contain release records; they are not a private workspace. Consumers must pin the exact tag, asset, byte count, and SHA-256.

No WorkDesk release has been published in this catalog yet. Candidate builds in the private source repository are not automatically installable releases.
