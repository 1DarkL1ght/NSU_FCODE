import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.data import astronaut


def process_image(image: cv2.Mat, delta: float) -> cv2.Mat:
    image_cpy = image.copy()
    image_cpy[:, :, 2] = image_cpy[:, :, 2] * delta

    return image_cpy


def main():
    # Load image
    image = astronaut()
    
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
            break


if __name__ == "__main__":
    main()