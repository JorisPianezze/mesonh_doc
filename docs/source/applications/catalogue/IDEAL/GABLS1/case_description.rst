Stable nocturnal boundary layer (GABLS1)
=========================================

Case description
----------------
The GABLS1 (GEWEX Atmospheric Boundary Layer Study) case simulates a stable boundary layer over Arctic land during winter. This case tests the model ability to reproduce nocturnal boundary layer turbulence and low-level jets.

.. warning::

   The 3D configuration requires MPI parallelization and the 1D configuration can only be run on a single core.

Configuration
----------------
.. csv-table::
   :header: Parameter, 1D, 3D
   :widths: 30, 30, 30

   Horizontal grid spacing, 2 m (1x1), 2 m (100x100)
   Integration length, 9 hours, 9 hours
   Time step, 10 s, 0.2 s
   Turbulence, TKEL (1D), TKEL (3D)
   Shallow convection, NONE, NONE
   Cloud scheme, NONE, NONE
   Radiation, NONE, NONE

Namelist: https://src.koda.cnrs.fr/mesonh/mesonh-code/-/tree/MNH-master/examples/integration_cases/hpc/GABLS1


Declination
-------------
.. csv-table::
   :header: Configuration, Turbulence
   :widths: 30, 30

   GABLS1/1D/BL89, 1D-TKEL (BL89)
   GABLS1/1D/RM17, 1D-TKEL (RM17)
   GABLS1/3D, 3D-TKEL (DEAR)

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_case
   002_mesonh, run_mesonh

Specificities
----------------
**Scientific specificities**

- Stable boundary layer (Arctic location)
- Weak surface temperature cooling (-0.25 K for first 8 hours)
- Geostrophic forcing (8 m/s)
- Low-level jet development
- Very high vertical resolution (2m near surface, stretching to 6m)
- 155 vertical levels

**Technical specificities**

- 1D: single point domain
- 3D: 100x100 horizontal grid with DEAR length scale
- ISBA surface scheme with prescribed surface temperature and rugosity z0 (NAM_DATA_TSZ0)

Validation
----------------
- Turbulent heat flux profiles
- Temperature evolution
- Wind profile (low-level jet)
- Boundary layer height

Numerical ressources
----------------
.. csv-table::
   :header: Configuration, Ressources
   :widths: 30, 30

   GABLS1_1D, 1 core
   GABLS1 (3D), 256 cores

References
----------------
- Beare, R. J., & Macvean, M. K. (2004). Resolution sensitivity and scaling of large-eddy simulations of the stable boundary layer. Boundary-layer meteorology, 112(2), 257-281.
- Cuxart, J., Holtslag, A. A., Beare, R. J., Bazile, E., Beljaars, A., Cheng, A., ... & Xu, K. M. (2006). Single-column model intercomparison for a stably stratified atmospheric boundary layer. Boundary-Layer Meteorology, 118(2), 273-303.
