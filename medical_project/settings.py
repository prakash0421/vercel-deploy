"""

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--*71!kik#^myyj*4la+(0a7gx%fg__)il*od*0plzlg@7+mxoh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.vercel.app']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'medical_app',
    'storages'
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

ROOT_URLCONF = 'medical_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'medical_project.wsgi.application'
LOGIN_REDIRECT_URL='patient_dashboard'
LOGOUT_REDIRECT_URL='login'
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',                             # Supabase database name
        'USER': 'postgres.qhygyhaqwusjqdzodapq',        # Supabase user
        'PASSWORD': 'XHzjU06U1B40yPZ7',                 # Supabase password
        'HOST': 'aws-0-ap-south-1.pooler.supabase.com', # Supabase host
        'PORT': '6543',                                 # Supabase port
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/





# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL='medical_app.CustomUser'


# Add 'storages' to your INSTALLED_APPS



# AWS S3 Settings (directly in settings.py)
AWS_ACCESS_KEY_ID = 'AKIAZI2LFMFHJ6XCNZVC'
AWS_SECRET_ACCESS_KEY = 'SJ0TXRnt//Lm9kiHi52xuXiNo3Uv8gji+5zK5U18'
AWS_STORAGE_BUCKET_NAME = 'prakash-1234'
AWS_S3_REGION_NAME = 'us-east-1'  # Example: 'us-west-1'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_LOCATION ='static'

# Optional settings
AWS_S3_FILE_OVERWRITE = False  # To prevent overwriting files with the same name
AWS_DEFAULT_ACL = None  # Recommended to avoid issues with ACLs
AWS_QUERYSTRING_AUTH = False  # To make the URLs for static files public without query string


MEDIA_URL = 'https://prakash-1234.s3.us-east-1.amazonaws.com/'
# Optional settings
STATIC_ROOT = BASE_DIR / 'staticfiles'
AWS_S3_FILE_OVERWRITE = False  # To prevent overwriting files with the same name
AWS_DEFAULT_ACL = None  # Recommended to avoid issues with ACLs
AWS_QUERYSTRING_AUTH = False  # To make the URLs for static files public without query string
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (Uploads)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_ROOT = ''

