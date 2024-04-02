FROM ubuntu:latest

# Set working directory
WORKDIR /app

COPY . /app/

RUN apt-get update && \ 
    apt-get install -y python3-pip && \ 
    pip install --no-cache-dir -r requirements.txt && \
    pip install django

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
