# Python version
FROM python:3.10

# Set dir
WORKDIR /workspace

# Testing
RUN ls -la

# Install deps
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy files
COPY src src

# Expose HTTP port
EXPOSE 8000

# Config
RUN python manage.py collectstatic
RUN python manage.py migrate

# Run
CMD gunicorn --bind :${PORT} src.wsgi
