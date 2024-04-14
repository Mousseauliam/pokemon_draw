import tkinter as tk
import tkinter.font as font
import pygame
from PIL import Image
from PIL import ImageTk
import customtkinter as ctk

class Menu(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Musique

        pygame.mixer.init()
        pygame.mixer.music.load("Dossierpoke/Musique1.mp3")
        pygame.mixer.music.play()

        #Images

        self.gif = tk.PhotoImage(file="Dossierpoke/fond.gif").subsample(2)
        self.titre = tk.PhotoImage(file="Dossierpoke/TITREPIXEL.png").subsample(2)
        self.pierreR = tk.PhotoImage(file="Dossierpoke/Pierre-2.png").subsample(3)
        self.hauteur = self.gif.height()
        self.largeur= self.gif.width()
        self.resizable(width=False,height=False)
        self.canvas = tk.Canvas(self, width=self.largeur, height=self.hauteur)
        self.canvas.create_image(self.largeur/2, self.hauteur/2, image=self.gif)
        self.canvas.create_image(self.largeur/2,120,image=self.titre)


        #Boutons et police.

        self.police = ctk.CTkFont("dogica", size=22)
        self.policeR = ctk.CTkFont("dogica", size=9)

        self.boutonJ = ctk.CTkButton(self.canvas, text="Jouer", command=self.quit, height=50, width=300, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonR = ctk.CTkButton(self.canvas, text="Règles", command=self.AfficheRegles, height=50, width=300, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonQ = ctk.CTkButton(self.canvas, text="Quitter", command=self.quit, height=50, width=300, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonS = ctk.CTkButton(self.canvas, text="Son", command=self.quit, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonB = ctk.CTkButton(self.canvas, text="Retour", command=self.AfficheMenu, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")

        #Pages Règles 

        self.texte = tk.Label(self,justify="left",bg="white",bd=4,relief="ridge",fg="black",font=self.policeR,text="Bienvenue dans PokéDraw, le but est de dessiner un Pokémon parmi \ntrois disponibles (Pikachu, Tiplouf ou Mentali) de manière à ce que l'ordinateur puisse le reconnaître. \nVoici les règles du jeu : \n     1. Joueurs : Le jeu se joue à une personne. \n     2. Choix du Pokémon : Avant de commencer à dessiner,\n     vous devez choisir un pokémon à dessiner entre Pikachu, Tiplouf et Mentali. \n     3. Dessin : Une fois le pokémon choisi, vous pouvez dessiner le pokémon,\n   en couleur ou en noir et blanc.\n     4. Soumission du dessin :\n     Lorsque le pokémon est dessinez, cliquez sur “Jouer“ et prenez en photo votre pokémon.\n     5. Résultats : Enfin, l‘ordinateur tente de déterminer de quel pokémon il s‘agit.\n     Il donnera également quelques informations sur le pokémon reconnu!\nVoilà, vous êtes désormais prêt à jouer à PokéDraw. Bon jeu!")
        self.AfficheMenu()

    def AfficheMenu(self):
        self.boutonB.place_forget()
        self.texte.place_forget()
        self.canvas.pack()
        self.boutonJ.place(relx=0.5, rely=0.5, anchor="center")
        self.boutonR.place(relx=0.5, rely=0.625, anchor="center")
        self.boutonQ.place(relx=0.5, rely=0.75, anchor="center")
        self.boutonS.place(relx=0.9, rely=0.9, anchor="center")
        
    def AfficheRegles(self):
        self.boutonJ.place_forget()
        self.boutonR.place_forget()
        self.boutonQ.place_forget()
        self.canvas.create_image(300,120,image=self.pierreR)
        self.boutonB.place(relx=0.5, rely=0.75, anchor="center")
        self.texte.place(relx=0.5, rely=0.5, anchor="center")
        

    def FermeMenu(self):
        self.destroy()
        

if __name__ == "__main__":
    app = Menu()
    app.title("POKÉDRAW")
    app.mainloop()
