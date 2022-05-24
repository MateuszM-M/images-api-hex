from imagesAPI.settings.base import *
import os

DEBUG = True

ALLOWED_HOSTS = [
    "herokuapp.com", 
    "127.0.0.1"
    ]

SECRET_KEY = 'django-insecure-(vkqbnopay#_2grm8z_+lr5&qls3nwd94qyvb_9*ti+2w$g=%^'


DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql',
        "NAME": 'postgres',
        "USER": 'postgres',
        "PASSWORD": 'postgres',
        "HOST": 'db',
        "PORT": "5432"
    }
}