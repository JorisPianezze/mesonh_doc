.. _nam_sfx_lake_cpl:

NAM_SFX_LAKE_CPL
----------------------------------------------------------------------------- 

.. warning::

   This namelist comes from SURFEX code.

.. csv-table:: NAM_SFX_LAKE_CPL content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XTSTEP_CPL_LAKE", "REAL", "-1.0"
   "CLAKE_EVAP", "CHAR(LEN=8)", ""
   "CLAKE_RAIN", "CHAR(LEN=8)", ""
   "CLAKE_SNOW", "CHAR(LEN=8)", ""
   "CLAKE_WATF", "CHAR(LEN=8)", ""

* :code:`XTSTEP_CPL_LAKE`: Coupling time step for lake

* :code:`CLAKE_EVAP`: Evaporation over lake area

* :code:`CLAKE_RAIN`: Rainfall over lake area

* :code:`CLAKE_SNOW`: Snowfall over lake area

* :code:`CLAKE_WATF`: Net freshwater flux
