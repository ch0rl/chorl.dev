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
RUN apt update && apt install -y systemctl nginx sqlite3
RUN apt install -y postgresql postgresql-contrib libpq-dev python3-dev
COPY site.conf /etc/nginx/conf.d/site.conf
RUN nginx -t

# Gunicorn/Django
ENV VIRTUAL_ENV=/workspace/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PROD=1

ARG DB_HOST
ARG DB_USER
ARG DB_NAME
ARG DB_PASS

WORKDIR /workspace

COPY --from=builder /workspace/venv venv
COPY main main
COPY opriq opriq
COPY static static
COPY projects projects
COPY articles articles
COPY manage.py manage.py
COPY forward_logs.py forward_logs.py

# Config
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput

EXPOSE 8000

CMD nginx & python forward_logs.py & gunicorn --bind localhost:8001 main.wsgi
