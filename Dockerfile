FROM python:latest

COPY ./app /app
COPY ./req.txt .

RUN apt-get update && apt-get upgrade -y
RUN apt install libpq-dev build-essential -y
RUN pip install -r req.txt

WORKDIR /app

EXPOSE 8000

