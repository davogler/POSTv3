# Django settings for post project.


import os.path

#-------private settings outside of repository-----#

from settings_private import *

#-------private settings outside of repository-----#


# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

ROOT_PATH = os.path.dirname(__file__)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(ROOT_PATH, '../media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = (
	os.path.join(ROOT_PATH, '../assets')
)

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/assets/'

# Additional locations of static files
STATICFILES_DIRS = (
	os.path.join(ROOT_PATH, './static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

LOGIN_URL = '/admin/'
LOGIN_REDIRECT_URL = '/admin/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'post.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'post.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_PATH, '../templates'),
)

# For Grappelli Dashboard:

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.static",
    "articles.context_processors.site",
)

FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_URL_FILEBROWSER_MEDIA =  STATIC_URL + "filebrowser/"
FILEBROWSER_PATH_FILEBROWSER_MEDIA = os.path.join(STATIC_ROOT, 'filebrowser/')
FILEBROWSER_MAX_UPLOAD_SIZE = '10485760'
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg','.jpeg','.gif','.png','.tif','.tiff'],
    'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
    'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm'],
    'Audio': ['.mp3','.mp4','.wav','.aiff','.midi','.m4p']
}

FILEBROWSER_SELECT_FORMATS = {
    'file': ['Folder','Image','Document','Video','Audio'],
    'image': ['Image'],
    'document': ['Document'],
    'media': ['Video','Audio'],
}


FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail(60x60)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail(60x60)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'micro': {'verbose_name': 'Micro(50x-)', 'width': 50, 'height': '', 'opts': ''},
    'product_thumb':{'verbose_name': 'Product Thumbnail(100x-)', 'width': 100, 'height': '', 'opts': ''},
    'threeup': {'verbose_name': 'Three Col(313x-)', 'width': 313, 'height': '', 'opts': ''},
    'small': {'verbose_name': 'Small(525x-)', 'width': 525, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium(640x-)', 'width': 640, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big(960x-)', 'width': 960, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large(1280x-)', 'width': 1280, 'height': '', 'opts': ''},
}
FILEBROWSER_ADMIN_VERSIONS = ['micro', 'thumbnail', 'product_thumb', 'threeup', 'small', 'medium', 'big', 'large']
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'

GRAPPELLI_INDEX_DASHBOARD = 'post.dashboard.CustomIndexDashboard'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'mailsnake',
    'signups',
    'subscribers',
    'articles',
    'staff',
    'south',
    
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

from logging import *
