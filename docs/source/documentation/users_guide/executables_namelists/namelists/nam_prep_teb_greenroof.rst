.. _nam_prep_teb_greenroof:

NAM_PREP_TEB_GREENROOF
----------------------

.. csv-table:: NAM_PREP_TEB_GREENROOF content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "XHUG_SURF_GR", "REAL", "none"
   "XHUG_ROOT_GR", "REAL", "none"
   "XHUG_DEEP_GR", "REAL", "none"
   "XHUGI_SURF_GR", "REAL", "none"
   "XHUGI_ROOT_GR", "REAL", "none"
   "XHUGI_DEEP_GR", "REAL", "none"
   "CFILE_HUG_SURF_GR", "CHARACTER(LEN=28)", "CFILE_HUG_GR"
   "", "", "in this namelist"
   "CFILE_HUG_ROOT_GR", "CHARACTER(LEN=28)", "CFILE_HUG_GR"
   "", "", "in this namelist"
   "CFILE_HUG_DEEP_GR", "CHARACTER(LEN=28)", "CFILE_HUG_GR"
   "", "", "in this namelist"
   "CFILE_HUG_GR", "CHARACTER(LEN=28)", "CFILE_GR"
   "", "", "in this namelist"
   "CTYPE_HUG", "CHARACTER(LEN=6)", "CTYPE"
   "", "", "in this namelist"
   "", "", ""
   "XTG_SURF_GR", "REAL", "none"
   "XTG_ROOT_GR", "REAL", "none"
   "XTG_DEEP_GR", "REAL", "none"
   "CFILE_TG_SURF_GR", "CHARACTER(LEN=28)", "CFILE_TG_GR"
   "", "", "in this namelist"
   "CFILE_TG_ROOT_GR", "CHARACTER(LEN=28)", "CFILE_TG_GR"
   "", "", "in this namelist"
   "CFILE_TG_DEEP_GR", "CHARACTER(LEN=28)", "CFILE_TG_GR"
   "", "", "in this namelist"
   "CFILE_TG_GR", "CHARACTER(LEN=28)", "CFILE_GR"
   "", "", "in this namelist"
   "CTYPE_TG", "CHARACTER(LEN=6)", "CTYPE"
   "", "", "in this namelist"
   "", "", "in this namelist"
   "CFILE_GR", "CHARACTER(LEN=28)", "CFILE in"
   "", "", "NAM_PREP_SURF_ATM"
   "CTYPE", "CHARACTER(LEN=6)", "CFILETYPE in"
   "", "", "NAM_PREP_SURF_ATM"
   "CFILEPGD_GR", "CHARACTER(LEN=28)", "CFILEPGD in"
   "", "", "NAM_PREP_SURF_ATM"
   "CTYPEPGD", "CHARACTER(LEN=6)", "CFILEPGDTYPE in"
   "", "", "NAM_PREP_SURF_ATM"

* :code:`XHUG_SURF_GR` : uniform prescribed value of liquid soil water index (SWI) for the surface soil layer. This prescribed value, if defined, has priority on the use of CFILE_HUG_GR and CFILE_GR data.

* :code:`XHUG_ROOT_GR` : uniform prescribed value of liquid soil water index (SWI) for the root zone soil layer(s). This prescribed value, if defined, has priority on the use of CFILE_HUG_GR and CFILE_GR data.

* :code:`XHUG_DEEP_GR` : uniform prescribed value of liquid soil water index (SWI) for the deep soil layer(s). This prescribed value, if defined, has priority on the use of CFILE_HUG_GR and CFILE_GR data.

* :code:`XHUGI_SURF_GR` : uniform prescribed value of ice soil water index (SWI) for the surface soil layer. This prescribed value, if defined, has priority on the use of CFILE_HUG_GR and CFILE_GR data.

* :code:`XHUGI_ROOT_GR` : uniform prescribed value of ice soil water index (SWI) for the root zone soil layer(s). This prescribed value, if defined, has priority on the use of CFILE_HUG_GR and CFILE_GR data.

* :code:`XHUGI_DEEP_GR` : uniform prescribed value of ice soil water index (SWI) for the deep soil layer(s). This prescribed value, if defined, has priority on the use of CFILE_HUG_GR and CFILE_GR data.

* :code:`CFILE_HUG_SURF_GR` : name of the file used to define the liquid soil water index (SWI) for the surface soil layer.

* :code:`CFILE_HUG_ROOT_GR` : name of the file used to define the liquid soil water index (SWI) for the root zone soil layer(s).

* :code:`CFILE_HUG_DEEP_GR` : name of the file used to define the liquid soil water index (SWI) for the deep soil layer(s).

* :code:`CFILE_HUG_GR` : name of the file used to define the soil water profiles.\\

* :code:`CTYPE_HUG` : type of the CFILE_HUG_GR file, if the latter is provided. CTYPE_HUG must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "GRIB ": the file type is a GRIB file, coming from any of these models:
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": Arome french forecast local model
    * "MOCAGE": Mocage french research chemistry model
  * "ASCII / LFI ": PREP file from Surfex
  * "ASCLLV": ASCII latlonval file (one file for each depth)
* :code:`XTG_SURF_GR` : uniform prescribed value of temperature for the surface soil layer, supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_TG_GR and CFILE_GR data.

* :code:`XTG_ROOT_GR` : uniform prescribed value of temperature for the root zone soil layer(s), supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_TG_GR and CFILE_GR data.

* :code:`XTG_DEEP_GR` : uniform prescribed value of temperature for the deep soil layer(s), supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_TG_GR and CFILE_GR data.

* :code:`CFILE_TG_SURF_GR` : name of the file used to define the surface soil temperature profile.

* :code:`CFILE_TG_ROOT_GR` : name of the file used to define the root zone soil temperature profile.

* :code:`CFILE_TG_DEEP_GR` : name of the file used to define the deep soil temperature profile.

* :code:`CFILE_TG_GR` : name of the file used to define the soil temperature profile.\\

* :code:`CTYPE_TG` : type of the CFILE_TG_GR file, if the latter is provided. CTYPE_TG must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "GRIB ": the file type is a GRIB file, coming from any of these models:
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": Arome french forecast local model
    * "MOCAGE": Mocage french research chemistry model
  * "ASCII / LFI ": PREP file from Surfex
  * "ASCLLV": ASCII latlonval file (one file for each depth)
* :code:`CFILE_GR / CFILEPGD_GR` : name of the PREP / PGD files used to define any GARDEN variable. The use of a file or prescribed value XHUG_SURF_GR, XHUG_ROOT_GR, XHUG_DEEP_GR, XTG_SURF_GR, XTG_ROOT_GR, XTG_DEEP_GR, CFILE_WG_GR and CFILE_TG_GR has priority on the data in CFILE_GR file.

* :code:`CTYPE / CTYPEPGD` : type of the CFILE_GR / CFILEPGD_GR files, if the latter is provided. CTYPE / CTYPEPGD must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "GRIB ": the file type is a GRIB file, coming from any of these models:
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": Arome french forecast local model
    * "MOCAGE": Mocage french research chemistry model
  * "ASCII ": PREP/PGD Surfex ASCII file
  * "LFI ": PREP/PGD Surfex LFI file
