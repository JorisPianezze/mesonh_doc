.. _nam_sfx_wave_cpl:

NAM_SFX_WAVE_CPL
----------------------------------------------------------------------------- 

.. warning::

   This namelist comes from SURFEX code.

.. csv-table:: NAM_SFX_WAVE_CPL content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XTSTEP_CPL_WAVE", "REAL", "-1.0"
   "CWAVE_U10", "CHAR(LEN=8)", ""
   "CWAVE_V10", "CHAR(LEN=8)", ""
   "CWAVE_CHA", "CHAR(LEN=8)", ""
   "CWAVE_UCU", "CHAR(LEN=8)", ""
   "CWAVE_VCU", "CHAR(LEN=8)", ""
   "CWAVE_HS", "CHAR(LEN=8)", ""
   "CWAVE_TP", "CHAR(LEN=8)", ""

* :code:`XTSTEP_CPL_WAVE`: Coupling time step for waves

* :code:`CWAVE_U10`: zonal component of the wind at 10 meters

* :code:`CWAVE_V10`: meridian component of the wind at 10 meters

* :code:`CWAVE_CHA`: Charnock coefficient

* :code:`CWAVE_UCU`: zonal surface current (from wave model)

* :code:`CWAVE_VCU`: meridian surface current (from wave model)

* :code:`CWAVE_HS`: significant height

* :code:`CWAVE_TP`: peak period
