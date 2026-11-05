# Build TechE ServOS 1.0.0 from the public source

This procedure uses only the public release assets. No private product
repository, GitHub login, Proxmox host or TechE service is needed.

## 1. Prepare a Debian 13 build host

Use x86-64 Debian 13 with Internet access and root privileges for the build.
Allow at least 2 GiB free RAM and 2 GiB free temporary disk space. Install:

```sh
sudo apt update
sudo apt install --no-install-recommends xorriso cpio xz-utils dpkg wget curl coreutils kmod unzip python3 ca-certificates
```

The official candidate was built in a pinned `debian:13.7-slim` container.
`build-iso.sh` checks the pinned input ISO and its downloaded build components
by SHA-256, normalizes timestamps and refuses to overwrite an output.

## 2. Download and verify the inputs

```sh
base='https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0'
curl -fL -o TechE-ServOS-13.7-v1.0-SOURCE.zip "$base/TechE-ServOS-13.7-v1.0-SOURCE.zip"
curl -fL -o BUILD-INPUT-Pinned-Base-ISO.iso "$base/BUILD-INPUT-Pinned-Base-ISO.iso"
curl -fL -o SHA256SUMS.txt "$base/SHA256SUMS.txt"
sha256sum -c SHA256SUMS.txt --ignore-missing
```

The build input must be exactly 63,307,776 bytes with SHA-256
`7a473b485c3a81406098e2806a6a489b88eb10e44da188db86b92e7a37dfa55a`.
It is **not** the deployable ServOS ISO.

## 3. Inspect, test and build

```sh
mkdir servos-source
cd servos-source
unzip -q ../TechE-ServOS-13.7-v1.0-SOURCE.zip
python3 qa/frame_contract_test.py
python3 qa/screen_walkthrough.py
python3 qa/message_audit.py
sudo sh build-iso.sh \
  "$PWD/../BUILD-INPUT-Pinned-Base-ISO.iso" \
  "$PWD/../servos-rebuilt.iso"
cd ..
sha256sum servos-rebuilt.iso
```

The official ISO SHA-256 is
`b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`.
Different tool versions or archive metadata can change an independently
rebuilt image's bytes; a changed hash identifies a new build and requires its
own boot and install QA. Do not present a rebuilt image as the official
signed or accepted TechE binary. The published ISO is currently identified by
SHA-256; no release signature is claimed.

The public source ZIP contains the complete installer source, build script,
simulation and screen checks, feature/policy text and a dated TechE source
license. Debian target packages are downloaded from configured repositories
while installing on the destination. The builder also downloads pinned
components; the build log records those checks. See [legal notices](LEGAL.md)
for upstream licensing.
