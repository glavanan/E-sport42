import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = TEMPLATE_DEBUG = True

ADMINS = (("Camille", "camwag.w@gmail.com"), ("Guillian", "guillian.lavanant@gmail.com"))

AUTH_USER_MODEL = 'base.MyUser'
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'django_countries',
    'base',
    'post',
    'tournoi',
    'djangular',
    'rest_framework',
    'jsonify',
    'djrill'
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    )
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'esport42.urls'

WSGI_APPLICATION = 'esport42.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DB = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'testing'
}

DATABASES = {
    'default': DB
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Logs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/webapps/esport42/site/debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'tournoi' : {
            'handlers' : ['file'],
            'level' : 'DEBUG',
        },
                'base' : {
            'handlers' : ['file'],
            'level' : 'DEBUG',
        },
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


FRONT_POST = 'static/post/img'

MEDIA_URL = '/'

STATIC_URL = '/static/'

from local_settings import *

