Newsletter #11
================================================

**14 October 2026.** English version, version française `ici <newsletter_11.html>`_.


Dear Meso-NH users,

Below is the 11th newsletter from our community. In it, you’ll find an interview with the co-chairs of the Meso-NH brand-new Scientific Committee, news from the support team, and the list of the latest publications and project using Meso-NH.

Interview with `Christelle Barthe <mailto:christelle.barthe@cnrs.fr>`_ (LAERO) and `Didier Ricard <mailto:didier.ricard@meteo.fr>`_ (CNRM)
******************************************************************************************************************

|pic1|     |pic2|

.. |pic1| image:: photo_cb.png
  :width: 250

.. |pic2| image:: photo_dr.jpg
  :width: 250

Christelle and Didier, you are the co-chairs of the Meso-NH Scientific Committee. Could you explain what it is and who is involved?
  The organisation surrounding the Meso-NH community code has been thoroughly overhauled this year. In place of the Steering Committee that previously existed, two bodies have been created: a Scientific Committee and a Supervisory Committee, both of which work closely with the Meso-NH Service and its two divisions: the Technical Division and the User Division.

  The Scientific Committee (SC) is responsible for discussing, organising and evaluating the necessary developments to the Meso-NH code, ensuring that they are properly monitored. It organises quarterly meetings on specific topics or issues raised by developers or users, with a view to fostering interaction and co-development, and anticipating future changes to the model.

  The members of the Scientific Committee have been selected for their expertise in the scientific areas central to the development of the Meso-NH code (numerical schemes, convection, turbulence, microphysics, radiation, atmospheric electricity, aerosols, chemistry, urban schemes, the ocean and coupling, wildfires, wind turbines). Members of the SNO-CC (National Observation Service – Community Code) attend every meeting of the Scientific Committee, at which a specialist in the topic under discussion, from outside Meso-NH, is invited to provide a fresh perspective.

What is the aim of this Scientific Committee? What is its purpose?
  The primary aim of the Scientific Committee is to monitor scientific and technical developments in the Meso-NH model, define scientific priorities for the code’s development, and provide recommendations on priority technical developments to the Technical Division. 

What have you been able to discuss so far?
  The Scientific Committee met for the first time on 1 July 2026. In addition to general updates on the latest developments in Meso-NH, this first meeting focused on the representation of microphysics. The topics covered ranged from highly technical issues, such as consistency between the various microphysical variables, to topics at the interface with other Meso-NH schemes—such as the initialisation of the two-time-step scheme by aerosols—as well as longer-term projects such as the unification of microphysical schemes (KHKO, ICE3, LIMA) to facilitate their maintenance and use. Future developments in microphysics within Meso-NH were also discussed.

  The second meeting of the Scientific Committee took place on 23 September 2026. We began by reviewing the ongoing work on the microphysical schemes that had been agreed at the previous meeting, then discussed the next steps in porting Meso-NH to GPUs, and recent work on the implementation of surface fluxes was presented. An update on the Technical Division’s work and priorities was also presented by Philippe Wautelet.

What prospects do you see for the Scientific Committee?
  The forthcoming meetings will be devoted to issues or topics that require relatively swift attention (diagnostics in output files, numerical efficiency, simulation preparation steps, etc.) and which will help to improve the model’s usability and efficiency. We also wish to explore the role of AI in modelling, whilst continuing to invite specialists in the field to contribute.

.. note::

  If you too would like to explain a development you have implemented in Meso-NH, or an analytical method you wish to share with the community, please do not hesitate to let me know by `email <mailto:thibaut.dauhut@utoulouse.fr>`_.

News from the support team
************************************

New version
  Meso-NH version `5.7.4 <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/releases>`_ was released on 11 August 2026. All users of the 5.7 branch are encouraged to download and install this new *bug fix*, particularly if you use AROME files to initialise or force the model. Full details can be found in the release notes available via the link.

Development in progress
  - Multiple series of frequent outputs (independent time series with fine-grained selection of fields, sub-domains, compression parameters, etc.): implementation is now complete and has been tested. These will be available in the upcoming version 6.1 (scheduled for release in late 2026 or early 2027).
  - `Koda <https://src.koda.cnrs.fr/mesonh/mesonh-code>`_ software forge (code repository): gradual roll-out of continuous integration with automatic code verification (compilation, syntax, test cases, etc.).

Prioritising future developments
  An overview of “Technical challenges and difficulties” has been drawn up to provide a comprehensive picture of these issues and to prioritise the Technical Division’s actions in collaboration with the Meso-NH Scientific Committee. The `Technical Division <mailto:mesonhsupport@obs-mip.fr>`_ remains open to any new suggestions.

User Forum
  The next forum will be held towards the end of this year. This will be another opportunity for you to share any difficulties you are experiencing or suggestions for future developments. You can now complete the `survey <https://framadate.org/polls/4bf863f22a93203585b0>`_ to help choose the date for this upcoming forum. We will be discussing, in particular, which developments to prioritise.

Upcoming Meso-NH training sessions
  - 22–25 March 2027 (hybrid format, in English)
  - 15–18 November 2027 (face-to-face, in French)

.. note::
  If you have any requirements, ideas, suggestions for improvements, bugs to fix or feedback regarding Meso-NH, `Philippe Wautelet <mailto:philippe.wautelet@cnrs.fr>`_ and the whole team would be delighted to hear from you.


Latest publications and projects using Meso-NH
***************************************************************************************

Fire meteorology
  - Assessing the impact of forest canopy drag on experimental fire behavior using coupled atmosphere-fire large-eddy simulations [`Antolin et al. <http://dx.doi.org/10.1007/s10546-026-01001-7>`_, 2026]
  - From daily to hourly scale: improving fire weather index with high-resolution Meso-NH simulations [`Campos et al. <https://doi.org/10.1038/s41598-026-72729-y>`_, *in press*]
  - Multi-Scale High-Resolution Mapping of Wildfire Hotspots and Fire-Prone Areas Using Earth Observation and Atmospheric Modeling [`Couto et al. <https://doi.org/10.3390/geographies6030086>`_, 2026]

Surface wind and temperature
  - Meso to sub-mesoscale origins of strong surface winds and influence of surface waves in an extra-tropical cyclone [`Brumer et al. <https://egusphere.copernicus.org/preprints/2026/egusphere-2026-4453/>`_, *in discuss.*]
  - A neural network-based downscaling method for near surface temperature in urban areas [`García Cristóbal et al. <https://doi.org/10.1016/j.uclim.2026.103076>`_, 2026]
  - Complementarity between Large-Eddy Simulation and Synthetic-Aperture Radar observations to characterise surface wind in an extratropical cyclone [`Maury et al. <https://doi.org/10.5194/egusphere-2026-3679>`_, *in discuss.*]

Tropical meteorology
  - Characteristics of a multi-model ensemble of mock-Walker simulations [`O’Donnell et al. <https://doi.org/10.1029/2026MS005781>`_, 2026]
  - Localized precipitation enhancement induced by orography and wind dynamics in southern Réunion Island during Tropical Cyclone Batsirai [`Ramanamahefa et al. <https://doi.org/10.2139/ssrn.5529525>`_, *submitted*]
  - Le projet OrgAmazon (LAERO Univ. Toulouse & IAG Univ. São Paulo, 2027-2032) a été financé par l'ANR et la FAPESP, agence de recherche de l'état de São Paulo. Des simulations Meso-NH seront réalisées dans le but de comprendre l'évolution de l'organisation de la convection en Amazonie due au changement climatique et à la déforestation. Un déploiement instrumental autour du site d' `ATTO-Campina <https://doi.org/10.1175/BAMS-D-24-0092.1>`_ est prévu en 2030.

PhD thesis
  Interactions entre les éoliennes et la stratification de l'atmosphère : impacts sur la météorologie proche de la surface [`P. Boumendil <https://theses.fr/s415518>`_, Univ. Toulouse, 2026]




.. note::

   If you’d like to share with the community the news that one of your projects using Meso-NH has received funding, or any other updates on your work (including posters and presentations *available online*), please feel free to `email me <mailto:thibaut.dauhut@utoulouse.fr>`_. I’m also always keen to hear your feedback on the newsletters.

Happy simulating with Meso-NH!

See you soon,

Thibaut Dauhut and the whole Meso-NH team: Philippe Wautelet, Quentin Rodier, Didier Ricard, Joris Pianezze, Juan Escobar et Jean-Pierre Chaboureau
