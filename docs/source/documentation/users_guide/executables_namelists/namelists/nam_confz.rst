.. _nam_confz:

NAM_CONFZ
-----------------------------------------------------------------------------

.. csv-table:: NAM_CONFZ content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NZ_VERB","INTEGER","0"
   "NZ_PROC","INTEGER","0"
   "NB_PROCIO_R","INTEGER","1"
   "NB_PROCIO_W","INTEGER","1"
   "MPI_BUFFER_SIZE","INTEGER","40"
   "LMNH_MPI_BSEND","LOGICAL",".TRUE."
   "LMNH_MPI_ALLTOALLV_REMAP","LOGICAL",".FALSE."
   "NZ_SPLITTING","INTEGER","10"
   "NPMAX_T1DFLAT_R", "INTEGER","130"

* :code:`NZ_VERB`: level of message for NZ solver and I/O
              
* :code:`NZ_PROC`: number of processes to use in the Z splitting. The default value (0) yields an automatic calculation of the number.
             
* :code:`NB_PROCIO_R`: number of processes to use for parallel I/O when reading file. The default value (1) yields a reading from 1 file only. If more than 1 file, the 3D field are written as several 2D slices.

* :code:`NB_PROCIO_W`: Number of processes to use for parallel I/O when writing file. The default value (1) yields a writing into 1 file only. If more than 1 file, the 3D field are written as several 2D slices.
              
* :code:`MPI_BUFFER_SIZE`: default size for MPI_BSEND buffer in :math:`10^6` bytes. MPI_BUFFER_SIZE corresponds approximately to the size of the domain, that is, :math:`NX*NY*NZ` for I/O in 1 file, and :math:`NX*NY` for I/O in N 2D-slice files.

* :code:`LMNH_MPI_BSEND`: during HALO exchange and FFT transposition, switch to use bufferized either MPI_BSEND routine or asynchrone MPI_ISEND routine. Depending on the computer and size of the problem, one or the other option could run faster. MPI_ISEND also uses less memory so MPI_BUFFER_SIZE should be decreased.

* :code:`LMNH_MPI_ALLTOALLV_REMAP`:

  * FALSE: FFT remap with send/recv <=> NZ_SPLITTING=10
  * TRUE: FFT remap with mpi_alltoallv <=> NZ_SPLITTING=14 (BG/MPICH optimization) 

* :code:`NZ_SPLITTING`: setting by namelist for debugging by expert user only. The non-expert user will use LMNH_MPI_ALLTOALLV_REMAP=T/F only: IZ=1=flat_inv; IZ=2=flat_invz; IZ=1+2=the two; +8=P1/P2.

* :code:`NPMAX_T1DFLAT_R`: setting to determine the size of the memory buffer allocated for the GPU version of Meso-NH to store real fields.
  The total buffer size is this setting multiplied by the number of mesh points. This buffer is used to remove allocations and deallocations that are
  very costly on GPUs. This value can be increased when needed (if too small, an error will be raised at runtime),
  but it should not be too large to avoid wasting memory.
