"""
Django settings for site project.

Generated by 'django-admin startproject' using Django 4.2.1.
"""

# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ~~~ Secrets
SECRET_KEY = os.environ.get("DJANGO_KEY")
DB_USER = os.environ.get("DJANGO_DB_USER")
DB_PASSWORD = os.environ.get("DJANGO_DB_PASS")

if SECRET_KEY is None or DB_USER is None or DB_PASSWORD is None:
    raise ValueError("Environment lacking one of: DJANGO_KEY, DJANGO_DB_USER, DJANGO_DB_PASS")

PROD = os.environ.get("PROD", False)
DEBUG = not PROD

# ~~~ Localhost and all subdomains
ALLOWED_HOSTS = [
    # "*",
    "localhost",
    "127.0.0.1",
    "chorl.dev",
    ".chorl.dev"
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'src/pages'    
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'

# ~~~ Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ~~~ Internationalization
LANGUAGE_CODE = 'en-uk'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ~~~ Static files
if PROD:
    STATIC_URL = '/static/'
    STATIC_ROOT = "/var/www/chorl.dev/static/"
    
    STATICFILES_DIRS = [
       BASE_DIR / "static"
    ]
else:
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ~~~ Mail
if PROD:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    SERVER_EMAIL = "django.root@chorl.dev"
    DEFAULT_FROM_EMAIL = "django.default@chorl.dev"
    EMAIL_HOST = "chorl.dev"

    ADMINS = [("Autumn", "django.admin@chorl.dev")]

# ~~~ Static/Media
if PROD:
    MEDIA_ROOT = "/var/www/chorl.dev/media/"
    MEDIA_URL = "media/"

if PROD:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
            "LOCATION": "/var/tmp/django_cache",
        }
    }
