FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip cache purge
RUN pip install -r requirements.txt
RUN pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]