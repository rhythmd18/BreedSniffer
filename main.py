from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'breed': 'german shepherd'})
