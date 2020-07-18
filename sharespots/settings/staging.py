from .base import *


SECRET_KEY = get_env('SECRET_KEY')
ALLOWED_HOSTS = ['*']

# Activate Django-Heroku.
django_heroku.settings(locals(), logging=True, allowed_hosts=False, databases=not DEBUG)
