from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# access heroku environment environment-variable (config variable) of the secret key
SECRET_KEY = get_env['SECRET_KEY']
ALLOWED_HOSTS = ['https://sharespots.herokuapp.com/', 'https://sharespots.co.uk']
