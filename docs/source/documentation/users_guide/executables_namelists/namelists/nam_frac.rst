.. _nam_frac:

NAM_FRAC
--------

.. csv-table:: NAM_FRAC content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LECOCLIMAP", "LOGICAL", "T"
   "LECOSG", "LOGICAL", "F"
   "XUNIF_SEA", "REAL", "none"
   "CFNAM_SEA", "CHARACTER(LEN=28)", "' '"
   "CFTYP_SEA", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_WATER", "REAL", "none"
   "CFNAM_WATER", "CHARACTER(LEN=28)", "' '"
   "CFTYP_WATER", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_NATURE", "REAL", "none"
   "CFNAM_NATURE", "CHARACTER(LEN=28)", "' '"
   "CFTYP_NATURE", "CHARACTER(LEN=6)", "none"
   "", "", ""
   "XUNIF_TOWN", "REAL", "none"
   "CFNAM_TOWN", "CHARACTER(LEN=28)", "' '"
   "CFTYP_TOWN", "CHARACTER(LEN=6)", "' '"

* :code:`LECOCLIMAP` : flag to use ECOCLIMAP or not. From version 7.1, it’s possible to partially use ECOCLIMAP to complete missing parameters when they are given directly in the namelist.

* :code:`LECOSG` : flag to use ECOCLIMAP-SG database (from SURFEX 8.1)

* :code:`XUNIF_SEA` : uniform prescribed value of sea fraction. If XUNIF_SEA is set, file CFNAM_SEA is not used.

* :code:`CFNAM_SEA` : sea fraction data file name. If XUNIF_SEA is set, file CFNAM_SEA is not used.

* :code:`CFTYP_SEA` : type of sea data file ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV')

* :code:`XUNIF_WATER` : uniform prescribed value of water fraction. If XUNIF_WATER is set, file CFNAM_WATER is not used.

* :code:`CFNAM_WATER` : water fraction data file name. If XUNIF_WATER is set, file CFNAM_WATER is not used.

* :code:`CFTYP_WATER` : type of water data file ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV')

* :code:`XUNIF_NATURE` : uniform prescribed value of nature fraction. If XUNIF_NATURE is set, file CFNAM_NATURE is not used.

* :code:`CFNAM_NATURE` : nature fraction data file name. If XUNIF_NATURE is set, file \\

* :code:`CFTYP_NATURE` : type of nature data file ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV')

* :code:`XUNIF_TOWN` : uniform prescribed value of town fraction. If XUNIF_TOWN is set, file CFNAM_TOWN is not used.

* :code:`CFNAM_TOWN` : town fraction data file name. If XUNIF_TOWN is set, file CFNAM_TOWN is not used.

* :code:`CFTYP_TOWN` : type of town data file ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV')

