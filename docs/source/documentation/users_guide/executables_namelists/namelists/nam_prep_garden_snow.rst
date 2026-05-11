.. _nam_prep_garden_snow:

NAM_PREP_GARDEN_SNOW
--------------------

.. csv-table:: NAM_PREP_GARDEN_SNOW content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CSNOW_GD", "CHARACTER(LEN=3)", "'D95'"
   "NSNOW_LAYER_GD", "INTEGER", "1"
   "CFILE_SNOW_GD", "CHARACTER(LEN=28)", "CFILE_GD in"
   "", "", "NAM_PREP_TEB_GARDEN"
   "CTYPE_SNOW", "CHARACTER(LEN=6)", "CTYPE in"
   "", "", "NAM_PREP_TEB_GARDEN"
   "CFILEPGD_SNOW_GD", "CHARACTER(LEN=28)", "CFILEPGD_GD in"
   "", "", "NAM_PREP_TEB_GARDEN"
   "CTYPEPGD_SNOW", "CHARACTER(LEN=6)", "CTYPEPGD in"
   "", "", "NAM_PREP_TEB_GARDEN"
   "LSNOW_IDEAL_GD", "LOGICAL", "F"
   "XWSNOW_GD", "REAL(20)", "0."
   "XZSNOW_GD", "REAL(20)", "1.E+20"
   "XTSNOW_GD", "REAL(20)", "273.16"
   "XLWCSNOW_GD", "REAL(20)", "0."
   "XRSNOW_GD", "REAL(20)", "300."
   "XASNOW_GD", "REAL", "0.5"

* :code:`CSNOW_GD` : type of snow scheme. Possible snow schemes are:

  * 'D95': Douville et al (1995) snow scheme.
  * '3-L': Boone and Etchevers (2000) three layers snow scheme.
  * 'EBA': Bogatchev and Bazile (2005), Arpege operational snow scheme.
* :code:`NSNOW_LAYER_GD` : number of snow layers

* :code:`CFILE_SNOW_GD` : name of the file used to define the snow profiles. The use of a file or prescribed value of XRSNOW_GD, XTSNOW_GD, XWSNOW_GD and XASNOW_GD has priority on the data in CFILE_SNOW_GD file

* :code:`CTYPE_SNOW` : type of the CFILE_SNOW_GD file, if the latter is provided. CTYPE_SNOW must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "GRIB ": the file type is a GRIB file, coming from any of these models:
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": Arome french forecast local model
    * "MOCAGE": Mocage french research chemistry model
  * "LFI ": LFI PREP file
  * "ASCII": ASCII PREP FILE
* :code:`CFILEPGD_SNOW_GD` : name of the associated PGD file if CFILE_SNOW_GD is a PREP files.

* :code:`CTYPEPGD_SNOW` : type of the CFILEPGD_SNOW file, if the latter is provided. CTYPEPGD_SNOW must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "LFI ": LFI PREP file
  * "ASCII": ASCII PREP FILE
* :code:`LSNOW_IDEAL_GD` : if LSNOW_IDEAL_GD = F , only one value can be given for following snow parameters and a vertical interpolation is processed. If LSNOW_IDEAL_GD = T, values are given for each layer and there is no vertical interpolation performed.

* :code:`XWSNOW_GD` : uniform value to initialize snow content, one for each layer (kg/m$^{2}$)

* :code:`XZSNOW_GD` : uniform value to initialize snow depth, one for each layer (m) (alternative to XWSNOW_GD)

* :code:`XTSNOW_GD` : uniform value to initialize snow temperature, one for each layer (K)

* :code:`XLWCSNOW_GD` : uniform value to initialize liquid snow water contents, one for each layer (kg/m$^{3}$)

* :code:`XRSNOW_GD` : uniform value to initialize snow density, one for each layer (kg/m$^{3}$)

* :code:`XASNOW_GD` : uniform value to initialize snow albedo (-)

