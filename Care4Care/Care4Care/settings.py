"""
Django settings for Care4Care project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import django.conf.global_settings as DEFAULT_SETTINGS
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from django.utils.translation import gettext_lazy as _

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x9lbrg+bw^=0&@grs2em_^s9!kq(_0ogkbhae-@1-rk2n96m_@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# This id is used to store information in case of simulation by using session variables
SESSION_ID_SIMU = '2b1189a188b44ad18c35e113ac6ceead'

# Session backend
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters',
    'localflavor',
    'C4CApplication'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware', 
)

ROOT_URLCONF = 'Care4Care.urls'

WSGI_APPLICATION = 'Care4Care.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'OPTIONS' : { "init_command": "SET foreign_key_checks = 0;" },  #Je sais pas a quoi ca sert, mais ca fait tout bugge
        'USER': 'root',
        'PASSWORD': 'MOTDEPASSE',
        #'HOST': '127.0.0.1',
        #'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#setting de l'internationalisation
SITE_ID = 1
USE_I18N = True
USE_L10N = True
DEF_ULT_LANGUAGE = 1
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale')
)
LANGUAGES =(
    ('fr' , ('French')),
    ('en', ('English')),
)


MEDIA_URL  = '/data/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'C4CApplication/data/')
MEDIAFILES_DIRS = (
    os.path.join(BASE_DIR, 'C4CApplication/data/')
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = '/var/www/care4care.be/static/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'C4CApplication/static'),
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'C4CApplication/templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
'django.core.context_processors.i18n',
)
