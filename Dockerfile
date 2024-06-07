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

ENV DJANGO_KEY=${DJANGO_KEY}
ENV DB_PASS=${DB_PASS}
ENV DB_HOST=${DB_HOST}
ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV PROD=true

WORKDIR /workspace

COPY --from=builder /workspace/venv venv
COPY src src
COPY static static
COPY manage.py manage.py

# Config
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput

EXPOSE 8000

CMD nginx & gunicorn --bind localhost:8001 src.wsgi --access-logfile '-'
