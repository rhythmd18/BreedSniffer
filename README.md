
# BreedSniffer

A simple FastAPI app that classifies 10 most popular dog breeds harnessing a traditional ML model viz., Support Vector Machine.

It leverages transfer learning by using a pretrained neural network architecture (VGG16) to extract features from the uploaded dog image. These features are then used as an input to a traditional ML model to hopefully classify the correct breed. 

The optimal model is chosen through hyperparameter tuning using `GridSearchCV`.

Data was collected from Google Images using a [batch downloader](https://chromewebstore.google.com/detail/fatkun-batch-download-ima/efcapamiilmdfbbilogcddbdckjhpajj) extension.


## Demo




## Files description

- **Main application files**
    - `main.py`: This is the file that runs the FastAPI application. It sets up the server and routes for the API, and serves the hybrid model (the CNN and the ML model combined).
    - `src/utils.py`: It has all the necessary functions for preprocessing the image data, loading the models, and so on, that are served by the API route.
    - `src/dogbreedclassifier.ipynb`: Notebook file that contain the model training scripts.
    - `static/index.js`: A JavaScript file that contains scripts to interact with the API route. It sends the image to the API and receives response in JSON format, which is then used to update the DOM.

- **Data preprocessing files**
    - `data/data_preprocessing.py`: This file contains the entire data preprocessing pipeline that loads the raw images and performs the necessary processing on them into suitable format for model training and validation. The steps include:
        - *Extracting labels from the image folders (Named after the dog breeds).*
        - *Resizing the images and reshaping them.*
        - *Augmenting the images (Flipping the images horizontally).*
        - *Separating image files into separate training and testing folders.*
    - `data/utils.py`: It contains the necessary functions that performs the processing of the images which are used by the `data_preprocessing.py` file.
    - `clean_data.py`: This cleans up the data by deleting additional unnecessary files from the image folders that crept in while downloading the images.
## Tech Stack

**Client:** HTML, CSS, JavaScript

**Server:** FastAPI

**Pretrained CNN Model**: PyTorch

**ML Models and Hyperparameter-Tuning**: scikit-learn


## Acknowledgements

 - [FatKun Batch Image Downloader](https://chromewebstore.google.com/detail/fatkun-batch-download-ima/efcapamiilmdfbbilogcddbdckjhpajj)
 - [DigitalSreeni](https://www.youtube.com/@DigitalSreeni) for this [video](https://www.youtube.com/watch?v=IuoEiemAuIY)


