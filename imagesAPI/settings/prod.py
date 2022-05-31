from imagesAPI.settings.base import *
import os

DEBUG = False

ALLOWED_HOSTS = [
    "herokuapp.com",
    "images-api-hex.herokuapp.com",
    "127.0.0.1"
    ]

SECRET_KEY = os.environ.get("PROD_SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PROD_DB_NAME"),
        "USER": os.environ.get("PROD_DB_USER"),
        "PASSWORD": os.environ.get("PROD_DB_PS"),
        "HOST": os.environ.get("PROD_DB_HOST"),
        "PORT": "5432",
    }
}


AWS_ACCESS_KEY_ID = os.environ.get("CS_S3_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("CS_S3_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("CS_S3_BUCKET_NAME")

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_QUERYSTRING_AUTH = False

AWS_S3_HOST = "s3.eu-central-1.amazonaws.com"
AWS_S3_REGION_NAME = "eu-central-1"

CSRF_TRUSTED_ORIGINS = ['https://images-api-hex.herokuapp.com']