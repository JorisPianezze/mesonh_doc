.. _aclib:

ACLIB
----------------------------------------------------------------------------

ACLIB (Aerosols and Chemistry LIBrary) is an external repository which contains the aerosols and chemistry core codes from Méso-NH, MOCAGE and ARPEGE-ALADIN-climat. 
The main objective of building such library is exposing a single interface to access every existing routines at the CNRM relating to aerosols physics 
and chemistry. The aerosols and chemistry code of MOCAGE and ARPEGE-ALADIN-climat are now available in Méso-NH (and vice-versa). ACLIB is also plugged into AROME.

The library comes with a new way to set-up parameters with aerosols and gas species: it uses tables in a :file:`.csv` format which makes easier to define each 
parameter for individual aerosols more easily than re-compiling the code (i.e. modd_dust.f90 to change parameters of the log-normal distribution).
Pre-defined configurations of these tables are provided by each host-models in order to ease the use of their own schemes in different host models.

.. note::

   In Méso-NH, the code of ARPEGE-ALADIN-climat and MOCAGE is now available but have not been adapted nor tested yet. 
   Using these codes needs scientific adaptation with Méso-NH objects and can be done with a scientific coordination of ACLIB team (ACLIB referee for Méso-NH: quentin.rodier@meteo.fr)

Tree structure
****************************************************************************
The ACLIB sources can be found here:

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/ACLIB
      
        - :dir:`folder` aer

          - :dir:`folder` scav
          - :dir:`folder` sedim
          - :dir:`folder` suflux
          - :dir:`folder` transfo
          - :dir:`folder` diag
          
        - :dir:`folder` chem
        - :dir:`folder` aux

* aer: main interface :file:`aer_aclib.f90`, main initialization of aerosols propreties from the csv data :file:`init_aer_aclib.f90` and definition of the 
  variables in :file:`modd_param_aer_aclib.f90`
* aer/scav: scavenging codes of all models, including Méso-NH ones (e.g. :file:`aer_wet_dep_kmt_warm.f90`)
* aer/sedim: sedimentation codes of all models, including Méso-NH ones (e.g. :file:`sedim_dslt.f90`)
* aer/suflux: dry deposition and emission of other models than SURFEX. For Méso-NH, it is still through SURFEX.
* aer/transfo: secondary transformations of aerosols corresponding to ORILAM scheme in Méso-NH (:file:`ch_orilam.f90`)
* aer/diag: diagnostics: not pluggd to Méso-NH
* chem: main interface :file:`chem_aclib.f90` with all main chemistry code and solvers. For Méso-NH, :file:`BASIC.f90`, the main :file:`ch_*.f90` routines 
  and :file:`ch_aer_*.f90` routines for ORILAM scheme. MOCAGE solvers are :file:`mocage_*.f90` routines and ARPEGE-ALADIN-climat ones are :file:`acch_*.f90`
* aux: auxilliary routines that are not used only in one specific folder but necessary to compile each codes in all host models.



Interfaces and implementation in Méso-NH
****************************************************************************

Aerosols
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/MNH
      
        - :dir:`file` ini_modeln.f90

          - CALL INIT_AER_ACLIB: init of aerosols properties and read of csv data
        
        - :dir:`file` modeln.f90
            
            - CALL AER_ACLIB 
      - :dir:`folder` |MNH_directory_extract_current|/src/ACLIB/aer/aer_aclib.f90

               - CALL AER_ACLIB_EMIS
               - CALL AER_ACLIB_DRYDEP
               - CALL AER_ACLIB_SEDIM
               - CALL AER_ACLIB_SCAV
               - CALL AER_ACLIB_TRANSFO
               - CALL AER_ACLIB_DIAGS


**Sedimentation**

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/ACLIB/aer/sedim
      
        - :dir:`file` aer_aclib_sedim.f90

          - CALL SEDIM: sedimentation in MOCAGE
          - CALL TACTIC_SEDIMNT: sedimentation in ARPEGE-ALADIN-climat
          - CALL SEDIM_DSLT: sedimentation in Méso-NH for DUST and SALT
          - CALL CH_AER_SEDIM_n: sedimentation in Méso-NH for aerosols of ORILAM

.. note::

   The routines of sedimentation from dust and salt are merged from MNH-V6-0-0

**Scavenging**

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/ACLIB/aer/scav
      
        - :dir:`file` aer_aclib_scav.f90

          - CALL WETSCAV: scavenging in MOCAGE
          - CALL TACTIC_SCAV: sedimscavengingentation in ARPEGE-ALADIN-climat
          - CALL AER_WET_DEP_KMT_WARM: scavenging in Méso-NH for DUST and SALT

.. note::

   The routines of scavenging of ORILAM aerosols are not in ACLIB.

**Transformations (secondary in-organic aerosols)**

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/ACLIB/aer/transfo
      
        - :dir:`file` aer_aclib_transfo.f90

          - CALL MOCAERO: MOCAGE transfo
          - CALL TACTIC_CGROWTH, _SO2SO4, _NO3NH4 : ARPEGE-ALADIN-climat transfo
          - CALL CH_ORILAM: Méso-NH ORILAM

The routine of ORILAM-Méso-NH are not in ACLIB/aer/transfo but in ACLIB/chem because it can not be used without the chemistry module


Aerosols of ORILAM
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The sedimentation, scavenging and dry deposition of ORILAM aerosols have been externalized from the chemistry, it is now in a new routine
:file:`ch_aer_ext_orilam.f90`:

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/MNH
        
        - :dir:`file` modeln.f90
            
            - CALL CH_AER_EXT_ORILAM 

               - CALL MNH_TO_AER_ACLIB
            
                  - CALL AER_ACLIB
            
                     - CALL CH_AER_SEDIM_n

               - CALL CH_AER_WET_DEP_n
               - CALL CH_AER_DEPOS

Chemistry solver
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

For the chemistry solver, a new interface :file:`chem_aclib.f90` contains the call to the chemistry monitors:

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/MNH
      
        - :dir:`file` modeln.f90

          - CALL INIT_CHEM_MODEL: init of other chemistries
          - CALL MNH_TO_CHEM_ACLIB
            
            - CALL CHEM_ACLIB 
      - :dir:`file` |MNH_directory_extract_current|/src/ACLIB/chem/chem_aclib.f90

               - CALL CH_MONITOR_n: Méso-NH chemistry monitor
               - CALL CHEM_SUGAR: MOCAGE monitor
               - CALL ACCHEM: ARPEGE-ALADIN-climat monitor

Note that the init of Méso-NH chemistry is not yet moved to init_chem_model.
               
.. note::

   In the interfaces CHEM_ACLIB and MNH_TO_CHEM_ACLIB, the arguments are written with explicit dimensions because Méso-NH and MOCAGE are using 2 dimensions for
   latitudes and longitudes whereas ARPEGE-ALADIN-climat uses only 1 dimension (lat/lon are packed). The pack/unpack operations are done correctly at the execution if the arrays are contiguous.

The use of the extra interface MNH_TO_CHEM_ACLIB is necessary for diagnostics allocated with different dimensions regarding the host model.

ACLIB custom types
****************************************************************************

To ease the use of ACLIB in each host models, new custom types have been created:

* for individual aerosols and gas species, :code:`YCHEMS` and :code:`YAEROSOLS` regroup the definition of each individual chemical species and aerosols.

* for general parameters for aerosols and chemistry schemes :code:`YPAER_ACLIB` and :code:`YPCHEM_ACLIB` are defined.

* for diagnostics, :code:`YAEROUT_ACLIB` and :code:`YCHEMOUT_ACLIB` are defined (not yet used in Meso-NH).

* for general constants used in ACLIB, :code:`CST_ACLIB` is defined. 

.. csv-table:: ACLIB objects
   :header: "Object name", "Definition", "Initialization", "Data source"
   :widths: 25, 25, 25, 25

   "YCHEMS","chem/modd_param_chem_aclib.f90","chem/init_chem_aclib.f90", "Table_chem_species_aclibn.csv (`example <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/blob/MNH-60-branch/examples/test_cases/012_dust/003_run/Table_aer_general_aclib1.csv?ref_type=heads>`_)"
   "YPCHEM_ACLIB","chem/modd_param_chem_aclib.f90","chem/init_chem_aclib.f90", "Table_chem_general_aclibn.csv (`example <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/blob/MNH-60-branch/examples/test_cases/012_dust/003_run/Table_aer_species_aclib1.csv?ref_type=heads>`_)"
   "YAEROSOLS","aer/modd_param_aer_aclib.f90","aer/init_aer_aclib.f90", "Table_aer_species_aclibn.csv (`example <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/blob/MNH-60-branch/examples/test_cases/011_KW78CHEM/002_mesonh/Table_chem_general_aclib1.csv?ref_type=heads>`_)"
   "YPAER_ACLIB","aer/modd_param_aer_aclib.f90","aer/init_aer_aclib.f90", "Table_aer_species_aclibn.csv (`example <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/blob/MNH-60-branch/examples/test_cases/011_KW78CHEM/002_mesonh/Table_chem_species_aclib1.csv?ref_type=heads>`_)"
   "CST_ACLIB","aux/modd_cst_aclib.f90","aer/init_cst_aclib.f90", ""


CSV input parameters
****************************************************************************
To ease the use of ACLIB within different host models, a common input parameters format has been designed using csv tables (see the list in the previous section).

For aerosols, :file:`Table_aer_general_aclibn.csv`, with :code:`n` the Méso-NH domain number, defines general options such as the number of total aerosols/modes used,
the number of families (dust, salt, etc) and the code wanted for each processus (sedimentation, scavenging, deposition, emission, and transformation). 

The same general csv table is for chemical species.

For a smooth transition from the classic FORTRAN Méso-NH namelist to csv format, a new namelist is available

.. csv-table:: NAM_ACLIB new entries
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LUSEAERTABLE","LOGICAL",".FALSE."
   "LUSECHEMTABLE","LOGICAL",".FALSE."

* :code:`LUSEAERTABLE`: true to use :file:`Table_aer_general_aclibn.csv` to read namelist input instead of the traditional namelist for **some** aerosols general parameters

* :code:`LUSECHEMTABLE`: true to use :file:`Table_chem_general_aclibn.csv` to read namelist input instead of the traditional namelist for **some** chemistry general parameters

.. note::

   By default, :file:`Table_aer_general_aclibn.csv` and :file:`Table_chem_general_aclibn.csv` are ignored (not read). Traditional Méso-NH namelist is used.

.. warning::

   The Table_aer_species_aclibn.csv are always read, so using NAM_DUST, NAM_SALT or NAM_CH_ORILAM must be carefully cross-checked with the Tables!

   The Table_chem_species_aclibn.csv are not read/implemented yet.

How to code in ACLIB ?
****************************************************************************
ACLIB is shared with other models. Specific rules must be followed:

* Use explicit dimensions in variable declaration

* Do not add Méso-NH specific modules/variables into ACLIB, but add variables through the interfaces instead. 
  If a new specific module is needed, make sure that this module is Méso-NH agnostic (not dependent of other Méso-NH specific modules that would be incompatible with other host models)

* Use dedicated ACLIB custom types as it is implemented (e.g. use CST_ACLIB for constants and not MODD_CST from MesoNH world)

* Internal routines in :file:`src/ACLIB` must be agnostic from parallelization as much as possible to ease future use of cross-codes in different host models.
