import cv2
import keyboard

# Capture vidéo à partir de la webcam
cap = cv2.VideoCapture(0)

# Vérifier si la webcam est ouverte correctement
if not cap.isOpened():
    print("Erreur: Impossible d'ouvrir la webcam")
    exit()

# Boucle de capture d'images
while True:
    # Lire une nouvelle image de la webcam
    ret, frame = cap.read()

    # Afficher l'image capturée
    cv2.imshow('Webcam', frame)

    # Attendre 1 milliseconde et vérifier si l'utilisateur appuie sur la touche 'p' pour prendre une photo
    if keyboard.is_pressed('p'):
        # Enregistrer l'image capturée sur le disque
        cv2.imwrite('photo_webcam.jpg', frame)
        print("Pokémon capturé!")
        
    # Attendre 1 milliseconde et vérifier si l'utilisateur appuie sur la touche 'q' pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et fermer la fenêtre d'affichage
cap.release()
cv2.destroyAllWindows()
