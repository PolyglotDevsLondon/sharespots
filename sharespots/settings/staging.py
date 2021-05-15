from .base import *


SECRET_KEY = get_env('SECRET_KEY')
ALLOWED_HOSTS = ['*']

# Activate Django-Heroku.
django_heroku.settings(locals(), logging=True, allowed_hosts=False, databases=not DEBUG)

###############
# Storages S3 #
###############
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = get_env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
