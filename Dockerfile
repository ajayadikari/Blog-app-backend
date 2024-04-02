FROM python:3.8

# Set working directory
WORKDIR /app

# Copy project files and install dependencies
COPY . .

# Install Python, pip, and Django dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir -r requirements.txt && \
    pip3 install --no-cache-dir django

# Expose port
EXPOSE 8000

# Set environment variables (optional)
# ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Command to run the application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
