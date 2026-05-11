.. _nam_isba_snown:

NAM_ISBA_SNOWn
--------------

.. csv-table:: NAM_ISBA_SNOWn content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CSNOWDRIFT", "CHARACTER(LEN=4)", "'DFLT'"
   "LSNOWDRIFT_SUBLIM", "LOGICAL", "F"
   "LSNOW_ABS_ZENITH", "LOGICAL", "F"
   "CSNOWMETAMO", "CHARACTER(LEN=3)", "'B92'"
   "CSNOWMOB", "CHARACTER(LEN=4)", "'GM98'"
   "CSNOWRAD", "CHARACTER(LEN=3)", "'B92'"
   "LATMORAD", "LOGICAL", "F"
   "LSNOWSYTRON", "LOGICAL", "F"
   "CSNOWFALL", "CHARACTER(LEN=3)", "'V12'"
   "CSNOWCOND", "CHARACTER(LEN=3)", "'Y81'"
   "CSNOWHOLD", "CHARACTER(LEN=3)", "'B92'"
   "CSNOWCOMP", "CHARACTER(LEN=3)", "'B92'"
   "CSNOWZREF", "CHARACTER(LEN=3)", "'CST'"
   "LSNOWCOMPACT_BOOL", "LOGICAL", "F"
   "LSNOWMAK_BOOL", "LOGICAL", "F"
   "LSNOWMAK_PROP", "LOGICAL", "F"
   "LSNOWTILLER", "LOGICAL", "F"
   "LSELF_PROD", "LOGICAL", "F"
   "LSNOWPAPPUS", "LOGICAL", "F"
   "CSNOWPAPPUSERODEPO", "CHARACTER(LEN=3)", "'DIV'"
   "CSNOWFPAPPUS", "CHARACTER(LEN=4)", "'NONE'"
   "CPAPPUSSUBLI", "CHARACTER(LEN=4)", "'NONE'"
   "CSALTPAPPUS", "CHARACTER(LEN=3)", "'P90'"
   "CLIMVFALL", "CHARACTER(LEN=4)", "'MIXT'"
   "OPAPPULIMTFLUX", "LOGICAL", "F"
   "OPAPPUDEBUG", "LOGICAL", "F"

* :code:`CSNOWDRIFT` : key to activate the snowdrift scheme, with 4 possible values

  * NONE: snowdrift scheme disactivated (equivalent to LSNOWDRIFT=F in SURFEX V8.1)
  * DFLT: Default snowdrift scheme activated, properties of falling snow are purely dendritic (equivalent to LSNOWDRIFT = T in SURFEX V8.1)
  * VI13: Properties of falling snow are taken from Vionnet et al. (2013)
  * GA01: Properties of falling snow are taken from Gallée et al. (2001)
* :code:`LSNOWDRIFT_SUBLIM` : logical for snowdrift subliation

* :code:`LSNOW_ABS_ZENITH` : if T modify solar absorption as a function of solar zenithal angle (physically wrong but better results in polar regions when CSNOWRAD=B92)

* :code:`CSNOWMETAMO` : Scheme of snow metamorphism (Crocus)

  * B92: obsolete option which will be removed in a next version. Historical version, Brun et al. 1992
  * C13: Translation of B92 option in terms of Optical Diameter and spericity (Carmagnola et al 2014)
  * T07: Experimental evolution law of optical diameter from Taillandier et al 2007
  * F06: Evolution law of the optical diameter from Flanner et al 2006, which fitst the model outputs of a snow microstructure model representing the diffusive vapour fluxes among the grains.
  * S-C: Experimental evolution law of Optical Diameter from Schleef et al, 2014 for the first 48 hours after snowfall, then C13 option.
  * S-F: Experimental evolution law of Optical Diameter from Schleef et al, 2014 for the first 48 hours after snowfall, then F06 option.
* :code:`CSNOWMOB` : To choose the way threshold wind speed is computed in SnowPappus when surface snow age is superior to the threshold value XAGELIMPAPPUS

  * GM98: (default) historical version, Guyomarc'h et Mérindol (1998), see SnowPappus description article
  * CONS: threshold wind speed constant and equal to 9 m/s (at 5m height)
  * VI12: parameterization described in Vionnet et al 2012
  * LI07: parameterization as a function of density as described in Liston et al. 2007
  * COGM: constant at 9 m/s if snow is non-dendritic, given by GM98 parameterization for dendritic snow
* :code:`CSNOWRAD` : radiative transfer scheme in snow (Crocus)

  * B92: historical version, Brun et al. 1992 with empirical parameterization of ageing in the visible band (default)
  * T17: 2 flow spectral scheme TARTES (Libois et al, 2013) with explicit impact of SSA, impurities, and zenithal angle on spectral reflectances. Increase computing time by a factor of 10. Require a careful setting of impurities deposition.
* :code:`LATMORAD` : key to activate atmotartes scheme

* :code:`LSNOWSYTRON` : to activate the blowing snow module SYTRON (Vionnet et al. 2018) which simulates erosion and accumulation between opposite slope aspects in the topographic-based geometry used by MF operational simulations for avalanche hazard forecasting. This option must be maintained to FALSE in all other simulation geometries. It is recommended to combine LSNOWSYTRON=T with CSNOWDRIFT=VI13 (better skill scores in terms of blowing snow occurrence)

* :code:`CSNOWFALL` : parametrization of falling snow compaction

  * V12: function of air temperature and wind speed following Vionnet et al 2012 from experiments of Pahaut at Col de Porte (default)
  * S14: function of air temperature and wind speed following Schmucki et al 2014, law used in the swiss SNOWPACK model
  * A76: function of air temperature from Anderson, 1976 (law used in ISBA-ES)
  * NZE: constant at 200 kg/m$^{3}$ for maritime climates (New Zealand)
* :code:`CSNOWCOND` : parameterization of snow thermal conductivity from snow density

  * Y81: Yen et al 1981 (Default) from experimental values
  * I02: rom ISBA-ES (Boone, 2002; Sun et al., 1999) The law depends not only on density but also on snow temperature and it has a higher conductivity than experimental values to indirectly compensate for the fact that latent heat fluxes due to vapour fluxes are not represented in the model. This is expected to increase vertical heat transfer as temperature increases.
* :code:`CSNOWHOLD` : parameterization of maximum liquid water holding capacity in the bucket parameterization

  * B92: fixed maximal percentage of the pores’ volumes from Pahaut 1975
  * SPK: parameterization of the swiss SNOWPACK model (Wever et al 2014) fitting the experiments of Coléou and Lesaffre (1998)
  * B02: maximal liquid water mass fraction. This parameterization has an opposite behaviour: the higher the density, the higher the maximal volumetric liquid water content.
* :code:`CSNOWCOMP` : parameterization of snow compaction

  * B92: visco-elastic model using a viscosity function of density and air temperature from Brun et al, 1992 (default)
  * T11: visco-elastic model using a viscosity function of density and air temperature from Teufelsbauer (2011) fitting the data of separate experimental works
  * S14: non-linear relationship between settlement, stress and SSA decrease due to metamorphism from Schleef et al. (2014) for the first 48 h after snowfall. Then, B92 option.
* :code:`CSNOWZREF` : Reference heights for temperature and wind can be modified depending on snow depth when CSNOWZREF=='VAR'

  * CST: constant reference
  * VAR: variable reference height from the snow surface (i.e. constant from the ground, snow depth has to be removed from reference height)
* :code:`LSNOWCOMPACT_BOOL` : Activate grooming if T. By default, grooming only applies if SWE > 20 kg/m$^{2}$ and between 20h and 21h (and also 6h-9h if there is some snowfall during the night)

* :code:`LSNOWMAK_BOOL` : Activate snowmaking By default, snowmaking only applies if the wind speed is < 10 km/h, during all the day during the period 01/11-15/12 and between 18h-8h during the period 15/12-31/03. During the first period (base-layer generation), the production is allowed until reaching a water consumption of 150 kg/m$^{2}$, according to an average water availability of = 1500 m$^{3}$/ha. During the second period (snowpack reinforcement), the production is allowed if the total (natural+machine-made) snow height is < 60 cm. Finally, a loss of 30% in the snow production process is applied in every condition.

* :code:`LSNOWMAK_PROP` : Activate machine made snow physical properties. The machine-made snow properties are set as follows: SSA = 23 m$^{2}$/kg, Sphericity = 0.9.

* :code:`LSNOWTILLER` : Switch for the activation of the tiller effect, which applies down to 35 kg/m$^{2}$ below the surface (F = no tiller effect, only compaction).

* :code:`LSELF_PROD` : Activate the control of snow production. If T, the production follows the pre-defined rules defined above (threshold of 150 kg/m$^{2}$ during the base-layer generation period, threshold of 60 cm during the snowpack reinforcement period).If F, the production is forced to match the pre-set production scheme defined by XPROD_SCHEME.

* :code:`LSNOWPAPPUS` : key to activate SnowPappus option.

* :code:`CSNOWPAPPUSERODEPO` : determines how the deposition flux is computed.

  * ERO: pure erosion (can be used in point-scale simulation)
  * DIV: erosion/deposition calculated (default option, needs 2D grid)
  * DEP: pure deposition (can be used in point-scale simulation)
  * NON: snowPappus diagnostics are computed but it does not adds or removes any snow (can be used in point-scale simulation)
* :code:`CSNOWFPAPPUS` : overcomes 'CSNOWDRIFT' to select falling snow microstructure.

  * GM98: Guyomarc'h and Merindol 1998
  * VI13: Vionnet 2013
  * NONE: no effect, CSNOWDRIFT prevails (default)
* :code:`CPAPPUSSUBLI` : to choose different parameterizations of blowing snow sublimation rate in SnowPappus

  * NONE: no sublimation in pappus transport scheme
  * SBSM: SBSM (Simplified Blowing Snow Model) sublimation parametrisation from R. Essery,L. Li, and J. Pomeroy (1999)
  * BJ10: Bintanja 1998 with 10m wind
  * BJ03: Bintanja 1998 with 3m wind
  * GR06: Gordon 2006 sublimation parameterization
* :code:`CSALTPAPPUS` : option for saltation transport in SnowPappus

  * P90: saltation transport given by Pomeroy 1990 formulation
  * S04: Sorensen 2004 / Vionnet 2012 formulation
* :code:`CLIMVFALL` : option to decide what is old or new snow for fall speed calculation

  * DEND: fall speed of blowing snow particles is computed as old snow if snow is non-dendritic
  * PREC: old snow = non-dendritic OR age < XAGELIMPAPPUS2
  * MIXT: old snow for non-dendritic, new snow for dendritic age < XAGELIMPAPPUS2 , weighted average if dendritic more aged snow
* :code:`OPAPPULIMTFLUX` : if True, snow transport flux limitation activated. It limits the flux on a pixel if there is not enough snow on it to avoid removing more snow than there is on it.

* :code:`OPAPPUDEBUG` : if True, triggers snowpappus debug mode. This option displays additional information on the computation. It displays warnings, SWE conservation verification results, time and date during computation for easier debugging. And proof of SnowPappus mass conservation.

