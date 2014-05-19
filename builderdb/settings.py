"""
Django settings for builderdb project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qg6bsln!vh4sbb4)_(=1qnb)r41u2fvdn*5k^u%&b25j^0e@aj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Markup Field
# https://github.com/jamesturk/django-markupfield

import markdown
MARKUP_FIELD_TYPES = (
    ('markdown', markdown.markdown),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'autocomplete_light',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    'foundation',
    'crispy_forms',
    'crispy_forms_foundation',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'easy_thumbnails',
    'avatar',
    'sitetree',

    'builders',
    'accounts',
)

# Template Context Processors
# https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
    'django.core.context_processors.request',
)

# Template Directories
# https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'builderdb', 'templates'),
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

ROOT_URLCONF = 'builderdb.urls'

WSGI_APPLICATION = 'builderdb.wsgi.application'

# Crispy Forms

CRISPY_TEMPLATE_PACK = 'foundation-5'
CRISPY_FAIL_SILENTLY = not DEBUG

# Sites
# https://docs.djangoproject.com/en/dev/ref/contrib/sites/

SITE_ID = 1

# Email
# https://github.com/perenecabuto/django-sendmail-backend

EMAIL_BACKEND = 'django_sendmail_backend.backends.EmailBackend'

# Authentication

ANONYMOUS_USER_ID = -1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Easy Thumbnails
# https://github.com/SmileyChris/easy-thumbnails

THUMBNAIL_ALIASES = {
    'builders.Builder.thumb': {
        'square': {'size': (220, 220), 'crop': 'smart', 'upscale': True},
    },

    'builders.Builder.banner': {
        'large': {'size': (970, 194), 'crop': 'smart', 'upscale': True},
    },

    'builders.Photo.image': {
        'thumb': {'size': (125, 125), 'crop': 'smart', 'upscale': True},
        'thumb_portait': {'size': (150, 300), 'crop': 'smart', 'upscale': True},
    }
}

try:
    from .local_settings import *
except ImportError:
    pass

if DEBUG:
    INSTALLED_APPS = tuple(list(INSTALLED_APPS)+['debug_toolbar'])
