# Python version
FROM python:3.10

# Install deps
RUN pip install -r requirements.txt

# Expose HTTP port
EXPOSE 8000

# Start server
CMD python manage.py runserver
