Ocean-wave-atmosphere
===========================================================================
   
Description
----------------------------------------------------------------------------

Meso-NH can be coupled to an ocean model (e.g. `NEMO <https://nemo-ocean.eu>`_, `CROCO <https://www.croco-ocean.org>`_) and/or a wave model (e.g. `WW3 <https://polar.ncep.noaa.gov/waves/wavewatch/>`_) in order to represent air-sea interactions. Such coupled simulations rely on the `OASIS <https://oasis.cerfacs.fr/>`_ coupler, which is currently the only coupler implemented in Meso-NH.

This documentation describes how to set up and run a coupled simulation between Meso-NH and a `toy model <https://github.com/JorisPianezze/toy>`_ with the OASIS coupler. A simplified toy model is used here, rather than a full ocean/wave model, in order to focus on the coupling mechanism itself, independently of the complexity of a real ocean or wave model. This documentation does not contain detailed explanations on the use of OASIS. You are therefore advised to familiarize yourself with this library if you need more information.

.. note::

   The developments presented here were carried out within the Ocean-Wave-Atmosphere project group initiated by `CNRM <https://cnrm.sedoo.fr/>`_ around the `SURFEX <https://www.umr-cnrm.fr/surfex>`_ surface model, which is the surface interface model in Meso-NH used to compute air-sea fluxes :cite:p:`voldoire_surfex_2017,pianezze_new_2018`.

.. tip::

   If you are interested to run coupled simulations between Meso-NH, `CROCO <https://www.croco-ocean.org>`_ and/or `WW3 <https://polar.ncep.noaa.gov/waves/wavewatch/>`_, please go to this `dedicated documentation <https://recowa.readthedocs.io/en>`_.

.. warning::

   To be able to launch the applications described in the following sections, you have to :ref:`compile Meso-NH with OASIS <compile_mesonh_with_oasis>`. The toy model used in these applications is compiled during OASIS compilation. Nothing has to be compiled manually by users.

Examples
----------------------------------------------------------------------------

This section presents two examples of coupled simulations between Meso-NH and the toy model, both based on an idealized case in the Iroise Sea.

* In the :ref:`first example <owa_analytical>`, the toy model computes and sends an analytical field to Meso-NH, which is useful to test and validate the OASIS coupling implementation itself.

* In the :ref:`second example <owa_realistic>`, the toy model instead sends a realistic field read from a netCDF file (sea surface temperature from `CMEMS <https://marine.copernicus.eu>`_), which corresponds to a more typical use case where Meso-NH is forced by external, interactive oceanic data.

.. _owa_analytical:

Couple to an analytical field
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

To perform a Meso-NH simulation coupled to a toy model sending analytical field, you  need to :ref:`prepare the input files for Meso-NH <owa_analytical_input_mnh>`, :ref:`prepare the input files for the toy model <owa_analytical_input_toy>`, :ref:`prepare the input files for OASIS <owa_analytical_input_oasis>` and run the coupled simulations :ref:`(toy = wave model) <owa_analytical_run_wave>` and :ref:`(toy = ocean model) <owa_analytical_run_ocean>`. These steps are described in the following sections:

.. contents::
   :local:
   :depth: 1
   :backlinks: top

.. warning::

   This kind of simulation is parallelized and can has to be run with more than 1 core (at minimum 1 core for Meso-NH and 1 core for the toy model).

.. note::

   You can find all the namelists presented in this section as well as the scripts here:

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/examples/test_cases/013_Iroise_OASIS_coupling/
      
        - :dir:`folder` 1_input_mnh : directory to :ref:`prepare the input files for Meso-NH <owa_analytical_input_mnh>`
        - :dir:`folder` 2_input_toy : directory to :ref:`prepare the input files for the toy model <owa_analytical_input_toy>`        
        - :dir:`folder` 3_input_oasis : directory to :ref:`prepare the input files for the OASIS <owa_analytical_input_oasis>` 
        - :dir:`folder` A_cpl_mnh_toywav : directory to :ref:`run the coupled simulation (toy = wave model) <owa_analytical_run_wave>`        
        - :dir:`folder` B_cpl_mnh_toyoce : directory to :ref:`run the coupled simulation (toy = ocean model) <owa_analytical_run_ocean>`        

   The different steps must be performed in the order indicated by the directory numbers and letters.

.. tip::

   We recommend that you execute the steps one by one, by going to each folder and running the corresponding run_* scripts. However, it is also possible to launch the different steps using:
   
   .. code-block:: bash
      :substitutions:
      
      cd |MNH_directory_extract_current|/examples/test_cases/013_Iroise_OASIS_coupling/
      ./run_013_Iroise_OASIS_coupling

.. _owa_analytical_input_mnh:

Prepare the input files for Meso-NH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To prepare the input files for Meso-NH model, go to 1_input_mnh directory.
PREP_PGD and PREP_IDEAL_CASE steps are identical to an uncoupled simulation (without OASIS).

Run the following script to create the PGD and PREP_IDEAL_CASE files :

.. code-block:: bash

  run_prep_mesonh_xyz

At the end of run_prep_mesonh_xyz script, a rstrt_MNH.nc file is generated using the python script :command:`create_restart_file_from_PREP_IDEAL_CASE.py`.
This file contains the fields from the PREP_IDEAL_CASE file that will be sent to the toy model. It is essential to OASIS in order to start the coupled simulation.

.. note::

   The namelist EXSEG1.nam is also present in the 1_input_mnh directory. This namelist is used in the A_cpl_mnh_toy directory.

.. _owa_analytical_input_toy:

Prepare the input files for the toy model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To prepare the input files for toy model, go to 2_input_toy directory. A python script create_grid_and_restart_files_for_TOY_from_etopo2.py is used to generate a grid file read by the toy model from the etopo2.nc file. You need to enter the extension of your domain at the beginning of this script :

.. code-block:: python

   lon_domain = [-6.2, -4.0]
   lat_domain = [47.0, 49.5]


Run the following script to initialise the toy:

.. code-block:: bash

   run_prep_toy

This scrip create two files, the file grid_toy_model.nc contains the grid for the toy model and the file rst_T.nc contains the field to send to OASIS at the first time step.

.. note::

   * This script can also be used to generate a grid from a Meso-NH output, so that the toy model can have the same grid as Meso-NH.
   * This folder contains the namelists TOYNAMELIST.nam, which will be used in the A_cpl_mnh_toy directory. Go to the section about :ref:`RST TOY` for more information.

.. _owa_analytical_input_oasis:

Prepare the input files for OASIS 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To prepare the input files for toy model, go to 3_input_oasis directory.
This folder contains the namelist for OASIS called namcouple.
Information relating to the coupling is contained within this namelist. Go to the section about :ref:`RST OASIS` coupler for more information.

 The simulation lasts 360 seconds and the fields are exchanged every 60 seconds. Only two fields are exchanged. 10m u-wind speed is send by Meso-NH to the toy model using bilinear interpolation method (:command:`SCRIPR BILINEAR LR SCALAR LATLON 1`).
Toy model model send to Meso-NH an analytical field based on a sinusoidal function using distance weight interpolation method using 4 neighboors (:command:`SCRIPR DISTWGT LR SCALAR LATLON 1 4`).

Summary of necessary files for the coupled simulations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

==================  =========================================================
Model/Coupler       List of necessary files                  
==================  =========================================================
OASIS               namcouple
TOY                 TOYNAMELIST.nam, grid_toy_model.nc, rstrt_TOY.nc
Meso-NH             EXSEG1.nam, PGD and PREP_IDEAL_CASE files, rstrt_MNH.nc                
==================  =========================================================

.. _owa_analytical_run_wave:

Launch the coupled simulation (toy = wave model)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To launch the simulation go to A_cpl_mnh_toy directory and do :

.. code-block:: bash

   run_mesonh_xyz

.. note::

   This simulation take less than 20 seconds on a Linux laptot with a processor `Intel Core i7 <https://ark.intel.com/content/www/fr/fr/ark/products/208662/intel-core-i71165g7-processor-12m-cache-up-to-4-70-ghz.html>`_ at 2.8 Ghz.

This script is described below :

.. code-block:: bash

   #!/bin/bash
   
   echo '--------------------------------------'
   echo '    Run Meso-NH coupling              '
   echo '--------------------------------------'

   export PATH_EXETOY=${SRC_MESONH}/src/LIB/toy_1.0/

   #~~~~~ MESONH
   ln -sf ../1_input_mnh/IROISE_5KM* .
   ln -sf ../1_input_mnh/EXSEG1.nam .
   cp     ../1_input_mnh/rstrt_MNH.nc rst_A.nc

   #~~~~~ TOY
   ln -sf ../2_input_toy/grid_toy_model.nc .
   ln -sf ../2_input_toy/TOYNAMELIST.nam .
   cp     ../2_input_toy/rstrt_TOY.nc rst_T.nc

   #~~~~~ OASIS
   ln -fs ../3_input_oasis/namcouple .

   # ------------------------------------------
   time mpirun -np 1 $PATH_EXETOY/toy_model : -np 1 MESONH${XYZ}
   # ------------------------------------------                                           

.. note::

   Following files are created during the simulation :
   
   * **outputs for OASIS:** debug.01.000000, debug.02.000000, nout.000000, grids.nc, masks.nc, areas.nc, MNH__U10_mesonh_01.nc, MNH__CHA_mesonh_02.nc, VARRCV01_toyexe_01.nc, VARSIN01_toyexe_02.nc, rmp_ssea_to_toyt_BILINEAR.nc, rmp_toyt_to_ssea_DISTWGT_4.nc
   * **outputs for TOY:** OUTPUT_TOY.txt
   * **outputs for Meso-NH/SurfEX:** OUTPUT_LISTING0, OUTPUT_LISTING1, IROIS.1.00-01.000.des, IROIS.1.00-01.000.nc, IROIS.1.00-01.001.des, IROIS.1.00-01.001.nc

And this figure needs to be plotted (MY_RUN/KTEST/013_Iroise_OASIS_coupling/A_cpl_mnh_toy/U10_CHA/U10_CHA.png): 

.. figure:: U10_CHA.png

   The first line corresponds to the 10m u-wind speed sent from Meso-NH (a) to the toy model (b). The second line corresponds to the Charnock coefficient sent by the toy model (c) to Meso-NH (d).
   Differences are due to the interpolation method (:command:`SCRIPR BILINEAR LR SCALAR LATLON 1` for first line, :command:`SCRIPR DISTWGT LR SCALAR LATLON 1 4` for second line). 

.. _owa_analytical_run_ocean:

Launch the coupled simulation (toy = ocean model)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _owa_realistic:

Couple to a realistic field
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

In this example based on :ref:`RST Examples_Iroise_sea`, the toy send SST from CMEMS to Meso-NH. This kind of simulation is usually used when we want to force Meso-NH by an interactive SST and if we want to compare with coupled simulation with a 3d oceanic model.

You can copy/paste the structure of the :ref:`RST Examples_Iroise_sea` example :

.. code-block:: console

   ├── 1_input_mnh   : preparation of the input files for Meso-NH model
   ├── 2_input_toy   : preparation of the input files for toy model
   ├── 3_input_oasis : preparation of the input file  for OASIS
   └── A_cpl_mnh_toy : simulation's directory


Preparation of the input files for Meso-NH model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Same as :ref:`RST Examples_Iroise_sea` but you need now to use in EXSEG1.nam :

.. code-block:: fortran

   &NAM_SFX_SEA_CPL XTSTEP_CPL_SEA  =  60.0,
                    CSEA_FWSU       = 'MNH_TAUX',
                    CSEA_FWSV       = '        ',
                    CSEA_HEAT       = '        ',
                    CSEA_SNET       = '        ',
                    CSEA_WIND       = '        ',
                    CSEA_FWSM       = '        ',
                    CSEA_EVAP       = '        ',
                    CSEA_RAIN       = '        ',
                    CSEA_SNOW       = '        ',
                    CSEA_WATF       = '        ',
                    CSEA_PRES       = '        ',
                    CSEA_SST        = 'MNH__SST',
                    CSEA_UCU        = '        ',
                    CSEA_VCU        = '        ' /
                    
and put XTSTEP_CPL_WAVE=-1.0 to not activate coupling with wave model.

Preparation of the input files for toy model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To prepare the input files for toy model, go to 2_input_toy directory. A python script create_grid_and_restart_files_for_TOY_from_CMEMS_IBI.py is used to generate a netcdf files for the toy model from the CMEMS IBI file. But before using this script you need to extract SST file from CMEMS server. For that purpose, you can use following command :

.. code-block:: bash

   python -m motuclient --motu https://nrt.cmems-du.eu/motu-web/Motu                 \
                     --user <USER>    --pwd <PASSWORD>                             \
                     --service-id IBI_ANALYSISFORECAST_PHY_005_001-TDS            \
                     --product-id cmems_mod_ibi_phy_anfc_0.027deg-2D_PT1H-m        \
                     --longitude-min -6.2 --longitude-max -4.0 \
                     --latitude-min 47.0 --latitude-max 49.5 \
                     --date-min "2023-09-01 00:00:00" --date-max "2023-09-15 00:00:00" \
                     --variable thetao --variable uo --variable vo \
                     --out-dir ${PWD} \
                     --out-name sst_currents_20230901_20230915_IBI.nc

Then, you need to enter the extension of your domain at the beginning of the script create_grid_and_restart_files_for_TOY_from_CMEMS_IBI.py :

.. code-block:: python

   lon_domain = [-6.2, -4.0]
   lat_domain = [47.0, 49.5]


Then you have to change the name of the python script in script run_prep_toy and do:

.. code-block:: bash

   ./run_prep_toy

This scrip creates three files (1) grid_toy_model.nc which contains the grid for the toy model, (2) rst_T.nc which contains the field to send to OASIS at the first time step and (3) forcing_for_toy.nc which contains hourly SST from CMEMS server with new variables names.

In TOYNAMELIST.nam you need to change following namelist :

.. code-block:: fortran

   &nam_fct_send type_send='files',
                 forcing_file_name='forcing_for_toy.nc' /

   &nam_send_fields nsend_fields=1,
                    name_send_fields(1)='TOY__SST' /

.. note::

   * This script can also be used to generate a grid from a Meso-NH output, so that the toy model can have the same grid as Meso-NH.
   * This folder contains the namelists TOYNAMELIST.nam, which will be used in the A_cpl_mnh_toy directory. Go to the section about :ref:`RST TOY` for more information.

Preparation of the input files for OASIS 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Same as :ref:`RST Examples_Iroise_sea` but you need to use for the exchanged fields :

.. code-block:: fortran

   #                     -----------------------------------------
   #                        MESONH (mesonh) ==> TOY (toyexe)
   #                     -----------------------------------------
   #
   #~~~~~~~~~~~
   # Field 1 : 
   #~~~~~~~~~~~
   MNH_TAUX VARRCV01 1 60 1 rst_A.nc EXPOUT
   20 20 80 91 ssea toyt LAG=+10
   R  0  R  0
   SCRIPR
   BILINEAR LR SCALAR LATLON 1
   #
   #                     ------------------------------------------
   #                        TOY (toyexe) ==> MESONH (mesonh)
   #                     ------------------------------------------
   #
   #~~~~~~~~~~~
   # Field 2 : 
   #~~~~~~~~~~~
   TOY__SST MNH__SST 1 60 2 rst_T.nc EXPOUT
   80 91 20 20 toyt ssea LAG=+60
   R  0  R  0
   BLASNEW SCRIPR
   1.0 1
   CONSTANT 273.15
   DISTWGT LR SCALAR LATLON 1 4

Summary of necessary files for the coupled simulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

==================  =========================================================
Model/Coupler       List of necessary files                  
==================  =========================================================
OASIS               namcouple
TOY                 TOYNAMELIST.nam, grid_toy_model.nc, forcing_for_toy.nc, rstrt_TOY.nc
Meso-NH             EXSEG1.nam, PGD and PREP_IDEAL_CASE files, rstrt_MNH.nc                
==================  =========================================================

Launch the coupled simulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To launch the simulation go to A_cpl_mnh_toy directory and do :

.. code-block:: bash

   run_mesonh_xyz

.. note::

   This simulation take less than 20 seconds on a Linux laptot with a processor `Intel Core i7 <https://ark.intel.com/content/www/fr/fr/ark/products/208662/intel-core-i71165g7-processor-12m-cache-up-to-4-70-ghz.html>`_ at 2.8 Ghz.

This script is described below :

.. code-block:: bash

   #!/bin/bash
   
   echo '--------------------------------------'
   echo '    Run Meso-NH coupling              '
   echo '--------------------------------------'

   export PATH_EXETOY=${SRC_MESONH}/src/LIB/toy_1.0/

   #~~~~~ MESONH
   ln -sf ../1_input_mnh/IROISE_5KM* .
   ln -sf ../1_input_mnh/EXSEG1.nam .
   cp     ../1_input_mnh/rstrt_MNH.nc rst_A.nc

   #~~~~~ TOY
   ln -sf ../2_input_toy/grid_toy_model.nc .
   ln -sf ../2_input_toy/forcing_for_toy.nc .   
   ln -sf ../2_input_toy/TOYNAMELIST.nam .
   cp     ../2_input_toy/rstrt_TOY.nc rst_T.nc

   #~~~~~ OASIS
   ln -fs ../3_input_oasis/namcouple .

   # ------------------------------------------
   time mpirun -np 1 $PATH_EXETOY/toy_model : -np 1 MESONH${XYZ}
   # ------------------------------------------                                           

.. note::

   Following files are created during the simulation :
   
   * **outputs for OASIS:** debug.01.000000, debug.02.000000, nout.000000, grids.nc, masks.nc, areas.nc, MNH_TAUX_mesonh_01.nc, MNH__SST_mesonh_02.nc, VARRCV01_toyexe_01.nc, TOY__SST_toyexe_02.nc, rmp_ssea_to_toyt_BILINEAR.nc, rmp_toyt_to_ssea_DISTWGT_4.nc
   * **outputs for TOY:** OUTPUT_TOY.txt
   * **outputs for Meso-NH/SurfEX:** OUTPUT_LISTING0, OUTPUT_LISTING1, IROIS.1.00-01.000.des, IROIS.1.00-01.000.nc, IROIS.1.00-01.001.des, IROIS.1.00-01.001.nc

And you will have this figure : 

.. figure:: TAUX_SST.png

   The first line corresponds to the 10m u-wind speed sent from Meso-NH (a) to the toy model (b). The second line corresponds to the sea surface temperature sent by the toy model (c) to Meso-NH (d).
   Differences are due to the interpolation method (:command:`SCRIPR BILINEAR LR SCALAR LATLON 1` for first line, :command:`SCRIPR DISTWGT LR SCALAR LATLON 1 4` for second line). 


Technical information
----------------------------------------------------------------------------

OASIS
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The information presented in this section is described in detail in the OASIS user guide (https://verc.enes.org/oasis/).
The OASIS source code is either available in the Meso-NH version in the src/LIB/oasis3-mct_5.0/ folder (if you are using a Meso-NH version greater than or equal to 5.3.0)
or by downloading it from the OASIS website. 

To sum up, OASIS3-MCT is fully parallelized, has no executable specific to the coupler, is capable of managing 2d and 3d coupling field exchanges, is capable of supporting unstructured meshes, is capable of transferring fields in parallel, across all source or target component processes, has a namelist that allows the coupling characteristics to be changed without having to recompile the codes (type of interpolation, simulation duration, exchange time, etc.).


Installation and compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the folder containing the OASIS code (src/LIB/oasis3-mct_5.0/), following directories are presented:

.. code-block:: bash

   doc/                 : Documentation
   lib/                 : Libraries : mct, psmile and scrip
   pyoasis/             : API for python
   util/load_balancing/ : Tools for load balancing analysis
   util/make_dir/       : Makefiles

It is important to compile OASIS with the same libraries (NetCDF, MPI, etc.) as those that will be used that will be used for the code you wish to couple. So, if you decide to change one of these libraries, you will have to recompile OASIS and the codes
with this new library.

To compile OASIS manually, you need to modify the make.inc file in the util/make_dir folder according to the desired libraries, then
run the following commands:

.. code-block:: bash

   cd oasis_dir/util/make_dir/
   make realclean -f TopMakefileOasis3
   make -f TopMakefileOasis3

Functions implemented in models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using OASIS involves an instrumentation phase which consists of placing the various calls to the OASIS3-MCT routines in the codes (in this case Meso-NH and
TOY). The use of a specific precompilation key is used if you want to compile Meso-NH linking to OASIS. This key is called CPLOASIS.

OASIS3-MCT is used in the following phases:

* **initialisation phase:**

  * oasis_init_comp : initialization of the coupling
  
  * oasis_get_localcomm : creation by OASIS3-MCT of a local (to the model) MPI communicator. This new communicator must be used throughout the model (a precompilation key is used to force the model to use this communicator in the case of a coupled run).

* **definition of interpolation grids:**

  The interpolation methods used in OASIS call files created during this step.
  Once defined, the interpolation grids are stored in netcdf files: grids.nc, area.nc and mask.nc.
  These files contain the grids for all the coupled models.
  The OASIS functions used in this step are:

  * oasis_start_grids_writing : starts writing grid files, masks, ...

  * oasis_write_grid defines model grids (essential for CONSERV or SCRIP interpolation).

  * oasis_write_corner defines the corners of model grids: essential for CONSERV or SCRIP interpolation.)

  * oasis_write_mask defines the mask.

  * oasis_write_area which defines the area of the meshes

  * oasis_terminate_grids_writing which is used to finish writing.

  At the end of these stages, netcdf files are generated by OASIS: grids.nc, areas.nc and masks.nc with information about the different grids.
  The creation of these files is completed by calling the oasis_enddef routine, which is located after the local partitions have been defined.
  The creation of the grids requires the variables to be in global physical space (without the halo).


* **definition of local partitions:**

  description of the local partitions of each of the processes in the space of global indexes:

  * oasis\_def\_partition: with the following main arguments:

    * ig\_paral: used to describe local partitions, in particular to say whether
      in the case of sequential or parallel execution, and in the second case,
      what type of partition it is

    * isize: used to specify the size of the global grid for which data is
      data is actually exchanged. This optional parameter is
      important, particularly when, for a given model, certain parts of its domain are not
      are not included in the calculation. For example, for an ocean model
      land points are excluded from the calculation but are still part of the
      grid. OASIS is able to manage this situation thanks to this parameter.

  At the end of this step, netcdf files with weights for interpolations (remapping) from one grid to another are generated: rmp*.nc.

* **declaration of coupling fields:** 
  
  declare the fields that will be received and sent. These fields must all be identified in the namcouple described below. To do this, use the function:

  * oasis_def_var

* **end of initialisation phase:**

  * oasis_enddef: the grid definition files are created at this point.

* **exchange of coupling fields:**

  calls to the routines that allow to send and receive data are placed in the model time-stepping.

  * oasis_get : at the beginning of the loop to receive fields.

  * oasis_put : at the end of the time loop, to send fields.

  The coupled models cannot start at the same time because the fields are received at the beginning of the time loop (before they are sent).
  It is therefore necessary to time-shift (the notion of LAG, which will be described later) the coupled models so that each oasis_get coincides with an oasis_put and vice versa.
  The fields received by the model which first makes an oasis_get will come from a previously created rstrt.nc files.

* **end of coupling:**

  * oasis_terminate

Description of the namcouple
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The namcouple file is the namelist for the OASIS coupler, which contains all the information relating to exchanges between models.
It follows a syntax which is clearly explained in the OASIS3-MCT user manual. There are no blank lines!
Since there is no syntax check on this file, the slightest error will result in a crash with no error indication.

First of all, we need to declare the general parameters of the coupled simulation: the number of coupling fields, the number of models, the name of the models (identical to what is given to OASIS via the oasis\_init\_comp routine): mesonh (for Meso-NH) and toyexe (for the toy model), the duration of the simulation in seconds (it has to be the same for both models).

All these parameters are used to write the first part of the namcouple.

.. code-block:: bash

   # This is a typical input file for OASIS3-MCT.
   # Keywords used in previous versions of OASIS3 
   # but now obsolete are marked "Not used"
   # Don't hesitate to ask precisions or make suggestions (oasishelp@cerfacs.fr). 
   #
   # Any line beginning with # is ignored. Blank lines are not allowed.
   #
   #########################################################################
   $NFIELDS
   # The number of fields described in the second part of the namcouple.
   #
               2
   $END
   #########################################################################
   $NBMODEL
   # The number of models in this experiment + their names (6 characters)
   #
     2  mesonh   toyexe
   $END
   ###########################################################################
   $RUNTIME
   # The total simulated time for this run in seconds
   #
    70
   $END
   ###########################################################################
   $NLOGPRT
   # Amount of information written to OASIS3-MCT log files (see User Guide)
   # Premier nombre: quantite d'information pour debugger
   # Second nombre: statistics des processeurs
    30 3
   $END

The second part of the namcouple concerns exchanges between models. You need to have a precise idea of the coupling algorithm you want to implement.
you want to implement. First of all, we need to decide on a coupling period for the different fields.

It is not possible to give a coupling period shorter than the largest time step of the models.
In addition, the coupling period must be proportional to the model time steps and must be positive; reals are not allowed.
OASIS only sends data when a send date corresponds to a receive date,
It is therefore necessary to ensure that the coupling period is such that the two models can "meet".

You also need to choose the type of interpolation for the transition from one grid to another.

.. note::

   It is possible to choose different exchange periods and interpolations for each exchanged field.

We are particularly interested in the namcouple parameters for the exchange of SST exchange in the context of the coupling between Meso-NH and TOY. This case is sufficiently generic to be adapted to other exchanges:

.. code-block:: fortran

   #~~~~~~~~~~~
   # Field 1 : SEA SURFACE TEMPERATURE
   #~~~~~~~~~~~
   (l.1) TOY__SST MNH__SST 1 10 3 rstrt.nc EXPOUT
   (l.2) 321 194 100 87 toy mnht LAG=+10
   (l.3) R 0 R 0
   (l.4) LOCTRANS BLASOLD SCRIPR
   (l.5) AVERAGE
   (l.6) 1.0 1
   (l.7) CONSTANT 273.15
   (l.8) BILINEAR LR SCALAR LATLON 1

* (l.1) : here we have the field identifier, with the one on the source side (TOY__SST) and then the one on the target side (MNH__SST). The
  following parameter is not used but must be present to ensure compatibility with the older version of OASIS. Next, we have the coupling period for this exchange
  (10 seconds), the number of operations that will be applied to this field, the name of the restart file and the status of the field.
* (l.2) : the dimensions of the source (toyt) and target (mnht) grids, their names and the value of the LAG where applicable.
  if applicable. The grids here are those in the grids.nc, masks.nc and areas.nc files.
* (l.3) : characteristics of the source and target grids ("R": regional and "0": no overlapping
  overlap of grid points).
* (l.4 à 8) : list of operations to be performed on this field, followed by the parameters for each of these
  operations:
  
  * LOCTRANS : temporal transformation - AVERAGE (l. 5)
  * BLASOLD: multiplication of the field by 1 (l. 6) to which is added the value 273.15 (l. 7): conversion from Kelvin to Celsius.
  * SCRIPR: interpolation whose parameters are supplied (l. 8): in this case bilinear interpolation

.. note::

   You need to repeat this block for each coupling fields.

Meso-NH/SurfEx
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

77 functions have been modified/created to cover the implementation of coupling in Meso-NH/SurfEx: 9 functions concern Meso-NH and 66 SurfEx.
These functions are described in the routines. Only the tree structure and the steps for compiling Meso-NH are described in this section.

Tree structure of Meso-NH/SurfEx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   -- mesonh.f90
     |-- sfx_oasis_init.f90
         |-- OASIS *oasis_init_comp*
         |-- OASIS *oasis_get_localcomm*
     |-- init_mnh.f90
         |-- init_ground_paramn.f90
             |-- init_surf_atmn.f90
                 |-- init_sean.f90
                     |-- init_seafluxn.f90
     |-- sfx_oasis_read_nam.f90
     |-- mnh_oasis_grid.f90
         |-- OASIS *oasis_start_grids_writing*
         |-- OASIS *oasis_write_grid*
         |-- OASIS *oasis_write_corner*
         |-- OASIS *oasis_write_area*
         |-- OASIS *oasis_write_mask*
         |-- OASIS *oasis_terminate_grids_writing*
     |-- mnh_oasis_define.f90
         |-- sfx_oasis_define.f90
             |-- OASIS *oasis_def_partition*
             |-- OASIS *oasis_def_var*
             |-- OASIS *oasis_enddef*
     |** start time-stepping **|
     |-- modeln.f90
     |-- phys_paramn.f90
         |-- ground_paramn.f90
             |-- mnh_oasis_recv.f90
                 |-- sfx_oasis_recv.f90
                     |-- OASIS *oasis_get*
                 |-- put_sfxcpln.f90
                     |-- put_sfx_land.f90
                     |-- put_sfx_sea.f90
                     |-- put_sfx_wave.f90
             |** go to SurfEx **|
             |-- coupling_surf_atmn.f90
                 |-- coupling_sean.f90
                     |-- coupling_seaflux_orogn.f90
                         |-- coupling_seawat_sbln.F90
                             |-- coupling_seafluxn.f90
                                 |-- coare30_seaflux.f90
                                     |-- coare30_flux.f90
             |** end of SurfEx **|
             |-- mnh_oasis_send.f90
                 |-- get_sfx_lake.f90
                 |-- get_sfx_land.f90
                 |-- get_sfx_sea.f90
                 |-- get_sfx_wave.f90
                 |-- sfx_oasis_send.f90
                     |-- OASIS *oasis_put*
      |** end of time-stepping **|
      |-- sfx_oasis_end.f90
          |-- OASIS *oasis_terminate*


Preparing initial files for Meso-NH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The coupling only affects the simulation (MESONH executable). The initial Meso-NH files for a simulation are therefore obtained in the same way as for a forced simulation as for a forced simulation. The initial files will come from the PREP\_PGD and PREP\_REAL\_CASE or PREP\_IDEAL\_CASE stages.

It is necessary to have an rstrt.nc file which will allow the model starting first, which needs to receive a field via oasis\_get, to read the field in the rstrt.nc file.
This rstrt.nc file can be created using the python script used in KTEST.

Description of the EXSEG1.nam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Namelists specific to the coupling have been created and are presented below. The other namelists for EXSEG1.nam are identical to an uncoupled simulation.

&NAM_OASIS

==================  ===================  ===============  =============================
Name                Type                 Default          Signification
==================  ===================  ===============  =============================
LOASIS              LOGICAL              .False.          Activate OASIS
LOASIS_GRID         LOGICAL              .False.          Create grids and rmp files
CMODEL_NAME         CHARACTER            'mesonh'         Model name
==================  ===================  ===============  =============================

.. note::

   CMODEL_NAME name must the same as the one in namcouple.

&NAM_SFX_SEA_CPL

==================  ===================  ===============  ======================================================
Name                Type                 Default          Signification
==================  ===================  ===============  ======================================================
XTSTEP_CPL_SEA      REAL                 -1.0             Coupling time-step for oceanic fields
CSEA_FWSU           CHARACTER(LEN=8)     \-               OASIS name for the u-momentum flux (send)
CSEA_FWSV           CHARACTER(LEN=8)     \-               OASIS name for the v-momentum flux (send)
CSEA_HEAT           CHARACTER(LEN=8)     \-               OASIS name for the non-solar heat flux (send)
CSEA_SNET           CHARACTER(LEN=8)     \-               OASIS name for the solar flux (send)
CSEA_WIND           CHARACTER(LEN=8)     \-               OASIS name for the wind speed (send)
CSEA_FWSM           CHARACTER(LEN=8)     \-               OASIS name for the momentum flux (send)
CSEA_EVAP           CHARACTER(LEN=8)     \-               OASIS name for the evaporation flux (send)
CSEA_RAIN           CHARACTER(LEN=8)     \-               OASIS name for the rain flux (send)
CSEA_SNOW           CHARACTER(LEN=8)     \-               OASIS name for the snow flux (send)
CSEA_WATF           CHARACTER(LEN=8)     \-               OASIS name for the freshwater flux (send)
CSEA_PRES           CHARACTER(LEN=8)     \-               OASIS name for the surface pressure (send)
CSEA_SST            CHARACTER(LEN=8)     \-               OASIS name for the sea surface temperature (received)
CSEA_UCU            CHARACTER(LEN=8)     \-               OASIS name for the u-surface current (received)
CSEA_VCU            CHARACTER(LEN=8)     \-               OASIS name for the v-surface current (received)
==================  ===================  ===============  ======================================================

.. note::

   * The CSEA_* character strings correspond to the OASIS names of the variables exchanged between the ocean and the atmosphere and must be identical to those present in the namcouple. This identifier must be 8 characters long. An empty space of 8 characters corresponds to the default value: no exchange of this variable.
   * XTSTEP_CPL_SEA equal to -1 indicates no coupling with the ocean.


&NAM_SFX_WAVE_CPL

==================  ===================  ===============  ======================================================
Name                Type                 Default          Signification
==================  ===================  ===============  ======================================================
XTSTEP_CPL_WAVE     REAL                 -1.0             Coupling time-step for wave fields
CWAVE_U10           CHARACTER(LEN=8)     \-               OASIS name for the 10m u-wind speed (send)  
CWAVE_V10           CHARACTER(LEN=8)     \-               OASIS name for the 10m v-wind speed (send)  
CWAVE_CHA           CHARACTER(LEN=8)     \-               OASIS name for the Charnock coefficient (received)   
CWAVE_UCU           CHARACTER(LEN=8)     \-               OASIS name for the u-surface current (received)
CWAVE_VCU           CHARACTER(LEN=8)     \-               OASIS name for the v-surface current (received)  
CWAVE_HS            CHARACTER(LEN=8)     \-               OASIS name for the significant wave height (received)       
CWAVE_TP            CHARACTER(LEN=8)     \-               OASIS name for the peak period (received)          
==================  ===================  ===============  ======================================================

.. note::

   * The CWAVE_* character strings correspond to the OASIS names of the variables exchanged between the oceanic wave and the atmosphere and must be identical to those present in the namcouple. This identifier must be 8 characters long. An empty space of 8 characters corresponds to the default value: no exchange of this variable.
   * XTSTEP_CPL_WAVE equal to -1 indicates no coupling with the oceanic wave.
   * The choice of the parameterisation of turbulent fluxes with waves is made with &NAM_SEAFLUXn NGRWAVES and is only available with CSEA_FLUX='COARE3'. Please refer to the `SURFEX <https://www.umr-cnrm.fr/surfex/>`_ documentation for more details.

.. note::

   You need to use &NAM_DIAG_SURFn N2M=2 / namelist in order to compute sea surface fluxes.
   The rest of the namelist is identical to the case without coupling.


Toy model
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The toy model that has been developed for the Meso-NH/SurfEx coupling with OASIS is inspired by the toy models available in the OASIS tutorial. It has been completely rewritten in version 570 of Meso-NH. This toy model simulates an ocean or wave model that can be coupled with Meso-NH.
There is no physics involved in this model, which simply sends and receives fields without modifying them.
Among other things, it can be used to test the coupling algorithm used.

Toy model tree structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tree structure of the toy model and the various calls to OASIS functions are presented here:

.. code-block:: console

   -- toy_model.F90
      |-- OASIS *oasis_init_comp*
      |-- OASIS *oasis_get_localcomm*
      |-- read_namelist.F90
      |-- read_dimgrid.F90
      |-- read_grid.F90
      |-- OASIS *oasis_start_grids_writing*
      |-- OASIS *oasis_write_grid*
      |-- OASIS *oasis_write_corner*
      |-- OASIS *oasis_write_area*
      |-- OASIS *oasis_write_mask*
      |-- OASIS *oasis_terminate_grids_writing*
      |-- decomp_def.F90
      |-- OASIS *oasis_def_partition*
      |-- OASIS *oasis_def_var*
      |-- OASIS *oasis_enddef*
      |** start time-stepping **
      |-- OASIS *oasis_get*
      |-- get_values_to_send.F90
          |-- read_forcing.F90
      |-- OASIS *oasis_put*
      |** end of time-stepping **
      |-- OASIS *oasis_terminate*


Toy model compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To compile the toy model, In the toy folder there are :

.. code-block:: console

  readme   : a documentation file
  Makefile : the makefile for the toy model
  *.F90    : the source files

The toy model supplied with Meso-NH is compiled automatically when Meso-NH is compiled (like OASIS) but it may be necessary to modify it and then recompile it.

To compile the toy model manually, do

.. code-block:: bash

   cd src/
   . ../conf/profile_mesonh
   make toy

Description of the TOYNAMELIST.nam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use the toy model, you also need to create a TOYNAMELIST.nam with the following namelists :

* &nam_grid

==================  ==================  ===============  ================
Name                Type                Default          Signification
==================  ==================  ===============  ================
ntime_steps         INTEGER             \-               Nb of time step
time_step           REAL                \-               Time step [s]
grid_file_name      CHARACTER(LEN=30)   \-               Grid file name
==================  ==================  ===============  ================


* &nam_fct_send

==================  ==================  ===============  ================================================================================================================
Name                Type                Default          Signification
==================  ==================  ===============  ================================================================================================================
type_send           CHARACTER(LEN=5)    \-               Type of field send to Meso-NH ('cnste', 'sinus', 'files')       
forcing_file_name   CHARACTER(LEN=30)   \-               If type_send = 'files', forcing_file_name is the name of the netcdf file.
value_send          REAL                \-               | If type_send = 'cnste', value_send corresponds to the value of the field which will be homogeneous over the zone.
                                                         | If type_send = 'sinus' then value_send will be equal to the amplitude of the sine.
==================  ==================  ===============  ================================================================================================================

* &nam_recv_fields

==================  ======================  ===============  ================================================================================================================
Name                Type                    Default          Signification
==================  ======================  ===============  ================================================================================================================
nrecv_fields        INTEGER                 \-               Nb of fields received by the toy model
name_recv_fields    | CHARACTER(LEN=8,      \-               OASIS name for the fields received by the toy model
                    | DIM=nrecv_fields)                    
==================  ======================  ===============  ================================================================================================================

.. note::

   name_recv_fields name must the same as the one in namcouple and must be 8 characters long

* &nam_send_fields

==================  =====================  ===============  ================================================================================================================
Name                Type                   Default          Signification
==================  =====================  ===============  ================================================================================================================
nsend_fields        INTEGER                \-               Nb of fields send by the toy model
name_send_fields    | CHARACTER(LEN=8,     \-               OASIS name for the fields send by the toy model
                    | DIM=nsend_fields)                   
==================  =====================  ===============  ================================================================================================================

.. note::

   name_send_fields name must the same as the one in namcouple and must be 8 characters long

TOYNAMELIST.nam example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is an example of a 3600s simulation, with a time step of 60s.
The grid and mask definition file is called grid_toy_model.nc. The 3 fields sent come from the file named wave.nc.
The OASIS identifiers for the 3 fields sent are: VARSND01, VARSND02 and VARSND03. 2 fields are received by the toy and have identifiers VARRCV01 and VARRCV02.

.. code-block:: fortran

   &nam_grid ntime_steps=60,
             time_step=60,
             grid_file_name='grid_toy_model.nc' /

   &nam_fct_send type_send='files',
                 forcing_file_name='wave.nc',
                 value_send=10 /

   &nam_recv_fields nrecv_fields=2,
                    name_recv_fields(1)='VARRCV01',
                    name_recv_fields(2)='VARRCV02' /

   &nam_send_fields nsend_fields=3,
                    name_send_fields(1)='VARSND01',
                    name_send_fields(2)='VARSND02',
                    name_send_fields(3)='VARSND03' /
