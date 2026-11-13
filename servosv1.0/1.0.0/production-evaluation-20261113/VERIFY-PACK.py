#!/usr/bin/env python3
"""Independently check the extracted ServOS evidence pack with Python 3."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
EXPECTED_ISO = "b449436c0575a0dd95d61a3a228b0cbe465f415b64dea392352b1da2c04556cf"
ISO_NAME = "TechE-ServOS-13.7-v1.0-amd64-network.iso"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


manifest = json.loads((ROOT / "pack-manifest.json").read_text(encoding="utf-8"))
expected = {item["path"]: item for item in manifest["files"]}
if len(expected) != len(manifest["files"]):
    fail("duplicate manifest path")
checksum_lines = (ROOT / "SHA256SUMS-pack.txt").read_text(encoding="utf-8").splitlines()
checksums = {}
for line in checksum_lines:
    if "  " not in line:
        fail("malformed pack checksum line")
    digest, name = line.split("  ", 1)
    if name in checksums:
        fail(f"duplicate checksum path: {name}")
    checksums[name] = digest
if set(checksums) != set(expected) | {"pack-manifest.json"}:
    fail("checksum list differs from manifest plus its own file")
actual = {path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*") if path.is_file()}
if actual != set(expected) | {"pack-manifest.json", "SHA256SUMS-pack.txt"}:
    fail("undeclared or missing pack file")
for name, item in expected.items():
    path = (ROOT / name).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        fail(f"missing or unsafe file: {name}")
    if path.stat().st_size != item["bytes"] or sha256(path) != item["sha256"]:
        fail(f"manifest mismatch: {name}")
for name, digest in checksums.items():
    if sha256(ROOT / name) != digest:
        fail(f"checksum mismatch: {name}")

iso = ROOT / "assets" / ISO_NAME
if iso.stat().st_size != 71696384 or sha256(iso) != EXPECTED_ISO:
    fail("original ISO mismatch")
transport = ROOT / "assets" / "TechE-ServOS-13.7-v1.0-amd64-network.one-file.zip"
with ZipFile(transport) as archive:
    entries = archive.infolist()
    if len(entries) != 1 or entries[0].filename != ISO_NAME or entries[0].is_dir():
        fail("transport ZIP must contain exactly one root-level original ISO")
    if archive.testzip() is not None:
        fail("transport ZIP CRC mismatch")
    h = hashlib.sha256()
    with archive.open(entries[0]) as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    if h.hexdigest() != EXPECTED_ISO:
        fail("transport member differs from original ISO")

print(f"PASS: {len(expected)} manifest files, {len(checksums)} checksum entries, exact ISO and one-file transport ZIP")
