from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='pikachu.yaml',
   imgsz=1280,
   epochs=50,
   batch=8,
   name='test pika'
)