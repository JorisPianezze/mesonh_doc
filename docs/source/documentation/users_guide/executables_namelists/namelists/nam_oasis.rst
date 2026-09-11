.. _nam_oasis:

NAM_OASIS
----------------------------------------------------------------------------- 

.. warning::

   This namelist comes from SURFEX code.

.. csv-table:: NAM_OASIS content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LOASIS", "LOGICAL", ".FALSE."
   "LOASIS_GRID", "LOGICAL", ".FALSE."
   "CMODEL_NAME", "CHAR(LEN=6)", "surfex"
   
* :code:`LOASIS` : flag to use OASIS coupler.

* :code:`LOASIS_GRID` : flag to define grids and remap files online (during the simulation).

* :code:`CMODEL_NAME` : model name for OASIS (namcouple).
