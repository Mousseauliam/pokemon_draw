import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.image import imread

    base_url = "https://pokeapi.co/api/v2/pokemon/"
    pokemon = "pikachu"
    
    res=requests.get(base_url+pokemon).json()

    print("Affichage de l'image du pokemon : " + pokemon)
    image_url = res1['sprites']['front_default']
    response = requests.get(image_url, stream=True)
    img = imread(BytesIO(response.content))
    
    plt.figure()
    plt.imshow(img, aspect='auto')
    plt.xticks([], [])
    plt.yticks([], [])
    plt.show()