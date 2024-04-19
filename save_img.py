import cv2

def num_save (num):
    with open('enregistrement/num.txt', 'w') as fichier:
        fichier.write(str(num))
    
def recup_num ():
    with open('enregistrement/num.txt', 'r') as fichier:
        num = fichier.read()
        return int(num)
    
def save_frame (frame):
    largeur_cible = int(750 * frame.shape[1] / frame.shape[0])
    frame_redimensionnee = cv2.resize(frame, (largeur_cible, 750))
    num=recup_num()+1
    nom='enregistrement/save'+str(num)+'.png'
    cv2.imwrite(nom, frame_redimensionnee, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    num_save(num)

