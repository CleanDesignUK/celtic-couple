from .base import *
import dj_database_url

DEBUG = False

# Replace with your actual secret key
SECRET_KEY = 'q*d)3!g-59j1k118-b177mx4p1gdd152r2%#2f#3ss'

# Allowed hosts
ALLOWED_HOSTS = ['celticcouple.com', 'celticcouple.uk', 'celtic-blog-10cb8fe7bf21.herokuapp.com']

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'qYkwbmDnqJeRkvAgXwyvCMCWOVdgijkO',
        'HOST': 'roundhouse.proxy.rlwy.net',
        'PORT': '5432',
    }
}

# SSL and security settings
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Logging for production
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'root': {'handlers': ['console'], 'level': 'INFO'},
}
