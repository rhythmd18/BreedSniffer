import cv2
import numpy as np

def preprocess_img(path, size):
    img = cv2.imread(path)
    processed_img = resize(img, size)
    return processed_img


def resize(img, size):
    resized_img = cv2.resize(img, (size, size))
    return resized_img


if __name__=='__main__':
    img = cv2.imread('./data/raw_images/train/golden retriever/81.jpg')
    img = resize(img, 100)
    cv2.imwrite('./padded_81.jpg', img)