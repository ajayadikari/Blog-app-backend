FROM ubuntu:latest

# Set working directory
WORKDIR /app

# Copy requirements and project files
COPY requirements.txt /app/
COPY base /app/

# Install Python and Django dependencies
RUN apt-get update && \ 
    apt-get install -y python3-pip && \ 
    pip install --no-cache-dir -r requirements.txt && \
    pip install django


# Expose port
EXPOSE 8000

# Set environment variables (optional)
# ENV DJANGO_SETTINGS_MODULE=myproject.settings
# Command to run the application
CMD ["python3", "base/manage.py", "runserver", "0.0.0.0:8000"]