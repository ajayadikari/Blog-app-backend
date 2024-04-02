FROM python:latest

# Set working directory
WORKDIR /app

# Copy project files and install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Install Python, pip, and Django dependencies
RUN apt-get update

# Expose port
EXPOSE 8000

# Set environment variables (optional)
# ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Command to run the application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
