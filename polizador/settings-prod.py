"""
Django settings for polizador project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from .settings import * 

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get("SECRET")
with open("/var/www/Polizador-v3.0/polizador/SECRET.TXT") as f:
	SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["willylobo.net.ar"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
with open("/var/www/Polizador-v3.0/polizador/DBSECRET.TXT") as s:
        DBSECRET = s.read().strip()
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
            "HOST": "127.0.0.1",
            "USER": "willy",
	    "PASSWORD":DBSECRET,
            "NAME":"polizadordb",
    }
}