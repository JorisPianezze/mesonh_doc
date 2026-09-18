FIRE Stratocumulus
=================

Case description
----------------
The case referred to as FIRE/REF was developed along the European Project on Cloud Systems in Climate Models (EUROCS) to study the diurnal cycle of stratocumulus. The case is based on observations collected in July 1987 during the First International Satellite Cloud Climatology Project (ISCCP) Regional Experiment (FIRE), off the coast of California, more specifically during the FIRE-I observing period (see Duynkerke et al. 2004 and reference therein for details).

Configuration
----------------
.. csv-table::
   :header: Parameter, 1D (FIRE_1D), 3D (FIRE)
   :widths: 30, 30, 30

   Category, Idealized cases, HPC cases
   Horizontal grid spacing, 2500 m (1x1), 50 m (50x50)
   Integration length, 90000 s (25 hours), 90000 s (25 hours)
   Time step, 120 s, 1 s
   Turbulence, TKEL (1D), TKEL (3D)
   Shallow convection, EDKF, NONE
   Cloud scheme, KHKO, KHKO
   Deep convection, NONE, NONE
   Radiation, ECMWF, ECMW
   LES diagnostics, enabled, enabled

Namelist: 1D: https://src.koda.cnrs.fr/mesonh/mesonh-code/-/tree/MNH-master/examples/integration_cases/local/FIRE_1D

3D: https://src.koda.cnrs.fr/mesonh/mesonh-code/-/tree/MNH-master/examples/integration_cases/hpc/FIRE

Declination
----------
.. csv-table::
   :header: Configuration, Cloud scheme, Radiation
   :widths: 30, 30, 30

   FIRE_1D/KHKO, KHKO, ECMWF
   FIRE_1D/KHKO_MALA, KHKO, MALA
   FIRE_1D/LIMA_ECRAD, LIMA, ECRAD
   FIRE_1D/LIMA_MALA, LIMA, MALA
   FIRE/CEN4TH_RKC4, KHKO, ECMW
   FIRE/CEN4TH_LEFR, KHKO, ECMW
   FIRE/CEN4TH_RKC4_LIMA_ECRAD, LIMA, ECRAD
   FIRE/WENO5, KHKO, ECMW

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_case_xyz / run_prep_ideal
   002_mesonh, run_mesonh_xyz / run_mesonh

Specificities
----------------
**Scientific specificities**

- Marine stratocumulus layer with cloud-top radiative cooling
- Sea surface temperature: 289 K prescribed
- Geostrophic forcing with vertical motion
- in LES, several advection scheme (WENO5, CEN4TH+RKC4 or CEN4TH+LEFR)
- radiation: different LW and SW optical properties; ECMWF vs ECRAD
- microphysics: KHKO vs LIMA

**Technical specificities**

- 1D: single point domain with 120 vertical levels
- 3D: 50x50 horizontal grid (2.5km x 2.5km domain)
- Initial perturbation (0.1 m/s vertical for 3D)
- CSEA="SEAFLX" with prescribed SST XSST_UNIF
- NAM_LES and diagnostics used and plots

Validation
----------------
- Cloud fraction evolution
- Liquid water path
- Radiative fluxes
- Turbulent fluxes

Numerical ressources
----------------
.. csv-table::
   :header: Configuration, Ressources
   :widths: 30, 30

   FIRE_1D, 1 core
   FIRE (3D), 256 cores

References
----------------
- Chlond, A., F. Muller and I. Sednev, 2004: Numerical simulation of the diurnal cycle of marine stratocumulus during FIRE - An LES and SCM modelling study. Quarterly Journal of the Royal Meteorological Society, 130(604), pp. 3297-3321, link.

- Duynkerke, P. G., S. R. de Roode, M. C. van Zanten, J. Calvo, J. Cuxart, S. Cheinet, A. Chlond, H. Grenier, P. J. Jonker, M. Köhler, G. Lenderink, D. Lewellen, C.-L. Lappen, A. P. Lock, C.-H. Moeng, F. Müller, D. Olmeda, J.-M. Piriou, E. Sanchez and I. Sednev, 2004: Observations and numerical simulations of the diurnal cycle of the EUROCS stratocumulus case. Quarterly Journal of the Royal Meteorological Society, 130(604), pp. 3269-3296, link.