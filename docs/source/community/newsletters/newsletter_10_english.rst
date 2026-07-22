Newsletter #10
================================================

**22 July 2026.** English version, version française `ici <newsletter_10.html>`_.


Dear Meso-NH users,

Below is the 10th newsletter from our community. In it, you’ll find an interview with the developer of a tool that may prove very useful to you, **plenty** of news from the support team, and a list of the latest publications using Meso-NH.

Interview with `Clément Soufflet <mailto:clement.soufflet@univ-reunion.fr>`_ (LACy)
******************************************************************************************************************

|pic1|

.. |pic1| image:: photo_cs.jpg
  :width: 400

Clément, you developed FrameIt to make it easier to analyse cyclone simulations. FrameIt is particularly well suited to Meso-NH users. Could you summarise what this tool does?
  **FrameIt** is a tool developed at LACy by the Cyclones and Tropical Meteorology team, specifically by Kevin Hoarau, Adrien Colomb, Rémi Laxenaire and myself. In its first version, this tool is designed as a model output data management tool, written entirely in Python and based on the *xarray* library. The idea behind the development of **FrameIt** stems from the analysis of cyclone simulations, which require a large domain, but where only a small part (the cyclone) is of real interest to us.

  **FrameIt** allows you to extract a time-varying mobile (or fixed) subdomain centred on a meteorological object, whilst selecting the variables and vertical levels of interest. This subdomain is also available in polar coordinates centred on the object under study. The output consists of a series of very lightweight *netCDF* files, sorted by coordinate system and dimension, covering the desired subdomain and containing all time steps of the simulation.

  It is worth noting that **FrameIt** can process both *netCDF* files from Meso-NH and *grib* files from the AROME model.

How does this make life easier for modellers?
  **FrameIt** does not replace the analysis of standard output files, but it enables users to get to grips with these files quickly by eliminating the issues associated with data management and the processing of large data files. In other words, it is a tool that facilitates analysis by reducing the size of the files and standardising them in relation to the meteorological phenomenon under study.

  In addition, **FrameIt** allows data to be analysed in a polar coordinate system, which is useful for meteorological objects with azimuthal symmetry.

  Finally, as the output consists of relatively small *netCDF* files, **FrameIt** helps to facilitate the sharing of simulation data, particularly in the context of collaborations with non-modelling researchers (and thus contributes to raising the profile of Meso-NH).

Are there any other, non-cyclonic situations in which **FrameIt** would also be useful?
  At present, **FrameIt** is mainly used for cyclone simulations, but this tool is not limited to that. In my view, **FrameIt** is particularly useful in cases where the domain of a numerical simulation is much larger than the meteorological phenomenon under study, but also in cases where a polar coordinate system facilitates the analysis of the meteorological phenomenon in question.

What advice would you give to Meso-NH users who’d like to start using it?
  Naturally, my first recommendation would be to consult the fairly comprehensive documentation for the project on `Météo France’s GitHub <https://meteofrance.github.io/frameit/>`_. Installing and using **FrameIt** requires a specific conda virtual environment, the installation of which is described in this documentation.

  Next, you’ll need to familiarise yourself with the syntax of the tool’s single configuration file, an example of which is available in the project. And finally, of course, start with a simple case that you’re already familiar with, involving just a few files, to get the hang of it.

What are the current limitations? Do you have any plans for future developments? 
  One aspect of **FrameIt** that may, at first glance, seem limiting is its focus on the study of cyclones. In fact, the object-tracking method is designed for tropical cyclones and is not applicable to all other meteorological objects. However, to overcome this limitation, users have the option of providing a predefined trajectory to guide the extraction for the meteorological object of their choice. That said, **FrameIt** has been designed to be modular (Git), specifically to enable interested users to develop useful features for the community themselves. It is therefore entirely feasible to develop a new tracking method associated with another type of meteorological feature (convective cell, thunderstorm, etc.). Indeed, there is a section in the documentation dedicated to the integration of new tracking methods.

  This initial version will serve as the basis for numerous future developments, notably the calculation of diagnostics specific to cyclones, which will be available in the tool’s output files.

  Finally, as one of the research areas at LACy focuses on ocean–atmosphere interactions, the aim is eventually to be able to apply this tool to ocean and wave model outputs from coupled simulations in order to gain an overview of the interactions between these three compartments.


.. note::

  If you’d also like to explain a feature you’ve implemented in Meso-NH, or an analytical method you’d like to share with the community, please do let me know by `email <mailto:thibaut.dauhut@utoulouse.fr>`_.

News from the support team
************************************

New versions
  - Version 5.7.3 was released on 4 May 2026; here is the `release note <https://mesonh.readthedocs.io/en/mnh-master/getting_started/releases/release_note_573.html#release-note-573>`_ for this version.
  - Version 6.0.1 was released on 10 July 2026; here is the `release note <https://mesonh.readthedocs.io/en/mnh-6-0/getting_started/releases/release_note_601.html>`_. We strongly recommend that you upgrade to this new version, particularly users of AROME files (for initialisation and pairing) dated 15 October 2024 or later (cy48).
  - Following the new branch management and naming policy (see below), minor versions (the X.Y part of the X.Y.Z version numbering scheme) will be supported for two years from the release date of the next minor version. Maintenance means that we will continue to release versions containing only bug fixes (the letter Z in the X.Y.Z version numbering scheme).
  - Finally, we are launching a continuous integration trial on GitLab: as soon as a development change is ready for integration, you can send it to us (it must be merged with at least the latest published minor version, which is currently 6.0). Note to developers: **There will be no further calls for contributions**.

Branch management and naming
  - A new policy for branch management and naming has been introduced. It is set out in detail `here <https://mesonh.readthedocs.io/en/mnh-6-0/documentation/coding_instructions.html#branch-management-strategy>`_ and also in the Git repository in the ``BRANCHING.md`` file. Specific rules have been established for managing release, development and bug branches. Specific courses for researchers are also on offer. This structure is not final, and adjustments will be made as required and in response to feedback from everyone.
  - The immediate result of this new approach is a major overhaul, which is largely complete. Many obsolete courses have been removed, whilst most of the remaining ones have been renamed. If you are using the repository, you will probably need, at the very least, to re-establish the link between your local branches and the remote branches in the repository. To do this, the command ``git branch -u origin/new_branch_name`` (run from the relevant local branch) will help you to **restore tracking**.

Meso-NH Users’ Forum 1
  - On 3 June 2026, the first forum was held at the Midi-Pyrénées Observatory. Four new developments were presented and discussed with 33 participants, both in person and online. There were plenty of questions and two cakes at the end of the drinks reception to celebrate the new version of Meso-NH! The presentations focused on:
  - The **new organisational structure** centred on the Meso-NH code and service, including, amongst other things, the creation of the Scientific Committee and the Supervisory Committee
  - **Version 6** and all its new features!
  - The **two new websites**: a `showcase site <https://mesonh.cnrs.fr/>`_ to discover Meso-NH and encourage people to use it, and a `technical site <https://mesonh.readthedocs.io>`_ to guide you through getting started with the model and to find all the documentation, including the user guide.
  - A **graphical user interface** for Meso-NH to assist users in creating their *namelists*, domains and forcings, as well as for visualising simulations. It is available (beta version) online `here <https://mesonh.streamlit.app/>`_ (except for Workspace) or locally `here <https://github.com/QuentinRodier/mesonh-interface>`_ (tested only on PC and Belenos).

Scientific Committee 1
  The first scientific committee meeting took place on 1 July 2026. Chaired by Christelle Barthe and Didier Ricard, it brought together numerous code developers and members of the department. After a brief update on recent developments, the discussion focused on cloud microphysics in Meso-NH. Céline Planche (LaMP) was invited as an expert on this topic.

Kairos Meso-Challenge (CALMIP)
  Part of the department was involved in the Kairos Meso-Challenge, named after the new supercomputer commissioned at the CALMIP (Calcul en Midi-Pyrénées) mesocentre, located at the Espace Clément Ader in Toulouse. Simulations of Tropical Storm Ianos were carried out using the coupled CROCO–Meso-NH models – quite a technical challenge on this new machine!

Documentation
  The documentation on the `technical website <https://mesonh.readthedocs.io>`_ is the result of a long-term effort to maintain and update it. Gone are the days of PDF files and Ctrl+F searches (though, to be fair, this is still possible for those who are nostalgic). We invite you to browse this site to find all the important information, for example on installing the model, setting up simulations and all the possible parameters for *namelists*.

Further developments and information
  - Development work is underway on the **implementation of surface fluxes and turbulence**, as well as the merging of tridiagonal matrix solutions between shallow convection and turbulence, with a view to improving vertical numerical stability relative to the model’s time step.
  - **Multiple time series** will be possible for **frequent outputs**. This feature allows you to create several separate sets of frequently generated output files. These sets are entirely independent (choice of fields, output times, selected boxes, compression settings, etc.). They will be available from version 6.1 of Meso-NH (before the end of the year).
  - Registration for the **Meso-NH training course** is now open for the session from 2 to 5 November, delivered in French and in person `here <https://mesonh.readthedocs.io/en/mnh-master/documentation/tutorial_material.html>`_.
  - Philippe Wautelet is currently compiling, with the help of the entire Meso-NH team, a list of all the challenges and technical issues we are facing or are likely to face. The aim is to gain as comprehensive and accurate a picture of the situation as possible, so that we can determine our technical development priorities. **Please do not hesitate to contact us if you wish to report any technical requirements or difficulties**.

.. note::
  If you have any requirements, ideas, suggestions for improvements, bugs to fix or suggestions regarding Meso-NH, `Philippe Wautelet <mailto:philippe.wautelet@cnrs.fr>`_ and the whole team would be delighted to hear from you.

Latest publications using Meso-NH
****************************************************************************************

Convection
  - Dataset of a Kilometer-Scale Meso-NH Simulation for C2OMODO: The RCElarge300 Collection of MesoNHforC2OMODO [`Chaboureau <https://doi.org/10.1016/j.dib.2026.112954>`_, 2026]
  - Exploring the influence of equatorial waves on a record‐breaking extreme precipitation event in Central Sahel: Insights from convection permitting simulations [`Diakhaté et al. <https://doi.org/10.1029/2026GL122000>`_, 2026]
  - A parametrization of the convective boundary layer with subgrid orography [`Philippot et al. <https://doi.org/10.1175/JAS-D-25-0192.1>`_, 2026]

Urban meteorology
  - The Paris 2024 Olympics Research Demonstration Project [`Masson et al. <https://doi.org/10.1175/BAMS-D-25-0008.1>`_, 2026]
  - Coupling the atmospheric model Meso-NH-v5.5 with the Monte-Carlo solver of conductive-radiative-convective heat exchanges stardis-v0.11.1 to calculate the surface energy balance of complex geometries [`Schoetter et al. <https://doi.org/10.5194/egusphere-2026-2061>`_, *in discuss.* 2026]

Wind energy
  - Multi-scale simulations of wind farm impacts on nighttime near-surface temperature in complex terrain [`Boumendil et al. <https://doi.org/10.5194/wes-2026-84>`_, *in discuss.* 2026]

.. note::

   If you’d like to share with the community the news that one of your projects using Meso-NH has received funding, or any other updates on your work (including posters and presentations *available online*), please feel free to `email me <mailto:thibaut.dauhut@utoulouse.fr>`_. I’m also always keen to hear your feedback on the newsletters.

Have a lovely summer and enjoy your simulations with Meso-NH!

See you soon,

Thibaut Dauhut et the whole Meso-NH team : Philippe Wautelet, Quentin Rodier, Didier Ricard, Joris Pianezze, Juan Escobar et Jean-Pierre Chaboureau

