import os
import cv2

# Fonction pour redimensionner une image tout en conservant le ratio hauteur/largeur
def resize_image_keep_ratio(image, target_height):
    # Récupérer les dimensions de l'image
    height, width = image.shape[:2]
    
    # Calculer le facteur de redimensionnement
    ratio = target_height / height
    
    # Redimensionner l'image en conservant le ratio
    resized_image = cv2.resize(image, (int(width * ratio), target_height))
    
    return resized_image

# Dossier source contenant les images
input_folder = "bddpokemon/Mentali"
# Dossier de destination pour les images redimensionnées
output_folder =  "datasets/train/mentali/images"

# Créer le dossier de sortie s'il n'existe pas
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Parcourir le dossier source
for filename in os.listdir(input_folder):
    # Vérifier si le fichier est une image
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        # Chemin complet de l'image d'entrée
        input_path = os.path.join(input_folder, filename)
        
        # Charger l'image
        img = cv2.imread(input_path)
        
        # Redimensionner l'image en conservant le ratio avec une hauteur de 500 pixels
        resized_img = resize_image_keep_ratio(img, 750)
        
        # Chemin de sortie pour l'image redimensionnée
        output_path = os.path.join(output_folder, filename)
        
        # Enregistrer l'image redimensionnée
        cv2.imwrite(output_path, resized_img)
        print(f"Image {filename} redimensionnée et enregistrée dans {output_folder}")

print("Le redimensionnement des images est terminé.")
