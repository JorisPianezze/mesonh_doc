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

News from the support team
************************************

New versions
  - Version 5.7.3 was released on 4 May 2026; here is the `release note <https://mesonh.readthedocs.io/en/mnh-master/getting_started/releases/release_note_573.html#release-note-573>`_ for this version.
  - Version 6.0.1 was released on 10 July 2026; here is the `release notes <https://mesonh.readthedocs.io/en/mnh-6-0/getting_started/releases/release_note_601.html>`_. We strongly recommend that you upgrade to this new version, particularly users of AROME files (for initialisation and pairing) dated 15 October 2024 or later (cy48).
  - Following the new branch management and naming policy (see below), minor versions (the X.Y part of the X.Y.Z version numbering scheme) will be supported for two years from the release date of the next minor version. Maintenance means that we will continue to release versions containing only bug fixes (the letter Z in the X.Y.Z version numbering scheme).
  - Finally, we are launching a continuous integration trial on GitLab: as soon as a development change is ready for integration, you can send it to us (it must be merged with at least the latest published minor version, which is currently 6.0). Note to developers: **There will be no further calls for contributions**.

Branch management and naming
  - A new policy for branch management and naming has been introduced. It is set out in detail `here <https://mesonh.readthedocs.io/en/mnh-6-0/documentation/coding_instructions.html#branch-management-strategy>`_ and also in the Git repository in the ``BRANCHING.md`` file. Specific rules have been established for managing release, development and bug branches. Specific courses for researchers are also on offer. This structure is not final, and adjustments will be made as required and in response to feedback from everyone.
  - The immediate result of this new approach is a major overhaul, which is largely complete. Many obsolete courses have been removed, whilst most of the remaining ones have been renamed. If you are using the repository, you will probably need, at the very least, to re-establish the link between your local branches and the remote branches in the repository. To do this, the command ``git branch -u origin/new_branch_name`` (run from the relevant local branch) will help you to **restore tracking**.

Meso-NH Users’ Forum 1
  - On 3 June 2026, the first forum was held at the Midi-Pyrénées Observatory. Four new developments were presented and discussed with 33 participants, both in person and online. There were plenty of questions and two cakes at the end of the drinks reception to celebrate the new version of Méso-NH! The presentations focused on:
  - The **new organisational structure** centred on the Méso-NH code and service, including, amongst other things, the creation of the Scientific Committee and the Supervisory Committee
  - **Version 6** and all its new features!
  - The **two new websites**: a `showcase site <https://mesonh.cnrs.fr/ >`_ to discover Méso-NH and encourage people to use it, and a `technical site <https://mesonh.readthedocs.io>`_ to guide you through getting started with the model and to find all the documentation, including the user guide.
  - A **graphical user interface** for Méso-NH to assist users in creating their *namelists*, domains and forcings, as well as for visualising simulations. It is available (beta version) online `here <https://mesonh.streamlit.app/>`_ (except for Workspace) or locally `here <https://github.com/QuentinRodier/mesonh-interface>`_ (tested only on PC and Belenos).

Scientific Committee 1
  The first scientific committee meeting took place on 1 July 2026. Chaired by Christelle Barthe and Didier Ricard, it brought together numerous code developers and members of the department. After a brief update on recent developments, the discussion focused on cloud microphysics in Méso-NH. Céline Planche (LaMP) was invited as an expert on this topic.

Kairos Meso-Challenge (CALMIP)
  Part of the department was involved in the Kairos Meso-Challenge, named after the new supercomputer commissioned at the CALMIP (Calcul en Midi-Pyrénées) mesocentre, located at the Espace Clément Ader in Toulouse. Simulations of Tropical Storm Ianos were carried out using the coupled CROCO–Meso-NH models – quite a technical challenge on this new machine!

