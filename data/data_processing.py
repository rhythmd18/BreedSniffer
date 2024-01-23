import cv2
import numpy as np
import os
from utils import preprocess_img

path = './data/raw_images/train'
dest = './data/images/train'

def preprocess_data(path, dest):
    for breed in os.listdir(path):
        breed_path = os.path.join(path, breed) # f"{path}/{breed}"
        os.mkdir(os.path.join(dest, breed))
        img_idx = 0
        for image in os.listdir(breed_path):
            image_path = os.path.join(breed_path, image) # f"{breed_path}/{image}"
            img = preprocess_img(image_path, 200)
            dest_path = os.path.join(dest, breed)
            cv2.imwrite(f'{dest_path}/{img_idx}.jpg', img)
            img_idx += 1

preprocess_data(path, dest)
