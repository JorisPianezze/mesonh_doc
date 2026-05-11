.. _nam_prep_greenroof_snow:

NAM_PREP_GREENROOF_SNOW
-----------------------

.. csv-table:: NAM_PREP_GREENROOF_SNOW content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CSNOW_GR", "CHARACTER(LEN=3)", "'3-L'"
   "NSNOW_LAYER_GR", "INTEGER", "3"
   "CFILE_SNOW_GR", "CHARACTER(LEN=28)", "CFILE_GR in"
   "", "", "{\footnotesize NAM_PREP_TEB_GREENROOF}"
   "CTYPE_SNOW", "CHARACTER(LEN=6)", "CTYPE in"
   "", "", "{\footnotesize NAM_PREP_TEB_GREENROOF}"
   "CFILEPGD_SNOW_GR", "CHARACTER(LEN=28)", "CFILEPGD_GR in"
   "", "", "{\footnotesize NAM_PREP_TEB_GREENROOF}"
   "CTYPEPGD_SNOW", "CHARACTER(LEN=6)", "CTYPEPGD in"
   "", "", "{\footnotesize NAM_PREP_TEB_GREENROOF}"
   "LSNOW_IDEAL_GR", "LOGICAL", "F"
   "XWSNOW_GR", "REAL(20)", "0."
   "XZSNOW_GR", "REAL(20)", "1.E+20"
   "XTSNOW_GR", "REAL(20)", "273.16"
   "XLWCSNOW_GR", "REAL(20)", "0."
   "XRSNOW_GR", "REAL(20)", "300."
   "XASNOW_GR", "REAL", "0.5"

* :code:`CSNOW_GR` : type of snow scheme. Possible snow schemes are:

  * 'D95': Douville et al (1995) snow scheme.
  * '3-L': Boone and Etchevers (2000) three layers snow scheme.
  * 'EBA': Bogatchev and Bazile (2005), Arpege operational snow scheme.
* :code:`NSNOW_LAYER_GR` : number of snow layers

* :code:`CFILE_SNOW_GR` : name of the file used to define the snow profiles. The use of a file or prescribed value of XRSNOW_GR, XTSNOW_GR, XWSNOW_GR and XASNOW_GR has priority on the data in CFILE_SNOW_GR file

* :code:`CTYPE_SNOW` : type of the CFILE_SNOW_GR file, if the latter is provided. CTYPE_SNOW must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "GRIB ": the file type is a GRIB file, coming from any of these models:
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": Arome french forecast local model
    * "MOCAGE": Mocage french research chemistry model
  * "LFI ": LFI PREP file
  * "ASCII": ASCII PREP FILE
* :code:`CFILEPGD_SNOW_GR` : name of the associated PGD file if CFILE_SNOW_GR is a PREP files.

* :code:`CTYPEPGD_SNOW` : type of the CFILEPGD_SNOW file, if the latter is provided. CTYPEPGD_SNOW must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "LFI ": LFI PREP file
  * "ASCII": ASCII PREP FILE
* :code:`LSNOW_IDEAL_GR` : if LSNOW_IDEAL_GR = F , only one value can be given for following snow parameters and a vertical interpolation is processed. If LSNOW_IDEAL_GR = T, values are given for each layer and there is no vertical interpolation performed.

* :code:`XWSNOW_GR` : uniform value to initialize snow content, one for each layer

* :code:`XZSNOW_GR` : uniform value to initialize snow depth, one for each layer (m)

* :code:`XTSNOW_GR` : uniform value to initialize snow temperature, one for each layer

* :code:`XLWCSNOW_GR` : uniform value to initialize snow liquid water content, one for each layer (kg/m3)

* :code:`XRSNOW_GR` : uniform value to initialize snow density, one for each layer

* :code:`XASNOW_GR` : uniform value to initialize snow albedo

