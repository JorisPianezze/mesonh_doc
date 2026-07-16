Infolettre #10
================================================

**17 juillet 2026.** Version française, English version `here <newsletter_10_english.html>`_.


Chers utilisateurs, chères utilisatrices de Méso-NH,

Voici ci-dessous la 10ème infolettre de notre communauté. Vous y trouverez un entretien avec le développeur d'un outil qui peut vous être bien utile, les **nombreuses** nouvelles de l’équipe support et la liste des dernières publications utilisant Méso-NH.

Entretien avec `Clément Soufflet <mailto:clement.soufflet@univ-reunion.fr>`_ (LACy)
******************************************************************************************************************

|pic1|

.. |pic1| image:: photo_cs.jpg
  :width: 400

Clément, tu as développé FrameIt pour faciliter l’analyse de simulations de cyclones. FrameIt est particulièrement adapté pour les utilisateur.ices de Méso-NH. Pourrais-tu résumer ce que fait cet outil ?
  **FrameIt** est un outil développé au LACy par l'équipe Cyclone et Météorologie Tropicale, plus particulièrement par Kevin Hoarau, Adrien Colomb, Rémi Laxenaire et moi-même. Dans sa première version cet outil est orienté comme un outil de gestion de données de sortie modèle entièrement codé en Python et basé sur la librairie *xarray*. L'idée du développement de **FrameIt** vient de l’analyse de simulations de cyclone pour lesquelles un grand domaine est nécessaire mais seul une petite partie (le cyclone) nous intéresse vraiment.

  **FrameIt** permet d’extraire un sous domaine mobile (ou fixe) dans le temps, centré sur un objet météorologique, tout en sélectionnant les variables et les niveaux verticaux d’intérêt. Ce sous domaine est aussi disponible en coordonnée polaire centré sur l’objet étudié. En sortie on obtient une série de fichiers *netcdf* très légers, triés par système de coordonnées et par dimension, sur le sous-domaine voulu, contenant tous les pas de temps de la simulation.

  À noter que **FrameIt** peut aussi bien traiter des fichiers *netcdf* venant de Méso-NH que des fichiers *grib* issue du modèle AROME.

En quoi est-ce que cela facilite la vie aux modélisateur.ices ?
  **FrameIt** ne remplace pas l’analyse des fichiers de sortie modèle, mais il permet une prise en main rapide de ces fichiers en s’affranchissant des problématiques de gestion de donnée ou de traitement de gros fichiers de données. En d’autres termes c’est un outil qui va faciliter l’analyse en réduisant la taille des fichiers et en les normalisant par rapport à l’objet météorologique étudié.

  En plus de ça, **FrameIt** permet l’analyse des données dans un système de coordonnées polaires, utile pour les objets météorologiques à symétrie azimutale.

  Enfin, les sorties étant des fichiers *netcdf* relativement légers, **FrameIt** contribue à faciliter le partage de données de simulations notamment dans le cadre de collaboration avec des chercheurs non-modélisateur (et contribuera ainsi au rayonnement de Méso-NH).

Y a-t-il d'autres situations, non-cycloniques, pour lesquels FrameIt serait également utile ?
  Pour le moment **FrameIt** est utilisé majoritairement pour des simulations de cyclones mais cet outil n’est pas limité à ça. Selon moi, **FrameIt** possède un vrai intérêt pour les cas où le domaine d’une simulation numérique est bien plus grand que l’objet météorologique étudié, mais aussi les cas où un système de coordonnées polaires permet de faciliter l’analyse de l’objet météorologique en question.

Quelles recommandations ferais-tu aux utilisateurs.rices de Méso-NH qui voudrait commencer à l’utiliser ?
  Évidemment je ne peux que recommander, en premier lieu, d'aller voir la documentation, assez fournie, associée au projet sur le `GitHub de Météo France <https://meteofrance.github.io/frameit/>`_. L'installation et l'utilisation de **FrameIt** nécessite un environnement virtuel conda spécifique dont l'installation est décrite dans cette documentation.

  Ensuite il faut s'approprier la syntaxe de l’unique fichier de configuration de l’outil dont un exemple est disponible dans le projet. Et enfin, bien sûr, commencer par un cas simple que vous connaissez déjà, avec peu de fichiers, pour vous faire la main.

Quelles sont les limites actuelles ? As-tu des perspectives de développements futurs ? 
  Un aspect de **FrameIt** qui peut, au premier abord, paraître limitant c’est l’orientation vers l’étude des cyclones. En effet la méthode de suivi d’objet est construite pour les cyclones tropicaux et n’est pas applicable à tous les autres objets météorologiques. Cependant pour palier cette limitation, l’utilisateur.ice à la possibilité de fournir une trajectoire a priori pour guider l’extraction sur l’objet météorologique de son choix. Ceci étant dit, **FrameIt** a été pensé modulable (Git) notamment pour permettre aux utilisateur.ices intéressé.es de développer à leur tour des fonctionnalités utiles pour la communauté. Il est donc tout à fait envisageable d’implémenter une nouvelle méthode de suivi associée à un autre type d’objet météorologique (cellule convective, orage…), une rubrique est d’ailleurs dédiée à l’implémentation de nouvelles méthode de suivie dans la documentation.

  Cette première version va servir de base à de nombreux développements futurs, notamment le calcul de diagnostics dédiés aux cyclones qui seront accessibles dans les fichiers de sortie de l'outil.

  Enfin, comme un des axes de recherche au LACy porte sur les interactions océan-atmosphère, l’idée est de pouvoir à terme appliquer cet outil sur les sorties de modèle d’océan et de vagues issue de simulations couplées afin d’avoir une vue d’ensemble des interactions de ces trois compartiments.


.. note::

  Si vous aussi vous souhaitez expliquer un développement que vous avez mis en place dans Méso-NH, ou une méthode d’analyse que vous partagez à la communauté, n’hésitez pas à me le signaler par `mail <mailto:thibaut.dauhut@utoulouse.fr>`_.


    
    
Les nouvelles de l’équipe support
************************************

Nouvelles versions
  - Sortie de la version 5.7.3 le 4 mai 2026, voici la `note <https://mesonh.readthedocs.io/en/mnh-master/getting_started/releases/release_note_573.html#release-note-573>`_ associée à cette version.
  - Sortie de la version 6.0.1 le 10 juillet 2026, dont voici la `note <https://mesonh.readthedocs.io/en/mnh-6-0/getting_started/releases/release_note_601.html>`_. Nous vous recommandons vivement de passer à cette nouvelle version, en particulier les utilisateurs de fichiers AROME (pour l'initialisation et le couplage) datés du 15/10/2024 ou après (cy48).
  - Suite à la nouvelle politique de gestion et de nommage des branches (voir juste en-dessous), depuis la version 6.0, les versions mineures (la valeur de X.Y dans la numérotation de version X.Y.Z) seront maintenues pendant deux ans à compter de la date de sortie de la version mineure suivante. Par exemple, la version 5.7 sera maintenue jusqu’au 19 mars 2028, soit deux ans après la date de sortie de la version 6.0. Le maintien signifie que nous continuerons à publier des versions ne contenant que des corrections de bogues (la lettre Z dans la numérotation X.Y.Z). Au moins une nouvelle version mineure (X.Y) et deux corrections de bogues (X.Y.Z) seront publiées chaque année.
  - Enfin, nous lançons une expérience d'intégration continue sur GitLab : dès qu'un développement est prêt à être intégré, vous pouvez nous l'envoyer (il doit être fusionné au moins avec la dernière version mineure publiée, qui est actuellement la 6.0). Avis aux développeur.euses : **Il n'y aura plus d'appel à contributions**.

Gestion et nommage des branches
  - Une nouvelle politique de gestion et de nommage des branches a été mise en place. Elle est détaillée `ici <https://mesonh.readthedocs.io/en/mnh-6-0/documentation/coding_instructions.html#branch-management-strategy>`_ et également sur le dépôt Git dans le fichier ``BRANCHING.md``. Des règles précises pour la gestion des branches de versions publiées, de développement et de bugs ont été établies. Des branches spécifiques pour les chercheur.euses sont également proposées. Ce schéma n'est pas définitif et des ajustements seront effectués selon les besoins et retours de toutes et tous.
  - La conséquence immédiate de cette nouvelle approche est un ménage important en grande partie achevé. De nombreuses branches obsolètes ont été supprimées, tandis que la plupart de celles restantes ont changé de nom. Si vous utilisez le dépôt, il faudra probablement au minimum rétablir le lien entre vos branches locales et les branches distantes du dépôt. Pour cela, la commande ``git branch -u origin/nouveau_nom_branche`` (lancée depuis la branche locale concernée) vous sera utile pour **restaurer le suivi**.

Forum 1 des Utilisateur.ices de Méso-NH
  - Le 3 juin 2026 le premier forum a été organisé à l'Observatoire Midi-Pyrénées. Quatre nouveautés ont été présentées et discutées avec 33 participant.es autant sur place qu'à distance. De nombreuses questions et deux gâteaux à la fin du pot pour fêter la nouvelle version de Méso-NH ! Les présentations ont porté sur :
  - La **nouvelle organisation** autour du code et du service Méso-NH avec, entre autres, la création du Comité Scientifique et du Comité des tutelles
  - La **version 6** et toutes ses nouvelles fonctionnalités !
  - Les **deux nouveaux sites web** : un `site vitrine <https://mesonh.cnrs.fr/>`_ pour découvrir Méso-NH et donner envie de l'utiliser, et un `site technique <https://mesonh.readthedocs.io>`_ pour être guidé.e dans la prise en main du modèle et y retrouver toute la documentation, notamment le guide de l'utilisateur.
  - Une **interface graphique** de Méso-NH (en béta) pour assister les utilisateur.ices dans la création de leurs namlistes, domaines et forçages, ainsi pour la pévisualisation des simulations. Elle est utilisable en ligne `ici <https://mesonh.streamlit.app/>`_ (sauf pour Workspace) ou en local `là <https://github.com/QuentinRodier/mesonh-interface>`_ (uniquement testé sur PC et Belenos).

Comité Scientifique 1
  Le premier comité scientifique a eu lieu le 1er juillet 2026. Animé par Christelle Barthe et Didier Ricard, il regroupe de nombreux.ses développeur.euses du code et le service. Après un temps sur les actualités, la discussion a porté sur la microphysique nuageuse dans Méso-NH. Céline Planche (LaMP) était invitée en tant que spécialiste de cette thématique.

Méso-Challenge Kairos (CALMIP)
  Une partie du service était investie dans le méso-challenge Kairos, du nom du nouveau calculateur inauguré dans le mésocentre CALMIP (Calcul en Midi-Pyrénées) situé à l'Espace Clément Ader de Toulouse. Des simulations du médicanne Ianos ont été réalisées avec les modèles couplés CROCO - Méso-NH, un sacré challenge technique sur cette nouvelle machine !

Documentation
  La documentation sur le site technique fait l'objet d'un long travail de maintenance et de mise à jour. Finis le fichier pdf et les ctrl-F (à vrai dire encore possible pour les nostalgiques), nous vous invitons à naviguer sur ce site pour y retrouver toutes les infos importantes, par ex. sur l'installation du modèle, la mise en place des simulations et l'ensemble des paramètres possibles des namlistes.

Autres développements et informations
  - Un travail de développement est mené sur l'implicitation des flux de surface et de la turbulence ainsi que la fusion de la résolution des matrices tridiagonales entre la convection peu profonde et la turbulence en vue de gagner en stabilité numérique sur la verticale par rapport au pas de temps du modèle.
  - Les séries multiples seont possibles pour les sorties fréquentes. Cette fonctionnalité permet de créer plusieurs séries distinctes de fichiers de sorties fréquentes. Ces séries sont entièrement indépendantes (choix des champs, instants de sortie, boîtes sélectionnées, paramètres de compression...). Elles seront disponibles dès la version 6.1 de Méso-NH (avant la fin de l'année).
  - L'inscription au **stage Méso-NH** est ouverte pour la session du 2 au 5 novembre en français et présentiel `ici <https://mesonh.readthedocs.io/en/mnh-master/documentation/tutorial_material.html>`_.
  - Philippe Wautelet est en train de collecter, avec l'aide de toute l'équipe Méso-NH, la liste de tous les défis et problèmes techniques auxquels nous sommes ou allons être confrontés. Le but est d'avoir une image la plus complète et fidèle de la situation afin de pouvoir déterminer nos priorités de développements techniques. **N'hésitez pas à nous contacter si vous souhaitez nous rapporter des besoins ou difficultés techniques**.

.. note::
  Si vous avez des besoins, idées, améliorations à apporter, bugs à corriger ou suggestions concernant les entrées/sorties, `Philippe Wautelet <mailto:philippe.wautelet@cnrs.fr>`_ est toujours preneur.


Dernières publications utilisant Méso-NH
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

   Si vous souhaitez partager avec la communauté le fait qu’un de vos projets utilisant Méso-NH a été financé ou toute autre communication sur vos travaux (notamment posters et présentations *disponibles en ligne*), n’hésitez pas à `m’écrire <mailto:thibaut.dauhut@utoulouse.fr>`_. Je suis également toujours preneur de vos avis sur les infolettres.

Bel été et bonnes simulations avec Méso-NH !

A bientôt,

Thibaut Dauhut et toute l’équipe Méso-NH : Philippe Wautelet, Quentin Rodier, Didier Ricard, Joris Pianezze, Juan Escobar et Jean-Pierre Chaboureau
