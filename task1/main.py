import cv2
import numpy as np
from skimage.data import astronaut
from jsonargparse import CLI

def process_image(image: cv2.Mat, delta: float) -> cv2.Mat:
    """Changes S (saturation) channel in HSV image"""

    image_cpy = image.copy()
    image_cpy[:, :, 1] = image_cpy[:, :, 1] * delta

    if np.any(image_cpy[:, :, 1] > 255):
        print("Warning! Clipping by value 255")
        image_cpy = np.clip(image_cpy, 0, 255)

    return image_cpy


def main(image_path: str | None=None):
    """Main function. Loads image, converts to HSV, calls process_image(), converts back to BGR, visualizes results"""
    # Load image
    if image_path is None:
        image = astronaut()
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    else:
        image = cv2.imread(image_path)

    assert len(image.shape) == 3 and image.shape[-1] == 3

    # Convert to HSV color palette
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Process image
    image_hsv_lower_s = process_image(image_hsv, delta=0.5)
    image_hsv_higher_s = process_image(image_hsv, delta=2)

    # Convert back to RGB
    image_new_lower_s = cv2.cvtColor(image_hsv_lower_s, cv2.COLOR_HSV2BGR)
    image_new_higher_s = cv2.cvtColor(image_hsv_higher_s, cv2.COLOR_HSV2BGR)

    # Show image
    while True:
        cv2.imshow("Original", image)
        cv2.imshow("Lower S channel", image_new_lower_s)
        cv2.imshow("Higher S channel", image_new_higher_s)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            del image, image_hsv, image_hsv_lower_s, image_hsv_higher_s, image_new_lower_s, image_new_higher_s
            break


if __name__ == "__main__":
    CLI(main, as_positional=False)