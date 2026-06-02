Moist convective boundary layer (IHOP)
============================================================

Case description
----------------

The International H2O Project (IHOP) case simulates a moist convective boundary layer based on the IHOP_2002 field campaign :cite:t:`weckwerth_overview_2004`.
This case is used to evaluate boundary layer parameterizations under realistic large-scale forcing conditions, including
geostrophic wind and large-scale vertical motion. It exists in two configurations: a 1D single-column mode and a 3D Large Eddy Simulation.

.. warning::

   The 3D configuration requires MPI parallelization and the 1D configuration can only be run on a single core.

.. note::

   You can find the workflow as well as the namelists and the scripts to launch this case here :

   .. treeview::

      - :dir:`folder` |MNH_directory_extract_current|/examples/integration_cases/hpc/IHOP

        - :dir:`folder` 1D : directory to prepare and run the 1D configuration
        - :dir:`folder` 3D : directory to prepare and run the 3D configuration
        - :dir:`folder` PYTHON : directory to plot the figure

   The different steps must be performed in the order indicated by the directory numbers.

Numerical set-up
----------------

.. tab-set::

   .. tab-item:: Grids

      .. list-table::
         :header-rows: 1
         :widths: 40 30 30

         * - Parameter
           - 1D
           - 3D

         * - Domain
           - Cartesian flat domain
           - Cartesian flat domain

         * - Horizontal grid
           - 1 x 1 pt (1D)
           - 256 x 256 pt

         * - Horizontal resolution
           - 1000 m
           - 50 m

         * - Vertical levels
           - 90
           - 90

   .. tab-item:: Dynamics

      .. list-table::
         :header-rows: 1
         :widths: 40 30 30

         * - Parameter
           - 1D
           - 3D

         * - Integration length
           - 43200 s (12 h)
           - 43200 s (12 h)

         * - Time step
           - 60 s
           - 1 s

         * - Coriolis force
           - Enabled
           - Enabled

         * - Lateral boundary condition
           - Cyclic
           - Cyclic

   .. tab-item:: Physics

      .. list-table::
         :header-rows: 1
         :widths: 40 30 30

         * - Scheme
           - 1D
           - 3D

         * - Turbulence
           - TKEL (1D, BL89)
           - TKEL (3D)

         * - Cloud microphysics
           - LIMA
           - LIMA

         * - Shallow convection
           - EDKF
           - NONE

         * - Deep convection
           - NONE
           - NONE

         * - Radiation
           - NONE
           - NONE

   .. tab-item:: Forcings

      .. list-table::
         :header-rows: 1
         :widths: 50 50

         * - Parameter
           - Value

         * - Large-scale forcing
           - Geostrophic forcing + large-scale vertical motion

   .. tab-item:: Diagnostics

      .. list-table::
         :header-rows: 1
         :widths: 50 50

         * - Parameter
           - Value

         * - LES diagnostics
           - Enabled

Validation
----------------
- Boundary layer height evolution
- Heat and moisture budgets
- Cloud fraction
- Vertical velocity profiles
