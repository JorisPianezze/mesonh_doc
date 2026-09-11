.. _nam_sfx_sea_cpl:

NAM_SFX_SEA_CPL
----------------------------------------------------------------------------- 

.. warning::

   This namelist comes from SURFEX code.

.. csv-table:: NAM_SFX_SEA_CPL content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XTSTEP_CPL_SEA", "REAL", "-1.0"
   "LWATER", "LOGICAL", ".FALSE."
   "LSEAICE_2FLX", "LOGICAL", ".FALSE."
   "CSEA_FWSU", "CHAR(LEN=8)", ""
   "CSEA_FWSV", "CHAR(LEN=8)", ""
   "CSEA_HEAT", "CHAR(LEN=8)", ""
   "CSEA_SNET", "CHAR(LEN=8)", ""
   "CSEA_WIND", "CHAR(LEN=8)", ""
   "CSEA_EVAP", "CHAR(LEN=8)", ""
   "CSEA_RAIN", "CHAR(LEN=8)", ""
   "CSEA_SNOW", "CHAR(LEN=8)", ""
   "CSEA_WATF", "CHAR(LEN=8)", ""
   "CSEA_PRES", "CHAR(LEN=8)", ""
   "CSEAICE_HEAT", "CHAR(LEN=8)", ""
   "CSEAICE_SNET", "CHAR(LEN=8)", ""
   "CSEAICE_EVAP", "CHAR(LEN=8)", ""
   "CSEA_SST", "CHAR(LEN=8)", ""
   "CSEA_UCU", "CHAR(LEN=8)", ""
   "CSEA_VCU", "CHAR(LEN=8)", ""
   "CSEAICE_SIT", "CHAR(LEN=8)", ""
   "CSEAICE_CVR", "CHAR(LEN=8)", ""
   "CSEAICE_ALB", "CHAR(LEN=8)", ""
   "CSEA_CO2", "CHAR(LEN=8)", ""
   "CSEA_FCO2", "CHAR(LEN=8)", ""

* :code:`XTSTEP_CPL_SEA`: Coupling time step for lake

* :code:`LWATER`: Switch to add water into sea oasis mask

* :code:`LSEAICE_2FLX`: flag to activate a tile scheme to compute fluxes over sea and sea-ice separately

* :code:`CSEA_FWSU`: zonal wind stress

* :code:`CSEA_FWSV`: meridian wind stress

* :code:`CSEA_HEAT`: Non solar net heat flux

* :code:`CSEA_SNET`: Solar net heat flux

* :code:`CSEA_WIND`: module of 10m wind speed

* :code:`CSEA_FWSM`: module of wind stress

* :code:`CSEA_EVAP`: Evaporation

* :code:`CSEA_RAIN`: Rainfall

* :code:`CSEA_SNOW`: Snowfall

* :code:`CSEA_WATF`: Net freshwater flux

* :code:`CSEA_PRES`: Surface pressure over sea

* :code:`CSEAICE_HEAT`: Sea-ice non solar net heat flux

* :code:`CSEAICE_SNET`: Sea-ice solar net heat flux

* :code:`CSEAICE_EVAP`: Sea-ice sublimation

* :code:`CSEA_SST`: Sea surface temperature

* :code:`CSEA_UCU`: Sea u-current stress

* :code:`CSEA_VCU`: Sea v-current stress

* :code:`CSEAICE_SIT`: Sea-ice temperature

* :code:`CSEAICE_CVR`: Sea-ice cover

* :code:`CSEAICE_ALB`: Sea-ice albedo

* :code:`CSEA_CO2`: coupling variable that allow to send cumulated atmospheric CO2 in ppm.s to ocean model

* :code:`CSEA_FCO2`: coupling variable that allow to get CO2 fluxes produces by the oceanic biogeochemistry scheme
