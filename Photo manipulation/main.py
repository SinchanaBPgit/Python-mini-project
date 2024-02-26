import cv2
import numpy as np

def adjust_brightness(image, factor):
    adjusted_image = cv2.convertScaleAbs(image, alpha=factor, beta=0)
    return adjusted_image

def adjust_contrast(image, factor, midpoint=127):
    adjusted_image = np.int16(image)
    adjusted_image = adjusted_image * factor + (midpoint * (1 - factor))
    adjusted_image = np.clip(adjusted_image, 0, 255)
    adjusted_image = np.uint8(adjusted_image)
    return adjusted_image

def apply_blur(image, kernel_size):
    blurred_image = cv2.blur(image, (kernel_size, kernel_size))
    return blurred_image

def apply_kernel(image, kernel):
    filtered_image = cv2.filter2D(image, -1, kernel)
    return filtered_image

def combine_images(image1, image2):
    combined_image = np.sqrt(np.square(image1) + np.square(image2))
    combined_image = np.clip(combined_image, 0, 255)
    combined_image = np.uint8(combined_image)
    return combined_image

if name == "main":
    image1 = cv2.imread("image1.jpg")
    image2 = cv2.imread("image2.jpg")

    
    brightened_image = adjust_brightness(image1, 1.5)

    contrasted_image = adjust_contrast(image1, 1.5)

    blurred_image = apply_blur(image1, 5)

    sobel_kernel = np.array([[-1, 0, 1],
                             [-2, 0, 2],
                             [-1, 0, 1]])

    edges_image = apply_kernel(image1, sobel_kernel)

    combined_image = combine_images(image1, image2)
