from .base import *
import os
import dj_database_url

# Whether Django is in debug mode
# For production, generally set this to False
DEBUG = True

# Secret key for production
SECRET_KEY = 'q*d)3!g-59j1k118-b177mx4p1gdd152r2%#2f#3ss'

# Allowed hosts for the application
ALLOWED_HOSTS = [
    'celticcouple.com',
    'celticcouple.uk',
    'celtic-blog-10cb8fe7bf21.herokuapp.com',
    'glorious-space-guacamole-wrjj47wp97q35wp-8000.app.github.dev',
    'localhost',
]

CSRF_TRUST_ORIGINS = [
    'https://celtic-blog-10cb8fe7bf21.herokuapp.com',
    'https://celticcouple.com',
    'https://celticcouple.uk',
    'https://glorious-space-guacamole-wrjj47wp97q35wp-8000.app.github.dev',
    'http://localhost:8000'   # Add any other domains you might use
]


# Database configuration (using your Railway Postgres credentials)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',     # Database name
        'USER': 'postgres',    # DB username
        'PASSWORD': 'eYsPHtJnUbPGbyMrjYFkcmuOdRIJutxQ',  # <-- Actual password from your logs
        'HOST': 'monorail.proxy.rlwy.net',              # Host from your logs
        'PORT': '30364',                                # Port from your logs
    }
}

# Wagtail admin base URL

WAGTAILADMIN_BASE_URL = 'https://celtic-blog-10cb8fe7bf21.herokuapp.com'
# SSL and security settings


# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'root': {'handlers': ['console'], 'level': 'INFO'},
}

# Disable collectstatic during deployment (Heroku-like behavior)
DISABLE_COLLECTSTATIC = True
