from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        # 'NAME': BASE_DIR.child('db.sqlite3'),
        'NAME': 'dbempleado',
        'USER': 'genaro',
        'PASSWORD': 'DesarrolloGenaro',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]        # Archivos estaticos

MEDIA_URL = '/media/' #prefijo del url web de todas las imagenes
MEDIA_ROOT = BASE_DIR.child('media') #carpeta donde se ubicaran los archivos