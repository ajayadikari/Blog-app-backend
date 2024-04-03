# Use a lightweight base image
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/

# Install system dependencies
RUN apt-get update && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Expose the port the Django application will be listening on
EXPOSE 8000

# Set environment variables, if necessary
# ENV MY_ENV_VAR=value
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
