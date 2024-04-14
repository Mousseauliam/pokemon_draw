import tkinter as tk
import tkinter.font as font
#from playsound import playsound
from PIL import Image
from PIL import ImageTk
import customtkinter as ctk

class Menu(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        #Création de l'image de fond et du titre.

        self.gif = tk.PhotoImage(file="/Users/noahmilakovic/Desktop/Imagepokemon/fond.gif").subsample(2)
        self.titre = tk.PhotoImage(file="/Users/noahmilakovic/Desktop/Imagepokemon/TITRE.png").subsample(2)

        #Création de la fenetre d'affichage.

        self.hauteur = self.gif.height()
        self.largeur= self.gif.width()
        self.canvas = tk.Canvas(self, width=self.largeur, height=self.hauteur)
        self.canvas.create_image(self.largeur/2, self.hauteur/2, image=self.gif)
        self.canvas.create_image(self.largeur/2,120,image=self.titre)
        self.canvas.pack()
 
        #Création du bouton QUITTER

        self.police = ctk.CTkFont(family="Pokemon Solid", size=30)
        self.boutonQ = ctk.CTkButton(self, text="Quitter", command=self.quit,height=50,width=300, font=(self.police),text_color="#FFCB29",fg_color="#3860A8", hover_color="#00C4F0",corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonQ.pack()
        self.fenetreBouton = self.canvas.create_window(480,425, anchor="center", window=self.boutonQ)
        
        #Création du bouton JOUER

        self.boutonJ = ctk.CTkButton(self, text="Jouer", command=self.quit,height=50,width=300, font=(self.police),text_color="#FFCB29",fg_color="#3860A8", hover_color="#00C4F0",corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonJ.pack()
        self.fenetreBouton = self.canvas.create_window(480,275, anchor="center", window=self.boutonJ)

        #Création du bouton RÈGLES

        self.boutonJ = ctk.CTkButton(self, text="Règles", command=self.quit,height=50,width=300, font=(self.police),text_color="#FFCB29",fg_color="#3860A8", hover_color="#00C4F0",corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonJ.pack()
        self.fenetreBouton = self.canvas.create_window(480,350, anchor="center", window=self.boutonJ)

        
        

if __name__ == "__main__":
    app = Menu()
    app.title("POKÉDRAW")
    app.mainloop()