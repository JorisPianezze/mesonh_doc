ARM Cumulus
===========

Case description
----------------
The case referred to as ARMCU focuses on the diurnal cycle of shallow cumulus over land. It is based on an idealisation of the measurements at the Atmospheric Radiation Measurement (ARM) program Southern Great Plains (SGP) site made on 21 June 1997. It has been used in the large‐eddy simulation intercomparison study of Brown et al. (2002) and in the single column model intercomparison study of Lenderink et al. (2004).

Configuration
----------------
.. csv-table::
   :header: Parameter, 1D (ARMCU_1D_CONDSAMP), 3D (ARMCU_LES)
   :widths: 30, 30, 30

   Horizontal grid spacing, 40000 m (1x1), 500 m (64x64)
   Integration length, 54000 s (15 hours), 43200 s (12 hours)
   Time step, 100 s, 2 s
   Turbulence, TKEL (1D), TKEL (3D)
   Cloud scheme, ICE3, ICE3
   Shallow convection, EDKF, NONE
   Deep convection, NONE, NONE
   Radiation, NONE, NONE

Namelist, 3D: https://src.koda.cnrs.fr/mesonh/mesonh-code/-/tree/MNH-master/examples/integration_cases/hpc/ARMCU_LES

Namelist, 1D: https://src.koda.cnrs.fr/mesonh/mesonh-code/-/tree/MNH-master/examples/integration_cases/local/ARMCU_1D_CONDSAMP

Declination
----------
.. csv-table::
   :header: Configuration, Turbulence
   :widths: 30, 30, 30

   ARMCU_1D_CONDSAMP, TKEL (BL89)
   ARMCU_LES/HM21, TKEL (HM21)
   ARMCU_LES/DEAR, TKEL (DEAR)

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

- Cumulus clouds
- Idealized forcing using time-varying surface fluxes (heat, moisture, momentum)

**Technical specificities**

- Cyclic boundary conditions for 3D
- Test of HM21 mixing length in a LES context
- Conditional sampling (CONDSAMP) enabled
- LES diagnostics with time-averaging from 3600s to 43200s (12h daytime period)


Validation
----------------
- Vertical profiles of mean quantities: MEAN_RC, MEAN_RR, MEAN_U, MEAN_V, MEAN_W, MEAN_THL
- Subgrid flux profiles: SBG_WTHL, SBG_WRT
- Total water and mass flux: MEAN_RT, MEAN_MF
- Cloud fraction validation at different levels

Numerical ressources
----------------
.. csv-table::
   :header: Configuration, Ressources
   :widths: 30, 30

   FIRE_1D, 1 core
   FIRE (3D), 128 cores

References
----------------
- Atmospheric Radiation Measurement (ARM) user facility. 1996, updated hourly. Infrared Thermometer (IRT10M). 1996-04-16 to 2021-05-27, Southern Great Plains (SGP) Central Facility, Lamont, OK (C1). Compiled by V. Morris and J. Howie. ARM Data Center. Data set accessed 2021-05-29 at http://dx.doi.org/10.5439/1025203.

- Brown, A. R., R. T. Cederwall, A. Chlond, P. G. Duynkerke, J. C. Golaz, M. Khairoutdinov, D. C. Lewellen, A. P. Lock, M. K. MacVean, C. H. Moeng, R. A. J. Neggers, A. P. Siebesma, and B. Stevens, 2002: Large-eddy simulation of the diurnal cycle of shallow cumulus convection over land. Quarterly Journal of the Royal Meteorological Society, 128(582), 1075–1093, link.

- Lenderink, G., A. P. Siebesma, S. Cheinet, S. Irons, C. G. Jones, P. Marquet, F. Müller, D. Olmeda, J. Calvo, E. Sanchez, and P. M. M. Soares. The diurnal cycle of shallow cumulus clouds over land, 2004: A single-column model intercomparison study. Quarterly Journal of the Royal Meteorological Society, 130(604), 3339–3364, link.