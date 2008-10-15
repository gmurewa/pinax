# -*- coding: utf-8 -*-
# Django settings for pinax project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'dev.db'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Eastern'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

import os.path

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "site_media")

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bk-e2zv3humar79nm=j*bwc=-ymeit(8a20whp3goq4dh71t)s'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#    'dbtemplates.loader.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_openidconsumer.middleware.OpenIDMiddleware',
#    'account.middleware.LocaleMiddleware',
#    'django.middleware.doc.XViewMiddleware',
#    'djangologging.middleware.LoggingMiddleware',
    'pagination.middleware.PaginationMiddleware',
#    'things_app.middleware.SortOrderMiddleware',
#    'crashlog.CrashLogMiddleware',
#    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'basic_project.urls'

import os.path

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    
    # "notification.context_processors.notification",
    # "announcements.context_processors.site_wide_announcements",
    "account.context_processors.openid",
    "core.context_processors.contact_email",
    # "core.context_processors.site_name",
    # "messages.context_processors.inbox",
    # "friends_app.context_processors.invitations",
    # "core.context_processors.combined_inbox_count",
)

# COMBINED_INBOX_COUNT_SOURCES = (
#     "messages.context_processors.inbox",
#     "friends_app.context_processors.invitations",
#     "notification.context_processors.notification",
# )

INSTALLED_APPS = (
    # included
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    
    # external
#    'notification', # must be first
    'emailconfirmation',
#    'django_extensions',
#    'robots',
#    'dbtemplates',
#    'friends',
#    'mailer',
#    'messages',
#    'announcements',
    'django_openidconsumer',
    'django_openidauth',
#    'oembed',
#    'crashlog',
    'pagination',
#    'gravatar',
#    'threadedcomments',
    'timezones',
#    'tagging',
    'ajax_validation',
#    'avatar',
#    'things',
    
    # internal (for now)
    'basic_profiles',
    'account',
    'core',
    
    'django.contrib.admin',

)

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/%s/" % o.username,
}

AUTH_PROFILE_MODULE = 'basic_profiles.Profile'
# NOTIFICATION_LANGUAGE_MODULE = 'account.Account'

# EMAIL_CONFIRMATION_DAYS = 2
# EMAIL_DEBUG = DEBUG
CONTACT_EMAIL = "feedback@example.com"
# SITE_NAME = "Pinax"
LOGIN_URL = "/account/login"

# LOGGING_OUTPUT_ENABLED = True
# LOGGING_SHOW_METRICS = True
# LOGGING_LOG_SQL = True

# INTERNAL_IPS = (
#     '127.0.0.1',
# )

# ugettext = lambda s: s
# if Django is running behind a proxy, we need to do things like use
# HTTP_X_FORWARDED_FOR instead of REMOTE_ADDR. This setting is used
# to inform apps of this fact
# BEHIND_PROXY = False

try:
    from localsettings import *
except ImportError:
    pass
