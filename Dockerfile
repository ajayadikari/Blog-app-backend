# Use a lightweight base image
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /app

# Install pip
RUN apt-get update && \
    apt-get install -y python3-pip

# Copy the requirements file and install dependencies
COPY requirements.txt /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir --upgrade pip setuptools && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Expose the port the Django application will be listening on
EXPOSE 8000

# Set environment variables, if necessary
# ENV MY_ENV_VAR=value
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
