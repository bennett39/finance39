import django_heroku
import dj_database_url
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Resolve environment name
STACK_NAME = os.environ['STACK_NAME']
IS_PRODUCTION = STACK_NAME == 'production'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if IS_PRODUCTION else True
ALLOWED_HOSTS = ['.finance39.herokuapp.com'] if IS_PRODUCTION else []

### Application definition ###

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'rest_framework',
    'categories',
    'credentials',
    'transactions',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Cache
# https://docs.djangoproject.com/en/3.2/topics/cache/
# https://devcenter.heroku.com/articles/memcachier#django

prod_cache_settings = {
    'default': {
        # Use django-bmemcached
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        # TIMEOUT is not the connection timeout! It's the default expiration
        # timeout that should be applied to keys! Setting it to `None`
        # disables expiration.
        'TIMEOUT': None,
        'LOCATION': os.getenv('MEMCACHIER_SERVERS'),
        'OPTIONS': {
            'username': os.getenv('MEMCACHIER_USERNAME'),
            'password': os.getenv('MEMCACHIER_PASSWORD'),
        }
    }
}

local_cache_settings = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

CACHES = prod_cache_settings if IS_PRODUCTION else local_cache_settings


# Sessions

SESSION_COOKIE_SECURE = True if IS_PRODUCTION else False
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# https://github.com/jacobian/dj-database-url - Use DATABASE_URL from .env

DATABASES = {'default': dj_database_url.config(conn_max_age=600)}

# Auto fields

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# After login

LOGIN_REDIRECT_URL = '/api'


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Django REST Framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

OAUTH2_PROVIDER = {
    'OIDC_ENABLED': True,
    'OIDC_RSA_PRIVATE_KEY': os.environ['OIDC_RSA_PRIVATE_KEY'],
    'PKCE_REQUIRED': True,
    'SCOPES': {
        'openid': 'OpenID Connect scope',
        'read': 'Read scope',
        'write': 'Write scope',
        'groups': 'Access to your groups'
    },
}

# Set Heroku settings
if IS_PRODUCTION:
    django_heroku.settings(locals())
