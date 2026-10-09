Infolettre #11
================================================

**12 octobre 2026.** Version française, English version `here <newsletter_11_english.html>`_.


Chers utilisateurs, chères utilisatrices de Méso-NH,

Voici ci-dessous la 11ème infolettre de notre communauté. Vous y trouverez un entretien avec l'animatrice et l'animateur du tout récent Comité scientifique de Méso-NH, les nouvelles de l’équipe support et la liste des dernières publications utilisant Méso-NH.

Entretien avec `Christelle Barthe <mailto:christelle.barthe@cnrs.fr>`_ (LAERO) et `Didier Ricard <mailto:didier.ricard@meteo.fr>`_ (CNRM)
******************************************************************************************************************

|pic1|     |pic2|

.. |pic1| image:: photo_cb.png
  :width: 250

.. |pic2| image:: photo_dr.jpg
  :width: 230

Christelle et Didier, vous êtes les animatrice et animateur du Comité scientifique de Méso-NH. Pourriez-vous nous expliquer ce que c'est, et qui y participe ?
  L'organisation autour du code communautaire Méso-NH a été repensée en profondeur cette année. En lieu et place du comité de pilotage qui existait auparavant, deux instances ont été créées : un Comité scientifique et un Comité des tutelles, en interactions fortes avec le Service Méso-NH et ses deux pôles : le Pôle technique et le Pôle utilisateur.ices.

  Le Comité scientifique (CS) a vocation à discuter, structurer et évaluer les développements nécessaires du code Méso-NH en assurant leur suivi. Il s’organise autour de réunions trimestrielles sur des thèmes ou problèmes spécifiques, soulevés par les développeur.euses ou les utilisateur.ices, afin de favoriser les interactions et le codéveloppement, et anticiper les évolutions du modèle.

  Les membres du comité ont été choisi.es pour leur expertise sur les thématiques scientifiques au cœur du développement du code Méso-NH (schémas numériques, convection, turbulence, microphysique, rayonnement, électricité atmosphérique, aérosols, chimie, schémas urbains, océan et couplage, feux, éoliennes). Les membres du SNO-CC (Service National d’Observation – Code Communautaire) participent à chaque réunion du Comité scientifique pendant laquelle un.e spécialiste de la thématique abordée, extérieur.e à Méso-NH, est invité.e pour nous apporter un regard neuf. 

Quel est l'objectif de ce Comité scientifique ? à quoi sert-il ?
  Le premier objectif du Conseil scientifique est de suivre les développements scientifiques et techniques du modèle Méso-NH, définir des priorités scientifiques de développement du code et donner des recommandations de développements techniques prioritaires au Pôle Technique. Le deuxième objectif est de faire remonter au Comité des tutelles les avancées, les difficultés rencontrées ainsi que les besoins identifiés nécessitant des moyens. Tout cela pour répondre aux priorités scientifiques du CNRS, de Météo-France et de la communauté des utilisateur.ices, et améliorer l’offre de service du code communautaire pour les applications académiques, appliquées et sociétales.

De quoi avez-vous pu discuter jusqu'à présent ?
  Le CS s’est réuni pour la première fois le 1er juillet 2026. En plus d’informations générales sur l’actualité de Méso-NH, cette première réunion a traité de la représentation de la microphysique. Les sujets abordés ont balayé des questions très techniques comme la cohérence entre les différentes variables microphysiques, des thèmes à la frontière avec d’autres schémas de Méso-NH comme l’initialisation du schéma à 2 moments par les aérosols, mais aussi des chantiers à plus long terme comme l’unification des schémas microphysiques (KHKO, ICE3, LIMA) pour faciliter leur maintenance et leur utilisation. Les évolutions futures de la microphysique dans Méso-NH ont aussi été évoquées. 

  La deuxième réunion du CS s’est tenue le 23 septembre 2026. Nous avons d’abord fait un retour sur les actions en cours sur les schémas microphysiques qui avaient été décidées à la précédente réunion, puis nous avons débattu de la suite du portage de Méso-NH sur GPU, et les travaux récents sur l’implicitation des flux de surface ont été présentés. Un point sur les travaux et priorités du Pôle technique a également été présenté par Philippe Wautelet.

Quelles perspectives voyez-vous pour le Comité scientifique ?
  Les prochaines séances vont être dédiées à des problèmes ou des thèmes qui nécessitent un traitement assez rapide (diagnostics dans les fichiers de sortie, efficacité numérique, étapes de préparation des simulations…) et qui permettront d’améliorer l’ergonomie et l’efficacité du modèle. Nous souhaitons aussi aborder le rôle de l’IA dans la modélisation, toujours en s’entourant d’invités spécialistes du sujet.

.. note::

  Si vous aussi vous souhaitez expliquer un développement que vous avez mis en place dans Méso-NH, ou une méthode d’analyse à partager avec la communauté, n’hésitez pas à me le signaler par `mail <mailto:thibaut.dauhut@utoulouse.fr>`_.

    
Les nouvelles de l’équipe support
************************************

Nouvelle version
  La version de Méso-NH `5.7.4 <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/releases>`_ est sortie le 11 août 2026. Tout.e utilisateur.ice de la branche 5.7 est invité.e à télécharer et installer ce nouveau *bugfix*, en particulier si vous utilisez des fichiers AROME pour initialiser ou forcer le modèle. Toutes les infos dans la note de version disponible sur le lien.

Développement en cours
  - Mise en place des séries multiples de sorties fréquentes (séries temporelles indépendantes avec sélection fine des champs, sous-domaines, paramètres de compression, ...) dont l'implantation est maintenant effective et testée. Elles seront disponibles dans la future version 6.1 (sortie prévue fin 2026 / début 2027).
  - Forge logicielle `Koda <https://src.koda.cnrs.fr/mesonh/mesonh-code>`_ (dépôt du code) : mise en place progressive de l’intégration continue avec de la vérification automatique de code (compilation, syntaxe, cas tests...).

Priorisation des développements à venir
  Un état des lieux des “Défis et difficultés techniques” a été établi afin d'avoir une vision globale de ceux-ci et de prioriser les actions du Pôle technique en collaboration avec le Comité scientifique de Méso-NH. Le `Pôle technique <mailto:mesonhsupport@obs-mip.fr>`_ reste ouvert à toute nouvelle suggestion.

Forum des utilisateur.ices
  Un prochain forum sera organisé cette fin d'année. Ce sera une autre occasion de nous faire remonter vos difficultés ou souhaits de développement. Vous pouvez dès à présent répondre au `sondage <URL>`_ pour choisir la date de ce prochain forum. Nous discuterons notamment de certains développements à prioriser.

Prochaines sessions de la formation Méso-NH
  - du 22 au 25 mars 2027 (en hybride et anglais)
  - du 15 au 18 novembre 2027 (en présentiel et français)

.. note::
  Si vous avez des besoins, idées, améliorations à apporter, bugs à corriger ou suggestions concernant Méso-NH, `Philippe Wautelet <mailto:philippe.wautelet@cnrs.fr>`_ et toute l'équipe sommes toujours preneurs.


Dernières publications utilisant Méso-NH
****************************************************************************************

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
  - Le projet OrgAmazon (2027-2032) a été financé par l'ANR et la FAPESP, agence de recherche de l'état de São Paulo. Des simulations Méso-NH seront réalisées dans le but de comprendre l'évolution de l'organisation de la convection en Amazonie, due au changement climatique et à la déforestation. Un déploiement instrumental autour du site d' `ATTO-Campina <https://doi.org/10.1175/BAMS-D-24-0092.1>`_ est prévu en 2030.

PhD thesis
  Interactions entre les éoliennes et la stratification de l'atmosphère : impacts sur la météorologie proche de la surface [`P. Boumendil <https://theses.fr/s415518>`_, Univ. Toulouse, 2026]



.. note::

   Si vous souhaitez partager avec la communauté le fait qu’un de vos projets utilisant Méso-NH a été financé ou toute autre communication sur vos travaux (notamment posters et présentations *disponibles en ligne*), n’hésitez pas à `m’écrire <mailto:thibaut.dauhut@utoulouse.fr>`_. Je suis également toujours preneur de vos avis sur les infolettres.

Bel été et bonnes simulations avec Méso-NH !

A bientôt,

Thibaut Dauhut et toute l’équipe Méso-NH : Philippe Wautelet, Quentin Rodier, Didier Ricard, Joris Pianezze, Juan Escobar et Jean-Pierre Chaboureau
