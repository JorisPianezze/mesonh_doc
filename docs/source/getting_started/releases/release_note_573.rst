.. _release_note_573:

MNH-V5-7-3
============================================================================

Release date : 04/05/2026

.. note::
   
   We fully encourage all users of 5-7-2 to move to 5-7-3.
   As this release includes only bug fixes, the results should be exactly the same as 5-7-2 (except for possible corrections), but with more stability and reliability.

Aircraft
**********************************
* ini_aircraft: ensure that first trajectory time is 0. (time since launch)
* treat case of aircraft initially outside of physical domain 
* ini_aircraft: set NMODEL=1 automatically if only 1 domain (does not need to set it explicitely in namelist anymore)

IBM
**********************************
* fix for IBM_GOTO_MODEL 
* IBM_INTERPOS: bugfix: use XXHTAM and XYHATM instead of MXF(XXHAT) and MYF(XYHAT) that introduce bad values near boundaries
* rewrite of IBM_LOCATCORN: fix for vertically non-regular grids + optimizations + safeguards

SURFEX
**********************************
* READ_SURFX2COV_MNH / READ_SURFX2COV_1COV_MNH: bugfix: force GCOVER_PACKED to FALSE if not found in file (instead of having an unpredictible value)
* WRITE_SURFX2_MNH: do not write emission fields (no real meaning in backup files + problem with last dimension which is the number of instants and not the vertical levels
* rewrite temporal_dists to handle dates < 1990 + simplify the algo using the 1st March deviation
* fix when using TEB and sea coupling

Outputs & Backups
**********************************
* minor fix for outputs: XOUT_TIME_FREQ_FIRST(s,m)=0. now allows output at start (instead of being ignored)
* budgets: correct condition to write vertical coordinates if MASK
* reduce NBULISTMAXLEN to 128 to workaround limitation of gfortran compiler for size of character strings in namelists

Others
**********************************
* fix when using export VER_CDF=CDFPERSO
* fix for LFILTERING in NAM_HURR_CONF
* increase compilation timelimit for compilation to 1h30 on HPC
* set_perturb: remove MPPDB_CHECK of XTHM (no more meaning + crash in some cases)
* fix: pass XSVT and not XSVT(:,:,:,1) to MEAN_FIELD to prevent crash in DEBUG mode if NSV=1
* fix when using coupling with oceanic currents + refactoring
* fix: XACPRR used before allocation (when using old electricity scheme, fix issue #52)
