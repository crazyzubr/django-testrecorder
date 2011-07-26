# Django settings for development project.
import os, sys

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

sys.path.insert(0, rel('..', '..'))

FIXTURE_DIRS = (
    rel('fixtures'),
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': rel('database.sqlite'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = rel('static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$g^_w#9*(an#-gn@l-em@)upegpzqg-u9!!ukhn%c8tuz5=#)u'

LOGIN_URL = '/login/'

# List of callables that know how to import templates from various sources.
if DEBUG:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )    
else:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'testrecorder.middleware.TestRecorderMiddleware', 
    'django.middleware.common.CommonMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'django.middleware.locale.LocaleMiddleware', 
    'django.middleware.csrf.CsrfViewMiddleware', 
    'django.contrib.auth.middleware.AuthenticationMiddleware', 
    'testrecorder.middleware.AutoLoginMiddleware'
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    rel('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'main',
    'testrecorder'
)

############
# RECORDER #
############

RECORDER_FIXTURES = [
    'test1.json', 
    'test2.json', 
    'test3.json',
    'test4.json'
]

RECORDER_INIT_ON_START = False
RECORDER_AUTO_START = True

RECORDER_IGNORE = (
    '^/favicon.ico',
)

RECORDER_TEST_EMAIL_SENDING = True

try:
    from settings_local import *
except ImportError:
    pass