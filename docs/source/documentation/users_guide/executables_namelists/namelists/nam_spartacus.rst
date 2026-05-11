.. _nam_spartacus:

NAM_SPARTACUS
-------------

.. csv-table:: NAM_SPARTACUS content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LDO_SW", "LOGICAL", "T"
   "LDO_LW", "LOGICAL", "T"
   "LUSE_SW_DIRECT_ALBEDO", "LOGICAL", "F"
   "LDO_VEGETATION", "LOGICAL", "T"
   "LDO_URBAN", "LOGICAL", "T"
   "N_VEGETATION_REGION_URBAN", "REAL", "1"
   "N_VEGETATION_REGION_FOREST", "REAL", "1"
   "NSW", "REAL", "1"
   "NLW", "REAL", "1"
   "N_STREAM_SW_URBAN", "REAL", "4"
   "N_STREAM_SW_FOREST", "REAL", "4"
   "N_STREAM_LW_URBAN", "REAL", "4"
   "N_STREAM_LW_FOREST", "REAL", "4"
   "LUSE_SYMMETRIC_VEGETATION_SCALE_URBAN", "LOGICAL", "F"
   "LUSE_SYMMETRIC_VEGETATION_SCALE_FOREST", "LOGICAL", "F"
   "XVEGETATION_ISOLATION_FACTOR_URBAN", "REAL", "0.0"
   "XVEGETATION_ISOLATION_FACTOR_FOREST", "REAL", "0.0"
   "XMIN_VEGETATION_FRACTION", "REAL", "1.0E-6"
   "XMIN_BUILDING_FRACTION", "REAL", "1.0E-6"

* :code:`LDO_LW` : if T, compute longwave fluxes

* :code:`LUSE_SW_DIRECT_ALBEDO` : if T, specify groud and roof albedos separately for direct solar radiation

* :code:`LDO_VEGETATION` : if T, vegetation will be represented

* :code:`LDO_URBAN` : if T, urban areas will be represented

* :code:`N_VEGETATION_REGION_URBAN` : Number of regions used to describe urban vegetation (2 needed for heterogeneity)

* :code:`N_VEGETATION_REGION_FOREST` : Number of regions used to describe forests (2 needed for heterogeneity)

* :code:`NSW` : Number of spectral bands for solar radiation

* :code:`NLW` : Number of spectral bands for infrared radiation

* :code:`N_STREAM_SW_URBAN` : Number of streams per hemisphere to describe shortwave radiation, urban areas

* :code:`N_STREAM_LW_URBAN` : Number of streams per hemisphere to describe longwave radiation, urban areas

* :code:`N_STREAM_SW_FOREST` : Number of streams per hemisphere to describe diffuse shortwave radiation, forests

* :code:`N_STREAM_LW_FOREST` : Number of streams per hemisphere to describe longwave radiation, forests

* :code:`LUSE_SYMMETRIC_VEGETATION_SCALE_URBAN` : If T tree crowns touch each other ; Eq. 2018 Hogan et al. (2018). If F tree crowns separate (shyness) ; Eq. 19 of Hogan et al. (2018).

* :code:`LUSE_SYMMETRIC_VEGETATION_SCALE_FOREST` : If T tree crowns touch each other ; Eq. 2018 Hogan et al. (2018).If F tree crowns separate (shyness) ; Eq. 19 of Hogan et al. (2018).

* :code:`XVEGETATION_ISOLATION_FACTOR_URBAN` : 0.0 = Dense vegetation region is embedded with in sparse region. 1.0 = Dense vegetation is in physically isolated regions

* :code:`XVEGETATION_ISOLATION_FACTOR_FOREST` : 0.0 = Dense vegetation region is embedded with in sparse region. 1.0 = Dense vegetation is in physically isolated regions

* :code:`XMIN_VEGETATION_FRACTION` : Minimum area fraction below which a vegetation region is removed completely.

* :code:`XMIN_BUILDING_FRACTION` : Minimum area fraction below which a building region is removed completely.

