.. _release_note_601:

MNH-V6-0-1
============================================================================

Release date : 10/07/2026

.. warning::
   
   A major bugfix has been corrected for digesting AROME files (init or coupling) with dates >= 15/10/2024 (cy48)


* First integration of automatic tests into CI (08 Jul 2026).
* **RTTOV**: add support for new Intel compilers (08 Jul 2026).
* **IBM**: rewrite of ``IBM_LOCATCORN`` for non‑regular vertical grids, plus optimisations and safeguards (30 Jan 2026).
* **IBM_INTERPOS**: bug‑fix to use ``XXHTAM``/``XYHATM`` instead of ``MXF(XXHAT)``/``MYF(XYHAT)`` (30 Jan 2026).
* **IBM_GOTO_MODEL**: bug‑fix (30 Jan 2026).
* **READ_SURFX2COV_MNH / READ_SURFX2COV_1COV_MNH**: force ``GCOVER_PACKED`` to ``FALSE`` when absent (08 Apr 2026).
* **Elec solver**: manage upper=Neumann / lower=Dirichlet boundary conditions in QLAP for non‑flat electric solver (23 Jun 2026).
* **call_rttov14**: add out‑of‑bounds check (02 Jul 2026).
* **Budget module**: enable ASSE source term only for centred scheme with Leap‑frog (20 May 2026).
* **Budget module**: ensure ``L2D=FALSE`` when ``L1D=TRUE`` (20 May 2026).
* **PREP_REAL_CASE**: fix LB conditions when LIMA variables are initialized by ORILAM (13 May 2026).
* **ini_elecn**: fix use of ``XACPRR`` before allocation (04 May 2026).
* Add ``BRANCHING.md`` to document branch management (22 May 2026).
* Add README for ``pyfortool`` installation with PyInstaller on nuwa/X86_6 & turpan/aarch64 (20 Mar 2026).
* Adapt configuration files for the Datarmor supercomputer (20 Mar 2026).
