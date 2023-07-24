# Python version
FROM python:3.10

# Set dir
WORKDIR /workspace

# Testing
RUN ls -la

# Install deps
RUN pip install -r requirements.txt

# Expose HTTP port
EXPOSE 8000

# Config
COPY chorl.dev.conf /etc/nginx/conf.d/chorl.dev.conf
RUN python manage.py collectstatic
RUN python manage.py migrate

# Run
CMD gunicorn 'src/wsgi:app'
