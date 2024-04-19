import tkinter as tk
import tkinter.font as font
import pygame
from PIL import Image
from PIL import ImageTk
import customtkinter as ctk
from Cwebcam import Cweb
from save_img import save_frame
from find_pokemon import find_pokemon
import threading

class Menu(tk.Tk):
    
    cam=Cweb
    
    def __init__(self):
        tk.Tk.__init__(self)
        
        #Lance la camera

        self.charg_cam()

        # Musique

        pygame.mixer.init()
        pygame.mixer.music.load("Dossierpoke/Musique1.mp3")
        pygame.mixer.music.play()

        #Images

        self.gif = tk.PhotoImage(file="Dossierpoke/fond.gif").subsample(2)
        self.titre = tk.PhotoImage(file="Dossierpoke/TITREPIXEL.png").subsample(2)
        self.regle = tk.PhotoImage(file="Dossierpoke/TITRER.png").subsample(4)
        self.pierreR = tk.PhotoImage(file="Dossierpoke/Pierre-2.png").subsample(3)
        self.cabane = tk.PhotoImage(file="Dossierpoke/CABANE.png")
        self.hauteur = self.gif.height()
        self.largeur= self.gif.width()
        self.resizable(width=False,height=False)
        self.canvas = tk.Canvas(self, width=self.largeur, height=self.hauteur)
        #self.canvas.create_image(self.largeur/2, self.hauteur/2, image=self.gif,tag="fond")
        
        #Boutons et police.

        self.police = ctk.CTkFont("dogica", size=22)
        self.policeR = ctk.CTkFont("dogica", size=15)

        self.boutonJ = ctk.CTkButton(self, text="Jouer", command=self.Jouer, height=50, width=300, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonR = ctk.CTkButton(self, text="Règles", command=self.AfficheRegles, height=50, width=300, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonQ = ctk.CTkButton(self, text="Quitter", command=self.quit, height=50, width=300, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonS = ctk.CTkButton(self, text="Son", command=self.Pause, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonB = ctk.CTkButton(self, text="Retour", command=self.AfficheMenu, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonB2 = ctk.CTkButton(self, text="Retour", command=self.Jouer, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonN = ctk.CTkButton(self, text="Suivant", command=self.InterPhoto, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonP = ctk.CTkButton(self, text="Prendre photo", command=self.Photo, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonM = ctk.CTkButton(self, text="Menu", command=self.AfficheMenu, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonRe = ctk.CTkButton(self, text="Rejouer", command=self.Jouer, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        
        #Pages Règles 

        self.texte = tk.Label(self,justify="left",bg="white",bd=4,relief="ridge",fg="black",font=self.policeR,text="Pierre : Hey salut, je m’appelle Pierre ! J’espère que tu es prêt à me monter tes meilleurs talents d’artiste.\nTu dois tout d’abord dessiner l’un des Pokémons parmi les 3 proposées : Pikachu, Tiplouf et Mentali.\nUne fois ton magnifique dessin terminé, montre-le-moi à la caméra et prend une photo !\nSi l’âme de l’artiste est en toi, je devrais être capable de reconnaitre quel Pokémon tu as dessiné\npour te donner quelques anecdotes sur ce dernier !")

        
        #Affiche le menu.

        self.AfficheMenu()
    
    def charg_cam(self):
        def cam_th():
            self.cam = Cweb(self)
        thread = threading.Thread(target=cam_th)
        thread.start()
    
    def cacher_boutons(self):
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkButton) or isinstance(widget, tk.Label):
                widget.place_forget()


    def AfficheMenu(self):
        self.cacher_boutons()
        self.canvas.create_image(self.largeur/2, self.hauteur/2, image=self.gif,tag="fond")
        self.canvas.create_image(self.largeur/2,120,image=self.titre,tag="TITRE")
        self.canvas.pack()
        self.canvas.delete("PierreR")
        self.canvas.delete("TITRER")
        self.canvas.delete("CABANE")
        self.boutonJ.place(relx=0.5, rely=0.5, anchor="center")
        self.boutonR.place(relx=0.5, rely=0.625, anchor="center")
        self.boutonQ.place(relx=0.5, rely=0.75, anchor="center")
        self.boutonS.place(relx=0.9, rely=0.9, anchor="center")
        
    def AfficheRegles(self):
        self.canvas.delete("TITRE")
        self.cacher_boutons()
        self.canvas.delete("fond")
        self.canvas.create_image(self.largeur/2,self.hauteur/2,image=self.cabane,tag="CABANE")
        self.canvas.create_image(self.largeur/2,120,image=self.regle,tag="TITRER")
        self.canvas.create_image(200,270,image=self.pierreR,tag="PierreR")
        self.boutonB.place(relx=0.8, rely=0.6, anchor="center")
        self.texte.place(relx=0.5, rely=0.8, anchor="center")
        

    def Pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        else: 
            pygame.mixer.music.play()

    def Jouer(self):
        self.canvas.delete("TITRE")
        self.cam.place_forget()
        self.cacher_boutons()
        self.boutonB.place(relx=0.8, rely=0.6, anchor="center")
        self.boutonN.place(relx=0.8, rely=0.5, anchor="center")

    
    def InterPhoto(self):
        self.cacher_boutons()
        self.cam.place(x=50,y=150)
        self.boutonB2.place(relx=0.8, rely=0.6, anchor="center")
        self.boutonP.place(relx=0.8, rely=0.5, anchor="center")

    def Photo(self):
        self.cacher_boutons()
        save_frame(self.cam.Frame())
        find_pokemon()
        self.cam.place_forget()
        self.boutonM.place(relx=0.8, rely=0.6, anchor="center")
        self.boutonRe.place(relx=0.8, rely=0.5, anchor="center")

if __name__ == "__main__":
    app = Menu()
    app.title("POKÉDRAW")
    app.mainloop()
