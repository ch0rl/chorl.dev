# https://github.com/koyeb/example-django/blob/main/Dockerfile
# Build first
FROM python:3.10 AS builder

WORKDIR /workspace

RUN python3 -m venv venv
ENV VIRTUAL_ENV=/workspace/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

# Stage 2
FROM python:3.10 AS runner

# Nginx
RUN apt update && apt install -y systemctl nginx
COPY site.conf /etc/nginx/conf.d/site.conf
RUN nginx -t

# Gunicorn/Django
ENV VIRTUAL_ENV=/workspace/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /workspace

COPY --from=builder /workspace/venv venv
COPY src src
COPY static static
COPY manage.py manage.py

# Config
RUN python manage.py collectstatic --noinput
RUN DB_PASS=${DB_PASS} DB_HOST=${DB_HOST} DB_NAME=${DB_NAME} DB_USER=${DB_USER} PROD=1 DJANGO_KEY=${DJANGO_KEY} python manage.py migrate --noinput

EXPOSE 8000

CMD DB_PASS=${DB_PASS} DB_HOST=${DB_HOST} DB_NAME=${DB_NAME} DB_USER=${DB_USER} PROD=1 DJANGO_KEY=${DJANGO_KEY} nginx & gunicorn --bind localhost:8001 src.wsgi --access-logfile '-'
