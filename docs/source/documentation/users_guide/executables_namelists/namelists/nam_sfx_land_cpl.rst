.. _nam_sfx_land_cpl:

NAM_SFX_LAND_CPL
----------------------------------------------------------------------------- 

.. warning::

   This namelist comes from SURFEX code.

.. csv-table:: NAM_SFX_LAND_CPL content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XTSTEP_CPL_LAND", "REAL", "-1.0"
   "XFLOOD_LIM", "REAL", "0.01"
   "CRUNOFF", "CHAR(LEN=8)", ""
   "CDRAIN", "CHAR(LEN=8)", ""
   "CCALVING", "CHAR(LEN=8)", ""
   "CWTD", "CHAR(LEN=8)", ""
   "CFWTD", "CHAR(LEN=8)", ""
   "CFFLOOD", "CHAR(LEN=8)", ""
   "CPIFLOOD", "CHAR(LEN=8)", ""
   "CSRCFLOOD", "CHAR(LEN=8)", ""
   "CDOCFLUX", "CHAR(LEN=8)", ""
   "CTWS", "CHAR(LEN=8)", ""

* :code:`XTSTEP_CPL_LAND`: Coupling time step for land

* :code:`XFLOOD_LIM`: threshold above which no flood for very small flooded area (default 1%)

* :code:`CRUNOFF`: Name of Surface runoff variable from SFX to TRIP

* :code:`CDRAIN`: Name of Deep drainage variable from SFX to TRIP

* :code:`CCALVING`: Name of Calving flux variable from SFX to TRIP

* :code:`CWTD`: water table depth from SFX to TRIP

* :code:`CFWTD`: grid-cell fraction of water table rise from SFX to TRIP

* :code:`CFFLOOD`: Name of Floodplains recipitation interception variable from SFX to TRIP

* :code:`CPIFLOOD`: Flood potential infiltration from SFX to TRIP

* :code:`CSRCFLOOD`: Floodplains freshwater flux froM SFX to TRIP

* :code:`CDOCFLUX`: coupling DOC flux when LCLEACH = T (in NAM_ISBA_CCn)

* :code:`CTWS`: coupling variable that allow to compute the Terrestrial Water Storage (TWS) that is the sum of all water over continent in each grid-cell (water on leaf, snow and soil moisture from ISBA, and lakes, inundations, aquifers from CTRIP).
