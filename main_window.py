import tkinter as tk
import tkinter.font as font
<<<<<<< HEAD
import pygame
=======
#from playsound import playsound
>>>>>>> 0f7112eb10fad2e84c183e963aea320ea75c421a
from PIL import Image
from PIL import ImageTk
import customtkinter as ctk

class Menu(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        #Création de la musique.

        pygame.mixer.init()
        pygame.mixer.music.load("Imagepokemon/Musique1.mp3")
        pygame.mixer.music.play()

        #Création de l'image de fond et du titre.

        self.gif = tk.PhotoImage(file="Imagepokemon/fond.gif").subsample(2)
        self.titre = tk.PhotoImage(file="Imagepokemon/TITRE.png").subsample(2)

        #Création de la fenetre d'affichage.

        self.hauteur = self.gif.height()
        self.largeur= self.gif.width()
        self.resizable(width=False,height=False)
        self.canvas = tk.Canvas(self, width=self.largeur, height=self.hauteur)
        self.canvas.create_image(self.largeur/2, self.hauteur/2, image=self.gif)
        self.canvas.create_image(self.largeur/2,120,image=self.titre)
        self.canvas.pack()
<<<<<<< HEAD
 
        #Création du bouton QUITTER.

        self.police = ctk.CTkFont(family="Pokemon Hollow", size=30)
        self.boutonQ = ctk.CTkButton(self, text="Quitter", command=self.quit,height=50,width=300, font=(self.police),text_color="#FFCB29",fg_color="#3860A8", hover_color="#00C4F0",corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonQ.pack()
        self.fenetreBouton = self.canvas.create_window(480,425, anchor="center", window=self.boutonQ)
=======

        self.police = ctk.CTkFont(family="Pokemon Solid", size=30)
        
        #Création du bouton QUITTER

        self.boutonQ = ctk.CTkButton(self.canvas, text="Quitter", command=self.quit, height=50, width=300, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonQ.place(relx=0.5, rely=0.75, anchor="center")
>>>>>>> 0f7112eb10fad2e84c183e963aea320ea75c421a
        
        #Création du bouton JOUER.

        self.boutonJ = ctk.CTkButton(self.canvas, text="Jouer", command=self.quit, height=50, width=300, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonJ.place(relx=0.5, rely=0.5, anchor="center")
        
        #Création du bouton REGLE

<<<<<<< HEAD
        #Création du bouton RÈGLES.

        self.boutonJ = ctk.CTkButton(self, text="Règles", command=self.quit,height=50,width=300, font=(self.police),text_color="#FFCB29",fg_color="#3860A8", hover_color="#00C4F0",corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonJ.pack()
        self.fenetreBouton = self.canvas.create_window(480,350, anchor="center", window=self.boutonJ)
=======
        self.boutonR = ctk.CTkButton(self.canvas, text="Règles", command=self.quit, height=50, width=300, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonR.place(relx=0.5, rely=0.625, anchor="center")
>>>>>>> 0f7112eb10fad2e84c183e963aea320ea75c421a

        
        

if __name__ == "__main__":
    app = Menu()
    app.title("POKÉDRAW")
    app.mainloop()
