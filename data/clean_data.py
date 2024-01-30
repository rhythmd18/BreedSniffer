import os

train_path = './data/raw_images/train'
test_path = './data/raw_images/test'

def clean_data(path):
    for folder in os.listdir(path):
        folder_path = os.path.join(path, folder)
        if 'pageInfo.txt' in os.listdir(folder_path):
            os.remove(os.path.join(folder_path, 'pageInfo.txt'))

clean_data(train_path)
clean_data(test_path)