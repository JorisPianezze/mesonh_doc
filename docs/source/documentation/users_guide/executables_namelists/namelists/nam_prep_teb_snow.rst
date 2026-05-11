.. _nam_prep_teb_snow:

NAM_PREP_TEB_SNOW
-----------------

.. csv-table:: NAM_PREP_TEB_SNOW content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CSNOW_ROOF", "CHARACTER(LEN=6)", "'1-L'"
   "CSNOW_ROAD", "CHARACTER(LEN=6)", "'1-L'"
   "CFILE_SNOW_TEB", "CHARACTER(LEN=28)", "''"
   "CTYPE_SNOW", "CHARACTER(LEN=6)", "''"
   "", "", ""
   "CFILEPGD_SNOW_TEB", "CHARACTER(LEN=28)", "''"
   "CTYPEPGD_SNOW", "CHARACTER(LEN=6)", "''"
   "XWSNOW_ROOF", "REAL", "none"
   "XWSNOW_ROAD", "REAL", "none"
   "XTSNOW_ROOF", "REAL", "none"
   "XTSNOW_ROAD", "REAL", "none"
   "XLWCSNOW_ROOF", "REAL", "none"
   "XLWCSNOW_ROAD", "REAL", "none"
   "XASNOW_ROOF", "REAL", "none"
   "XASNOW_ROAD", "REAL", "none"
   "XRSNOW_ROOF", "REAL", "none"
   "XRSNOW_ROAD", "REAL", "none"
   "LSNOW_IDEAL_TEB", "LOGICAL", "F"

* :code:`CSNOW_ROAD` : snow scheme used over roads

* :code:`CSNOW_ROOF` : snow scheme used over roofs

* :code:`CFILE_SNOW_TEB` : name of the file used to define the snow profiles. The use of a file or prescribed value of XRSNOW_ROOF/ROAD, XTSNOW_ROOF/ROAD, XWSNOW_ROOF/ROAD and XASNOW_ROOF/ROAD has priority on the data in CFILE_SNOW_TEB file

* :code:`CTYPE_SNOW` : type of the CFILE_SNOW_TEB file, if the latter is provided. CTYPE_SNOW must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "GRIB ": the file type is a GRIB file, coming from any of these models:
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": Arome french forecast local model
    * "MOCAGE": Mocage french research chemistry model
  * "LFI ": LFI PREP file
  * "ASCII": ASCII PREP FILE
* :code:`CFILEPGD_SNOW_TEB` : name of the associated PGD file if CFILE_SNOW_TEB is a PREP files.

* :code:`CTYPEPGD_SNOW` : type of the CFILEPGD_SNOW

* :code:`XWSNOW_ROAD` : snow reservoir for roads (kg/m$^{2}$)

* :code:`XWSNOW_ROOF` : snow reservoir for roofs (kg/m$^{2}$)

* :code:`XTSNOW_ROAD` : snow temperature for roads (K)

* :code:`XTSNOW_ROOF` : snow temperature for roofs (k)

* :code:`XLWCSNOW_ROAD` : snow liquid water content for roads (kg/m$^{3}$)

* :code:`XLWCSNOW_ROOF` : snow liquid water content for roofs (kg/m$^{3}$)

* :code:`XRSNOW_ROOF` : snow density for roofs (kg/m$^{3}$)

* :code:`XRSNOW_ROAD` : snow density for roads (kg/m$^{3}$)

* :code:`XASNOW_ROAD` : snow albedo for roads (-)

* :code:`XASNOW_ROOF` : snow albedo for roofs (-)

* :code:`LSNOW_IDEAL_TEB` : if LSNOW_IDEAL_TEB = F , only one value can be given for following snow parameters and a vertical interpolation is processed. If LSNOW_IDEAL_TEB = T, values are given for each layer and there is no vertical interpolation performed.

