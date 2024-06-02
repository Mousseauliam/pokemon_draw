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
import random

class Menu(tk.Tk):
    name=str
    
    def __init__(self):
        tk.Tk.__init__(self)
        """
        Creation of all necessary the elements for the interface.

        """
        # Lauch the camera in another thread.

        self.charg_cam()
        
        # Initialization of the music module then loading and playing the song (it will be looped).

        pygame.mixer.init()
        pygame.mixer.music.load("elements graphique/Musique.mp3")
        pygame.mixer.music.play(-1)
            
        # Creation of all images and resizing if necessary.

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

        # Creation of the display window.
        
        self.hauteur = self.gif.height()
        self.largeur= self.gif.width()
        self.resizable(width=False,height=False)
        self.title("POKÉDRAW")
        self.canvas = tk.Canvas(self, width=self.largeur, height=self.hauteur)
        
        # Creation of writting fonts.

        self.police = ctk.CTkFont("dogica", size=22)
        self.policeR = ctk.CTkFont("dogica", size=15)
        self.police2 = ctk.CTkFont("Courier", size=15)

        # Creation of all buttons.

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
    
        # Creation of all the texts.
        self.textReponse = [["Brock: It’s a Pikachu ! Did you know ? The impact\nand success of the Pokemon is such that the\nfranchise inspired science during a discovery.\nIn 2008, Japanese researchers discovered a\nnew protein that reacts to electricity. So\nthey simply decided to call it Pikachurine\n in obvious reference to Pikachu.",
                             "Brock: Ah! I know a Pikachu when I see one! Tell me\n, did you know that the name Pikachu had a\n rather funny origin? Indeed the “Pika” would\n come from the Japanese onomatopoeia\n “pika-pika” which would mean something\n sparkling, brilliant.  The “chu” would come from\n the noise made by a mouse in Japanese!",
                             "Brock: Wow! What a nice drawing of Pikachu! These\nPokemons live in the forest away from humans.\nThey basically eat fruit. When they are not\nmature enough, they electrify them with\nelectricity stored in their cheeks to make them\nmore tender. If a storm is approaching, it is\nbecause several Pikachu have gathered!"
                             ],["Brock: It’s a Piplup ! Despite appearances, it’s a very\nproud Pokémon that has a hard time\nconnecting with its trainer. He has a very\nawkward walk but still proudly bombs the\ntorso. He is also an excellent swimmer, who can\nsnorkel under water for up to ten minutes while\nhunting.",
                            "Brock: What a beautiful drawing of Piplup ! Did you\nknow that this Pokémon and its evolutions\nare mainly inspired by the emperor Napoleon\nBonaparte? Indeed, the name of his last\nevolution Empoleon is composed of \n“Emperor” and “Napoleon”, plus its size is\n1m70 or almost that of the French emperor.",
                            "Brock: I love this Piplup drawing! It’s a very popular\nPokémon among the Pokémon community.\nThis popularity is partly due to the Pokémon\nDiamond and Pearl games that rank fourth\namong the best-selling games of the\nNintendo DS, the 2nd best-selling console\nof all time."
                            ],["Brock: It’s a Espeon! The gem he wears in the\nmiddle reinforces the psychic powers he has\nacquired to protect his Trainer. His forked tail\nshudders when he predicts the movements of\nhis opponents. It is rare to find Mentali in the\nwild, and it is more often visible in urban areas.",
                            "Brock: Wow! Great drawing you made us there!\nApparently, Espeon’s appearance seems\nto be inspired by the legends of Bakeneko\nand Nekomata, two yōkai depicted as\nmysterious and intelligent cats with\nsupernatural powers. Unfortunately, this\ninformation has never been confirmed by the\ncreators.",
                            "Brock: Ah! That’s a beautiful drawing of Espeon!\nThis Pokemon is extremely faithful to any\nTrainer he deems worthy. It is said that this\nPokemon has developed its precognitive\npowers to protect its trainer from evil. He also\nlearned to read drafts in order to predict the\nmovements of these opponents."
                            ],"Oh… Looks like I couldn’t recognize the\nPokemon you wanted to draw! Maybe the\npicture was not taken correctly, make sure you\nhave good lighting! (Or maybe your drawing was\nhorrible, but I dare not tell you…)"]
        self.texteFinal = tk.Label(self,justify="left",bg="white",bd=4,relief="ridge",fg="black",font=self.police2)
        self.texte = tk.Label(self,justify="left",bg="white",bd=4,relief="ridge",fg="black",font=self.police2,text="Brock: Hey, my name is Brock! I hope you are ready to show me your best\nartistic talents. First, draw one of the three Pokemon proposed: Pikachu,\nPiplup and Espeon. Once your beautiful drawing is done, show it to me\non camera and take a picture! If the artist’s soul is in you, I should be able\n to recognize which Pokémon you drew to give you some anecdotes about it!")
        self.response = tk.Label(self,justify="left",bg="white",bd=4,relief="ridge",fg="black",font=self.policeR,text= "")
        self.texte2 = tk.Label(self,justify="left",bg="white",bd=4,relief="ridge",fg="black",font=self.police2,text="Brock : Choose the Pokémon you want to draw!\nDon’t hesitate to go online to get inspired!")
       
        # Display the menu.

        self.AfficheMenu()
        
        # Loading bar.

        self.progress_bar = ttk.Progressbar(self, orient="horizontal", mode="indeterminate")
    
    def charg_cam(self):
        """
        Purpose: Lauch the camera.

        """
        def cam_th():
            self.cam = Cweb(self)
        thread = threading.Thread(target=cam_th)
        thread.start()
    
    def cacher_boutons(self):
        """
        Purpose: Remove the progress bar, all buttons and texts from a page.

        """
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkButton) or isinstance(widget, tk.Label) or isinstance(widget, ttk.Progressbar):
                widget.place_forget()
        self.canvas.delete("all")
        self.canvas.create_image(self.largeur/2, self.hauteur/2, image=self.gif,tag="fond")

    def AfficheMenu(self):
        """
        Purpose: Creation of the home menu.
        
        """
        self.cacher_boutons()
        self.canvas.create_image(self.largeur/2,120,image=self.titre,tag="TITRE")
        self.canvas.pack()
        self.boutonJ.place(relx=0.5, rely=0.5, anchor="center")
        self.boutonR.place(relx=0.5, rely=0.625, anchor="center")
        self.boutonQ.place(relx=0.5, rely=0.75, anchor="center")
        self.boutonS.place(relx=0.9, rely=0.9, anchor="center")
        
    def AfficheRegles(self):
        """
        Purpose: Creation of the Rules page.

        """
        self.cacher_boutons()
        self.canvas.create_image(self.largeur/2,self.hauteur/2,image=self.cabane,tag="CABANE")
        self.canvas.create_image(self.largeur/2,120,image=self.regle,tag="TITRER")
        self.canvas.create_image(260,275,image=self.pierreR,tag="PierreR")
        self.boutonB.place(relx=0.8, rely=0.6, anchor="center")
        self.texte.place(relx=0.5, rely=0.8, anchor="center")
        

    def Pause(self):
        """
        Purpose: Creation of the pause fonction for the SOUND button.

        """
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else: 
            pygame.mixer.music.unpause()

    def Jouer(self):
        """
        Purpose: Creation of the Play page.
        
        """
        self.cam.place_forget()
        self.response['text'] = ""
        self.texteFinal['text'] = ""
        self.cacher_boutons()
        self.boutonB.place(relx=0.4, rely=0.9, anchor="center")
        self.boutonN.place(relx=0.6, rely=0.9, anchor="center")
        self.canvas.create_image(300,250,image=self.poke,tag="Poke")
        self.canvas.create_image(730,260,image=self.pierreM,tag="PierreM")
        self.texte2.place(relx=0.70, rely=0.75, anchor="center")
        

    
    def InterPhoto(self):
        """
        Purpose: Creation of the Take A Picture page.
        
        """
        self.cacher_boutons()
        self.canvas.create_image(300,250,image=self.poke,tag="Poke")
        self.boutonB2.place(relx=0.3, rely=0.9, anchor="center")
        self.boutonP.place(relx=0.7, rely=0.9, anchor="center")
        self.cam.place(x=475,y=125)
        self.cam.togle_cam()
        
    def find_poke_update_reponse(self):
        """
        Purpose: Analyze the photo that has just been taken and display the right items according to the pokemon detected.
        
        """
        self.name, self.confidence = find_pokemon()

        if self.name != None:
            print(f"Objet détecté : {self.name}, Score de confiance : {self.confidence}")
            if self.name == "tiplouf":
                self.canvas.create_image(310,220,image=self.tiplouf,tag="tiplouf")
                self.canvas.create_image(750,200,image=self.pierreP,tag="PierreP")
                self.texteFinal['text']=random.choice(self.textReponse[1])
                self.response['text'] = "Piplup"
            
            if self.name == "mentali":
                self.canvas.create_image(315,220,image=self.mentali,tag="mentali")
                self.canvas.create_image(750,200,image=self.pierreP,tag="PierreP")
                self.texteFinal['text']=random.choice(self.textReponse[2])
                self.response['text'] = "Espeon"
            
            if self.name == "pikachu":
                self.canvas.create_image(330,200,image=self.pikachu,tag="pikachu")
                self.canvas.create_image(750,200,image=self.pierreP,tag="PierreP")
                self.texteFinal['text']=random.choice(self.textReponse[0])
                self.response['text'] = "Pikachu"
        else :
            self.canvas.create_image(315,230,image=self.pastrouve,tag="Point_int")
            self.canvas.create_image(750,185,image=self.pierrePB,tag="PierrePB")
            self.texteFinal['text']=self.textReponse[3]
            self.response['text'] = "Pokemon not found"
        
            
    def Photo(self):
        """
        Porpose: Creation of the results page.
        
        """
        self.cam.togle_cam()
        self.cacher_boutons()
        self.canvas.create_image(310,280,image=self.rondin,tag="Rondin")
        save_frame(self.cam.Frame())
        self.find_thread = threading.Thread(target=self.find_poke_update_reponse)
        self.find_thread.start()
        self.progress_bar.start()
        self.updateProgressBar()
        self.progress_bar.place(relx=0.325, rely=0.35, anchor="center")
        self.response.place(relx=0.325, rely=0.65, anchor="center")
        self.texteFinal.place(relx=0.70, rely=0.65, anchor="center")
        self.cam.place_forget()
        self.boutonM.place(relx=0.4, rely=0.9, anchor="center")
        self.boutonRe.place(relx=0.6, rely=0.9, anchor="center")
        


    def updateProgressBar(self):
        """
        Purpose: Allows the loading bar to operate
        
        """
        if not self.find_thread.is_alive():
            self.progress_bar.stop()
            self.progress_bar.place_forget()
            return
        self.progress_bar.step(10)
        self.after(100, self.updateProgressBar)
        
if __name__ == "__main__":
    """
    Purpose: Allows the code to be executed when the file runs as a script.

    """
    app = Menu()
    app.mainloop()
