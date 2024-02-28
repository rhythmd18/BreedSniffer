import torch
import torch.nn as nn
from torchvision.transforms import v2
from torchvision.models import vgg16, VGG16_Weights
import joblib
import cv2


def extract_features_for_a_batch(model, batch):
    '''
    Extract features for a batch of images
    args:
        model: nn.Module
        batch: torch.Tensor
    returns:
        features: torch.Tensor
    '''
    features = model(batch)
    return features


def extract_all_features(model, dataloader):
    '''
    Extract features for all images in a dataloader
    args:
        model: nn.Module
        dataloader: torch.utils.data.DataLoader
    returns:
        all_features: numpy.ndarray
        labels: numpy.ndarray
    '''
    all_features = []
    labels = []
    model.eval()
    with torch.no_grad():
        for X, y in dataloader:
            batch_features = extract_features_for_a_batch(model, X)
            labels.append(y)
            all_features.append(batch_features)
    
    all_features = torch.cat(all_features, dim=0).cpu().numpy()
    all_features = all_features.reshape(all_features.shape[0], -1)
    
    labels = torch.cat(labels, dim=0).cpu().numpy()
    labels = labels.reshape(labels.shape[0])
    return all_features, labels


def feature_extractor():
    """
    This function initializes a VGG16 model with pre-trained ImageNet weights, 
    modifies its avgpool and classifier layers to be identity layers, and then returns the modified model.
    """
    model = vgg16(weights=VGG16_Weights.IMAGENET1K_V1)
    model.avgpool = nn.Identity()
    model.classifier = nn.Identity()
    return model


def clf():
    """
    Load the trained model from the specified file path and return it.
    """
    model = joblib.load('./src/models/model.pkl')
    return model


transform_img = v2.Compose([
    v2.ToImage(),
    v2.ToDtype(torch.float32, scale=True),
])


feature_extractor_model = feature_extractor()
classifier_model = clf()

labels = [
    'bulldog', 
    'german shepherd', 
    'golden retriever', 
    'labrador retriever', 
    'pomeranian', 
    'poodle', 
    'rottweiler', 
    'siberian husky', 
    'welsh corgi', 
    'yorkshire terrier'
]


def predict_breed(img):
    """
    Predicts the breed of a dog based on the input image.

    Parameters:
    img (numpy.ndarray): The input image of the dog.

    Returns:
    str: The predicted breed of the dog.
    """
    img = cv2.resize(img, (200, 200))
    transformed_img = transform_img(img).unsqueeze(0)
    feature_map = extract_features_for_a_batch(feature_extractor_model, transformed_img)
    feature_map = feature_map.detach().numpy()
    pred_idx = classifier_model.predict(feature_map)[0]
    breed = labels[pred_idx]
    return breed



# img = cv2.imread('./data/raw_images/train/pomeranian/BREED Hero_0095_pomeranian.jpg', cv2.IMREAD_COLOR)
# cv2.imshow('dog', img)
# cv2.waitKey(0)

# transformed_img = transform_img(img).unsqueeze(0)
# feature_map = extract_features_for_a_batch(feature_extractor_model, transformed_img)
# feature_map = feature_map.detach().numpy()
# pred_idx = classifier_model.predict(feature_map)[0]
# breed = labels[pred_idx]
# print(breed)