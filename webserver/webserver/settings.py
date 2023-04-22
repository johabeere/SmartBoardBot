"""
Django settings for webserver project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LIVE = True
FAKEGCODE = False
TABLE_HEIGHT = 915
TABLE_WIDTH = 1300

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eq1yz_(_k5wefh_x$)=qdmpn5%#gxq5ffu5^yf54_x&jusg@82'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'smartwebbot',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webserver.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = '/'

# Loggging 😀
LOGGING = {
    'version': 1,                       # the dictConfig format version
    'disable_existing_loggers': False,  # retain the default loggers
    'formatters': {
       'verbose': {
           'format': '{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}',
           'style': '{',
       },
       'kindaverbose': {
           'format': '{asctime} {levelname} {module} {message}',
           'style': '{',
       },
       'simple': {
           'format': '{levelname} {message}',
           'style': '{',
       },
   },
   'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'kindaverbose',
        },
    },
    'loggers': {
       # notice the blank '', Usually you would put built in loggers like django or root here based on your needs
        '': {
            'handlers': ['file'], #notice how file variable is called in handler which has been defined above
            'level': 'CRITICAL',
            'propagate': True,
        },
        '': {
            'handlers': ['file'], #notice how file variable is called in handler which has been defined above
            'level': 'WARNING',
            'propagate': True,
        },
        '': {
            'handlers': ['file'], #notice how file variable is called in handler which has been defined above
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['file'], #notice how file variable is called in handler which has been defined above
            'level': 'INFO',
            'propagate': True,
        },
        '': {
            'handlers': ['file'], #notice how file variable is called in handler which has been defined above
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}