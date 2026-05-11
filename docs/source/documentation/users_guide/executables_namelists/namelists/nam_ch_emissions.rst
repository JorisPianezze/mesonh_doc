.. _nam_ch_emissions:

NAM_CH_EMISSIONS
----------------

.. csv-table:: NAM_CH_EMISSIONS content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CCH_EMIS", "CHARACTER(LEN=4)", "'NONE'"

* :code:`CCH_EMIS` : option for emissions computations:

  * "NONE": no emission
  * "AGGR": one aggregated value for each specie and hour
  * "SNAP": from SNAP data using potential emission and temporal profile
