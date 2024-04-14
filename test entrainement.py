from ultralytics import YOLO
 
# Load the model.
model = YOLO("yolov8n.pt")
 
# Training.
"""
results = model.train(
   data='pikachu.yaml',
   imgsz=750,
   epochs=50,
   batch=8,
   name='pikachu_v2'
)"""

results = model.train(
   data='tiplouf.yaml',
   imgsz=750,
   epochs=50,
   batch=8,
   name='ti+pi_v1'
)