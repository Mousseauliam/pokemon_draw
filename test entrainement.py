from ultralytics import YOLO
 
# Load the model.
model = YOLO("yolov8n.pt")
 
# Training.
results = model.train(
   data='total.yaml',
   imgsz=750,
   epochs=50,
   batch=8,
   name='total_v1'
)