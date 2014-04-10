"""
Django settings for libnal project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b=htd1tbvg%#gr3=bet@1j06hjn%-0ktx7))cx-uvh^vnj5(zt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Definicion de las apps o modulos del aplicativo web

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Modulos desarrollados
    'libnal.apps.account',
    'libnal.apps.agencias',
    'libnal.apps.banner',
)

AUTH_PROFILE_MODULE = 'userprofile.UserProfile', 

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'libnal.urls'

WSGI_APPLICATION = 'libnal.wsgi.application'


# Configuracion de la base de datos
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Base de datos MySql
        'NAME': 'libnal',                     # Nombre de la base de datos
        # Configuracion para acceso a la base de datos
        'USER': 'root',
        'PASSWORD': '/**/',
        'HOST': '',        
        'PORT': '',        
    }
}

# Estandarizacion internacional
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Llamado de los templates o los HTML
TEMPLATE_DIRS = os.path.normpath(os.path.join(os.path.dirname(__file__),'templates/'))


# Archivos anexos (CSS, JavaScript, Imagenes)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__),'media/'))

MEDIA_URL = '/media/'