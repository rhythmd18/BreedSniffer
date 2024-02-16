import torch.nn as nn
from torchvision.models import vgg16, VGG16_Weights
import joblib

def feature_extractor():
    model = vgg16(weights=VGG16_Weights.IMAGENET1K_V1)
    model.avgpool = nn.Identity()
    model.classifier = nn.Identity()
    return model


def clf():
    model = joblib.load('./src/models/model.pkl')
    return model