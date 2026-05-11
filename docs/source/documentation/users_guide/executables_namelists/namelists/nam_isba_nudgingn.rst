.. _nam_isba_nudgingn:

NAM_ISBA_NUDGINGn
-----------------

.. csv-table:: NAM_ISBA_NUDGINGn content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LNUDG_SWE", "LOGICAL", "F"
   "LNUDG_SWE_MASK", "LOGICAL", "F"
   "XTRELAX_SWE", "REAL", "86400."
   "CNUDG_WG", "CHARACTER(LEN=3)", "'DEF'"
   "LNUDG_WG_MASK", "LOGICAL", "F"
   "XTRELAX_WG", "REAL", "86400."
   "XNUDG_Z_WG", "REAL", "1.0"

* :code:`LNUDG_SWE` : flag to activate the snow’s nudging

* :code:`LNUDG_SWE_MASK` : flag to restric the snow nudging to a given region, that is the nudging can be only regional

* :code:`XTRELAX_SWE` : relaxation time for the snow’s nudging (in s)

* :code:`CNUDG_WG` : key to activate the soil water’s nudging

  * 'DEF' :  no nudging (Default)
  * 'DAY': daily nudging
  * 'MTH': monthly nudging
* :code:`LNUDG_WG_MASK` : flag to restric the soil water’s nudging to a given region, that is the nudging can be only regional

* :code:`XTRELAX_WG` : relaxation time for the soil water’s nudging (in s)

* :code:`XNUDG_Z_WG` : vertical profile for the soil water’s nudging (Default = 1.0 for each soil layers).

