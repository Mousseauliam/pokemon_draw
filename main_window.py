import tkinter as tk
from tkinter import ttk
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
    name=str
    
    def __init__(self):
        tk.Tk.__init__(self)
        
        #Lance la camera sur autre thread
        self.charg_cam()
        #self.cam = Cweb(self)
        
        # Musique

        pygame.mixer.init()
        pygame.mixer.music.load("elements graphique/Musique.mp3")
        pygame.mixer.music.play(-1)
            
        #Images

        self.gif = tk.PhotoImage(file="elements graphique/fond.gif").subsample(2)
        self.titre = tk.PhotoImage(file="elements graphique/TITREPIXEL.png").subsample(2)
        self.regle = tk.PhotoImage(file="elements graphique/TITRER.png").subsample(4)
        self.pierreR = tk.PhotoImage(file="elements graphique/Pierre.png").subsample(3)
        self.cabane = tk.PhotoImage(file="elements graphique/CABANE.png")
        self.poke = tk.PhotoImage(file="elements graphique/Pokerock.png").subsample(4)
        self.pierreM = tk.PhotoImage(file="elements graphique/PierreMontre.png")
        self.pikachu = tk.PhotoImage(file="elements graphique/pikachu.png").subsample(4)
        self.tiplouf = tk.PhotoImage(file="elements graphique/tiplouf.png").subsample(4)
        self.mentali = tk.PhotoImage(file="elements graphique/mentali.png").subsample(4)
        self.pastrouve = tk.PhotoImage(file="elements graphique/Point_int.png").subsample(4)
        self.pierreP = tk.PhotoImage(file="elements graphique/PierrePouce.png").subsample(4)
        self.pierrePB = tk.PhotoImage(file="elements graphique/PierrePB.png").subsample(4)
        self.rondin = tk.PhotoImage(file="elements graphique/Rondin.png").subsample(3)

        #Fenetre
        
        self.hauteur = self.gif.height()
        self.largeur= self.gif.width()
        self.resizable(width=False,height=False)
        self.title("POKÉDRAW")
        
        self.canvas = tk.Canvas(self, width=self.largeur, height=self.hauteur)
        
        #Boutons et polices.

        self.police = ctk.CTkFont("dogica", size=22)
        self.policeR = ctk.CTkFont("dogica", size=15)
        self.police2 = ctk.CTkFont("Courier", size=15)

        self.boutonJ = ctk.CTkButton(self, text="Play", command=self.Jouer, height=50, width=300, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonR = ctk.CTkButton(self, text="Rules", command=self.AfficheRegles, height=50, width=300, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonQ = ctk.CTkButton(self, text="Quit", command=self.quit, height=50, width=300, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonS = ctk.CTkButton(self, text="Sound", command=self.Pause, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonB = ctk.CTkButton(self, text="Back", command=self.AfficheMenu, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonB2 = ctk.CTkButton(self, text="Back", command=self.Jouer, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonN = ctk.CTkButton(self, text="Next", command=self.InterPhoto, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonP = ctk.CTkButton(self, text="Take picture", command=self.Photo, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonM = ctk.CTkButton(self, text="Menu", command=self.AfficheMenu, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
        self.boutonRe = ctk.CTkButton(self, text="Replay", command=self.Jouer, height=30, width=50, font=(self.police), text_color="#FFCB29", fg_color="#3860A8", hover_color="#00C4F0", corner_radius=0, border_width=4, border_color="#1D2C60")
    
        #Textes 
        
        self.texte = tk.Label(self,justify="left",bg="white",bd=4,relief="ridge",fg="black",font=self.police2,text="Brock: Hey, my name is Brock! I hope you are ready to show me your best\nartistic talents. First, draw one of the three Pokemon proposed: Pikachu,\nPiplup and Espeon. Once your beautiful drawing is done, show it to me\non camera and take a picture! If the artist’s soul is in you, I should be able\n to recognize which Pokémon you drew to give you some anecdotes about it!")
        self.response = tk.Label(self,justify="left",bg="white",bd=4,relief="ridge",fg="black",font=self.policeR,text= "")
        self.texte2 = tk.Label(self,justify="left",bg="white",bd=4,relief="ridge",fg="black",font=self.police2,text="Brock : Choose the Pokémon you want to draw!\nDon’t hesitate to go online to get inspired!")
        self.texteR = tk.Label(self,justify="left",bg="white",bd=4,relief="ridge",fg="black",font=self.police2,text="It’s a Pikachu ! Did you know ? The impact\nand success of the Pokemon is such that the\nfranchise inspired science during a discovery.\nIn 2008, Japanese researchers discovered a\nnew protein that reacts to electricity. So\nthey simply decided to call it\nPikachurine in obvious reference to Pikachu.")
        
        #Affiche le menu.

        self.AfficheMenu()
        
        #test bar de charg

        self.progress_bar = ttk.Progressbar(self, orient="horizontal", mode="indeterminate")

    
    def charg_cam(self):
        def cam_th():
            self.cam = Cweb(self)
        thread = threading.Thread(target=cam_th)
        thread.start()
    
    def cacher_boutons(self):
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkButton) or isinstance(widget, tk.Label) or isinstance(widget, ttk.Progressbar):
                widget.place_forget()


    def AfficheMenu(self):
        self.cacher_boutons()
        self.canvas.create_image(self.largeur/2, self.hauteur/2, image=self.gif,tag="fond")
        self.canvas.create_image(self.largeur/2,120,image=self.titre,tag="TITRE")
        self.canvas.pack()
        self.canvas.delete("PierreR")
        self.canvas.delete("TITRER")
        self.canvas.delete("CABANE")
        self.canvas.delete("Poke")
        self.canvas.delete("PierreM")
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
        self.canvas.create_image(260,275,image=self.pierreR,tag="PierreR")
        self.boutonB.place(relx=0.8, rely=0.6, anchor="center")
        self.texte.place(relx=0.5, rely=0.8, anchor="center")
        

    def Pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        else: 
            pygame.mixer.music.play()

    def Jouer(self):
        self.cam.place_forget()
        self.canvas.delete("Pikachu")
        self.canvas.delete("Mentali")
        self.canvas.delete("Tiplouf")
        self.canvas.delete("PierreP")
        self.canvas.delete("Pikachu")
        self.canvas.delete("Mentali")
        self.canvas.delete("Tiplouf")
        self.canvas.delete("PierreP")
        self.canvas.delete("TITRE")
        self.canvas.delete("Point_int")
        self.canvas.delete("PierrePB")
        self.cacher_boutons()
        print('nom:',self.name)
        self.canvas.delete(self.name)
        self.boutonB.place(relx=0.4, rely=0.9, anchor="center")
        self.boutonN.place(relx=0.6, rely=0.9, anchor="center")
        self.canvas.delete("Poke")
        self.canvas.create_image(300,250,image=self.poke,tag="Poke")
        self.canvas.create_image(730,260,image=self.pierreM,tag="PierreM")
        self.texte2.place(relx=0.70, rely=0.75, anchor="center")
        

    
    def InterPhoto(self):
        self.cacher_boutons()
        self.canvas.delete("PierreM")
        self.boutonB2.place(relx=0.3, rely=0.9, anchor="center")
        self.boutonP.place(relx=0.7, rely=0.9, anchor="center")
        self.cam.place(x=475,y=125)
        self.cam.togle_cam()
        
    def find_poke_update_reponse(self):
        self.name, self.confidence = find_pokemon()
        if self.name != None:
            print(f"Objet détecté : {self.name}, Score de confiance : {self.confidence}")
            if self.name == "tiplouf":
                self.canvas.create_image(310,220,image=self.tiplouf,tag="tiplouf")
                self.canvas.create_image(750,180,image=self.pierreP,tag="PierreP")
                self.response['text'] = "Piplup"
            
            if self.name == "mentali":
                self.canvas.create_image(315,220,image=self.mentali,tag="mentali")
                self.canvas.create_image(750,200,image=self.pierreP,tag="PierreP")
                self.response['text'] = "Espeon"
            
            if self.name == "pikachu":
                self.canvas.create_image(330,200,image=self.pikachu,tag="pikachu")
                self.canvas.create_image(750,200,image=self.pierreP,tag="PierreP")
                self.response['text'] = "Pikachu"
        else :
            self.canvas.create_image(315,230,image=self.pastrouve,tag="Point_int")
            self.canvas.create_image(750,180,image=self.pierrePB,tag="PierreP")
            self.response['text'] = "Pokémon non identifié"
            
    def Photo(self):
        self.cam.togle_cam()
        self.cacher_boutons()
        self.canvas.create_image(310,280,image=self.rondin,tag="Rondin")
        self.canvas.delete("Poke")
        save_frame(self.cam.Frame())
        self.find_thread = threading.Thread(target=self.find_poke_update_reponse)
        self.find_thread.start()
        self.progress_bar.start()
        self.updateProgressBar()
        self.progress_bar.place(relx=0.325, rely=0.35, anchor="center")
        self.response.place(relx=0.325, rely=0.65, anchor="center")
        self.cam.place_forget()
        self.boutonM.place(relx=0.4, rely=0.9, anchor="center")
        self.boutonRe.place(relx=0.6, rely=0.9, anchor="center")

        


    def updateProgressBar(self):
        if not self.find_thread.is_alive():
            self.progress_bar.stop()
            self.progress_bar.place_forget()
            return
        self.progress_bar.step(10)
        self.after(100, self.updateProgressBar)
        
if __name__ == "__main__":
    app = Menu()
    app.mainloop()
