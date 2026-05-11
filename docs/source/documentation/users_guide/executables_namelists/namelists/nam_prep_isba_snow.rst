.. _nam_prep_isba_snow:

NAM_PREP_ISBA_SNOW
------------------

.. csv-table:: NAM_PREP_ISBA_SNOW content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CSNOW", "CHARACTER(LEN=3)", "'D95'"
   "", "", ""
   "NSNOW_LAYER", "INTEGER", "1"
   "CFILE_SNOW", "CHARACTER(LEN=28)", "CFILE_ISBA in"
   "", "", "NAM_PREP_ISBA"
   "CTYPE_SNOW", "CHARACTER(LEN=6)", "CTYPE in"
   "", "", "NAM_PREP_ISBA"
   "CFILEPGD_SNOW", "CHARACTER(LEN=28)", "CFILEPGD_ISBA in"
   "", "", "NAM_PREP_ISBA"
   "CTYPEPGD_SNOW", "CHARACTER(LEN=6)", "CTYPEPGD in"
   "", "", "NAM_PREP_ISBA"
   "LSNOW_IDEAL", "LOGICAL", "F"
   "LSNOW_FRAC_TOT", "LOGICAL", "F"
   "LSNOW_PREP_PERM", "LOGICAL", "T"
   "XWSNOW", "REAL(20)", "0."
   "XZSNOW", "REAL(20)", "1.E+20"
   "XTSNOW", "REAL(20)", "273.16"
   "XLWCSNOW", "REAL(20)", "0."
   "XRSNOW", "REAL(20)", "300."
   "XASNOW", "REAL", "0.5"
   "XSG1SNOW", "REAL(20)", "none"
   "XSG2SNOW", "REAL(20)", "none"
   "XHISTSNOW", "REAL(20)", "none"
   "XAGESNOW", "REAL(20)", "none"
   "LSWEMAX", "LOGICAL", "F"
   "XSWEMAX", "REAL", "500."
   "NIMPUR", "INTEGER", "0"

* :code:`CSNOW` : type of snow scheme. Possible snow schemes are:

  * 'D95': Douville et al (1995) snow scheme.
  * '3-L': Boone and Etchevers (2001); Decharme et al. (2016) N-layer (default 12) snow scheme
  * 'EBA': Bogatchev and Bazile (2005), Arpege operational snow scheme.
  * 'CRO': Crocus model
* :code:`NSNOW_LAYER` : number of snow layers

* :code:`CFILE_SNOW` : name of the file used to define the snow profiles. The use of a file or prescribed value of XRSNOW, XTSNOW, XWSNOW and XASNOW (and XSG1SNOW, XSG2SNOW, XHISTSNOW and XAGESNOW in case of CSNOW = CROCUS) has priority on the data in CFILE_SNOW file

* :code:`CTYPE_SNOW` : type of the CFILE_SNOW file, if the latter is provided. CTYPE_SNOW must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "GRIB ": the file type is a GRIB file, coming from any of these models:
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": AROME french forecast local model
    * "MOCAGE": Mocage french research chemistry model
  * "LFI ": LFI PREP file
  * "ASCII": ASCII PREP FILE
* :code:`CFILEPGD_SNOW` : name of the associated PGD file if CFILE_SNOW is a PREP files.

* :code:`CTYPEPGD_SNOW` : type of the CFILEPGD_SNOW file, if the latter is provided. CTYPEPGD_SNOW must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "LFI ": LFI PREP file
  * "ASCII": ASCII PREP FILE
* :code:`LSNOW_IDEAL` : if LSNOW_IDEAL = F , only one value can be given for following snow parameters and a vertical interpolation is processed. If LSNOW_IDEAL = T, values are given for each layer and there is no vertical interpolation performed.

* :code:`LSNOW_FRAC_TOT` : if LSNOW_FRAC_TOT = T, the total snow fraction XPSN = MIN(1.0, ZSNOWSWE(:)/XWCRN_EXPL) where ZSNOWSWE is the snow liquid water content, and XWCRN_EXPL is the critical value of the equivalent water content of the snow reservoir.

* :code:`LSNOW_PREP_PERM` : activates or disactivates initialization over permanent ice areas.

* :code:`XWSNOW` : uniform value to initialize snow content, one for each layer

* :code:`XZSNOW` : depth of snow layers (m). Alternative to XWSNOW.

* :code:`XTSNOW` : uniform value to initialize snow temperature, one for each layer

* :code:`XLWCSNOW` : snow liquid water content (kg/m3)

* :code:`XRSNOW` : uniform value to initialize snow density, one for each layer

* :code:`XASNOW` : uniform value to initialize snow albedo

* :code:`XSG1SNOW` : uniform value to initialize snow layers grain feature 1 for Crocus, one for each layer

* :code:`XSG2SNOW` : uniform value to initialize snow layers grain feature 2 for Crocus, one for each layer

* :code:`XHISTSNOW` : uniform value to initialize snow layer grain historical parameter for Crocus, one for each layer

* :code:`XAGESNOW` : uniform value to initialize snow grain age for Crocus, one for each layer

* :code:`LSWEMAX` : logical switch to set an upper limit on initial snow water equivalent

* :code:`XSWEMAX` : upper limit of initial snow water equivalent

* :code:`NIMPUR` : number of impurity you want to use in your simulation. NIMPUR=1 with black carbon only and NIMPUR=2 with black carbon and dust (to run a simulation with dust only you can set NIMPUR=2 and prescribe no black carbon deposition)

