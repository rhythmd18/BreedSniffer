from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import base64
import numpy as np
import cv2

from src.utils import predict_breed

app = FastAPI()

templates = Jinja2Templates(directory='templates')

# mount static files
app.mount("/static", StaticFiles(directory="static"), name="static") 

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/predict')
async def predict(request: Request):
    data = await request.json()
    img_data = data['image']
    img_data = base64.b64decode(img_data.split(',')[1])
    nparr = np.frombuffer(img_data, np.uint8)
    img = cv2.imread(nparr, cv2.IMREAD_COLOR)
    breed = predict_breed(img)
    return ({
        'status': 'success',
        'breed': breed
    })
