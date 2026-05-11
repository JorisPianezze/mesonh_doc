.. _nam_isba_agsn:

NAM_ISBA_AGSn
-------------

.. csv-table:: NAM_ISBA_AGSn content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CNITRO_DILU", "LOGICAL", "'NONE'"
   "LDOWNREGU", "LOGICAL", "F"
   "XCNLIM", "REAL", "-0.048"

* :code:`CNITRO_DILU` : this key activates a parameterization based on eq. 6 of Yin (2002) that modifies the leaf nitrogen content (CNA_NITRO), and hence the specific leaf area, according to the atmospheric CO$_{2}$ concentration.

  * 'NONE' : No nitrogen dilution (CNA_NITRO stays constant)
  * 'CA08' : Eq. 6 of Yin (2002) but simplified as described in Calvet et al, 2008
  * 'ESM2' : Eq. 6 of Yin (2002) and simplified as Calvet et al 2008 but taking into account the temperature term of eq 6. of Yin. When using CNITRO_DILU = 'ESM2', LDOWNREGU has to be set to TRUE.
* :code:`LDOWNREGU` : downregulation parameterization of CO$_{2}$ assimilation for CPHOTO=NCB option. Change in light-use efficiency for carbon assimilation with elevated CO$_{2}$ concentration.

* :code:`XCNLIM` : carbon nitrogen limitation parameter used in both the LNITRO_DILU and the LDOWNREGU options

