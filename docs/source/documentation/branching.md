# Branch Management Strategy

*Version 1.0 — 2026-05-22*


## 1. General principles

> **Note for end users:** this document targets developers who work directly with Git
> branches. Users who wish to modify the source code for their own simulations without
> contributing back to the repository could use the `make user` mechanism, which provides
> an isolated working copy without requiring Git knowledge. A documented pathway from
> `make user` to a proper Git branch exists for modifications that mature into shareable
> contributions.

* `MNH-master` **accepts direct pushes for minor changes.** Substantial changes go through a Merge Request (MR). See section 8 for the distinction.

* **Release branches are protected against direct writes.** Any change must go through an MR or a cherry-pick/merge from a validated commit (from master or another release branch).

* **Every temporary branch is associated with a GitLab issue.** The issue is mandatory whenever a branch is created — the issue number is part of the branch name. The only exception is trivial fixes applied directly on `MNH-master` without a dedicated branch.

* **Temporary branches are deleted after merge.** They have a limited lifespan and do not accumulate. GitLab can handle this automatically via the "Delete source branch" option in the MR, which is recommended. Otherwise the developer or the maintainer who performs the merge is responsible for deleting the branch.

* **The stability of `MNH-master` is ensured by collective discipline**, not by strict technical protection. The basic rule: if a direct push risks breaking the build for everyone, open an MR.

* **A compilation check is automatically run on all branches** at every push and before any merge. More advanced CI policies (non-regression tests, validation) are defined in a dedicated document.

***

## 2. Permanent branches

### `MNH-master`

The main branch and the sole convergence point for all developments. It must always be in a compilable and functional state. It is recommended (but not mandatory) to branch off `MNH-master` when creating all temporary branches, except for bugs specific to a release branch.

**Rules:**

* Direct push allowed for minor changes (see section 8).

* Substantial changes go through an MR.

* Each release is marked by a tag (see section 7).

### Release branches `MNH-X-Y`

A release branch is created at each minor version release (X.Y.0). It is maintained in parallel with `MNH-master` for a minimum of **2 years** after the release of the next minor version, to receive bug fixes only.

**Naming:** `MNH-X-Y` (e.g. `MNH-6-0`, `MNH-6-1`)

> Dots are replaced by hyphens to avoid ambiguities in shell and Git tools.

**Rules:**

* Direct push forbidden — any change goes through an MR or a cherry-pick.

* Only bug fixes may be integrated, never new features.

* Note: a performance optimisation may be considered a bug fix if it does not modify simulation results and the changes remain minor; otherwise it is a new development and must be integrated into `MNH-master` for the next minor version.

* Fixes applied to a release branch are ported to `MNH-master` and other release branches if necessary (see section 6).

**Lifecycle:**

```text
Release of Meso-NH 6.1.0
  → creation of tag PACK-MNH-V6-1-0
  → creation of branch MNH-6-1
  → 2-year support starting from the release of version 6.2.0 (bug fixes only)
  → at the end of the support period: archiving (branch set read-only for everyone,
    including maintainers, via Settings → Repository → Protected branches)
```

***

## 3. Temporary branches

There are only **two types** of temporary branches: `dev` and `bug`. The presence or absence of a version number in the name immediately indicates the target branch.

### Development branches — `MNH-dev-{issue}-{title}`

For any new feature, refactoring, performance improvement, or any substantial code change.

**Recommended starting point:** `MNH-master`. It is possible to start from a release tag (e.g. `PACK-MNH-V6-1-0`) if the developer prefers a validated and immutable starting point. In that case, the final merge into `MNH-master` will require integrating all commits made on master since that tag — the longer the branch has lived, the harder this becomes. Regardless of the origin, **regular resynchronisation with `MNH-master`** (rebase or merge) is strongly recommended to limit drift.

**Merged into:** `MNH-master` via MR

**Examples:**

```text
MNH-dev-42-turb-new-feature
MNH-dev-67-output-hdf5-12
MNH-dev-103-new-machine
```

### Bug branches on master — `MNH-bug-{issue}-{title}`

For fixing a bug present on `MNH-master` (and possibly also present on release branches).

**Created from:** free starting point (`MNH-master` (recommended), tag, or release as needed)\
**Merged into:** `MNH-master` via MR or direct push if the fix is trivial\
**Then ported to:** the affected release branches via cherry-pick (if a single commit) or merge (if multiple interdependent commits). Squashing commits at merge time is recommended to simplify porting.

**Examples:**

```text
MNH-bug-89-crash-restart-mpi
MNH-bug-94-wrong-pressure-output
```

### Bug branches on release — `MNH-X-Y-bug-{issue}-{title}`

For fixing a bug present on one or more release branches, but absent from `MNH-master`.

**Important note:** if the bug also affects `MNH-master`, refer to the previous section (no version number in the branch name).

**Created from:** the affected release branch (e.g. `MNH-6-0`)\
**Merged into:** that same release branch via MR\
**Then ported to:** the affected release branches via cherry-pick (if a single commit) or merge (if multiple interdependent commits). Squashing commits at merge time is recommended to simplify porting.

**Examples:**

```text
MNH-6-0-bug-112-bad-cherry-pick-radiation
MNH-6-1-bug-118-segfault-nested-domain
```

> The version number in the name is **mandatory** in this case: it immediately signals that the branch does not target `MNH-master` and avoids any confusion when running `git branch -a`.

***

## 4. Naming convention — summary

| Type             | Pattern                       | Example                           |
| ---------------- | ----------------------------- | --------------------------------- |
| Main branch      | `MNH-master`                  | `MNH-master`                      |
| Release branch   | `MNH-X-Y`                     | `MNH-6-0`                         |
| Development      | `MNH-dev-{issue}-{title}`     | `MNH-dev-42-turbulence-tke`       |
| Bug on master    | `MNH-bug-{issue}-{title}`     | `MNH-bug-89-crash-restart-mpi`    |
| Bug on release   | `MNH-X-Y-bug-{issue}-{title}` | `MNH-6-0-bug-112-bad-cherry-pick` |

**Format rules:**

* Separator: hyphen `-` only (no dots, no underscores).

* Short title: 2 to 4 words, lowercase, separated by hyphens.

* The issue number is **mandatory** for all temporary branches.

* No special characters, no spaces.

**Immediate reading of a branch name:**

* Starts with `MNH-dev-` → development, targets master.

* Starts with `MNH-bug-` → bug fix, targets master.

* Starts with `MNH-X-Y-bug-` → bug fix, targets release X.Y only.

***

## 5. Development workflow

```text
1. Open a GitLab issue describing the feature or improvement.
   → A dedicated issue template for development is not yet available at the time
     of publication of this document.
2. Create a branch MNH-dev-{issue}-{title} from MNH-master (or a release tag).
3. Develop, commit regularly with clear messages.
4. Open a Merge Request into MNH-master.
   → Mention "Closes #N" in the description to close the issue automatically.
   → Consider using the "Squash commits" option to produce a single clean commit,
     which simplifies the history on MNH-master.
5. If possible, review by at least one other developer.
6. Green CI + approved review → merge into MNH-master.
7. Delete the temporary branch.
```

***

## 6. Bug fix workflow

The starting point is free — what determines the naming is the destination, i.e. whether `MNH-master` is affected by the bug or not.

### Case 1 — Bug present on `MNH-master` and on release branches

This is the most common case.

```text
1. Open an issue using the bug report template (bug_report), identify the affected versions (e.g. master, 6.0.5, 6.1.0).
2. Create MNH-bug-{issue}-{title} from MNH-master, a tag, or an affected release.
3. Fix the bug.
   → If working directly on MNH-master (no bug branch): direct push if trivial, MR otherwise.
   → If working on a bug branch: MR into MNH-master (direct push not applicable).
4. Port the fix to all affected branches (MNH-master if needed, MNH-6-1, MNH-6-0…)
   via cherry-pick (single commit) or merge (multiple interdependent commits).
   This is the responsibility of the developer who fixed the bug.
5. Document the fixed versions in the issue before closing it.
```

> GitLab provides a "Cherry-pick" button directly on the merged commit,
> making the porting straightforward and error-free.
> If the bug branch contains several commits, it is recommended to squash them
> when merging (into `MNH-master` or into a release branch) using the GitLab
> "Squash commits" option, to simplify subsequent porting to other branches.
> If squashing is not desirable, a direct merge is preferable to multiple individual cherry-picks.

***

### Case 2 — Bug present on `MNH-master` only

Recent regression, not yet present in any release.

```text
1. If the bug is trivial, apply the fix directly on MNH-master (no issue or branch needed).
2. Otherwise, open an issue and create MNH-bug-{issue}-{title} from MNH-master.
   → No version number in the branch name (master-only bug).
3. Fix the bug, MR or direct push depending on complexity.
4. No cherry-pick needed.
```

***

### Case 3 — Bug present only on one or more release branches

Regression introduced by a cherry-pick, bug in code already removed from master…

```text
1. Open an issue using the bug report template (bug_report), confirm that master is not affected.
2. Create MNH-X-Y-bug-{issue}-{title} from any affected release branch.
3. Fix the bug, MR into that release branch.
4. Port the fix to other affected releases if needed,
   via cherry-pick (single commit) or merge (multiple interdependent commits).
   This is the responsibility of the developer who fixed the bug.
5. Document in the issue.
```

### Decision table

| Bug present on                          | Starting point                        | Branch name                   | Propagation                                    |
| --------------------------------------- | ------------------------------------- | ----------------------------- | ---------------------------------------------- |
| master + releases                       | `MNH-master`, a tag, or a release     | `MNH-bug-{issue}-{title}`     | Cherry-pick or merge to all affected branches           |
| master only                             | `MNH-master` or a recent tag          | `MNH-bug-{issue}-{title}`     | None                                           |
| one or more releases, not master        | any affected release branch           | `MNH-X-Y-bug-{issue}-{title}` | Cherry-pick or merge to all affected releases         |

***

### Backport tracking in issues

Each bug issue must explicitly mention:

* The affected versions.

* The fixed versions as cherry-picks or merge are applied.

**GitLab labels** should list the Meso-NH version numbers affected by the bug.

***

## 7. Tags and version numbering

The numbering follows the **X.Y.Z** scheme:

* **X**: major version (incompatible changes, deep refactoring).

* **Y**: minor version (new features, backward compatibility intended but not guaranteed).

* **Z**: bug fix (fixes only, no new features).

### Applying tags

| Event                                                  | Tag                                                                      | Tagged branch         |
| ------------------------------------------------------ | ------------------------------------------------------------------------ | --------------------- |
| Minor version release                                  | `PACK-MNH-V6-1-0`                                                        | `MNH-master`          |
| Bug fix on release                                     | `PACK-MNH-V6-1-1`                                                        | `MNH-6-1`             |
| Intermediate versions (i.e. preparing a new release)  | `PACK-MNH-VX-Y--Z-rc01 (2 hyphens between Y and Z for alphanumeric sort)` | MNH-master or MNH-X-Y |

***

## 8. Branch protection rules

### `MNH-master` — relaxed protection

Direct push is allowed for minor changes. The practical rule:

| Direct push acceptable                        | Merge Request mandatory                      |
| --------------------------------------------- | -------------------------------------------- |
| Typo fix, comment                             | New feature                                  |
| Trivial fix (a few lines, obvious)            | Refactoring                                  |
|                                               | Changes to interfaces or namelists           |
|                                               | Non-trivial bug fix                          |

**Basic rule: when in doubt, open an MR.**

### Release branches `MNH-X-Y` — strict protection

Direct push forbidden. Any change goes through an MR or a cherry-pick/merge from a commit already validated (on master or on another release branch). This strictness is justified by the long lifespan of these branches and their users' dependency on them.

### Recommended GitLab configuration

To be configured in `Settings → Repository → Protected branches`:

| Branch            | Direct push | Who can push | Merge                  |
| ----------------- | ----------- | ------------ | ---------------------- |
| `MNH-master`      | Allowed     | Developers   | All / Maintainers      |
| `MNH-X-Y` (explicit, e.g. MNH-6-1) — active support | Forbidden | — | Maintainers only |
| `MNH-X-Y` (explicit, e.g. MNH-6-0) — archived | Forbidden | — | No one |

When a release branch reaches the end of its support period, update its protection rule to revoke merge rights from maintainers. This effectively makes the branch fully read-only for everyone.

Release branches must be added **explicitly** by name, one by one, when created. A wildcard pattern cannot reliably distinguish `MNH-6-0` (release) from `MNH-6-0-bug-test` (bug branch on release), which must remain unprotected. Temporary branches (`MNH-dev-*`, `MNH-bug-*`, `MNH-X-Y-bug-*`) require no protection.

Every MR into a release branch must satisfy:

* Green CI (compilation at minimum).

* At least one approved review (ideally).

* No unresolved conflicts.

### Continuous integration policy

A compilation check is the minimum CI requirement and applies to **all branches** without exception. It is the basic safety net that ensures no push silently breaks the build for the rest of the team.

More advanced testing levels — non-regression tests, physical validation — are not yet fully defined. The intended direction is a three-level funnel:

| Level | Content | Trigger | Branches |
| ----- | ------- | ------- | -------- |
| 1 — Compilation | Build with standard gfortran | Every push | All |
| 2 — Quick tests | Short test cases, basic numerical non-regression | MR open/update | `MNH-dev-*`, `MNH-bug-*`, `MNH-X-Y-bug-*` |
| 3 — Full validation | Complete reference test cases, multiple compilers | Manual or merge on master/release | `MNH-master`, `MNH-X-Y` |

The detailed CI policy will be described in a dedicated document when finalised.

> [!note]
> At the time of publication of this document, the CI pipeline was not yet in place.

***

## 9. Schematic overview

### Developments

```{mermaid}
%%{init: { 'theme': 'base', 'gitGraph': {'mainBranchName': 'MNH-master', 'parallelCommits': true, 'showCommitLabel': true}} }%%
gitGraph
   commit
   commit id: "PACK-MNH-V6-1-0" tag: "PACK-MNH-V6-1-0"
   branch MNH-dev-42
   checkout MNH-dev-42
   commit id: "dev-42a"
   commit id: "dev-42b"
   checkout MNH-master
   commit
   commit
   branch MNH-dev-67
   checkout MNH-dev-67
   commit id: "dev-67a"
   commit id: "resync master"
   commit id: "dev-67b"
   checkout MNH-master
   merge MNH-dev-42
   merge MNH-dev-67
   commit
```

### Bug fix — from `MNH-master`

Bug present on master, MNH-6-0 and MNH-6-1.

```{mermaid}
%%{init: { 'theme': 'base', 'gitGraph': {'mainBranchName': 'MNH-master', 'parallelCommits': true, 'showCommitLabel': true}} }%%
gitGraph
   commit
   branch MNH-6-0
   checkout MNH-6-0
   commit
   checkout MNH-master
   commit
   branch MNH-6-1
   checkout MNH-6-1
   commit
   checkout MNH-master
   commit
   branch MNH-bug-89
   checkout MNH-bug-89
   commit id: "fix bug #89"
   checkout MNH-master
   merge MNH-bug-89
   checkout MNH-6-1
   commit id: "cherry-pick fix #89 for 6-1"
   checkout MNH-6-0
   commit id: "cherry-pick fix #89 for 6-0"
```

### Bug fix — from a release branch

Bug present on master, MNH-6-0 and MNH-6-1, fix made from MNH-6-1.

```{mermaid}
%%{init: { 'theme': 'base', 'gitGraph': {'mainBranchName': 'MNH-master', 'parallelCommits': true, 'showCommitLabel': true}} }%%
gitGraph
   commit
   branch MNH-6-0
   checkout MNH-6-0
   commit
   checkout MNH-master
   commit
   branch MNH-6-1
   checkout MNH-6-1
   commit
   branch MNH-bug-89
   checkout MNH-bug-89
   commit
   commit id: "fix bug #89"
   checkout MNH-6-1
   merge MNH-bug-89
   checkout MNH-master
   commit id: "cherry-pick fix #89 for master"
   checkout MNH-6-0
   commit id: "cherry-pick fix #89 for 6-0"
```

### Bug fix — specific to a release branch

Bug present only on MNH-6-0.

```{mermaid}
%%{init: { 'theme': 'base', 'gitGraph': {'mainBranchName': 'MNH-master', 'parallelCommits': true, 'showCommitLabel': true}} }%%
gitGraph
   commit
   branch MNH-6-0
   checkout MNH-6-0
   commit
   branch MNH-6-0-bug-112
   checkout MNH-6-0-bug-112
   commit id: "fix bug #112"
   checkout MNH-6-0
   merge MNH-6-0-bug-112
   checkout MNH-master
   commit
```
