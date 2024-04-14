#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import datetime
from ultralytics import YOLO
import cv2
from imutils.video import VideoStream
#from helper import create_video_writer


# define some constants
CONFIDENCE_THRESHOLD = 0.1
GREEN = (0, 255, 0)

def resize_image_keep_ratio(image, target_height):
    # Récupérer les dimensions de l'image
    height, width = image.shape[:2]
    
    # Calculer le facteur de redimensionnement
    ratio = target_height / height
    
    # Redimensionner l'image en conservant le ratio
    resized_image = cv2.resize(image, (int(width * ratio), target_height))
    
    return resized_image

image_list=['pika1.png','pika2.png','pika3.png','pika4.png','pika5.jpg','pika6.jpeg','pika7.jpg','pika8.png','pika9.jpg','test.png']

# load the pre-trained YOLOv8n model
#model = YOLO("yolov8n.pt")
model = YOLO("runs/detect/total_v2/weights/best.pt") # test trained model


for i,img in enumerate(image_list):
    #detect on image
    frame=resize_image_keep_ratio(cv2.imread(img),600)

    detections = model(frame)[0]
    # loop over the detections
    #for data in detections.boxes.data.tolist():
    for box in detections.boxes:
        #extract the label name
        label=model.names.get(box.cls.item())
            
        # extract the confidence (i.e., probability) associated with the detection
        data=box.data.tolist()[0]
        confidence = data[4]

        # filter out weak detections by ensuring the
        # confidence is greater than the minimum confidence
        if float(confidence) < CONFIDENCE_THRESHOLD:
            continue

        # if the confidence is greater than the minimum confidence,
        # draw the bounding box on the frame
        xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
        cv2.rectangle(frame, (xmin, ymin) , (xmax, ymax), GREEN, 2)

        #draw confidence and label
        y = ymin - 15 if ymin - 15 > 15 else ymin + 15
        cv2.putText(frame, "{} {:.1f}%".format(label,float(confidence*100)), (xmin, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, GREEN, 2)

    
    # show the frame to our screen
    cv2.imshow("Img{}".format(i), frame)

while True:
    if cv2.waitKey(1) == ord("q"):
        break