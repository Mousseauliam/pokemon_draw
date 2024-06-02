<div style="text-align: right;">
    BOILEAU Juline<br>
    BOULGHIB Jenine<br>
    MILAKOVIC Noah<br>
    MOUSSEAU Liam
</div>

![Titre](elements_graphique/TITREPIXEL.png)

Bienvenue dans PokemonDraw ! L'objectif de ce jeu est de permettre à l'utilisateur de dessiner un pokémon et de le montrer à la caméra afin que l'ordinateur soit capable de reconnaître celui-ci.

Nous allons essayer dans les quelques paragraphes suivants de vous décrire les différentes étapes de ce projet :

<font color="#1F28AE">

- *Entrainement du modèle*
   - *Le choix du modèle*
   - *Création d'une banque d'images de Pokémon*
   - *Mise en forme des données*
   - *Apprentissage*

- *Interface graphique*
    - *Introduction*
    - *Explication du code principal*
    - *Explication des scripts annexes*

</font>

Pour optimiser notre temps, nous avons segmenté les étapes à effectuer pour ensuite mettre en commun de manière à avoir un code complet. Pour cela, nous avons utilisé GITHUB, une plateforme open source de gestion de versions et de collaboration destinée aux développeurs de logiciels facilitant le travail en parallèle.

Pour lancer Pokedraw, il suffit d'exécuter le script `main_windows`. Suivant les ordinateur il peut y avoir une ereure si l'on clique trop vite sur 

# Entrainement du modèle

## Le choix du modèle

Le premier choix que nous avons fait a était de choisir quelle modele nous voulions entrainer. Nous nous somme tourner vers le modele open-source YOLO, car il y avait beaucoup de documentation a disposition et de bon resultat 

## Création d'une banque d'images de Pokémon

Avant tout, nous avons sélectionné un starter de 3 pokémons de différentes couleurs et formes comme base afin de faciliter leur différenciation.

![Starter](startera.png)

Nous avons alimenté la banque d'images de chacun de ces pokémons en utilisant des images numériques disponibles sur internet, des dessins trouvés en ligne et des dessins que nous avons faits nous-mêmes pour balayer un maximum de caractéristiques propres à chacun de nos pokémons. Nous les avons sélectionnés en couleur et en noir et blanc pour pouvoir reconnaître un dessin qui serait en couleur ou non. La base de données regroupe environ 80 images/dessins pour chacun de nos pokémons afin de l'enrichir et la diversifier pour le machine learning.

## Mise en forme des données

A l'aide du logiciel (aide-moi Juline, je ne me souviens plus du nom !), nous avons pu mettre en forme notre base de données, c'est-à-dire préciser quelle image correspond à quoi. Ce processus est appelé la labellisation, il permet de créer un fichier texte pour chaque image qui contient l'ID du pokémon present sur l'image (chaque pokémon est associé à un nombre) et sa position.

## Apprentissage

Pour mener a bien cette partie nous avons utiliser plusieure script, notament deux scritp de test trouvé sur internet (`webcam entrainement` et `yolo sur image`) qui permettent de tester un modele en live sur la webcam ou sur des image enregistrer. Tous les diffrent script que nous avons utiliser pour l'entrainement du modele son present dans le dossier `entrainement et test` ainsi que quelques images pour tester les performance de nos modèle. Il y a aussi un script (`resize img`) que nous avons ecrit pour redimensioner toute les images de notre base de données et standardiser le format. Pour lancer un entrainement il y a besoin de deux fichier, un fichier .yaml qui contient les chemin vers la base de donnée et un script python qui charge le modele et lance l'entrainement suivant les parametre du fichier yaml. Dans un premier temp nous avons fait des experimentation en entrainant un modele uniquement pour detecter pikachu. Puis en utilisant les fichier de test decrit ci-dessu nous avons pu tester le modele. En tatonant petit a petit nous avons réussi a obtenir un modele relativement satifaisant capable de diferencier les diferents pokemon. Malheuresement nous avons remarquer que notre modèle a tendance a prendre les humain pour des espeon, un probleme recurent mais pas très genant si le modele et utiliser correctement dans la mesure ou on n'est pas censé lui montré des photo d'humain.

# Interface graphique

## Introduction

![Pokedraw](elements_graphique/CaptureMD.PNG)

## Explication du code principal


## Explication des scripts annexes

Comme dit precedement pour rendre le projet plus comprehensible nous l'avons decoupé en plusieurs script. Cela permet de compartimenter certainne fonction et de simplifier la lecture. Je vais essayer dans les quelques lignes qui suive d'expliquer l'utiliter et le principe de focntionnement de ces scripts :

**Cwebcam**

La classe `Cweb` hérite de la classe `Canvas` de Tkinter et encapsule la fonctionnalité de la webcam pour capturer et afficher des flux vidéo en temps réel dans une interface graphique. Elle permet de gérer la capture vidéo, le traitement des images (comme le retournement et le redimensionnement), et l'affichage des images sur le canvas. Déclarer cette fonctionnalité dans un script séparé améliore la modularité et la réutilisabilité du code tout en permetant une ecriture moins 'lourde'.

**find_pokemon**

La fonction `find_pokemon` utilise le modèle YOLO pour détecter et reconnaître les Pokémon dans une image. L'image et entrée en parametre de la fonction, puis on effectue une rotation de l'image, de -10 à 10 degrés par incréments de 5, et nous effectuons une détection avec le modèle YOLO et stockons les résultats dans une liste. Cette methode et certe un peu plus longue que passer une seule fois l'image dans le modele mais elle permet d'obtenir des resultat plus fiable. Dans le tableau, chaque résultat contient le nom du détecté et la confiance associée. En cas de détection multiple, nous filtrons les résultats pour trouver celui avec la plus haute confiance et qui dépasse le seuil spécifié. Si aucun résultat ne dépasse le seuil, nous retournons [None, None].


<font color="#FF0000">

## Travail Jenine piocher dedant pour votre partie

## Récupération du dessin

Nous importons d'abord les bibliothèques datetime, YOLO d'ultralytics, et cv2 pour la manipulation des images et vidéos avec OpenCV. Ensuite, nous définissons des constantes comme le seuil de confiance pour les détections et la couleur verte pour les boîtes de détection. Nous chargeons le modèle pré-entraîné YOLOv8n à partir du fichier yolov8n.pt.

Nous initialisons la capture vidéo à partir d'un fichier vidéo en utilisant `cv2.VideoCapture`. Dans une boucle, nous commençons par mesurer le temps de traitement de chaque image pour calculer les FPS par la suite. Si aucune nouvelle image n'est capturée, nous quittons la boucle. Nous appliquons le modèle YOLO à chaque image capturée pour obtenir des détections. Pour chaque détection, nous extrayons le nom de l'objet et la confiance associée, et nous filtrons les détections ayant une confiance inférieure au seuil défini.

Pour les détections valides, nous dessinons des boîtes de détection sur l'image en utilisant `cv2.rectangle` et nous affichons le nom de l'objet et la confiance en utilisant `cv2.putText`. Nous calculons et affichons les FPS sur chaque image traitée, puis montrons l'image à l'écran avec `cv2.imshow`. Si l'utilisateur appuie sur la touche 'q', nous quittons la boucle. Enfin, nous libérons les ressources vidéo avec `video_cap.release()` et fermons toutes les fenêtres ouvertes par OpenCV avec `cv2.destroyAllWindows`.

## Reconnaissance du Pokémon

Dès lors, on applique notre reconnaissance par apprentissage supervisé déjà entraînée sur l'image qui renvoie dans un résultat le pokémon identifié par la machine.

## Renvoi des informations liées au pokémon

Notre machine ayant appris à reconnaître les pokémons du starter, nous allons pouvoir exploiter la réponse donnée à l'issue du traitement. En effet, nous récupérons le pokémon renvoyé en sortie et nous le rattachons à la base de données Pokémon [PokéAPI](https://pokeapi.co/api/v2/pokemon/) afin d'en extraire ses informations spécifiques : son nom, sa taille, son poids et sa couleur.

Pour cela, nous définissons une fonction `NomPokemon` qui va nous permettre de travailler avec une base de données distante par API. D'une part, nous interrogeons la base de données en construisant une URL à partir des variables `base_url` et `pokemon` dans le fichier `1_requetes_http.py`. Une fois cela fait, nous utilisons la librairie `requests`. Par la suite, nous effectuons une requête de type "GET" sur l’URL précédente afin d'afficher le texte brut du JSON obtenu. Finalement, nous transformons le résultat obtenu en un dictionnaire ce qui va nous permettre de récupérer et d'afficher en particulier les informations sur la taille et le poids du pokémon.

## Interface graphique

Nous avons décidé de mettre en forme notre code sous forme d'interface graphique de jeu.
</font>
