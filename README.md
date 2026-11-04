# TechEWorks releases

This public catalog lists approved TechEWorks product releases. Editable product source, build workspaces and private QA evidence remain in each private product repository. Each published version includes a reviewed product source snapshot, accepted delivery artifacts, required notices and a public release record. Publication requires a separate verified promotion.

| Product | Public release index |
| --- | --- |
| WorkDesk 1.0 | [workdeskv1.0/index.json](workdeskv1.0/index.json) |
| ServOS 1.0 | [servosv1.0/index.json](servosv1.0/index.json) |
| Fleet RMM 1.0 | [fleetrmmv1.0/index.json](fleetrmmv1.0/index.json) |
| UCP 1.0 | [ucpv1.0/index.json](ucpv1.0/index.json) |
| Maestro 1.0 | [maestrov1.0/index.json](maestrov1.0/index.json) |

An index lists **published** releases only; an empty index means none is published. A product version is written without a leading `v`, for example `1.0.0`. The public tag adds it once: `<product>-v<version>`, for example `workdeskv1.0-v1.0.0`. Each release record identifies its approved private source commit and Git tree hash, public source-snapshot hash, accepted output IDs, exact artifact names, byte sizes, SHA-256 hashes and signatures, applicable OS/architecture/device scope, QA result, licences and notices, approval and publication time, upgrade path, release notes and rollback path. It names pending or excluded outputs explicitly.

Finished binaries are attached to the GitHub Release or linked by exact hash to a verified artifact location when they exceed the host's asset limit. They are not committed as ordinary Git blobs. Installers and updaters pin the exact tag, artifact name, byte count and SHA-256; they do not use a moving `latest` URL. A changed public artifact requires a new numbered product version and release record.

WorkDesk's GUI offline, GUI network and text network installers are possible output parts of one product version. The accepted output matrix and verified artifact hashes determine what is actually released. A common core-image identity is recorded only when the build and QA evidence prove it. Update packages have their own declared output IDs and state their automatic or administrator-controlled installation policy.
