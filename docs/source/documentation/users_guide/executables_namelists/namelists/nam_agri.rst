.. _nam_agri:

NAM_AGRI
--------

.. csv-table:: NAM_AGRI content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LAGRIP", "LOGICAL", "F"
   "LIRRIGMODE", "LOGICAL", "F"
   "XTHRESHOLD", "REAL(4)", "(/0.70,0.55,0.40,0.25/)"
   "NVEG_IRR", "INTEGER", "6"
   "NPATCH_TREE", "INTEGER", "none"
   "NIRR_STOP_BTR", "INTEGER", "14 (days)"

* :code:`LAGRIP` : General switch for agricultural practices (seeding and irrigation)

* :code:`LIRRIGMODE` : flag to activate irrigation. With LAGRIP and/or LIRRIGMODE, if ECOCLIMAP-SG is activated (LECOSG = T in namelist NAM_FRAC) the vegetation types associated (define with NUNIF_VEG_IRR_USE, see NAM_DATA_ISBA ) are duplicated. In this case, NPATCH (from namelist NAM_ISBA) have to be adapted to indicate how many patch are finally considered (with default irrigated vegetation type, is currently 2, 4, 5, 10, 12, 14, 15, 19 or 26). Then, by default you need nothing more without ECOCLIMAP-SG. With ECOCLIMAP-SG it is extremely recommended to use the map provided with ECOCLIMAP-SG forcing (cf CFNAM_IRRIGFRAC and CFTYP_IRRIGFRAC in namelist NAM_DATA_ISBA).

* :code:`XTHRESHOLD` : if LIRRIGMODE is activated, XTHRESHOLD is the 4 successive stage threshold to trigger the irrigation. It can be overwrite by more specific values in the namelist NAM_DATA_ISBA.

* :code:`NVEG_IRR` : if LAGRIP or/and LIRRIGMODE are activated, correspond to the number of patch irrigated or/and with agricultural practices. The default value is 6 with ECOCLIMAP-SG and LIRRIGMODE, 0 without ECOCLIMAP-SG. NB if you indicate 0, the default value is used.

* :code:`NPATCH_TREE` : with ECOCLIMAP-SG and if LAGRIP or/and LIRRIGMODE are activated, correspond to the tree patch distribution without irrigation. By default (if default values of NVEG_IRR and NVEG_IRR_USE are used) it takes automatically a value corresponding to NPATCH, else the value of patch tree without irrigation use has to be indicated (1, 2, 3, 7, 9, 10, 12, 13 or 20).

* :code:`NIRR_STOP_BTR` : Number of days corresponding to the time when the irrigation stop before reaping.

