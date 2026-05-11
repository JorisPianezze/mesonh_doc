.. _nam_seaicen:

NAM_SEAICEn
-----------

.. csv-table:: NAM_SEAICEn content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CINTERPOL_SIC", "CHARACTER(LEN=6)", "'NONE'"
   "", "", ""
   "XCD_ICE_CST", "FLOAT", "0 (bulk)"
   "LDIAG_MISC_SEAICE", "LOGICAL", "T"
   "XSEAICE_TSTEP", "FLOAT", "SEA_TSTEP"
   "XSI_FLX_DRV", "FLOAT", "-20."
   "XSIC_EFOLDING_TIME", "FLOAT", "0."
   "CINTERPOL_SIT", "CHARACTER(LEN=6)", "’NONE ’"
   "", "", ""
   "XSIT_EFOLDING_TIME", "FLOAT", "0."
   "XFREEZING_SST", "FLOAT", "-1.8"

* :code:`"G"` : apply if an explicit sea-ice scheme is set in PREP (e.g. GELATO)

* :code:`CINTERPOL_SIC` : Type of interpolation of Sea Ice cover external fields. This applies whatever the role of these external fields: constraint fields (when CSEAICE_SCHEME=GELATO) or forcing fields (when value is CSEAICE_SCHEME=NONE and some interpolation is set)

  * LINEAR: linear interpolation between 3 months
  * READAY: impose directly daily SIC (sea ice cover)
* :code:`XCD_ICE_CST` : Turbulent exchange coefficient value for drag, heat and vapor on sea-ice. Default is 0 and means: apply a bulk formula.

* :code:`LDIAG_MISC_SEAICE` : should we output sea-ice diagnostics ? default to T is sea-ice cover is handled

* :code:`XSEAICE_TSTEP` : Time step (in s) for the Gelato sea-ice scheme. If not set, use the same time step as the SEA scheme

* :code:`XSI_FLX_DRV` : Derivative of the non-solar fluxes w.r.t. sea-ice temperature (in W.m$^{-2}$.K$^{-1}$). Allows Gelato to compute this flux on various ice categories, as long as Surfex handles only one sea-ice category.

* :code:`XSIC_EFOLDING_TIME` : If $\ge$ 0, a damping of sea-ice cover will occur in Gelato, with this e-folding time (in days). The sea-ice cover constraint is the data provided in the PREP file, interpolated in time according to CINTERPOL_SIC setting, or, as a default, the interpretation of SST data using XFREEZING_SST. [ note for Gelato wizzards: the Surfex default Gelato option for damping is "MONO" ]

* :code:`CINTERPOL_SIT` : Type of interpolation of Sea Ice thickness constraint, in Gelato.

  * READAY: impose directly daily SIT (sea ice thickness)
* :code:`XSIT_EFOLDING_TIME` : If $\ge$ 0, a damping of sea-ice thickness will occur in Gelato, with this e-folding time (in days). The sea-ice thickness constraint is the data provided in the PREP file [ note for Gelato wizzards: the Surfex default Gelato option for damping is "MONO_ADD" ]

* :code:`XFREEZING_SST` : Arbitrary SST freezing point (in Celsius). Indicates where the SST data you provide can be interpreted by Gelato as locations covered with sea-ice, if no SIC constraint field is provided. SST passed to Gelato will also anyway then be set there to the actual, salinity-dependant, freezing point.

