from PIL import Image
from ultralytics import YOLO
from save_img import recup_num

def find_pokemon(confidence_threshold=0.7):
    image_path = 'enregistrement/save'+str(recup_num())+'.png'
    image = Image.open(image_path)

    # Initialisation du modèle YOLO
    model = YOLO("runs/detect/total_v2/weights/best.pt")
    result=[]
    for i in range(-10,11,5):
        image_rotated = image.rotate(i)
        #image_rotated.show()
        detections = model(image_rotated)[0]
        for box in detections.boxes:
            result.append([model.names.get(box.cls.item()),box.data.tolist()[0][4]])
    print(result)
    if len(result)>1:
        res=max(result, key=lambda x: x[1])
        if res[1]>confidence_threshold:
            return res
        else:
            return[None,None]
    elif len(result)==1:
        return result[0]
    else:
        return [None,None]
