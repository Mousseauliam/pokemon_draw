import tkinter as tk
from PIL import Image, ImageTk
import cv2

#Pour mac : pip install opencv-python

class Cweb(tk.Canvas):
    
    def __init__(self, window, video_source=0):
        tk.Canvas.__init__(self, window, width=400, height=300 )
        self.window = window
        self.vid = cv2.VideoCapture(video_source)
        self.cam=True
        self.update()
    
    def update(self):
        # Capture une image depuis la vidéo
        ret, frame = self.vid.read()
        
        if ret:
            # Convertir l'image en format reconnu par Pillow
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            photo = ImageTk.PhotoImage(image=image)
            
            # Afficher l'image sur le canvas
            self.create_image(0, 0, image=photo, anchor=tk.NW)
            self.photo = photo
        
        # Répéter cette fonction à intervalle régulier
        if self.cam:
            self.window.after(10, self.update)


    def togle_cam(self):
        self.cam= not self.cam