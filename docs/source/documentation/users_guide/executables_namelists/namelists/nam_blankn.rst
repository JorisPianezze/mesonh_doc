.. _nam_blankn:

NAM_BLANKn
-----------------------------------------------------------------------------

.. csv-table:: NAM_BLANKn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XDUMMY1","REAL","0.0"
   "XDUMMY2","REAL","0.0"
   "XDUMMY3","REAL","0.0"
   "XDUMMY4","REAL","0.0"
   "XDUMMY5","REAL","0.0"
   "XDUMMY6","REAL","0.0"
   "XDUMMY7","REAL","0.0"
   "XDUMMY8","REAL","0.0"
   "NDUMMY1","INTEGER","0"
   "NDUMMY2","INTEGER","0"
   "NDUMMY3","INTEGER","0"
   "NDUMMY4","INTEGER","0"
   "NDUMMY5","INTEGER","0"
   "NDUMMY6","INTEGER","0"
   "NDUMMY7","INTEGER","0"
   "NDUMMY8","INTEGER","0"
   "LDUMMY1","LOGICAL","TRUE"
   "LDUMMY2","LOGICAL","TRUE"
   "LDUMMY3","LOGICAL","TRUE"
   "LDUMMY4","LOGICAL","TRUE"
   "LDUMMY5","LOGICAL","TRUE"
   "LDUMMY6","LOGICAL","TRUE"
   "LDUMMY7","LOGICAL","TRUE"
   "LDUMMY8","LOGICAL","TRUE"
   "CDUMMY1","CHARACTER(LEN=80)",""
   "CDUMMY2","CHARACTER(LEN=80)",""
   "CDUMMY3","CHARACTER(LEN=80)",""
   "CDUMMY4","CHARACTER(LEN=80)",""
   "CDUMMY5","CHARACTER(LEN=80)",""
   "CDUMMY6","CHARACTER(LEN=80)",""
   "CDUMMY7","CHARACTER(LEN=80)",""
   "CDUMMY8","CHARACTER(LEN=80)",""

Eight dummy variables and arrays (real, integer, logical, and character of length 80) are defined for testing and debugging. They are read through the namelist but are not used by any Meso-NH routine. If a developer wants to temporarily add a parameter to a subroutine, they can include a :code:`USE MODD_BLANK_n` statement in that subroutine. This allows them to access and modify these variables via the namelist input.
