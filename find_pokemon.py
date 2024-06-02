from PIL import Image
from ultralytics import YOLO
from save_img import recup_num

def find_pokemon(confidence_threshold=0.7):
    """
    Detects Pokemon in an image using a trained YOLO object detection model.

    Args:
    - confidence_threshold (float): Confidence threshold for considering a detection as valid.
    
    Returns:
    - tuple: A tuple containing the name of the detected Pokemon and its confidence score.
    """

    # Open the image
    image_path = 'enregistrement/save' + str(recup_num()) + '.png'
    image = Image.open(image_path)

    # Initialize the YOLO model
    model = YOLO("runs/detect/total_v2/weights/best.pt")

    result = []

    # Rotate the image and perform object detection at various angles
    for i in range(-10, 11, 5):
        image_rotated = image.rotate(i)
        detections = model(image_rotated)[0]
        
        for box in detections.boxes:
            result.append([model.names.get(box.cls.item()), box.data.tolist()[0][4]])

    # If multiple detections, select the one with the highest confidence
    if len(result) > 1:
        res = max(result, key=lambda x: x[1])
        
        # Check if confidence exceeds threshold
        if res[1] > confidence_threshold:
            return res
        else:
            return [None, None]
        
    # If single detection, return it
    elif len(result) == 1:
        return result[0]
    
    # If no detection, return None
    else:
        return [None, None]
