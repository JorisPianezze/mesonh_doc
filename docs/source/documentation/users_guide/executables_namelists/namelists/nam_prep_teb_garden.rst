.. _nam_prep_teb_garden:

NAM_PREP_TEB_GARDEN
-------------------

.. csv-table:: NAM_PREP_TEB_GARDEN content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "XHUG_SURF_GD", "REAL", "none"
   "XHUG_ROOT_GD", "REAL", "none"
   "XHUG_DEEP_GD", "REAL", "none"
   "XHUGI_SURF_GD", "REAL", "none"
   "XHUGI_ROOT_GD", "REAL", "none"
   "XHUGI_DEEP_GD", "REAL", "none"
   "CFILE_HUG_SURF_GD", "CHARACTER(LEN=28)", "CFILE_HUG_GD"
   "", "", "in this namelist"
   "CFILE_HUG_ROOT_GD", "CHARACTER(LEN=28)", "CFILE_HUG_GD"
   "", "", "in this namelist"
   "CFILE_HUG_DEEP_GD", "CHARACTER(LEN=28)", "CFILE_HUG_GD"
   "", "", "in this namelist"
   "CFILE_HUG_GD", "CHARACTER(LEN=28)", "CFILE_GD"
   "", "", "in this namelist"
   "CTYPE_HUG", "CHARACTER(LEN=6)", "CTYPE"
   "", "", "in this namelist"
   "", "", ""
   "XTG_SURF_GD", "REAL", "none"
   "XTG_ROOT_GD", "REAL", "none"
   "XTG_DEEP_GD", "REAL", "none"
   "CFILE_TG_SURF_GD", "CHARACTER(LEN=28)", "CFILE_TG_GD"
   "", "", "in this namelist"
   "CFILE_TG_ROOT_GD", "CHARACTER(LEN=28)", "CFILE_TG_GD"
   "", "", "in this namelist"
   "CFILE_TG_DEEP_GD", "CHARACTER(LEN=28)", "CFILE_TG_GD"
   "", "", "in this namelist"
   "CFILE_TG_GD", "CHARACTER(LEN=28)", "CFILE_GD"
   "", "", "in this namelist"
   "CTYPE_TG", "CHARACTER(LEN=6)", "CTYPE"
   "", "", "in this namelist"
   "", "", ""
   "CFILE_GD", "CHARACTER(LEN=28)", "CFILE in"
   "", "", "NAM_PREP_SURF_ATM"
   "CTYPE", "CHARACTER(LEN=6)", "CFILETYPE in"
   "", "", "NAM_PREP_SURF_ATM"
   "CFILEPGD_GD", "CHARACTER(LEN=28)", "CFILEPGD in"
   "", "", "NAM_PREP_SURF_ATM"
   "CTYPEPGD", "CHARACTER(LEN=6)", "CFILEPGDTYPE in"
   "", "", "NAM_PREP_SURF_ATM"

* :code:`XHUG_SURF_GD` : uniform prescribed value of liquid soil water index (SWI) for the surface soil layer. This prescribed value, if defined, has priority on the use of CFILE_HUG_GD and CFILE_GD data.

* :code:`XHUG_ROOT_GD` : uniform prescribed value of liquid soil water index (SWI) for the root zone soil layer(s). This prescribed value, if defined, has priority on the use of CFILE_HUG_GD and CFILE_GD data.

* :code:`XHUG_DEEP_GD` : uniform prescribed value of liquid soil water index (SWI) for the deep soil layer(s). This prescribed value, if defined, has priority on the use of CFILE_HUG_GD and CFILE_GD data.

* :code:`XHUGI_SURF_GD` : uniform prescribed value of ice soil water index (SWI) for the surface soil layer. This prescribed value, if defined, has priority on the use of CFILE_HUG_GD and CFILE_GD data.

* :code:`XHUGI_ROOT_GD` : uniform prescribed value of ice soil water index (SWI) for the root zone soil layer(s). This prescribed value, if defined, has priority on the use of CFILE_HUG_GD and CFILE_GD data.

* :code:`XHUGI_DEEP_GD` : uniform prescribed value of ice soil water index (SWI) for the deep soil layer(s). This prescribed value, if defined, has priority on the use of CFILE_HUG_GD and CFILE_GD data.

* :code:`CFILE_HUG_SURF_GD` : name of the file used to define the liquid soil water index (SWI) for the surface soil layer.

* :code:`CFILE_HUG_ROOT_GD` : name of the file used to define the liquid soil water index (SWI) for the root zone soil layer(s).

* :code:`CFILE_HUG_DEEP_GD` : name of the file used to define the liquid soil water index (SWI) for the deep soil layer(s).

* :code:`CFILE_HUG_GD` : name of the file used to define the soil water profiles.\\

* :code:`CTYPE_HUG` : type of the CFILE_HUG_GD file, if the latter is provided. CTYPE_HUG must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "GRIB ": the file type is a GRIB file, coming from any of these models:
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": Arome french forecast local model
    * "MOCAGE": Mocage french research chemistry model
  * "ASCII / LFI ": PREP file from Surfex
  * "ASCLLV": ASCII latlonval file (one file for each depth)
* :code:`XTG_SURF_GD` : uniform prescribed value of temperature for the surface soil layer, supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_TG_GD and CFILE_GD data.

* :code:`XTG_ROOT_GD` : uniform prescribed value of temperature for the root zone soil layer(s), supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_TG_GD and CFILE_GD data.

* :code:`XTG_DEEP_GD` : uniform prescribed value of temperature for the deep soil layer(s), supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_TG_GD and CFILE_GD data.

* :code:`CFILE_TG_SURF_GD` : name of the file used to define the surface soil temperature profile.

* :code:`CFILE_TG_ROOT_GD` : name of the file used to define the root zone soil temperature profile.

* :code:`CFILE_TG_DEEP_GD` : name of the file used to define the deep soil temperature profile.

* :code:`CFILE_TG_GD` : name of the file used to define the soil temperature profile.

* :code:`The use of a file or prescribed value of XTG_SURF_GD, XTG_ROOT_GD and XTG_DEEP_GD has priority on the data in CFILE_TG_GD file.`

* :code:`CTYPE_TG` : type of the CFILE_TG_GD file, if the latter is provided. CTYPE_TG must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "GRIB ": the file type is a GRIB file, coming from any of these models:
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": Arome french forecast local model
    * "MOCAGE": Mocage french research chemistry model
  * "ASCII / LFI ": PREP file from Surfex
  * "ASCLLV": ASCII latlonval file (one file for each depth)
* :code:`CFILE_GD / CFILEPGD_GD` : name of the PREP / PGD files used to define any GARDEN variable. The use of a file or prescribed value XHUG_SURF_GD, XHUG_ROOT_GD, XHUG_DEEP_GD, XTG_SURF_GD, XTG_ROOT_GD, XTG_DEEP_GD, CFILE_WG_GD and CFILE_TG_GD has priority on the data in CFILE_GD file.

* :code:`CTYPE / CTYPEPGD` : type of the CFILE_GD / CFILEPGD_GD files, if the latter is provided. CTYPE / CTYPEPGD must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "GRIB ": the file type is a GRIB file, coming from any of these models:
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": Arome french forecast local model
    * "MOCAGE": Mocage french research chemistry model
  * "ASCII ": PREP/PGD Surfex ASCII file
  * "LFI ": PREP/PGD Surfex LFI file
