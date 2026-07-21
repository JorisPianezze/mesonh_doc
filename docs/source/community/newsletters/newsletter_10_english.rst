Newsletter #10
================================================

**22 July 2026.** English version, version française `ici <newsletter_10.html>`_.


Dear Méso-NH users,

Below is the 10th newsletter from our community. In it, you’ll find an interview with the developer of a tool that may prove very useful to you, **plenty** of news from the support team, and a list of the latest publications using Meso-NH.

Interview with `Clément Soufflet <mailto:clement.soufflet@univ-reunion.fr>`_ (LACy)
******************************************************************************************************************

|pic1|

.. |pic1| image:: photo_cs.jpg
  :width: 400

Clément, you developed FrameIt to make it easier to analyse cyclone simulations. FrameIt is particularly well suited to Méso-NH users. Could you summarise what this tool does?

  **FrameIt** is a tool developed at LACy by the Cyclones and Tropical Meteorology team, specifically by Kevin Hoarau, Adrien Colomb, Rémi Laxenaire and myself. In its first version, this tool is designed as a model output data management tool, written entirely in Python and based on the *xarray* library. The idea behind the development of **FrameIt** stems from the analysis of cyclone simulations, which require a large domain, but where only a small part (the cyclone) is of real interest to us.

  **FrameIt** allows you to extract a time-varying mobile (or fixed) subdomain centred on a meteorological object, whilst selecting the variables and vertical levels of interest. This subdomain is also available in polar coordinates centred on the object under study. The output consists of a series of very lightweight *netCDF* files, sorted by coordinate system and dimension, covering the desired subdomain and containing all time steps of the simulation.

  It is worth noting that **FrameIt** can process both *netCDF* files from Méso-NH and *grib* files from the AROME model.

How does this make life easier for modellers?

  **FrameIt** does not replace the analysis of standard output files, but it enables users to get to grips with these files quickly by eliminating the issues associated with data management and the processing of large data files. In other words, it is a tool that facilitates analysis by reducing the size of the files and standardising them in relation to the meteorological phenomenon under study.

  In addition, **FrameIt** allows data to be analysed in a polar coordinate system, which is useful for meteorological objects with azimuthal symmetry.

  Finally, as the output consists of relatively small *netCDF* files, **FrameIt** helps to facilitate the sharing of simulation data, particularly in the context of collaborations with non-modelling researchers (and thus contributes to raising the profile of Méso-NH).
