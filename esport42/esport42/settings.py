import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = TEMPLATE_DEBUG = False

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
    'django_countries',
    'base',
    'post',
    'tournoi',
    'djangular',
    'rest_framework',
    'jsonify'
)

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
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'esport42_debug',
	'USER': 'esport42',
	'PASSWORD': os.getenv("DB_PASS")
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


FRONT_POST = 'static/img/post/'

MEDIA_URL = '/'

STATIC_URL = '/static/'

from local_settings import *
