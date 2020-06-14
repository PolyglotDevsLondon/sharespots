from .base import *


SECRET_KEY = get_env('SECRET_KEY')
ALLOWED_HOSTS = get_list('ALLOWED_HOSTS', separator=',')
