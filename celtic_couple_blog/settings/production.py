"""
production.py

Production settings for your Django/Wagtail project,
using the new Railway Postgres credentials (public domain).
"""
from .base import *
import os
import dj_database_url

# Whether Django is in debug mode
DEBUG = True  # Generally set this to False in real production

# Secret key for production
SECRET_KEY = 'q*d)3!g-59j1k118-b177mx4p1gdd152r2%#2f#3ss'

# Allowed hosts for the application
ALLOWED_HOSTS = [
    'thecelticcouple.com',
    'www.thecelticcouple.com',
    'www.thecelticcouple.uk',
    'thecelticcouple.uk',
    'celtic-blog-10cb8fe7bf21.herokuapp.com',
    'glorious-space-guacamole-wrjj47wp97q35wp-8000.app.github.dev',
    'localhost',
]

# CSRF trusted origins
CSRF_TRUST_ORIGINS = [
    'https://celtic-blog-10cb8fe7bf21.herokuapp.com',
    'https://thecelticcouple.com',
    'https://www.thecelticcouple.com',
    'https://www.thecelticcouple.uk',
    'https://thecelticcouple.uk',
    'https://glorious-space-guacamole-wrjj47wp97q35wp-8000.app.github.dev',
    'http://localhost:8000',
]

# ------------------------------------------------------------------------------
# Hardcoded Database Configuration (Railway public domain)
# ------------------------------------------------------------------------------
DATABASES = {
    'default': dj_database_url.config(
        default=(
            'postgresql://postgres:EtkHwIDBYruQuggELJfOOgTOtufRqYEC'
            '@monorail.proxy.rlwy.net:53345/railway'
        ),
        conn_max_age=600,
        # If your DB does not strictly require SSL, set to False
        ssl_require=True
    )
}

# Wagtail admin base URL
WAGTAILADMIN_BASE_URL = 'https://celtic-blog-10cb8fe7bf21.herokuapp.com'

# ------------------------------------------------------------------------------
# Logging configuration
# ------------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'root': {'handlers': ['console'], 'level': 'INFO'},
}

# ------------------------------------------------------------------------------
# Disable collectstatic during deployment (Heroku-like behavior)
# ------------------------------------------------------------------------------
DISABLE_COLLECTSTATIC = True
