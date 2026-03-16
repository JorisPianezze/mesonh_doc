Developer's guide
=============================================================================

Meso-NH is build upon many contribution since 30 years. As the code is growing and shared with increasing models and contributors, a number of coding norms must be followed.

.. contents::
   :local:
   :depth: 2

Coding best practices
*****************************************************************************

General
-----------------------------------------------------------------------------

These guidelines apply mostly to every FORTRAN sources in src/ MNH, SURFEX, PHYEX, ACLIB, LIB.

**File structure:**

* Check if the function you code is already coded

* Avoid CONTAINS routines, create a new fortran routine file

* For new file, keep the common structure with an updated statements for the LICENCE and documentation

**Code ergonomy:**

* Maximum 132 characters per line, use &

* Code in CAPITAL characters

* Comments in lower-case characters

* No blank line, use !

* Remove debugging PRINTs and WRITE before committing

* Comment your code !

**Clean code:**

* Remove debugging PRINTs and WRITE before committing

* Remove unused local variables

* Remove unused dummy variables

* Remove unused module variables (USE MODD ...)

* Select the variables used: USE MODD TOTO, ONLY : MYVAR

**Variables:**

* Variables names must be consistent through subroutines (a variable must be easily found with grep)

* All variables must be declared, use IMPLICIT NONE

* Allocatables must be deallocated

* Pointer must be initialized by NULL()

**Reproductibility:**

* Use the parallelizaded version of basic functions (functions ended by ll such as MAX_ll or SUM3D_ll)

* Avoid anticipated exit of a loop with EXIT, CYCLE, RETURN statements

Variables names
-----------------------------------------------------------------------------

 Variables first letter(s) must follow the DOCTOR norm:

.. csv-table:: Norm DOCTOR
   :header: "Type/Status", "INTEGER", "REAL", "LOGICAL", "CHARACTER", "TYPE"
   :widths: 30, 30, 30, 30, 30, 30
   
   "Global", "N", "X", "L (not LP)", "C", "T (not TP, TS, TZ)"
   "Dummy argument", "K", "P", "O (not PP)", "H", "TP"
   "Local", "I", "Z (not IS)", "G (not GS, ZS)", "Y (not YS, YP)", "TZ"   
   "Loop control", "J (not JP)", "/", "/", "/", "/"


Extra rules for PHYEX
-----------------------------------------------------------------------------

The externalized atmospheric physics PHYEX has extra rules in order to comply with all the models using PHYEX (AROME, HARMONIE-AROME, etc). These rules are more strict in order to transform automatically the code for GPU applications.
The general idea behind these rules is that all the physics can be run with arrays written in one physical dimension (the vertical axis). The fortran raw code is written in 2D or 3D in a way that automatic functions (e.g. written in python) can read the fortran code and transform it to another fortran code that can be run on any type of GPUs. The previous general rules applies to PHYEX.

The following extra rules apply on PHYEX/ :

**Variables:**

* Do not use allocatables

* Dimensions of dummy argument arrays must be explicit : no (:,:), use the structure D%

* No variables from modules can be imported except variables declared with the PARAMETER attribute. Put the variable in a type received by the subroutine interface

* Use loop index JIJ for computation on horizontal dimensions

* Use loop index JL on KSIZE microphysics computation point

* Horizontal dimensions arrays are packed into one dimension : instead of A(D%NIT, D%NJT, D%NKT), use A(D%NIJT, D%NKT) where D%NIT, D%NJT, D%NKT are physical dimensions in x, y, z directions and D%NIJT = D%NIT*D%NJT

**Subroutines:**

* Do not use functions returning arrays, use subroutines

* Avoid CONTAINS subroutines, if really needed, the local arrays of the subroutines must have different names than the hosting subroutine or than other contained subroutines Statements

* All calculation on arrays must show explicit dimensions. Instead of A = B + C, write : A(:,:) = B(:,:) + C(:,:) even for initialization

* Do not use nested WHERE, convert it to DO...IF...

* Temporary Do not use ANY, COUNT functions on arrays of horizontal dimensions

* Temporary no (:) on TYPE%VAR

* Compilation keys must be avoided. If really needed, the statements betwen ifdef and else must not split a statement

Extra rules for ACLIB
-----------------------------------------------------------------------------

ACLIB is shared with other models. Specific rules must be followed:

* Use explicit dimensions in variable declaration

* Do not add Méso-NH specific modules/variables into ACLIB, but add variables through the interfaces instead. 
  If a new specific module is needed, make sure that this module is Méso-NH agnostic (not dependent of other Méso-NH specific modules that would be incompatible with other host models)

* Use dedicated ACLIB custom types as it is implemented (e.g. use CST_ACLIB for constants and not MODD_CST from MesoNH world)

* Internal routines in :file:`src/ACLIB` must be agnostic from parallelization as much as possible to ease future use of cross-codes in different host models.


How to contribute to the code ?
*****************************************************************************

Meso-NH packs VX-X-X are divided into two categories :

* major release-pack: X and Y of VX-Y (e.g. 5.4, 5.5, 5.6, etc)

* bugfix release-pack: Z of VX-Y-Z (e.g. 5.4.1, 6.0.1)

A call of contribution is done for a major release-pack. For bugfixes only, you can contribute anytime.

Clone the git repository
-----------------------------------------------------------------------------

Contributions are merged into the official branches via the `official repository <https://src.koda.cnrs.fr/mesonh/mesonh-code>`_. Follow the instructions to clone the repository :ref:`here <git>`. Then:

* If you have a JANUS account (CNRS), log in and create a fork of the repository. Code in your own branch.

* If you **do not** have a JANUS account, contact us (mesonhsupport  .at.  utoulouse.fr) and we will send you a token to be able to create a personal branch in the official repository.

Once your developpement is ready, create a merge-request.

Major release-pack
-----------------------------------------------------------------------------

A major release contains several scientific and technical changes and numerous bugfixes. The time frequency of a major release is about one over 12 to 18 months depending on the amount of contributors. In the case of a major release-pack, please follow these guidelines :

* Merge the master's branch into your work before sharing your branch with :code:`git pull`. Resolve conflits if any and test the compilation.

* **New feature**: you must share at least **one new test case** related to your work **with python3 plots** showing the interesting variables related to your new work.

* **Major modification** of a current part of the code: you must share at least one new test case with python3 plots showing the interests variables related to your new work and to have tested your branch on 2 other cases that is impacted by your development (see the :ref:`cases_catalogue`)

* Provide a contribution to the user's guide (this website) and scientific guide.

Bugfix release-pack
-----------------------------------------------------------------------------

A bugfix release contains a sufficient number of minor bugfixes to justify a new release, or a hot bugfix that may impact a large number of users. The time frequency of bugfix can vary to a few days up to 12 months depending on the stability of the current pack release (usually a few months). Please follow these guidelines:

* Merge your branch on the last version of the master's branch with :code:`git pull`. Resolve conflits if any and test the compilation.

* only commits with bugfixes are asked. If your bugfixes are in a developpement branch, create a bugfix-branch and cherry-picks only bugfix commits.

.. warning::

   Contributions of branches with major developments would be declined and postponed to the next call of contributions for a major release.
