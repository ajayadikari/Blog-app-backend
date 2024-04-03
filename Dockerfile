# Base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Expose the port the Flask application will be listening on
EXPOSE 8000

# Set environment variables, if necessary
# ENV MY_ENV_VAR=value

# Run the Flask application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]