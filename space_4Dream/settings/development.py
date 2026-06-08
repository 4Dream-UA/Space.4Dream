import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Добавил 0.0.0.0, чтобы Docker мог пробрасывать порты наружу
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost,0.0.0.0").split(",")

# Database
# Переключаем на PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'space_4dream'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
IS_LOCAL = os.getenv("IS_LOCAL", "False") == "True"