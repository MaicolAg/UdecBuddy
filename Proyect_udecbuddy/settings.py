import os
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dgp675wp3el8y@knx0*5z#4$9l*3&en_g^8p7)@@(-x!4n%)+&'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'home'
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
ROOT_URLCONF = 'UdecBuddy.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./home/template'],
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
WSGI_APPLICATION = 'UdecBuddy.wsgi.application'
# Database
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'udebuddy_test',
        'USER': 'udebuddy_test',
        'PASSWORD': 'Udecbuddy1234',
        'HOST': 'mysql-udebuddy.alwaysdata.net',
        'PORT':3306,
    }
}'''


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'udecbuddy',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT':3306,
    }
}
# Password validation
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
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'  # Esto debería coincidir con el nombre de la ruta de tu vista de inicio de sesión
LOGIN_REDIRECT_URL = 'login'  # Esto debería coincidir con el nombre de la ruta de tu vista de inicio de sesión
LOGOUT_REDIRECT_URL ='login'
AUTHENTICATION_BACKENDS = ['home.views.EmailBackend', 'home.views.CustomLoginView']

AUTH_USER_MODEL = 'home.Usuarios'
SESSION_COOKIE_AGE = 1200  # 10 minutes
SESSION_SAVE_EVERY_REQUEST = True
# media
MEDIA_URL = '/archivos/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'archivos')
