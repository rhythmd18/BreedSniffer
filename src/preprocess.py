import torch

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