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

  Finally, as the output consists of relatively small *netCDF* files, **FrameIt** helps to facilitate the sharing of simulation data, particularly in the context of collaborations with non-modelling researchers (and thus contributes to raising the profile of Meso-NH).

Are there any other, non-cyclonic situations in which **FrameIt** would also be useful?
  At present, **FrameIt** is mainly used for cyclone simulations, but this tool is not limited to that. In my view, **FrameIt** is particularly useful in cases where the domain of a numerical simulation is much larger than the meteorological phenomenon under study, but also in cases where a polar coordinate system facilitates the analysis of the meteorological phenomenon in question.

What advice would you give to Méso-NH users who’d like to start using it?
  Naturally, my first recommendation would be to consult the fairly comprehensive documentation for the project on `Météo France’s GitHub <https://meteofrance.github.io/frameit/>`_. Installing and using **FrameIt** requires a specific conda virtual environment, the installation of which is described in this documentation.

  Next, you’ll need to familiarise yourself with the syntax of the tool’s single configuration file, an example of which is available in the project. And finally, of course, start with a simple case that you’re already familiar with, involving just a few files, to get the hang of it.

What are the current limitations? Do you have any plans for future developments? 
  One aspect of **FrameIt** that may, at first glance, seem limiting is its focus on the study of cyclones. In fact, the object-tracking method is designed for tropical cyclones and is not applicable to all other meteorological objects. However, to overcome this limitation, users have the option of providing a predefined trajectory to guide the extraction for the meteorological object of their choice. That said, **FrameIt** has been designed to be modular (Git), specifically to enable interested users to develop useful features for the community themselves. It is therefore entirely feasible to develop a new tracking method associated with another type of meteorological feature (convective cell, thunderstorm, etc.). Indeed, there is a section in the documentation dedicated to the integration of new tracking methods.

  This initial version will serve as the basis for numerous future developments, notably the calculation of diagnostics specific to cyclones, which will be available in the tool’s output files.

  Finally, as one of the research areas at LACy focuses on ocean–atmosphere interactions, the aim is eventually to be able to apply this tool to ocean and wave model outputs from coupled simulations in order to gain an overview of the interactions between these three compartments.


.. note::

  If you’d also like to explain a feature you’ve implemented in Méso-NH, or an analytical method you’d like to share with the community, please do let me know by `email <mailto:thibaut.dauhut@utoulouse.fr>`_.

