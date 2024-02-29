from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import numpy as np
import cv2
from src.utils import predict_breed

app = FastAPI()


templates = Jinja2Templates(directory='templates')

# mount static files
app.mount("/static", StaticFiles(directory="static"), name="static") 

@app.get('/')
async def home(request: Request):
    """
    Asynchronous function that handles the home endpoint. It takes a request of type Request as a parameter and returns a TemplateResponse.
    """
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/predict/')
async def predict(file: UploadFile = File(...)):
    """
    Asynchronous function that accepts an uploaded file and processes it to predict the breed of the image. 
    It returns a JSON response with the status and the predicted breed if successful, or a JSON response with the status and error message if an exception occurs.
    """
    img_data = await file.read()
    nparr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    try:
        breed = predict_breed(img)
        return JSONResponse(content={
            'status': 'Success',
            'breed': breed
        })
    except Exception as e:
        return JSONResponse(content={
            'status': 'Failed',
            'error': str(e)
        })
    
