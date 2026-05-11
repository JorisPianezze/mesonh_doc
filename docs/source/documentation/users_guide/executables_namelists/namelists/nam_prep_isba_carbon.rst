.. _nam_prep_isba_carbon:

NAM_PREP_ISBA_CARBON
--------------------

.. csv-table:: NAM_PREP_ISBA_CARBON content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CRESPSL", "CHARACTER(LEN=3)", "'DEF'"
   "LSOILGAS", "LOGICAL", "F"
   "LRESET_CSOIL", "LOGICAL", "F"

* :code:`CRESPSL` : soil respiration option. Possible values are:

  * 'DEF': no soil respiration
  * 'N92': Ecosystem respiration from Norman et al. 1992 (odl 'DEF' option befoire V9)
  * 'PRM': Rivalland 2003
  * 'CNT': Heterotrophic respiration following CENTURY model from Gibelin et al. 2008
  * 'DIF': activation of the carbon soil dynamics (discretization of soil carbon) from Morel et al. 2019 (JAMES)
* :code:`LSOILGAS` : activation of the soil gas diffusion module to simulate O2, CO2 and CH4 soil dynamics from Morel et al. 2019 (JAMES). !!! this scheme is actually a prototype !!!

* :code:`LRESET_CSOIL` : Flag to initialize isba physic but not soil carbon

