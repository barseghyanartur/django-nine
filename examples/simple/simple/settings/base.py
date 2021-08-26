"""
Django settings for simple project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

from django_nine import versions

from .core import PROJECT_DIR, gettext

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

try:
    from .local_settings import DEBUG_TEMPLATE
except Exception as err:
    DEBUG_TEMPLATE = False

try:
    from .local_settings import USE_CACHED_TEMPLATE_LOADERS
except Exception as err:
    USE_CACHED_TEMPLATE_LOADERS = False

if USE_CACHED_TEMPLATE_LOADERS:

    _TEMPLATE_LOADERS = [
        (
            "django.template.loaders.cached.Loader",
            (
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ),
        ),
    ]
else:

    _TEMPLATE_LOADERS = [
        "django.template.loaders.filesystem.Loader",
        "django.template.loaders.app_directories.Loader",
    ]

if versions.DJANGO_GTE_1_10:
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            # 'APP_DIRS': True,
            "DIRS": [PROJECT_DIR(os.path.join("..", "templates"))],
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "django_nine.context_processors.versions",
                ],
                "loaders": _TEMPLATE_LOADERS,
                "debug": DEBUG_TEMPLATE,
            },
        },
    ]
elif versions.DJANGO_GTE_1_8:
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            # 'APP_DIRS': True,
            "DIRS": [PROJECT_DIR(os.path.join("..", "templates"))],
            "OPTIONS": {
                "context_processors": [
                    "django.contrib.auth.context_processors.auth",
                    "django.template.context_processors.debug",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "django.template.context_processors.tz",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.request",
                    "django_nine.context_processors.versions",
                ],
                "loaders": _TEMPLATE_LOADERS,
                "debug": DEBUG_TEMPLATE,
            },
        },
    ]
else:
    TEMPLATE_DEBUG = DEBUG_TEMPLATE

    # List of callables that know how to import templates from various
    # sources.
    TEMPLATE_LOADERS = _TEMPLATE_LOADERS

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request",
        "django_nine.context_processors.versions",
    )

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or
        # "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        PROJECT_DIR(os.path.join("..", "templates")),
    )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "uzc&9xi6b#dz^z7tpa+br3ohq)-9%v9ux@9^t!(5fl41n%&mn$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEV = False

ALLOWED_HOSTS = [
    "*",
]

# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "urls"

WSGI_APPLICATION = "simple.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = "/static/"

# Do not put any settings below this line
try:
    from .local_settings import *
except Exception as err:
    pass

# Make the `django-nine` package available without installation.
if DEV:
    nine_source_path = os.environ.get("NINE_SOURCE_PATH", "src")
    # sys.path.insert(0, os.path.abspath('src'))
    sys.path.insert(0, os.path.abspath(nine_source_path))
