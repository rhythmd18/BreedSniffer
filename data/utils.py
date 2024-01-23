import cv2
import numpy as np

def preprocess_img(path, size):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    processed_img = resize(pad_image(img), size)
    return processed_img



def pad_image(img):
    if img.shape[0] < img.shape[1]:
        pad = np.zeros((img.shape[1] - img.shape[0], img.shape[1]))
        axis = 0
    else:
        pad = np.zeros((img.shape[0], img.shape[0] - img.shape[1]))
        axis = 1
    padded_img = np.concatenate((img, pad), axis=axis)
    return padded_img



def resize(img, size):
    resized_img = cv2.resize(img, (size, size))
    return resized_img


if __name__=='__main__':
    img = cv2.imread('./data/raw_images/train/golden retriever/golden-retriever (2).jpg', cv2.IMREAD_GRAYSCALE)
    img = pad_image(img)
    img = resize(img, 100)
    cv2.imwrite('./padded_81.jpg', img)