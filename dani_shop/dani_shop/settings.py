"""
Django settings for dani_shop project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ncdnrq4noti$!)3g3)@qqx)6v1qmaz272_)r-58z6k$-yb3iy4'

import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1', '.ngrok.io']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # OAUTH2
    'rest_framework',
    'oauth2_provider',
    'drf_yasg',
    # Celery
    'django_celery_results',
    'django_celery_beat',
    # APPs
    'dani_shop',
    'register_bot',
    'assistance_bot',
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

ROOT_URLCONF = 'dani_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'dani_shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        'rest_framework.permissions.DjangoModelPermissions'
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),

    'DEFAULT_RENDERER_CLASSES': (
        # UnicodeJSONRenderer has an ensure_ascii = False attribute, thus it will not escape characters.
        'rest_framework.renderers.JSONRenderer',
        # You only need to keep this one if you're using the browsable API
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    'PAGINATE_BY': 10,
    'PAGINATE_BY_PARAM': 'page_size'
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

EMAIL_TO_ASSISTANCE = ''

TELEGRAM_TOKEN = ''
TELEGRAM_CHAT_ID = ''
TELEGRAM_URL = "https://api.telegram.org/bot"

# Celery settings
CELERY_BROKER_URL = 'redis://%s:6379/0' % (os.environ.get('REDIS_SERVER', 'localhost'))
BROKER_URL = 'redis://%s:6379/0' % (os.environ.get('REDIS_SERVER', 'localhost'))
CELERY_RESULT_BACKEND = 'database'
CELERY_DEFAULT_QUEUE = 'dani_shop'
CELERY_TASK_DEFAULT_QUEUE = 'dani_shop'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'

from kombu import Queue
CELERY_QUEUE = CELERY_DEFAULT_QUEUE
CELERY_QUEUES = (Queue(CELERY_DEFAULT_QUEUE),)

from datetime import timedelta
CELERYBEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERYD_TASK_SOFT_TIME_LIMIT = timedelta(hours=16).seconds
CELERY_REDIRECT_STDOUTS_LEVEL = 'DEBUG' if DEBUG else 'INFO'
CELERY_TASK_RESULT_EXPIRES = timedelta(hours=16)
CELERY_TRACK_STARTED = True
CELERY_CONCURRENCY = 1
CELERYD_MAX_TASKS_PER_CHILD = 1

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'static'))

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Local settings
try:
    from .local_settings import *
except:
    pass
