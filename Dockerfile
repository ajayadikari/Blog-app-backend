FROM ubuntu:latest

# Update package lists and install Python 3 and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app

# Set the default command to run your application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
