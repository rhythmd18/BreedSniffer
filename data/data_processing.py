import cv2
import numpy as np
import os
import argparse
from utils import preprocess_img


parser = argparse.ArgumentParser()
parser.add_argument('type', action='store', help='Specify the type of data to preprocess (train or test)')
args = parser.parse_args()


if args.type == 'train' or args.type == 'test':
    path = f'./data/raw_images/{args.type}'
    dest = f'./data/images/{args.type}'
else:
    raise ValueError('Please specify the type of data correctly to preprocess (\'train\' or \'test\')')


def preprocess_data(path, dest):
    """
    Preprocesses data from the given path and saves it to the specified destination.
    
    Args:
        path (str): The path to the directory containing the data.
        dest (str): The destination directory where the preprocessed data will be saved.
        
    Returns:
        None
    """
    for breed in os.listdir(path):
        breed_path = os.path.join(path, breed) # f"{path}/{breed}"
        os.mkdir(os.path.join(dest, breed))
        img_idx = 0
        print(f'Preprocessing {breed}... ', end='')
        for image in os.listdir(breed_path):
            image_path = os.path.join(breed_path, image) # f"{breed_path}/{image}"
            img = preprocess_img(image_path, 200)
            dest_path = os.path.join(dest, breed)
            cv2.imwrite(f'{dest_path}/{img_idx}.jpg', img)
            img_idx += 1
        print('Done!')

if __name__=='__main__':
    preprocess_data(path, dest)
