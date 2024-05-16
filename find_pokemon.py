from PIL import Image
from ultralytics import YOLO
from save_img import recup_num

def find_pokemon(confidence_threshold=0.8):
    # Chargement de l'image
    image_path = 'enregistrement/save'+str(recup_num())+'.png'
    #image_path = 'enregistrement/pika2.png'
    image = Image.open(image_path)

    # Initialisation du modèle YOLO
    model = YOLO("runs/detect/total_v2/weights/best.pt")

    # Détection des objets dans l'image
    detections = model(image)[0]

    # Parcours des boîtes englobantes détectées
    for box in detections.boxes:
        # Extraction du nom de la classe de l'objet
        class_name=model.names.get(box.cls.item())

        # Extraction du score de confiance
        confidence = box.data.tolist()[0][4]

        # Affichage du nom de la classe et du score de confiance si le score dépasse le seuil
        if confidence >= confidence_threshold:
            print(f"Objet détecté : {class_name}, Score de confiance : {confidence}")
            return (class_name,confidence)

# Chemin de l'image PNG à tester
image_path = 'enregistrement/pika2.png'

