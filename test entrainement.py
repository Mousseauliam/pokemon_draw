from ultralytics import YOLO
 
# Load the model.
model = YOLO("runs/detect/v1_pikachu/weights/best.pt")
 
# Training.
results = model.train(
   data='pikachu.yaml',
   imgsz=750,
   epochs=50,
   batch=8,
   name='test pikav1 dd'
)