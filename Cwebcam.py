import tkinter as tk
from PIL import Image, ImageTk
import cv2
from save_img import save_frame

class Cweb(tk.Canvas):
    width = 400
    height = 300
    
    def __init__(self, window, video_source=0):
        # Initialize the canvas with given width and height
        tk.Canvas.__init__(self, window, width=self.width, height=self.height)
        self.window = window
        
        # Open the video source (default is webcam)
        self.vid = cv2.VideoCapture(video_source)
        
        # Flag to indicate if camera is active
        self.cam = False
    
    def update(self):
        # Read a frame from the video source
        ret, frame = self.vid.read()
        self.frame = frame
        
        if ret:
            # Flip the frame horizontally so you don't have a mirror effect
            frame = cv2.flip(frame, 1)
            
            # Convert the frame from BGR to RGB format
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Resize the image to match canvas dimensions
            image_r = cv2.resize(image, (self.width, self.height))
            
            # Convert the image array to a PIL Image
            image = Image.fromarray(image_r)
            
            # Convert the PIL Image to a Tkinter-compatible PhotoImage
            photo = ImageTk.PhotoImage(image=image)
            
            # Display the image on the canvas
            self.create_image(0, 0, image=photo, anchor=tk.NW)
            self.photo = photo
        
        # Repeat this function at regular intervals if camera is active
        if self.cam:
            self.window.after(10, self.update)

    def Frame(self):
        # return the current frame
        ret, frame = self.vid.read()
        return frame

    def togle_cam(self):
        # Toggle the camera on/off
        self.cam = not self.cam
        
        # If camera is activated, start updating the canvas
        if self.cam:
            self.update()
