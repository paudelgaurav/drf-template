"""
With these settings, tests run faster.
"""

import multiprocessing

from dotenv import dotenv_values

from .base import *  # noqa

config = dotenv_values(".env")

"""
The current implementation of the parallel test runner requires
multiprocessing to start subprocesses with fork() which is default for linux 
but macOS and windows uses spawn().
https://github.com/django/django/blob/stable/3.2.x/django/test/runner.py#L298

These things are handled in newer version of Django(4.1) which supports both spawn and fork.
https://github.com/django/django/blob/stable/4.1.x/django/test/runner.py#L365

"""
multiprocessing.set_start_method("fork")


# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"


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


DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
