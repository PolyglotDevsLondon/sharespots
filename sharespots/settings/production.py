from .base import *

# access heroku environment environment-variable (config variable) of the secret key
SECRET_KEY = get_env('SECRET_KEY')
ALLOWED_HOSTS = get_list('ALLOWED_HOSTS', separator=',')
