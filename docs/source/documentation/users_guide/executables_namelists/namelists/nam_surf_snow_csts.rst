.. _nam_surf_snow_csts:

NAM_SURF_SNOW_CSTS
------------------

.. csv-table:: NAM_SURF_SNOW_CSTS content 
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "XZ0ICEZ0SNOW", "REAL", "10."
   "XRHOTHRESHOLD_ICE", "REAL", "850."
   "XALBICE1", "REAL", "0.38"
   "XALBICE2", "REAL", "0.23"
   "XALBICE3", "REAL", "0.08"
   "XVAGING_NOGLACIER", "REAL", "60."
   "XVAGING_GLACIER", "REAL", "900."
   "XPERCENTAGEPORE", "REAL", "0.05"
   "XPERCENTAGEPORE_FRZ", "REAL", "1.0"
   "XVVISC3", "REAL", "0.023"
   "X_RI_MAX", "REAL", "0.20"
   "XIMPUR_WET", "REAL, DIMENSION(5)", "0.,0.,0.,0.,0."
   "XIMPUR_DRY", "REAL, DIMENSION(5)", "0.,0.,0.,0.,0."
   "XPSR_SNOWMAK", "REAL", "0.0012"
   "XRHO_SNOWMAK", "REAL", "600"
   "XPTA_SEUIL", "REAL", "268"
   "XPR_A", "REAL", "0."
   "XPR_B", "REAL", "0."
   "XPT", "REAL", "0."
   "XPP_D1", "REAL", "0."
   "XPP_D2", "REAL", "0."
   "XPP_D3", "REAL", "0."
   "XPP_H1", "REAL", "0."
   "XPP_H2", "REAL", "0."
   "XPP_H3", "REAL", "0."
   "XPP_H4", "REAL", "0."
   "XWT", "REAL", "0."
   "XPTR", "REAL", "0."
   "XPROD_SCHEME", "REAL, DIMENSION(5)", "2500, 5000, 4000, 2500, 1000"
   "XSM_END", "REAL, DIMENSION(4)", "4, 15, 4, 15"
   "XFREQ_GRO", "INTEGER", "1"
   "XSCAVEN_COEF", "REAL, DIMENSION(5)", "0.,0.,0.,0.,0."
   "XAGELIMPAPPUS", "REAL", "0.05"
   "XWINDTHRFRESH", "REAL", "6.0"
   "XRHODEPPAPPUS", "REAL", "250"
   "XDIAMDEPPAPPUS", "REAL", "0.0003"
   "XSPHDEPPAPPUS", "REAL", "1.0"
   "XLFETCHPAPPUS", "REAL", "250"
   "XAGELIMPAPPUS2", "REAL", "0.05"
   "XDEMAXVFALL", "REAL", "0.3"
   "XCROCOEF_FF", "REAL", "1.0"

* :code:`XZ0ICEZ0SNOW` : roughness length ratio between ice and snow

* :code:`XRHOTHRESHOLD_ICE` : density threshold for ice detection in CROCUS scheme (kg.m$^{-3}$)

* :code:`XALBICE1, XALBICE2, XALBICE3` : prescribed ice albedo in 3 spectral bands for glacier simulation with CROCUS scheme

* :code:`XVAGING_NOGLACIER, XVAGING_GLACIER` : for ageing effects

* :code:`XPERCENTAGEPORE` : percentage of the total pore volume to compute the max liquid water holding capacity

* :code:`XPERCENTAGEPORE_FRZ` : 

* :code:`XVVISC3` : density adjustement in the exponential correction for viscosity (in m$^{3}$.kg$^{-1}$)

* :code:`XIMPUR_WET` : corresponds to the initial amount of Light-Absorbing Particles (LAP) present in the falling snow

* :code:`XIMPUR_DRY` : corresponds to the dry deposition coefficient (always activated) at top of snowpack (in g/m$^{2}$/s) for black carbon (XIMPUR_DRY(1)), dust (XIMPUR_DRY(2)), and other types of impurities (XIMPUR_DRY(3:5))

* :code:`XPSR_SNOWMAK` : Machine-made snow precipitation rate (in kg/m$^{2}$/s)

* :code:`XRHO_SNOWMAK` : Machine-made snow density (kg/m$^{3}$)

* :code:`XPTA_SEUIL` : Wet but temperature threshold for machine-made snow production (K)

* :code:`XPR_A` : Adjustable coefficients depending on snow-gun type (Hanzer et al., 2014). Recommended value= -3.94

* :code:`XPR_B` : Adjustable coefficients depending on snow-gun type (Hanzer et al., 2014). Recommended value= -4.23

* :code:`XPT` : Water consumption threshold during base-layer generation production period (kg/m$^{2}$). Recommended value = 150

* :code:`XPP_D1` : Day of beginning (from 1$^{st}$ of December, with 31 days for all months) of base-layer generation production period (recommended value 1$^{st}$ of November=11*31+1=342). For CROCUS resort only.

* :code:`XPP_D2` : Day of end (from 1$^{st}$ of December, with 31 days for all months) of base-layer generation production period (recommended value 15$^{th}$ of December=12*31+15=387). For CROCUS resort only.

* :code:`XPP_D3` : Day of end (from 1$^{st}$ of December, with 31 days for all months) of reinforcement production period (recommended value 31$^{th}$ of March=3*31+31=124). For CROCUS resort only.

* :code:`XPP_H1` : Hour of beginning of base-layer generation production period (in seconds, from midnight). Production during this period is allowed all day (0s to 86400s). For CROCUS resort only.

* :code:`XPP_H2` : Hour of end of base-layer generation production period (in seconds, from midnight). Production during this period is allowed all day (0s to 86400s). For CROCUS resort only.

* :code:`XPP_H3` : Hour of beginning of reinforcement production period (in seconds, from midnight). Production during this period is allowed from 6pm (64800s) to 8am (28800s). For CROCUS resort only.

* :code:`XPP_H4` : Hour of end of reinforcement production period (in seconds, from midnight). Production during this period is allowed from 6pm (64800s) to 8am (28800s). For CROCUS resort only.

* :code:`XWT` : Wind speed threshold for snowmaking (m/s). Recommended value = 4.2

* :code:`XPTR` : Total (natural+machine-made) snow height threshold during reinforcement production period (m). Recommended value = 0.6

* :code:`XPROD_SCHEME` : Snow production by machines in Crocus-RESORT. When LSELF_PROD=F, the production is forced to match to production scheme defined by XPROD_SCHEME. For Nov, Dec, Jan, Feb and Mar, every day at 18:00, a production counter is compared to the target. If it's lower, the production is allowed.

* :code:`XSM_END` : Month and day to stop grooming in Crocus-RESORT. (for LSNOWMAK_BOOL = F and for LSNOWMAK_BOOL = T, respectively)

* :code:`XFREQ_GRO` : Grooming frequency (usually 1/day)

* :code:`XSCAVEN_COEF` : percentage of impurity leaving with percolating water, for black carbon (XSCAVEN_COEF(1)), dust (XSCAVEN_COEF(2)), and other types of impurities (XSCAVEN_COEF(3:5))

* :code:`XAGELIMPAPPUS` : maximum age (days) of snow layer for which wind speed threshold is set to fresh threshold wind speed

* :code:`XWINDTHRFRESH` : 5m wind speed threshold for transport of freshly fallen (or deposited) snow

* :code:`XRHODEPPAPPUS` : density (kg.m$^{-3}$) of wind blown deposited snow

* :code:`XDIAMDEPPAPPUS` : optical diameter (m) of wind blown deposited snow

* :code:`XSPHDEPPAPPUS` : sphericity of wind blown deposited snow

* :code:`XLFETCHPAPPUS` : constant fetch distance applied to all points for snowpappus blowing snow flux calculation (m)

* :code:`XAGELIMPAPPUS2` : maximum age (in days) of snow for using Naaim96 formulation of terminall fall speed in snowpappus

* :code:`XDEMAXVFALL` : maximum dendricity to have pure young snow fall speed, when option MIXT is chosen for terminal fall speed calculation (CLIMVFALL=’MIXT’ in NAM_ISBA_SNOW)

* :code:`XCROCOEF_FF` : to have the possibility to change the coefficient for gust diagnosis from average wind (ie to have XCOEF_FF value outside of Crocus and XCROCOEF_FF inside Crocus)

