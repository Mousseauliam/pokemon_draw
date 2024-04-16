import tkinter as tk
from PIL import Image, ImageTk
import cv2

class Cwebcam(tk.Canvas):
    def __init__(self, window, video_source=0):
        self.__init__(self,window)
        # Ouvrir la capture vidéo
        
        # Créer un canvas pour afficher les images
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        
        # Bouton pour démarrer/arrêter la capture vidéo
        self.btn_start_stop = tk.Button(window, text="Start", width=10, command=self.quit)
        self.btn_start_stop.pack(anchor=tk.CENTER, expand=True)
        
        # Mettre à jour l'affichage vidéo
        self.update()
        
        self.window.mainloop()
    
    def update(self):
        # Capture une image depuis la vidéo
        ret, frame = self.vid.read()
        
        if ret:
            # Convertir l'image en format reconnu par Pillow
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            photo = ImageTk.PhotoImage(image=image)
            
            # Afficher l'image sur le canvas
            self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            self.canvas.photo = photo
        
        # Répéter cette fonction à intervalle régulier
        self.window.after(10, self.update)

# Créer une instance de la fenêtre Tkinter
window = tk.Tk()

# Créer une instance de l'application de la webcam et spécifier la source vidéo
app = WebcamApp(window, "Webcam Viewer")

