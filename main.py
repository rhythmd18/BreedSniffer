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
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/predict/')
async def predict(file: UploadFile = File(...)):
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
    
