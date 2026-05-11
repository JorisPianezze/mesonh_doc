.. _nam_data_teb_garden:

NAM_DATA_TEB_GARDEN
-------------------

.. csv-table:: NAM_DATA_TEB_GARDEN content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "NTIME_GD", "INTEGER", "12"
   "CTYP_GARDEN_HVEG", "CHARACTER(LEN=4)", "'TEBD'"
   "", "", ""
   "", "", ""
   "", "", ""
   "CTYP_GARDEN_LVEG", "CHARACTER(LEN=4)", "'GRAS'"
   "", "", ""
   "", "", ""
   "CTYP_GARDEN_NVEG", "CHARACTER(LEN=4)", "'NO'"
   "CSHAPE_GARDEN_NVEG", "CHARACTER(LEN=3)", "'CYL'"
   "", "", ""
   "", "", ""
   "XUNIF_LAI_HVEG", "REAL", "1.E+20"
   "CFNAM_LAI_HVEG", "CHARACTER(LEN=28)", "' '"
   "CFTYP_LAI_HVEG", "CHARACTER(LEN=28)", "' '"
   "", "", ""
   "XUNIF_LAI_LVEG", "REAL", "1.E+20"
   "CFNAM_LAI_LVEG", "CHARACTER(LEN=28)", "' '"
   "CFTYP_LAI_LVEG", "CHARACTER(LEN=28)", "' '"
   "", "", ""
   "XUNIF_H_HVEG", "REAL", "1.E+20"
   "CFNAM_H_HVEG", "CHARACTER(LEN=28)", "' '"
   "CFTYP_H_HVEG", "CHARACTER(LEN=28)", "' '"
   "", "", ""
   "XUNIF_HTRUNK_HVEG", "REAL", "3.0"
   "CFNAM_HTRUNK_HVEG", "CHARACTER(LEN=28)", "' '"
   "CFTYP_HTRUNK_HVEG", "CHARACTER(LEN=28)", "' '"
   "", "", ""
   "XUNIF_WCROWN_HVEG", "REAL", "5.0"
   "CFNAM_WCROWN_HVEG", "CHARACTER(LEN=28)", "' '"
   "CFTYP_WCROWN_HVEG", "CHARACTER(LEN=28)", "' '"
   "", "", ""
   "XUNIF_RE25", "REAL", "1E+20"
   "CFNAM_RE25", "CHARACTER(LEN=28)", "' '"
   "CFTYP_RE25", "CHARACTER(LEN=28)", "' '"
   "", "", ""

* :code:`NTIME_GD` : time dimension

* :code:`CTYP_GARDEN_HVEG` : type of high vegetation

* :code:`CTYP_GARDEN_LVEG` : type of low vegetation

* :code:`CTYP_GARDEN_NVEG` : type of bare soil

* :code:`CSHAPE_GARDEN_NVEG` : shape of crown for urban trees. For the moment, only cylindric shape of crown 'CYL'is available.

* :code:`XUNIF_LAI_HVEG / CFNAM_LAI_HVEG / CFTYP_LAI_HVEG` : LAI of high vegetation (m$^{2}$/m$^{2}$)

* :code:`XUNIF_LAI_LVEG / CFNAM_LAI_LVEG / CFTYP_LAI_LVEG` : LAI of low vegetation (m$^{2}$/m$^{2}$)

* :code:`XUNIF_H_HVEG / CFNAM_H_HVEG / CFTYP_H_HVEG` : height of trees (m)

* :code:`XUNIF_HTRUNK_HVEG / CFNAM_HTRUNK_HVEG / CFTYP_HTRUNK_HVEG` : height of trunk of trees (m)

* :code:`XUNIF_WCROWN_HVEG / CFNAM_WCROWN_HVEG / CFTYP_WCROWN_HVEG` : width of crown of trees (m)

* :code:`XUNIF_RE25 / CFNAM_RE25 / CFTYP_RE25` : ecosystem respiration parameter (kg/m$^{2}$/s)

