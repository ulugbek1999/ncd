from settings.settings import INSTALLED_APPS, MIDDLEWARE, BASE_DIR

DEBUG = False

ALLOWED_HOSTS = ['test.uzncd.com', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ncd',
        'USER': 'ulugbek',
        'PASSWORD': '12345'
    }
}

import raven
# raven
INSTALLED_APPS.append('raven.contrib.django.raven_compat')
MIDDLEWARE.append('raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware')
MIDDLEWARE.append('raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware')
RAVEN_CONFIG = {
    'dsn': 'https://7924c5d8297f4bbeb5f1987dcbc012db:33f3e6bcb238448c89f5db30bd6f2f83@sentry.io/1398468',
    'release': raven.fetch_git_sha(BASE_DIR),
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s  %(asctime)s  %(module)s '
                      '%(process)d  %(thread)d  %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',  # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
