FROM python:3.11-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN export FLASK_APP=app.py
RUN export FLASK_DEV=develop

CMD flask run -h 0.0.0.0 -p 80
