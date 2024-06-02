from ultralytics import YOLO
 
# Load the model.
model = YOLO("yolov8n.pt")
 
# allows you to start training the model. and save the result in the runs folder under the name total_v3
results = model.train(
   data='total.yaml',
   imgsz=750,
   epochs=200,
   batch=8,
   name='total_v3'
)