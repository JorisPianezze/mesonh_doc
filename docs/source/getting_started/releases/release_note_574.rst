.. _release_note_574:

MNH-V5-7-4
============================================================================

Release date : 11/08/2026

.. note::
   
   We fully encourage all users of 5-7-3 to move to 5-7-4.
   As this release includes only bug fixes, the results should be exactly the same as 5-7-3 (except for possible corrections), but with more stability and reliability.
   This is true in the same environment (especially with the same compiler version and options).

Electricity
**********************************
* Solver Elec bugfix: add management of upper=Neumann / lower=Dirichlet boundary conditions in QLAP for the non-flat electric solver
* ini_elecn: bugfix: XACPRR used before allocation (fix issue #52)

SURFEX
**********************************
* READ_SURFX2COV_MNH / READ_SURFX2COV_1COV_MNH: bugfix: force GCOVER_PACKED to FALSE if not found in file (instead of having an unpredictible value)

RTTOV
**********************************
* call_rttov13: add out-of-bounds check (fix issue #67)

Budgets
**********************************
* budgets: enable ASSE source term only for the centered scheme with Leap-frog (fix issue #58)
* fix INIF/ENDF/AVEF TKE budget units (m2 s-1 -> m2 s-2) (fix issue #71)

Others
**********************************
* fix: ensure that L2D=FALSE if L1D=TRUE (fix issue #57)
* fix: boundaries overwritten for LIMA variables initialized with LORILAM (fix issue #56)
* PREP_REAL_CASE: fix LB conditions not set correctly if LIMA variables are initialized by ORILAM (fix issue #55)
* workaround bug with oneAPI 2025.0 (corrected since 2025.3 and maybe before) (fix issue #54)
* fill_sonfieldn: dummy-array workaround for child domain outside parent domain (fix issue #73)
* fix: ensure IVEC1/IVEC2 is set everywhere with ELSEWHERE in graupel WHERE blocks to prevent Valgrind false positive (fix issue #72)
