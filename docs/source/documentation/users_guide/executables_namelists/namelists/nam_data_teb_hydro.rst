.. _nam_data_teb_hydro:

NAM_DATA_TEB_HYDRO
------------------

.. csv-table:: NAM_DATA_TEB_HYDRO content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "XUNIF_DENS_WASTE", "REAL", "1.E+20"
   "CFNAM_DENS_WASTE", "CHARACTER(LEN=28)", ""
   "CFTYP_DENS_WASTE", "CHARACTER(LEN=6)", ""
   "", "", ""
   "XUNIF_DENS_STORM", "REAL", "1.E+20"
   "CFNAM_DENS_STORM", "CHARACTER(LEN=28)", ""
   "CFTYP_DENS_STORM", "CHARACTER(LEN=6)", ""
   "", "", ""
   "XUNIF_DSEWER", "REAL", "1.E+20"
   "CFNAM_DSEWER", "CHARACTER(LEN=28)", ""
   "CFTYP_DSEWER", "CHARACTER(LEN=6)", ""
   "", "", ""
   "XUNIF_WS_ROOF_MAX", "REAL", "1"
   "CFNAM_WS_ROOF_MAX", "CHARACTER(LEN=28)", ""
   "CFTYP_WS_ROOF_MAX", "CHARACTER(LEN=6)", ""
   "", "", ""
   "XUNIF_WS_ROAD_MAX", "REAL", "1"
   "CFNAM_WS_ROAD_MAX", "CHARACTER(LEN=28)", ""
   "CFTYP_WS_ROAD_MAX", "CHARACTER(LEN=6)", ""
   "", "", ""
   "XUNIF_IP_SEWER", "REAL", "0"
   "CFNAM_IP_SEWER", "CHARACTER(LEN=28)", ""
   "CFTYP_IP_SEWER", "CHARACTER(LEN=6)", ""
   "", "", ""
   "XUNIF_CONNEX", "REAL", "1"
   "", "", ""
   "CFNAM_CONNEX", "CHARACTER(LEN=28)", ""
   "CFTYP_CONNEX", "CHARACTER(LEN=6)", ""
   "", "", ""
   "XUNIF_INFIL_ROAD", "REAL", "0"
   "CFNAM_INFIL_ROAD", "CHARACTER(LEN=28)", ""
   "CFTYP_INFIL_ROAD", "CHARACTER(LEN=6)", ""
   "", "", ""
   "XUNIF_URBDRAIN", "REAL", "0"
   "", "", ""
   "CFNAM_URBDRAIN", "CHARACTER(LEN=28)", ""
   "CFTYP_URBDRAIN", "CHARACTER(LEN=6)", ""
   "", "", ""

* :code:`XUNIF_DENS_WASTE / CFNAM_DENS_WASTE / CFTYP_DENS_WASTE` : wastewater sewer length density (-)

* :code:`XUNIF_DENS_STORM / CFNAM_DENS_STORM / CFTYP_DENS_STORM` : tormwater sewer length density (-)

* :code:`XUNIF_DSEWER / CFNAM_DSEWER / CFTYP_DSEWER` : waste water sewer depth (m)

* :code:`XUNIF_WS_ROOF_MAX / CFNAM_WS_ROOF_MAX / CFTYP_WS_ROOF_MAX` : maximum capacity of surface roof water storage (mm)

* :code:`XUNIF_WS_ROAD_MAX / CFNAM_WS_ROAD_MAX / CFTYP_WS_ROAD_MAX` : maximum capacity of surface road water storage (mm)

* :code:`XUNIF_IP_SEWER / CFNAM_IP_SEWER / CFTYP_IP_SEWER` : parasite infiltrations into sewer (-)

* :code:`XUNIF_CONNEX / CFNAM_CONNEX/ CFTYP_CONNEX` : impervious surfaces connexion rate to the sewer (-)

* :code:`XUNIF_INFIL_ROAD / CFNAM_INFIL_ROAD / CFTYP_INFIL_ROAD` : water infiltration through the roads (kg/m$^{2}$/s)

* :code:`XUNIF_URBDRAIN / CFNAM_URBDRAIN / CFTYP_URBDRAIN` : limitation fraction of urban deep drainage (-)

