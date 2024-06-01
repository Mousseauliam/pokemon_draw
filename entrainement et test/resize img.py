import os
import cv2

# Function to resize an image while maintaining aspect ratio
def resize_image_keep_ratio(image, target_height):
    height, width = image.shape[:2]
    ratio = target_height / height
    resized_image = cv2.resize(image, (int(width * ratio), target_height))
    return resized_image

# Source folder containing the images
input_folder = "bddpokemon/Mentali"
# Destination folder for resized images
output_folder = "datasets/train/mentali/images"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through the source folder
for filename in os.listdir(input_folder):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        input_path = os.path.join(input_folder, filename)
        img = cv2.imread(input_path)
        resized_img = resize_image_keep_ratio(img, 750)
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, resized_img)
        print(f"Image {filename} resized and saved to {output_folder}")

print("Image resizing complete.")
