# Projet / Systeme de recommandation d'images

Creation d'un programme permettant de récupérer, analyser, et exploiter un ensemble de données relatives à des images ou photographies afin de proposer un système de recommandation personalisé à l'utilisateur.

L'analyse de l'image, comme détaillé plus bas, sera fondé sur deux principes distincts : l'analyse des couleurs principales de chaque image, et l'analyse des types des pokémons.

Consulter le lien suivant pour acceder au github d'origine : 
https://github.com/johnsamuelwrites/DataMining

## Contributeurs

Martin CHARRONDIERE, ROSE

- Etiquetage et annotation
- Systeme de recommandation

Arthur COLLIGNON, CLBD

- Collecte de données
- Systeme de recommandation

Louis ROBERT, ROSE

- Analyse de données
- Visualisation de données
- Deboggage général

## Detail par section

# Collecte de données

- La base d'image est constituée de 809 images libres de droit, illustrant des pokémons des générations 1 à 7.

- On récupère dans un premier temps des données à partir d'un document CSV, comprennant un identifiant (entier de 0 à 808), le nom anglais d'un pokémon, son ou ses types ainsi que l'image d'illustration, plus particulièrement son format (jpg ou png).

- Il est impératif d'ajouter une deuxième colonne afin d'homogénéiser le nombre de type des pokémons étudiés (un ou deux suivant l'entrée). On rajoute donc un second type 'null' si nécéssaire.

- Enfin, on fabrique un dataframe à partir des données récoltées dans le CSV, et on l'exporte au format JSON pour l'utiliser dans d'autres cellules.

# Etiquetage et annotation

- Dans un premier temps, on récupère le JSON créé préalablement afin de lui apporter des modifications. Cette étape sera systématique dans les autres cellules, elle sera abrégée en 'Récupération du JSON' à l'avenir.

- Ajout d'une colonne dans ce dernier pour y inscrire les couleurs dominantes.

- Grace à une régression de type K-means, étude et récupération des couleurs dominantes dans une image, dont on filtre les couleurs noir et blanche, très majoritaire à cause du fond non neutre de l'image.Puis, normalisation des valeurs récupérées.

- Exporation du fichie JSON modifié pour l'utiliser à nouveau par la suite sous sa nouvelle forme. Pour les mêmes raisons que pour le premier point de cette sous-section, cette étape sera par la suite simplement nommée 'Exportation du JSON'.

# Analyse de données

- Récupération du JSON.

- Ajout d'une colonne pour abriter la preference, nombre de type float indiquant la préférence de l'utilisateur pour cette image. Plus le score est élévé, plus il semble que l'utilisateur apprécie l'image.

- Selection aléatoire de 50 images dans la banque de données, et affichage de ces images accompagnées d'une checkbox précédée de la mention 'j'aime'. Le coche de cette boite par l'utilisateur indique qu'il apprécie l'image juxtaposée.

- Récupération et inscription dans le JSON des données récoltées grâce à cet échantillon d'images.

- Exportation du JSON.

# Visualisation de données

- Récupération du JSON.
 
- Stockage dans six dictionnaires bien distincts des différentes données relatives aux couleurs et aux types des 50 pokémons échantillonés (voir étape précédente).
(Trois dictionnaires traitent les couleurs, un pour l'ensemble, un pour les couleurs appréciées, l'autre pour les couleurs dépréciées; les trois autres sont consacrés aux types selon un découpage analogue).

- Les résultats sont alors affichés dans des diagrammes en batons horizontaux, dont le code couleur et la position indiquent visuellement le contenu (également, le titre et les indices & graduations facilitent la lecture).

# Système de recommandation

- Récupération du JSON.

- Creation d'une colonne supplémentaire indiquant l'indice 'likeable', rapportant comme son nom l'indique la supposée propension de l'utilisateur à apprécier ce contenu. 
NB: Ce score est appuyé par le traitement des données mais par aucune mesure supplémentaire aux précédentes.

- Calcul des scores de similarité d'une image à partir de l'échantillon préalablement soumis au jugement au jugement de l'utilisateur, à partir des couleurs et types.

- Pondération des scores selon le nombre d'images likées ainsi que selon si l'utilisateur a aimé ou non une image, et inscription des nouvelle valeurs dans le JSON.

- Exportation du JSON.

## Crédits

Bibliothèques utilisées : 

- pandas
- PIL (Pillow)
- numpy
- math
- scikit-learn
- ipywidgets
- random
- IPython
- matplotlib