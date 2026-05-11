.. _nam_isba_ccn:

NAM_ISBA_CCn
------------

.. csv-table:: NAM_ISBA_CCn content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LSPINUPCARBS", "LOGICAL", "F"
   "XSPINMAXS", "REAL", "0."
   "NNBYEARSPINS", "INTEGER", "0"
   "XMISSFCO2", "REAL", "0.0"
   "LFIRE", "LOGICAL", "F"
   "LCLEACH", "LOGICAL", "F"
   "LADVECT_SOC", "LOGICAL", "F"
   "LCRYOTURB", "LOGICAL", "F"
   "LBIOTURB", "LOGICAL", "F"

* :code:`LSPINUPCARBS` : if T, to do the soil carbon spinup

* :code:`XSPINMAXS` : This key defines the spinup time step as the increase of the physical time step by a factor equal to XSPINMAXS. So, if the physical (isba time step) = 300s and XSPINMAXS = 50, then the carbon spinup time step = 15000s.

* :code:`NNBYEARSPINS` : number of years needed to reach soil equilibrium (spinup time step is at its maximum during 80% of the defined NNBYEARSPINS, then decrease linearly to reach the physical time step). So, if XSPINMAXS = 50 and NNBYEARSPINS =250, the spinup procedure is at maximum during 200 physical years representing 200x50 = 10 000 carbon years.

* :code:`XMISSFCO2` : Missing carbon flux (cf. anthropic) required for ESM coupling in emission mode (default = 0.)

* :code:`LFIRE` : flag to activate simple biomass fire module

* :code:`LCLEACH` : flag to activate soil carbon leaching that produce dissolved organic carbon that can be routed by CTRIP

* :code:`LADVECT_SOC` : flag to activate vertical advection scheme for soil dynamics carbon module, only  if CRESPSL = DIF (in NAM_PREP_ISBA_CARBON)

* :code:`LCRYOTURB` : flag to activate vertical cryoturbation scheme if CRESPSL = DIF (in \\

* :code:`LBIOTURB` : flag to activate vertical bioturbation scheme if CRESPSL = DIF (in \\

