.. _nam_ch_snap_emis_pgd:

NAM_CH_SNAP_EMIS_PGD
--------------------

.. csv-table:: NAM_CH_SNAP_EMIS_PGD content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "NEMIS_NBR", "INTEGER", "0"
   "NEMIS_SNAP", "INTEGER", "0"
   "CEMIS_NAME", "CHARACTER(LEN=6)", "''"
   "CEMIS_COMMENT", "CHARACTER(LEN=40)", "''"
   "CSNAP_MONTHLY_FILE", "CHARACTER(LEN=28)", "''"
   "CSNAP_DAILY_FILE", "CHARACTER(LEN=28)", "''"
   "CSNAP_HOURLY_FILE", "CHARACTER(LEN=28)", "''"
   "CSNAP _POTENTIAL_FILE", "CHARACTER(LEN=50)", "''"
   "CSNAP_POTENTIAL_FILETYPE", "CHARACTER(LEN=6)", "''"
   "", "", ""
   "", "", ""
   "XUNIF_SNAP", "REAL", "none"
   "XUNIF_DELTA_LEGAL_TIME", "REAL", "none"
   "CDELTA_LEGAL_TIME_FILE", "CHARACTER(LEN=50)", "''"
   "CDELTA_LEGAL_TIME_FILETYPE", "CHARACTER(LEN=6)", "''"
   "", "", ""
   "", "", ""

* :code:`NEMIS_NBR` : number of chemical pgd fields chosen by user

* :code:`NEMIS_SNAP` : number of snaps

* :code:`CEMIS_NAME` : name of the chemical fields (emitted species)

* :code:`CEMIS_COMMENT` : comment on the chemical fields (emitted species)

* :code:`CSNAP_MONTHLY_FILE` : name of the snap ASCII monthly file

* :code:`CSNAP_DAILY_FILE` : name of the snap ASCII daily file

* :code:`CSNAP_HOURLY_FILE` : name of the snap ASCII hourly file

* :code:`CSNAP_POTENTIAL_FILE` : name of the snap potential file

* :code:`CSNAP_POTENTIAL_FILETYPE` : type of the snap potential file

* :code:`XUNIF_SNAP` : uniform value for the snap potential (emission factore for each chemical specie and each snap)

* :code:`XUNIF_DELTA_LEGAL_TIME` : uniform value for the difference (in hours) between lagal time and UTC time

* :code:`CDELTA_LEGAL_TIME_FILE` : name of file for the difference between legal time and UTC time

* :code:`CDELTA_LEGAL_TIME_FILETYPE` : filetype for the difference between legal time and UTC time

* :code:`the annual cycle (with a monthly timescale)`

* :code:`the weekly cycle (with a daily time scale), typically to separate weekdays, saturdays and sundays.`

* :code:`The diurnal cycle (with an hourly time scale). Note here that the hypothesis is done that the diurnal evolution is the same whatever the day in the week. The reference for the calculation of the hour (UTC, solar, legal) is provided at the beginning of this file. This allows to have different timing in different places at the same UTC (if solar or legal time is chosen), for example between China and Europe.`

