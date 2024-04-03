# Base image
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --no-cache-dir --upgrade pip setuptools && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port the Flask application will be listening on
EXPOSE 8000

# Set environment variables, if necessary
# ENV MY_ENV_VAR=value

# Run the Flask application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
