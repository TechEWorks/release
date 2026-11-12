# D09 — public scripts fetch diagnosis for exact candidate 582e026

**Observed result: FAIL, exit 65.** On disposable VM276, freshly installed and cold booted from ISO SHA-256 `9269b7641117b963986a4c6f5e157a41486fc84c5283fe8cf4fc96180617c097`, `sudo /usr/bin/teche get scriptsv1.0` installed Git, cloned `https://github.com/TechEWorks/release.git`, printed `Public scripts failed verification.`, and returned 65. No active scripts revision was installed. This is the D09 result in the [rapid 19-gate report](01%20Rapid%2019-gate%20smoke.md).

## Verified cause at the time of the test

The installed bootstrap points to `https://github.com/TechEWorks/release.git`, sparse-checks out `scriptsv1.0`, and requires `VERSION`, `SHA256SUMS.txt`, executable `bin/teche`, `bootstrap/teche`, complete file hashes, and shell syntax before activation. The publicly advertised `main` ref was `0ad70601d0a67b8fa5f48d3a6e77e2d05f6323a0`; `git ls-tree -r --name-only origin/main -- scriptsv1.0` returned no paths. Thus the required directory is absent on public main, which is sufficient to explain the verification failure. The bootstrap's generic error does not identify a more specific failed predicate.

The staged public [release PR #4](https://github.com/TechEWorks/release/pull/4) has head `8f293f45eb3affe435973810c9d58fbb4752330e` and contains nine `scriptsv1.0/` files, including a manifest and `VERSION` `1.0.8-qa`. It is **not published on main**. Its cumulative diff also includes unrelated product files; merging that entire PR solely to clear this ServOS gate would change more than the scripts path. The editable [scripts source PR #1](https://github.com/TechEWorks/scriptsv1.0/pull/1) head is `0e3ba8ba54198d8303d3cff75a5fefa32224fd36`, also unmerged. Source fixture results do not replace a public installed-client pull.

## Required repair and retest

1. Review the exact scripts runtime and its manifest against the scripts client policy and ServOS scripts-only scope. Establish an approved public `release/scriptsv1.0/` revision with no unrelated public-repo changes in the promotion diff.
2. Verify the published public main tree, manifest, executable modes and unauthenticated clone. Record the 40-character public commit and SHA-256 values.
3. On **the same exact ISO** installed in disposable VM276, rerun `sudo /usr/bin/teche get scriptsv1.0`, `teche ver`, help, aliases, update, tamper rejection and previous-revision retention. Record the result and installed revision. A public scripts change alone does not change the ISO bytes, but D09 stays FAIL until this live retest passes.
4. Keep final release approval open until full QA, rights, independent review, Business receiving and public artifact readback pass. Do not convert this diagnosis into a D09 PASS.
