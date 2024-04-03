FROM ubuntu:latest

WORKDIR /app

COPY requirements.txt /app
COPY . /app

RUN apt-get update && \ 
    apt-get install -y python3-pip && \ 
    pip install -r requirements.txt


CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]