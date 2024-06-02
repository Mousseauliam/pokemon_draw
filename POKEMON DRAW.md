<div style="text-align: right;">
    BOILEAU Juline<br>
    BOULGHIB Jenine<br>
    MILAKOVIC Noah<br>
    MOUSSEAU Liam
</div>

![Title](elements_graphique/TITREPIXEL.png)

Welcome to PokemonDraw! The aim of this game is to allow the user to draw a Pokémon and show it to the camera so that the computer can recognize it.

We will try to describe the different steps of this project in the following paragraphs:

<font color="#1F28AE">

- *Model Training*
   - *Model Selection*
   - *Building a Pokemon Image Database*
   - *Data Formatting*
   - *Training*

- *Graphical Interface*
    - *Introduction*
    - *Explanation of the Main Code*
    - *Explanation of Auxiliary Scripts*

</font>

To optimize our time, we segmented the steps to be performed and then merged them together to have a complete code. For this, we used GITHUB, an open source platform for version control and collaboration aimed at software developers to facilitate work in parallel.

To launch Pokedraw, simply execute the `main_windows` script. Depending on the computer, there may be an error if you click too quickly on...

# Model Training

## Model Selection

The first choice we made was to choose which model we wanted to train. We turned to the open-source YOLO model because there was a lot of documentation available and good results.

## Building a Pokemon Image Database

First, we selected a starter of 3 Pokémon of different colors and shapes as a base to facilitate their differentiation.

![Starter](startera.png)

We populated the image bank of each of these Pokémon using digital images available on the internet, drawings found online, and drawings we made ourselves to cover a maximum of characteristics specific to each of our Pokémon. We selected them in color and in black and white to be able to recognize a drawing that would be in color or not. The database gathers about 80 images/drawings for each of our Pokémon to enrich and diversify it for machine learning purposes.

## Data Formatting

With the help of the software (help me Juline, I don't remember the name!), we were able to format our database, i.e., specify which image corresponds to what. This process is called labeling, it allows us to create a text file for each image that contains the ID of the Pokémon present in the image (each Pokémon is associated with a number) and its position.

## Training

To carry out this part, we used several scripts, notably two test scripts found on the internet (`webcam training` and `yolo on image`) which allow testing a model live on the webcam or on saved images. All the different scripts we used for training the model are present in the `training and testing` folder along with a few images to test the performance of our models. There is also a script (`resize img`) that we wrote to resize all the images in our database and standardize the format. To start training, two files are needed, a .yaml file containing the paths to the database and a python script that loads the model and starts training according to the parameters of the yaml file. Initially, we experimented by training a model only to detect Pikachu. Then, using the test files described above, we were able to test the model. By tinkering little by little, we managed to get a relatively satisfactory model capable of differentiating between the different Pokémon. Unfortunately, we noticed that our model tends to mistake humans for Espeon, a recurring problem but not very annoying if the model is used correctly insofar as we are not supposed to show it pictures of humans.

# Graphical Interface

## Introduction

![Pokedraw](elements_graphique/CaptureMD.PNG)

## Explanation of the Main Code


## Explanation of Auxiliary Scripts

As previously stated, to make the project more understandable, we divided it into several scripts. This allows compartmentalizing certain functions and simplifying reading. I will try in the following lines to explain the utility and functioning principle of these scripts:

**Cwebcam**

The `Cweb` class inherits from the `Canvas` class of Tkinter and encapsulates webcam functionality to capture and display real-time video streams in a graphical interface. It manages video capture, image processing (such as flipping and resizing), and displaying images on the canvas. Declaring this functionality in a separate script improves code modularity and reusability while allowing for less 'heavy' writing.

**find_pokemon**

The `find_pokemon` function uses the YOLO model to detect and recognize Pokémon in an image. The image is input to the function, then we perform image rotation from -10 to 10 degrees in increments of 5, and we perform detection with the YOLO model and store the results in a list. This method is a bit longer than passing the image through the model only once but it allows for more reliable results. In the array, each result contains the name of the detected object and the associated confidence. In case of multiple detections, we filter the results to find the one with the highest confidence and that exceeds the specified threshold. If no result exceeds the threshold, we return [None, None].

<font color="#FF0000">

## Jenine's Work draw from here for your part

## Retrieval of the Drawing

We first import the datetime, ultralytics' YOLO, and cv2 libraries for image and video manipulation with OpenCV. Then, we define constants such as the confidence threshold for detections and the green color for detection boxes. We load the pre-trained YOLOv8n model from the yolov8n.pt file.

We initialize video capture from a video file using `cv2.VideoCapture`. In a loop, we start by measuring the processing time of each image to calculate the FPS later. If no new image is captured, we exit the loop. We apply the YOLO model to each captured image to get detections. For each detection, we extract the object name and associated confidence, and we filter out detections with confidence below the defined threshold.

For valid detections, we draw detection boxes on the image using `cv2.rectangle` and display the object name and confidence using `cv2.putText`. We calculate and display FPS on each processed image, then show the image on the screen with `cv2.imshow`. If the user presses the 'q' key, we exit the loop. Finally, we release video resources with `video_cap.release()` and close all windows opened by OpenCV with `cv2.destroyAllWindows`.

## Pokémon Recognition

From there, we apply our already trained supervised learning recognition on the image which returns in a result the Pokémon identified by the machine.

## Return of Pokémon-related information

Since our machine has learned to recognize the starter Pokémon, we will be able to exploit the response given at the end of the processing. Indeed, we retrieve the Pokémon returned as output and link it to the Pokémon database [PokéAPI](https://pokeapi.co/api/v2/pokemon/) to extract its specific information: its name, size, weight, and color.

For this, we define a `PokemonName` function which allows us to work with a remote database via an API. First, we query the database by building a URL from the `base_url` and `pokemon` variables in the `1_requetes_http.py` file. Once this is done, we use the `requests` library. Then,