import cv2

def num_save(num):
    """
    Save the current image number to a text file.

    Args:
    - num (int): The current image number.

    Returns:
    - None
    """
    with open('enregistrement/num.txt', 'w') as file:
        file.write(str(num))

def recup_num():
    """
    Retrieve the current image number from a text file.

    Returns:
    - int: The current image number.
    """
    with open('enregistrement/num.txt', 'r') as file:
        num = file.read()
        return int(num)

def save_frame(frame):
    """
    Save a frame as an image file with a unique filename.

    Args:
    - frame (numpy.ndarray): The frame to be saved.

    Returns:
    - None
    """
    target_width = int(750 * frame.shape[1] / frame.shape[0])
    resized_frame = cv2.resize(frame, (target_width, 750))
    num = recup_num() + 1
    filename = 'enregistrement/save' + str(num) + '.png'
    cv2.imwrite(filename, resized_frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    num_save(num)
