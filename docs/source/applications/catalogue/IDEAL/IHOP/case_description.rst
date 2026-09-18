IHOP
=====

Case description
----------------
The case referred to as IHOP focuses on the growing convective boundary layer over land, highlighting the complex links between advection, convective activity and moisture heterogeneity in the boundary layer. It is based on an idealisation of the measurements made during the International H20 Project (IHOP_2002) field experiment that took place over the Southern Great Plains (SGP) in May-June 2002. The case study selected here focuses on the growing CBL documented in the vicinity of Homestead, Oklahoma, 14 June 2002. The conditions during this day were optimal to focus on the growing convective boundary layer: very few clouds, weak winds in the CBL as well as aloft (i.e. small wind-shear across the CBL top). Numerous and various observations (soundings, aircraft data, lidar data, and surface-flux measurements) wer used both to design the LES initial and boundary conditions as well as to validate the LES ability to reproduce the development of the CBL in the late morning and early afternoon. More details are given in Couvreux et al (2005)

Configuration
----------------
.. csv-table::
   :header: Parameter, 1D, 3D
   :widths: 30, 30, 30

   Horizontal grid spacing, 1000 m (1x1), 50 m (256x256)
   Vertical levels, 90, 90
   Advection, -, CEN4TH
   Integration length, 50400 s , 43200 s
   Time step, 60 s, 1 s
   Turbulence, TKEL-BL89 (1D), TKEL-DEAR (3D)
   Cloud scheme, REVE, NONE
   Radiation, NONE, NONE
   Shallow convection, EDKF, NONE
   Deep convection, NONE, NONE

Namelist: url: https://src.koda.cnrs.fr/mesonh/mesonh-code/-/tree/MNH-master/examples/integration_cases/hpc/IHOP

Declination
----------
.. csv-table::
   :header: Configuration, Description
   :widths: 30, 30

   IHOP/1D, Single column with 1D turbulence
   IHOP/3D, Large-eddy simulation with 3D turbulence

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_case_xyz
   002_mesonh, run_mesonh

Specificities
----------------
**Scientific specificities**

- Moist convective boundary layer
- Large-scale forcing from IHOP campaign
- Geostrophic forcing with vertical motion
- Shallow convection (EDKF for 1D)

**Technical specificities**

- 1D: single column
- 3D: 256x256 horizontal grid (12.8km x 12.8km)
- 90 vertical levels
- Cyclic boundary conditions for 3D
- High vertical resolution near surface
- Surface flux forced with NAM_IDEAL_FLUX
- Conditional sampling (NAM_COND_SAMP)

Validation
----------------
- Boundary layer height evolution
- Heat and moisture budgets
- Cloud fraction
- Vertical velocity profiles

Numerical ressources
----------------
.. csv-table::
   :header: Configuration, Ressources
   :widths: 30, 30

   IHOP/1D, 1 core
   IHOP/3D, 2560 cores

References
----------------
- Couvreux, F., F. Guichard, J.-L. Redelsperger, C. Kiemle, V. Masson, J.-P. Lafore and C. Flamant, 2005: Assessment of water vapour variability within a convective boundary layer over land using Large Eddy Simulations and IHOP observations. Quarterly Journal of the Royal Meteorological Society, 131(611), 2665-2693
