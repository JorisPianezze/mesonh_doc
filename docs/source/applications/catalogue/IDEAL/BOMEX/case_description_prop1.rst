Shallow cumulus convection (BOMEX) (2)
=============================================================

Case description
----------------

The BOMEX (BOundary Layer EXperiment) case simulates shallow cumulus
convection over tropical ocean and is commonly used to evaluate shallow
convection parameterizations and LES configurations.

Configuration
-------------

.. list-table::
   :header-rows: 1
   :widths: 35 25 40

   * - Category
     - Parameter
     - Value

   * - Domain
     - Geometry
     - Cartesian flat domain (1x1)

   * -
     - Horizontal resolution
     - 40 km

   * -
     - Vertical grid
     - 75 levels (0–3000 m)

   * -
     - Vertical spacing
     - 40–300 m stretched grid

   * - Time
     - Integration length
     - 28800 s (8 h)

   * -
     - Time step
     - 120 s

   * - Physics
     - Turbulence
     - TKEL (1D, BL89)

   * -
     - Cloud microphysics
     - ICE3

   * -
     - Shallow convection
     - EDKF

   * -
     - Deep convection
     - NONE

   * -
     - Radiation
     - NONE

   * - Dynamics
     - Coriolis force
     - Enabled

   * -
     - LES diagnostics
     - Enabled

Forcing and surface setup
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 45 25

   * - Parameter
     - Value

   * - Sensible heat flux
     - 9.2 W m\ :sup:`-2`

   * - Latent heat flux
     - 6.16e-5 kg m\ :sup:`-2` s\ :sup:`-1`

   * - Friction velocity
     - 0.28 m s\ :sup:`-1`

   * - Roughness length (Z0)
     - 0.035 m

   * - Large-scale forcing
     - Geostrophic forcing + subsidence above 2600 m

Workflow
--------

.. list-table::
   :header-rows: 1
   :widths: 20 40

   * - Step
     - Script

   * - 001_prep_ideal
     - ``run_prep_ideal_case``

   * - 002_mesonh
     - ``run_mesonh``

Diagnostics and validation
--------------------------

- Mean vertical profiles: THL, RC, U, V
- Turbulent subgrid fluxes
- Cloud fraction evolution
- Boundary-layer height
- LES averages over 18000–21600 s
