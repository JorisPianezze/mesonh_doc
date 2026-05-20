.. _nam_lunitn:

NAM_LUNITn
-----------------------------------------------------------------------------

.. csv-table:: NAM_LUNITn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CINIFILE","CHARACTER(LEN=128)","'INIFILE'"
   "CINIFILEPGD","CHARACTER(LEN=128)","' '"
   "CCPLFILE", "CHARACTER(LEN=128)(:)","NONE"

.. warning::

   This namelist is shared in by PREP_IDEAL_CASE and MESONH programs but the CCPLFILE option is only relevant for MESONH.

* :code:`CINIFILE` : name of the initial Meso-NH file produced by :ref:`prep_ideal_case`, it will then be used as initial file in a :ref:`mesonh` simulation.

* :code:`CINIFILEPGD` : name of the PGD file if CSURF :math:`\neq` 'NONE' : 

  * If you use an input PGD file for the step :ref:`prep_ideal_case` (CPGD_FILE in :ref:`nam_real_pgd`), you must have CINIFILEPGD=CPGD_FILE.
  * If there is no input PGD, CINIFILEPGD is the name of the PGD file produced by :ref:`prep_ideal_case`.

* :code:`CCPLFILE` : name of the files which contains the field values used for the coupling of the outermost MESONH model. No more than JPCPLFILEMAX=1000 (since MNH-V6-0-0) files can be used in a simulation. These CCPLFILE file names are only meaningful for the outermost model which finds its boundary conditions from a previously executed run of Meso-NH or another model (prepared by PREP_REAL_CASE). No constraint are imposed on the coupling file names only that they must be temporally ordered

   If the coupling files are given by

      * CCPLFILE(1)= ’F_1’ -> t1
      * CCPLFILE(2)= ’F_2’ -> t2
      * CCPLFILE(3)= ’A_2’ -> t3
      * CCPLFILE(4)= ’A_5’ -> t4

   then, the instants must satisfy : tsegment ≤ t1 < t2 < t3 < t4. If it is not the case, the program stops. If the coupling fields are not time dependent, no coupling files are required because the coupling fields are read from the inital MESONH file of model 1 as the Larger scale fields ( LSUM, LSVM, LSWM, LSTHM, LSRVM ). More details can be found in the scientific documentation of the model.