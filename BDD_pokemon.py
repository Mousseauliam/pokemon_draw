import requests
from io import BytesIO
from matplotlib.image import imread
import matplotlib.pyplot as plt
import pickle
import os

base_url = "https://pokeapi.co/api/v2/pokemon/"
pokemon_names = ["pikachu", "piplup", "mew"]
pokemon_data = []

file_name = 'pokemon_data.pkl'

if os.path.isfile(file_name):
    with open(file_name, "rb") as file:
        pokemon_data = pickle.load(file)
    print("Données des pokémons chargées depuis le fichier.")
    
    for pok in pokemon_data:
        plt.figure()
        plt.imshow(pok['image'], aspect='auto')
        plt.title(pok['name'])
    
else:
    for name in pokemon_names:
        res = requests.get(base_url + name).json()
        print("Affichage de l'image du pokemon : " + name)
        image_url = res['sprites']['front_default']
        response = requests.get(image_url, stream=True)
        img = imread(BytesIO(response.content))
        pokemon_data.append({"name": name, "image": img})

        plt.figure()
        plt.imshow(img, aspect='auto')
        plt.title(name)

    with open(file_name, "wb") as file:
        pickle.dump(pokemon_data, file)
    print("Données des pokémons sauvegardées avec succès.")
plt.show()