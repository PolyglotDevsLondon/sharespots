import os
import dj_database_url
import django_heroku

from env_utils import (
    get_env,
    get_list,
    get_bool,
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

DEBUG = get_env('DJANGO_DEBUG', False)


############
# Security #
############

ALLOWED_HOSTS = get_list('ALLOWED_HOSTS', separator=',')

# SESSION_COOKIE_HTTPONLY = True

SESSION_COOKIE_SECURE = False

X_FRAME_OPTIONS = 'DENY'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'django_extensions',
    'django.contrib.postgres',
    'search',
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

ROOT_URLCONF = 'sharespots.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '..', 'templates')],
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

WSGI_APPLICATION = 'sharespots.wsgi.application'



############
# Database #
############

DATABASE_URL = get_env('DATABASE_URL')

DATABASES = dict(default=dj_database_url.config(default=DATABASE_URL))

DATABASES['default']['ATOMIC_REQUESTS'] = True

DATABASES['default']['CONN_MAX_AGE'] = 600

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


##########
# Static #
##########

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'dist'),
)

# Activate Django-Heroku.
django_heroku.settings(locals(), logging=True, allowed_hosts=False, databases=not DEBUG)

NOTEBOOK_ARGUMENTS = [
    '--ip', '0.0.0.0',
    #'--port', '8888',
    '--allow-root',
    '--no-browser',
]
