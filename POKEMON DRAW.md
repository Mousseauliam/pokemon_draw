<div style="text-align: justify;">
    <div style="text-align: right;">
   BOILEAU Juline 
</div>
<div style="text-align: right;">
   BOULGHIB Jenine
</div>
<div style="text-align: right;">
   MILAKOVIC Noah
</div>
<div style="text-align: right;">
   MOUSSEAU Liam
</div>
<div style="text-align: center;">
   <img src=logopac.png /div>
</div>

   <div style="text-align: Center;">  
   
   # Pokémon Draw
    
   </div>


<div style="text-align: justify;"> Bienvenue dans PokemonDraw ! L'objectif de ce jeu est de permettre à l'utilisateur de dessiner un pokémon et de le montrer à la caméra afin que l'ordinateur soit capable de reconnaître celui-ci en le nommant et a termes donner ses caractéristiques relatif au Pokédex. </div>

<div style="text-align: justify;">

Pour réaliser ce projet, nous avons défini les étapes caractéristiques du code final : 

<font color="#1F28AE">
    
- *Création d'une banque d'images de Pokemon*
- *Machine Learning de Pokemon*
- *Interface graphique*
    - *Récupération du dessin*
    - *Traitement d'images*
    - *Reconnaissance du Pokémon*
    - *Renvoi des informations liées au Pokemon*


</font>

Pour optimiser notre temps, nous avons segmenté les étapes à effectuer pour ensuite mettre en commun en un code complet en utilisant GITHUB qui est une plateforme open source de gestion de versions et de collaboration destiné aux developpeurs de logiciels facilitant le travail en parallèle.
</div>

## Création d'une banque d'images de Pokémon

<div style="text-align: justify;">Avant tout, nous avons sélectionné un starter de 3 pokémons de différentes couleurs et formes comme base afin de faciliter leur différenciation.</div>
<div style="text-align: left;">
   <img src=startera.png /div>
<div style="text-align: justify;">
Nous avons alimenté la banque d'images pour chacun de ces pokémons en utilisant des images numériques disponibles sur internet, des dessins trouvés en lignes et des dessins que nous avons fait nous même pour balayer un maximum de caractéristiques propres à chacun de nos pokémons. Nous les avons séléctionnés en couleur et en noir et blanc pour pouvoir reconnaître un dessin qui serait couleur ou non.
La base de données regroupe environ 80 images/dessins pour chacun de nos pokémons afin de l'enrichir et la diversifier pour le Machine learning.
</div>

## Machine Learning de Pokémon




<font color=" #1F28AE">*Récupération des données*</font> 

On récupère la banque d'images que l'on a créée auparavant qui va nous servir de base dans l'apprentissage de nos différents pokémons.

<font color=" #1F28AE">*Mise en forme des données*</font> 

On récupère la banque d'images que l'on a créée auparavant qui va nous servir de base dans l'apprentissage de nos différents pokémons.


<font color=" #1F28AE">*Apprentissage Supervisé de pokémons*</font> 

<div style="text-align: justify;">Une fois avoir procédé à la récupération de nos données, on entraîne notre réseau de neurones à reconnaître nos pokémons à partir de notre banque d'images par apprentissage supervisé. Après plusieurs essais de code, on remodèle le code jusqu'à ce que la machine soit capable de dire ce qu'est un pikachu dans un premier temps. Puis on reitère cette opération jusqu'à ce qu'il les dissocie et reconnaisse tous. Pour se faire, nous importons les bibliothèques `PIL` pour la manipulation des images et `ultralytics` pour la détection des objets. Ensuite, nous définissons une fonction `find_pokemon` qui accepte un seuil de confiance. La fonction génère le chemin de l'image en utilisant `recup_num()` et ouvre cette image. Nous initialisons le modèle YOLO avec des poids prédéfinis. Pour chaque rotation de l'image, de -10 à 10 degrés par incréments de 5, nous effectuons une détection avec le modèle YOLO et stockons les résultats dans une liste. Chaque résultat contient le nom du détecté et la confiance associée. Nous filtrons les résultats pour trouver celui avec la plus haute confiance qui dépasse le seuil spécifié. Si aucun résultat ne dépasse le seuil, nous retournons [None, None]. En cas de détection multiple, nous sélectionnons le meilleur, sinon nous retournons le seul résultat disponible ou [None, None] s'il n'y a aucune détection.</div>

## Interface graphique

Nous avons décidé de mettre en forme notre code sous forme d'interface graphique de jeu.
<div style="text-align: left;">
   <img src=pokedraw.png /div>

<font color=" #1F28AE">*Récupération du dessin*</font> 


<div style="text-align: justify;">
Nous importons d'abord les bibliothèques datetime, YOLO d'ultralytics, et cv2 pour la manipulation des images et vidéos avec OpenCV. Ensuite, nous définissons des constantes comme le seuil de confiance pour les détections et la couleur verte pour les boîtes de détection. Nous chargeons le modèle pré-entraîné YOLOv8n à partir du fichier yolov8n.pt.

Nous initialisons la capture vidéo à partir d'un fichier vidéo en utilisant cv2.VideoCapture. Dans une boucle, nous commençons par mesurer le temps de traitement de chaque image pour calculer les FPS par la suite. Si aucune nouvelle image n'est capturée, nous quittons la boucle. Nous appliquons le modèle YOLO à chaque image capturée pour obtenir des détections. Pour chaque détection, nous extrayons le nom de l'objet et la confiance associée, et nous filtrons les détections ayant une confiance inférieure au seuil défini.

Pour les détections valides, nous dessinons des boîtes de détection sur l'image en utilisant cv2.rectangle et nous affichons le nom de l'objet et la confiance en utilisant cv2.putText. Nous calculons et affichons les FPS sur chaque image traitée, puis montrons l'image à l'écran avec cv2.imshow. Si l'utilisateur appuie sur la touche 'q', nous quittons la boucle. Enfin, nous libérons les ressources vidéo avec video_cap.release() et fermons toutes les fenêtres ouvertes par OpenCV avec cv2.destroyAllWindows().</div>

<font color=" #1F28AE">*Reconnaissance du Pokémon*</font> 

<div style="text-align: justify;">Dès lors, on applique notre reconnaissance par apprentissage supervisé déja entrainé sur l'image  qui renvoie dans un resultat le pokemon identifié par la machine.
</div>

<font color=" #1F28AE">*Renvoi des informations liées au pokémon*</font> 

<div style="text-align: justify;">Notre machine ayant appris à reconnaître les pokémons du starter, on va pouvoir exploiter la réponse donnée a l'issu du traitement. En effet, on récupère le pokemon renvoyé en sortie et on le rattache à la base de données Pokémon https://pokeapi.co/api/v2/pokemon/ afin d'en extraire ses informations spécifiques: son nom, sa taille, son poids et sa couleur.

Pour cela, on définit une fonction NomPokemon qui va nous permettre de travailler avec une base de données distante par Api.
D'une part nous intérrogeons la base de données en construisant une url à partir des variables base_url et pokemon dans le fichier 1_requetes_http.py. Une fois cela fait, on utilise la libraire requests. Par la suite on effectue une requête de type « GET » sur l’URL précédente afin d'afficher le texte brut du JSON obtenu.
Finalement, nous transformons le résultat obtenu en un dictionnaire ce qui va nous permettre de récuperer et d'afficher en particulier les informations sur la taille et le poids du pokémon.
</div>


<font color=" #1F28AE">*Interface graphique*</font> 


```

```
