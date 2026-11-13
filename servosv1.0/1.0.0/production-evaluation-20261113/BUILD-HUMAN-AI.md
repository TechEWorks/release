# Build the exact public ISO — human and AI instructions

The [original public build guide](https://github.com/TechEWorks/release/blob/d89769b1695c4f4965404ee5317f54303ab6abf8/servosv1.0/1.0.0/BUILD.md) is the canonical command source. These instructions apply to the **published 1.0.0 source ZIP and base ISO**; they do not build a new scripts-only release. An [independent public rebuild](https://github.com/TechEWorks/release/actions/runs/41983978934) reported the exact published ISO hash. This content revision did not run a new Linux ISO build.

## Shared inputs and expected result

| Input/output | Bytes | SHA-256 |
|---|---:|---|
| [Source ZIP](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-SOURCE.zip) | 115,286 | `f63ce9c9dde59ff4e8f5b9260a589f32bfaec224de72f66ee0900001cd526013` |
| [Build-only base ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/BUILD-INPUT-Pinned-Base-ISO.iso) | 63,307,776 | `7a473b485c3a81406098e2806a6a489b88eb10e44da188db86b92e7a37dfa55a` |
| Expected [deployable ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-amd64-network.iso) | 71,696,384 | `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf` |

Use x86-64 Debian 13, Internet access and root privileges for the build, with at least 2 GiB free RAM and 2 GiB temporary disk space. The official candidate used a pinned `debian:13.7-slim` container. The builder downloads additional pinned components; save the build log and its checks. The original guide notes that tool/archive metadata can affect independent byte reproduction.

## Human procedure

Run in a fresh Debian 13 working directory containing the two input files and the [original `SHA256SUMS.txt`](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/SHA256SUMS.txt). The checksum file covers the original release files; `--ignore-missing` checks only files present in this working directory.

```sh
sudo apt update
sudo apt install --no-install-recommends xorriso cpio xz-utils dpkg wget curl coreutils kmod unzip python3 ca-certificates
sha256sum -c SHA256SUMS.txt --ignore-missing
mkdir servos-source
cd servos-source
unzip -q ../TechE-ServOS-13.7-v1.0-SOURCE.zip
python3 - <<'PY'
from pathlib import Path
for path in Path('.').rglob('*'):
    if path.is_file():
        data = path.read_bytes()
        if b'\0' not in data and b'\r\n' in data:
            path.write_bytes(data.replace(b'\r\n', b'\n'))
PY
python3 qa/frame_contract_test.py
python3 qa/screen_walkthrough.py
python3 qa/message_audit.py
sudo sh build-iso.sh "$PWD/../BUILD-INPUT-Pinned-Base-ISO.iso" "$PWD/../servos-rebuilt.iso"
cd ..
sha256sum servos-rebuilt.iso
```

Keep the original source ZIP unchanged. The LF conversion above applies only to extracted text before running shell scripts. Save the terminal transcript, Debian/tool versions, builder identity, fetched-component checks, test outputs, build exit status, output bytes and SHA-256. A hash mismatch is a different build: preserve its logs and run its own boot/install QA before distributing it as an official binary.

## AI operator procedure

An AI agent uses **the same commands and pinned inputs above** on a disposable Debian 13 build host. Before running a command it records the working directory, source ZIP and base ISO size/hash, host OS/tool versions and intended output path. It must show the observed checksum result and each QA script's actual exit code; command intent is not evidence of success. It captures the full build log and fetched-component checks, then compares the resulting ISO's bytes/hash with the expected value above. It stops and reports the exact failing command, exit code and logs on any mismatch. It does not change the recipe, overwrite a released asset or infer a PASS from a screenshot. The operator reviews the observations before using the output.

The Windows-side packaging check recorded one local `frame_contract_test.py` PASS. `screen_walkthrough.py` and `message_audit.py` could not run under the bundled Windows Python because `_curses` is unavailable; no local PASS is claimed for those scripts. The original public Linux rebuild and its QA record remain separate historical evidence.

## Exact source and input inventories

The [39-file source provenance index](audit/source-file-provenance.tsv) binds every original source ZIP member to its byte count and SHA-256. The [19-row builder input index](audit/builder-input-provenance.tsv) transcribes the pinned base ISO and eighteen Debian package URLs/hashes from the original `build-iso.sh`. These indexes preserve the historical source bytes. File-level authorship, complete upstream licence/notices, fetched package byte counts and builder tool versions still require review; the indexes do not claim rights clearance or a new rebuild.
