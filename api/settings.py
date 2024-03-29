"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "*", "0.0.0.0:1337"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_beat",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "spanglish",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "api.wsgi.application"
REST_FRAMEWORK = {
    # 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_VERSION": "v1",
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    "ALLOWED_VERSIONS": [
        "v1",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": (
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticated',
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Fedal API",
    "DESCRIPTION": "API documentation for our app",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "COMPONENT_SPLIT_REQUEST": False,
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "Spanglish"),
        "USER": os.environ.get("POSTGRES_USER", ""),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
        "HOST": os.environ.get("POSTGRES_HOST", ""),
        "PORT": os.environ.get("POSTGRES_PORT", ""),
    }
}

# CELERY SETTINGS


# set the celery broker url
CELERY_BROKER_URL = "sqs://" if os.environ.get("ENVIRONMENT", "DEV") == "PRO" else "redis://redis:6379/0"

# set the celery result backend
CELERY_RESULT_BACKEND = "redis://redis:6379/0"

# set the celery timezone
CELERY_TIMEZONE = "UTC"

# CELERY_BROKER_TRANSPORT_OPTIONS = {
#     "region": "eu-west-1",
#     "queue_name_prefix": "c3po-celery-",
#     "visibility_timeout": 3600,
# }
# CELERY_TASK_DEFAULT_QUEUE = "default"


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Logging
LOGGING = {
    "disable_existing_loggers": False,
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
        },
    },
    "formatters": {
        "simple": {
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "format": "%(asctime)-s [%(name)s] [%(levelname)s]: %(message)s",
        },
        "verbose": {
            "format": "%(asctime)-s [%(name)s] [%(levelname)s]: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "loggers": {
        "": {"handlers": ["console"], "level": "WARNING", "propagate": True},
        "api": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
        "django.request": {
            "handlers": ["console"],
            "propagate": True,
            "level": "ERROR",
        },
        "spanglish": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
        # Print queries to console
        # "django.db.backends": {
        #     "level": "DEBUG",
        #     "handlers": ["console"],
        # },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC
# ------------------------------------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_ROOT = os.path.join(BASE_DIR, "media-files")  # on beta doesn't have access rights
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates/")

# FILE STORAGE
# ------------------------------------------------------------------------------
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# Account templates
LOGIN_REDIRECT_URL = "/admin/"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
APPEND_SLASH = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# JWT SETTINGS
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# CSRF SETTINGS
ALLOWED_ORIGINS = ["http://*", "https://*", "http://localhost:1337", "http://0.0.0.0:1337", "http://0.0.0.0:8000", "http://0.0.0.0:80"]
CSRF_TRUSTED_ORIGINS = ALLOWED_ORIGINS.copy()
CSRF_COOKIE_SECURE = True
