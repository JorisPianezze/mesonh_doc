.. _nam_diag_flaken:

NAM_DIAG_FLAKEn
---------------

.. csv-table:: NAM_DIAG_FLAKEn content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LWATER_PROFILE", "LOGICAL", "F"
   "XZWAT_PROFILE", "REAL", ""
   "LSEDIM_PROFILE", "LOGICAL", "F"
   "XZSED_PROFILE", "REAL", ""
   "LFLKFLUX", "LOGICAL", "F"
   "LFLKWATER", "LOGICAL", "F"

* :code:`LWATER_PROFILE` : flag to save in the output file miscelleaneous fields. The diagnostic is temperature at the depths defined by:

* :code:`XZWAT _PROFILE` : depth of output levels (m) in namelist

* :code:`LSEDIM_PROFILE` : flag for sediment diagnostics

* :code:`XZSED_PROFILE` : depth of output levels (m) in namelist

* :code:`LFLKFLUX` : flag for heat and radiative diagnostics

* :code:`LFLKWATER` : flag for water budget P-E diagnostics

