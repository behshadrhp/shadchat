import os

from .common import *

import dj_database_url

from dotenv import load_dotenv

# Loading environment variable"s
load_dotenv()

# Django secret key
SECRET_KEY = os.environ.get("SECRET_KEY")

# Enable sever mode
DEBUG = False

if not DEBUG:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
        "rest_framework.renderers.JSONRenderer",
    )


# Allowed run server in this host
FIRST_HOST = os.environ.get("FIRST_HOST")
SECOND_HOST = os.environ.get("SECOND_HOST")

ALLOWED_HOSTS = ["127.0.0.1", FIRST_HOST, SECOND_HOST]

# Final database
DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL")),
}

# Configure Cache system
CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 604800 # 7 Days
CACHE_MIDDLEWARE_KEY_PREFIX = ""

# CSRF Attack
SESSION_COOKIE_SECURE = True

# XSS Attack
SECURE_BROWSER_XSS_FILTER = True
SECURE_COUNT_TYPE_NOSNIFF = True

# CORS Origin Header settings configuration
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOWED_ORIGINS = [
#     "https://example.com",
# ]
