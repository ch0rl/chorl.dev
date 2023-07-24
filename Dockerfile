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
RUN systemctl enable --now nginx

# Gunicorn/Django
ENV VIRTUAL_ENV=/workspace/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV DJANGO_KEY=${DJANGO_KEY}
ENV DJANGO_DB_USER=${DJANGO_DB_USER}
ENV DJANGO_DB_PASS=${DJANGO_DB_PASS}
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

CMD gunicorn --bind localhost:8001 src.wsgi --access-logfile '-'
