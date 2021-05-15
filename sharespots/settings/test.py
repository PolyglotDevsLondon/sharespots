from .base import *
from env_utils import get_env
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h)wmbja@&kvo3#0yyv@piqcp6*(xs=r5!2grbiej8y2!issrn@'

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': get_env('POSTGRES_HOST'),
        'NAME': get_env('POSTGRES_DB'),
        'USER': get_env('POSTGRES_USER'),
        'PASSWORD': get_env('POSTGRES_PASSWORD'),
    }
}

AWS_SECRET_ACCESS_KEY="foobar"
AWS_ACCESS_KEY_ID="foobar"
AWS_STORAGE_BUCKET_NAME="foobar"