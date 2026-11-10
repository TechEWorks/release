# TechEWorks releases

This public catalog lists TechEWorks product releases. Each published version
provides its buildable source snapshot, build and installation instructions,
release artifacts, licensing, known limitations and an exact release record.
Active development workspaces and private QA evidence remain in product
repositories; their privacy does not restrict access to the published source.

Shared TechEWorks standards are in [license](license/README.md) and
[IP](ip/README.md). Every published product version also carries its own
`LICENSE.txt` and component notices. Upstream components retain their own
licenses.

| Product | Public release index |
| --- | --- |
| WorkDesk 1.0 | [Product and download guide](workdeskv1.0/README.md) · [approved release index](workdeskv1.0/index.json) |
| ServOS 1.0 | [Product and download guide](servosv1.0/README.md) · [version index](servosv1.0/index.json) |
| Fleet RMM 1.0 | [fleetrmmv1.0/index.json](fleetrmmv1.0/index.json) |
| UCP 1.0 | [ucpv1.0/index.json](ucpv1.0/index.json) |
| Maestro 1.0 | [maestrov1.0/index.json](maestrov1.0/index.json) |

## Product-and-stage downloads (S4)

Every stage has its own users, testers, independently selected assets and QA. The public catalogs list **only already public, expressly cleared assets**, not private source, restricted test evidence or automatic product releases. For WorkDesk v1.0 the stage links are [00 PoC](workdeskv1.0/00-explore-poc/README.md), [01 Strawman](workdeskv1.0/01-strawman/README.md), [02 Alpha](workdeskv1.0/02-alpha/README.md), [03 Beta](workdeskv1.0/03-beta/README.md), [04 Base Release](workdeskv1.0/04-base-release/README.md), [05 Install/Deploy](workdeskv1.0/05-install-deploy/README.md) and [06 Support](workdeskv1.0/06-support/README.md).

A stage catalog `<product-id>/<NN-stage>/index.json` identifies its stage users/testers, available original assets, producer stage, hashes, immutable URLs, QA scope and limitations. An empty stage catalog truthfully means no publicly available stage asset. Cross-stage dependencies must pin the original producer digest and be tested again in the consuming stage. **Stage preview availability and an approved product release are different states.** New original files and their one-file ZIP envelopes must separately be strictly below 2,000,000,000 bytes; no multipart bypass. Older native public QA files are retained only as clearly marked `LEGACY_PREVIEW_NATIVE`.

An index lists **published** releases only; an empty index means none is published. A product version is written without a leading `v`, for example `1.0.0`. The public tag adds it once: `<product>-v<version>`, for example `workdeskv1.0-v1.0.0`. Each release record identifies its approved private source commit and Git tree hash, public source-snapshot hash, accepted output IDs, exact artifact names, byte sizes, SHA-256 hashes and signatures, applicable OS/architecture/device scope, QA result, licences and notices, approval and publication time, upgrade path, release notes and rollback path. It names pending or excluded outputs explicitly.

Finished binaries are attached to the GitHub Release or linked by exact hash to a verified artifact location when they exceed the host's asset limit. They are not committed as ordinary Git blobs. Installers and updaters pin the exact tag, artifact name, byte count and SHA-256; they do not use a moving `latest` URL. A changed public artifact requires a new numbered product version and release record.

WorkDesk's GUI offline, GUI network and text network installers are possible output parts of one product version. The accepted output matrix and verified artifact hashes determine what is actually released. A common core-image identity is recorded only when the build and QA evidence prove it. Update packages have their own declared output IDs and state their automatic or administrator-controlled installation policy.
