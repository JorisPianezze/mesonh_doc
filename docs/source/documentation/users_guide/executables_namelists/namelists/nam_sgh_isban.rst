.. _nam_sgh_isban:

NAM_SGH_ISBAn
-------------

.. csv-table:: NAM_SGH_ISBAn content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CRUNOFF", "CHARACTER(LEN=4)", "'WSAT'"
   "CKSAT", "CHARACTER(LEN=4)", "'DEF'"
   "LSOC", "LOGICAL", "F"
   "CRAIN", "CHARACTER(LEN=3)", "'DEF'"
   "CHORT", "CHARACTER(LEN=4)", "'DEF '"

* :code:`CRUNOFF` : type of subgrid runoff. The following options are currently available:

  * 'WSAT': runoff occurs only when saturation is reached
  * 'DT92': Dumenill and Todini (1992) subgrid runoff formula
  * 'SGH ': Decharme et al. (2006) Topmodel like subgrid runoff
  * 'TOPD': if LCOUPL_TOPD=T, allows that DUNNE runoff contains only saturated pixels on meshes so only catchments
* :code:`CKSAT` : Activates the exponential profile for Ksat. The following options are currently available:

  * 'DEF': homogeneous profile
  * 'SGH': exponential decreasing profile with depth (due to compaction of soil)
  * 'EXP': with CISBA='3-L' and LCOUPL_TOPD=T, allows to read a file containing values for the F parameter, computed by topmodel during PGD.
* :code:`LSOC` : to activate soil organic carbon effect.

* :code:`CRAIN` : Activates the spatial distribution of rainfall intensity. The following options are currently available:

  * 'DEF': homogeneous distribution
  * 'SGH': exponential distribution which depends on the fraction of the mesh where it rains. This fraction depends on the mesh resolution and the intensity of hourly precipitation. (If the horizontal mesh is lower than 10km then the fraction equals 1).
* :code:`CHORT` : Activates the Horton runoff due to water infiltration excess. The following options are currently available:

  * 'DEF': no Horton runoff
  * 'SGH': Horton runoff computed
