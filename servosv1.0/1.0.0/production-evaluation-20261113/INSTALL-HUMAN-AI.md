# Install and observe ServOS 1.0.0 — human and AI operators

Use the [original numbered installer guide](original-repo/servosv1.0/1.0.0/INSTALL.md) for the on-screen sequence. This sheet binds both operators to the same **unchanged published ISO**, SHA-256 `b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf`, and the same stop conditions. It describes an installation procedure; it is not a fresh QA result.

## 01. Prepare and identify

1. Download the [native ISO](https://github.com/TechEWorks/release/releases/download/servosv1.0-v1.0.0/TechE-ServOS-13.7-v1.0-amd64-network.iso) and compare its actual SHA-256 to the value above. Record the command, observed digest, file size and source URL. Stop on a mismatch.
2. Use a disposable x86-64 UEFI VM for evaluation, or obtain the target owner's approved backup and installation window for a real server. Secure Boot must be off; provide a wired IPv4 route to a reachable Debian mirror, console access, at least 8 GiB for each selected whole disk and at least 2 GiB RAM for ZFS.
3. Record VM/host identity, intended target disk **stable IDs**, model, size and existing partitions. Take a before-state inventory. The installer erases every selected whole disk after typed `ERASE`. Stop if any target identity is uncertain.

## 02. Install

1. Boot `Install TechE ServOS (13.7) v1.0`. Record welcome/legal screen, keyboard choice and network mode. For static networking record the IPv4/prefix, gateway and DNS without publishing secrets or private infrastructure addresses.
2. Review the disk list against the before-state inventory. Select only intended whole disks. An `OS PRESENT` disk requires an extra Space press. Choose a layout with an exact-public-ISO case in the [case matrix](RELEASE-QA-MATRIX.tsv) if this run is intended to reproduce published acceptance. Other offered menus are not proven by their presence.
3. Create a non-root administrator using a password or a **public** SSH key. Never enter or publish a private key. Review the complete network, layout, target disks and account summary. Type `ERASE` only when that reviewed summary exactly matches the intended target.
4. Observe numbered tasks and the live log. Record any failed task and actual error. On completion, remove the ISO or change boot order, cold boot the installed disk and retain the install log. Do not describe a screen as a PASS until the installed target is observed.

## 03. Observe the installed result

Run the read-only commands in [VERIFICATION.md](VERIFICATION.md#safe-first-boot-checks). Capture actual output and exit status for Debian release, root/boot/EFI mounts, storage health, SSH, administrator identity, `teche -v`, and the installer log path. Compare disk IDs, filesystem type, array members and network reachability with the reviewed choices. Record an actual SSH login and sudo/APT observation if those are claimed for this case. A command invocation without its output is not evidence.

**PASS** only when the ISO digest matched, the reviewed target was the only intended disk set, the installer completed, the installed system cold booted from disk, and every case-specific expected result was observed. **FAIL** on a wrong target, failed task, unexpected mount/member, missing boot, failed SSH or mismatched version. **NOT_RUN** when the case was never executed; **BLOCKED** when the test environment prevents a decisive result. Preserve the failed state and logs. Do not change an observed FAIL to PASS by narrowing the wording afterward.

## 04. AI operator record

An AI operator follows sections 01–03 verbatim, with an authorized human controlling any real-disk destructive action. Before each action it states the VM/host, target stable IDs, expected result and stop condition. After each action it records the observed output, exit code, UTC, tester and evidence hash. It may automate a disposable VM; it may not infer completion from a menu, command text or screenshot alone. It stops on an identity mismatch or ambiguous result, and gives the human the original logs and case record for review. Use the [QA matrix](RELEASE-QA-MATRIX.tsv) to assign the case ID and distinguish recorded public-ISO cases from unrun negative/failure/AI cases.
