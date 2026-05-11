.. _nam_data_teb_greenroof:

NAM_DATA_TEB_GREENROOF
----------------------

.. csv-table:: NAM_DATA_TEB_GREENROOF content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "NTIME_GR", "INTEGER", "1"
   "NLAYER_GR", "INTEGER", "6"
   "CTYP_GR", "CHARACTER(LEN=5)", "'GRASS'"
   "XUNIF_OM_GR", "REAL,DIMENSION(NLAYER_GR)", "1.E+20"
   "XUNIF_CLAY_GR", "REAL,DIMENSION(NLAYER_GR)", "1.E+20"
   "XUNIF_SAND_GR", "REAL,DIMENSION(NLAYER_GR)", "1.E+20"
   "XUNIF_LAI_GR", "REAL,DIMENSION(NTIME_GR)", "1.E+20"
   "CFNAM_OM_GR", "CHARACTER(LEN=28),DIM(NLAYER_GR)", "''"
   "CFNAM_CLAY_GR", "CHARACTER(LEN=28),DIM(NLAYER_GR)", "''"
   "CFNAM_SAND_GR", "CHARACTER(LEN=28),DIM(NLAYER_GR)", "''"
   "CFNAM_LAI_GR", "CHARACTER(LEN=28),DIM(NTIME_GR)", "''"
   "CFTYP_OM_GR", "CHARACTER(LEN=6),DIM(NLAYER_GR)", "''"
   "", "", ""
   "CFTYP_CLAY_GR", "CHARACTER(LEN=6),DIM(NLAYER_GR)", "''"
   "", "", ""
   "CFTYP_SAND_GR", "CHARACTER(LEN=6),DIM(NLAYER_GR)", "''"
   "", "", ""
   "CFTYP_LAI_GR", "CHARACTER(LEN=6),DIM(NTIME_GR)", "''"
   "", "", ""

* :code:`NTIME_GR` : time dimension (1=uniform LAI / 12=monthly LAI)

* :code:`NLAYER_GR` : number of layers in greenroofs

* :code:`CTYP_GR` : type of vegetation for greenroofs

  * 'GRASS': Grasses - graminoïds
  * 'SEDUM': Sedum (succulent plants)
* :code:`XUNIF_OM_GR / CFNAM_OM_GR / CFTYP_OM_GR` : fraction of organic matter in greenroof layer

* :code:`XUNIF_CLAY_GR / CFNAM_CLAY_GR / CFTYP_CLAY_GR` : fraction of clay for the non-OM part of the green roof layer

* :code:`XUNIF_SAND_GR / CFNAM_SAND_GR / CFTYP_SAND_GR` : fraction of sand for the non-OM part of the green roof layer

* :code:`XUNIF_LAI_GR / CFNAM_LAI_GR / CFTYP_LAI_GR` : LAI of green roof vegetation (m$^{2}$/m$^{2}$)

