.. _nam_data_teb_irrig:

NAM_DATA_TEB_IRRIG
------------------

.. csv-table:: NAM_DATA_TEB_IRRIG content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "XUNIF_GD_START_MONTH", "REAL", "1.E+20"
   "CFNAM_GD_START_MONTH", "CHARACTER(LEN=28)", "' '"
   "CFTYP_GD_START_MONTH", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_GD_END_MONTH", "REAL", "1.E+20"
   "CFNAM_GD_END_MONTH", "CHARACTER(LEN=28)", "' '"
   "CFTYP_GD_END_MONTH", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_GD_START_HOUR", "REAL", "1.E+20"
   "CFNAM_GD_START_HOUR", "CHARACTER(LEN=28)", "' '"
   "CFTYP_GD_START_HOUR", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_GD_END_HOUR", "REAL", "1.E+20"
   "CFNAM_GD_END_HOUR", "CHARACTER(LEN=28)", "' '"
   "CFTYP_GD_END_HOUR", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_GD_24H_IRRIG", "REAL", "1.E+20"
   "CFNAM_GD_24H_IRRIG", "CHARACTER(LEN=28)", "' '"
   "CFTYP_GD_24H_IRRIG", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_GR_START_MONTH", "REAL", "1.E+20"
   "CFNAM_GR_START_MONTH", "CHARACTER(LEN=28)", "' '"
   "CFTYP_GR_START_MONTH", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_GR_END_MONTH", "REAL", "1.E+20"
   "CFNAM_GR_END_MONTH", "CHARACTER(LEN=28)", "' '"
   "CFTYP_GR_END_MONTH", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_GR_START_HOUR", "REAL", "1.E+20"
   "CFNAM_GR_START_HOUR", "CHARACTER(LEN=28)", "' '"
   "CFTYP_GR_START_HOUR", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_GR_END_HOUR", "REAL", "1.E+20"
   "CFNAM_GR_END_HOUR", "CHARACTER(LEN=28)", "' '"
   "CFTYP_GR_END_HOUR", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_GR_24H_IRRIG", "REAL", "1.E+20"
   "CFNAM_GR_24H_IRRIG", "CHARACTER(LEN=28)", "' '"
   "CFTYP_GR_24H_IRRIG", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_RD_START_MONTH", "REAL", "1.E+20"
   "CFNAM_RD_START_MONTH", "CHARACTER(LEN=28)", "' '"
   "CFTYP_RD_START_MONTH", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_RD_END_MONTH", "REAL", "1.E+20"
   "CFNAM_RD_END_MONTH", "CHARACTER(LEN=28)", "' '"
   "CFTYP_RD_END_MONTH", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_RD_START_HOUR", "REAL", "1.E+20"
   "CFNAM_RD_START_HOUR", "CHARACTER(LEN=28)", "' '"
   "CFTYP_RD_START_HOUR", "CHARACTER(LEN=6)", "none"
   "", "", ""

.. csv-table:: NAM_DATA_TEB_IRRIG content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "Name", "TYPE", "Default"
   "XUNIF_RD_END_HOUR", "REAL", "1.E+20"
   "CFNAM_RD_END_HOUR", "CHARACTER(LEN=28)", "' '"
   "CFTYP_RD_END_HOUR", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_RD_24H_IRRIG", "REAL", "1.E+20"
   "CFNAM_RD_24H_IRRIG", "CHARACTER(LEN=28)", "' '"
   "CFTYP_RD_24H_IRRIG", "CHARACTER(LEN=6)", "none"
   "", "", ""

* :code:`XUNIF_GD_START_MONTH / CFNAM_GD_START_MONTH / \\`

* :code:`XUNIF_GD_END_MONTH / CFNAM_GD_END_MONTH / CFTYP_GD_END_MONTH` : end month for irrigation for gardens (included)

* :code:`XUNIF_GD_START_HOUR / CFNAM_GD_START_HOUR / CFTYP_GD_START_HOUR` : start solar hour for irrigation for gardens (included)

* :code:`XUNIF_GD_END_HOUR / CFNAM_GD_END_HOUR / CFTYP_GD_END_HOUR` : end solar hour for irrigation for gardens (excluded)

* :code:`XUNIF_GD_24H_IRRIG / CFNAM_GD_24H_IRRIG / CFTYP_GD_24H_IRRIG` : total irrigation over 24 hours for gardens (kg/m$^{2}$)

* :code:`XUNIF_GR_START_MONTH / CFNAM_GR_START_MONTH / \\`

* :code:`XUNIF_GR_END_MONTH / CFNAM_GR_END_MONTH / CFTYP_GR_END_MONTH` : end month for irrigation for greenroofs (included)

* :code:`XUNIF_GR_START_HOUR / CFNAM_GR_START_HOUR / CFTYP_GR_START_HOUR` : start solar hour for irrigation for greenroofs (included)

* :code:`XUNIF_GR_END_HOUR / CFNAM_GR_END_HOUR / CFTYP_GR_END_HOUR` : end solar hour for irrigation for greenroofs (excluded)

* :code:`XUNIF_GR_24H_IRRIG / CFNAM_GR_24H_IRRIG / CFTYP_GR_24H_IRRIG` : total irrigation over 24 hours for greenroofs (kg/m$^{2}$)

* :code:`XUNIF_RD_START_MONTH / CFNAM_RD_START_MONTH / \\`

* :code:`XUNIF_RD_END_MONTH / CFNAM_RD_END_MONTH / CFTYP_RD_END_MONTH` : end month for irrigation for roads (included)

* :code:`XUNIF_RD_START_HOUR / CFNAM_RD_START_HOUR / CFTYP_RD_START_HOUR` : start solar hour for irrigation forroads  (included)

* :code:`XUNIF_RD_END_HOUR / CFNAM_RD_END_HOUR / CFTYP_RD_END_HOUR` : end solar hour for irrigation for roads (excluded)

* :code:`XUNIF_RD_24H_IRRIG / CFNAM_RD_24H_IRRIG / CFTYP_RD_24H_IRRIG` : total irrigation over 24 hours for roads (kg/m$^{2}$)

