.. _extracticon:

Extract ICON data
===============================

ICON digestion in Meso-NH is only available since MNH-V6-0-0.

Data source
-------------------------------

The ICON model is run and support by several institues such as the german national weather services DWD among other (https://www.icon-model.org/about-us/icon-partners/icon-partners)
It is run in a global configuration; a limited-area configuration over europe ICON-EU at 7km resolution updated every 3 hours for the next 120 hours forecast.

The official website is https://www.icon-model.org/

For Meso-NH, only the ICON-EU and ICON-Global digestion was tested. 

Historical mode
*******************************

No data are publicly available

Operational mode
***********************************

A new cycle is run every 3 hours

ICON-EU: data are available here http://opendata.dwd.de/weather/nwp/icon-eu/grib/

ICON-Global: data are available here  http://opendata.dwd.de/weather/nwp/icon/grib/

Using ICON-EU
-------------------------------

Fill the HATMFILE field in PRE_REAL1.nam with the file name iconeu.RRz.HH.grib2 extracted with a script :file:`fetch_icon.sh` found in the :file:`examples/integration_cases/hpc/GRIB/ICONEU` test case.

You must also specify :ref:`_nam_real_conf` NVERLEVEL_GRIB=74

Using ICON-Global
-------------------------------

In examples/integration_cases/hpc/GRIB/ICONGLOBAL, there are scripts to :file:`fetch_icon.sh` ICON-global and :file:`icosahedral_to_latlon.sh` to convert the icosahedral ICON grid into a regular lat/lon grid.

Fill the HATMFILE field in PRE_REAL1.nam with the file name icon-global-latlon.grb extracted with a script found in the :file:`examples/integration_cases/hpc/GRIB/ICONGLOBAL` test case.

You must also specify :ref:`_nam_real_conf` NVERLEVEL_GRIB=120