FROM python:3.11-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ./entrypoint.sh