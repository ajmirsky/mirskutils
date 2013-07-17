import os.path
import logging
import sys

USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/New_York'

gettext = lambda s: s

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = ()
for root, dirs, files in os.walk(PROJECT_PATH):
    if 'templates' in dirs: TEMPLATE_DIRS = TEMPLATE_DIRS + (os.path.join(root, 'templates'),)

FIXTURE_DIRS = ()
for root, dirs, files in os.walk(PROJECT_PATH):
    if 'fixtures' in dirs: FIXTURE_DIRS = FIXTURE_DIRS + (os.path.join(root, 'fixtures'),)


STATICFILES_DIRS = ( )
for root, dirs, files in os.walk(PROJECT_PATH):
    if 'static' in dirs: STATICFILES_DIRS = STATICFILES_DIRS + (os.path.join(root, 'static'),)

try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(PROJECT_PATH, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            import random
            SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters  to generate your secret key!' % SECRET_FILE)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf', #necessary for csrf protection
)

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (

    'admin_tools',
    'admin_tools.theming',
    #'admin_tools.menu',
    'admin_tools.dashboard',
        
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',    
    
    'mirskutils',
    'south',
    'compressor',
    'sekizai',
        
)

EMAIL_USE_TLS=False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#ADMIN_TOOLS_MENU = 'menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'app.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'app.dashboard.CustomAppIndexDashboard'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse',
         }
     },    
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },        
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'standard',
        },        
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_PATH + "/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'MYAPP': {
            'handlers': ['console', 'logfile','mail_admins'],
            'level': 'WARNING',
        },
    }
}


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/welcome/'
LOGIN_ERROR_URL = '/error/'


try:
    from local_settings import *
except:
    print "warning local settings not defined"