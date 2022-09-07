from .base import *

from dotenv import dotenv_values

config = dotenv_values(".env")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config["DB_NAME"],
        "USER": config["DB_USER"],
        "PASSWORD": config["DB_PASSWORD"],
        "HOST": config["DB_HOST"],
        "PORT": config["DB_PORT"],
        "CONN_MAX_AGE": 600,
    }
}
