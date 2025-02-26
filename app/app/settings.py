"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.2.25.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""


from pathlib import Path
import os
#import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = bool(int(os.environ.get('DEBUG', 0)))

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get('ALLOWED_HOSTS', '').split(','),
    )
)



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'storages',
    'corsheaders',
    'rest_framework',
    'import_export',
    'core',
    'users',
    'riskmanagement',
    'extcommungrievancemechanism',
    'emergencyresponse',
    'documentmanagement',
    'programsmanagement',
    'organizationalcapacityandcompetency',
    'reportingmonitoringandreview',
    'resourceefficiencyandpollutionprevention',

   # 'dj_database_url'
    # 'tailwind',
    # 'sweetify',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),  # Defaults to '5432' if DB_PORT is not set
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'OPTIONS': {
            'sslmode': 'require',  # Ensures SSL connection (required by Supabase)
        },
    }
}

# DATABASES = {
#     'default': dj_database_url.parse(
#         os.environ.get('DATABASE_URL'),
#         conn_max_age=0
#     )
# }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CORS_ALLOW_ALL_ORIGINS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

MEDIA_ROOT = '/vol/web/media' 
STATIC_ROOT = '/vol/web/static'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

SUPABASE_PROJECT_ID = os.environ.get('SUPABASE_PROJECT_ID')
SUPABASE_ACCESS_KEY = os.environ.get('SUPABASE_ACCESS_KEY')
SUPABASE_BUCKET_NAME = os.environ.get('SUPABASE_BUCKET_NAME', 'documents')

AWS_ACCESS_KEY_ID = os.environ.get('S3_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = SUPABASE_BUCKET_NAME
AWS_S3_ENDPOINT_URL = f'https://{SUPABASE_PROJECT_ID}.supabase.co/storage/v1/s3'
AWS_S3_REGION_NAME = 'eu-west-3'
AWS_S3_SIGNATURE_VERSION = 's3v4'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

GRAPHENE = {
    'SCHEMA': 'app.schema.schema',
    'MIDDLEWARE': [
        'app.middlewares.CustomAuthMiddleware',
     #   'graphql_jwt.middleware.JSONWebTokenMiddleware',
        'app.middlewares.CustomPaginationMiddleware'
    ],
    'PAGE_SIZE': 20
}

# AUTHENTICATION_BACKENDS = [
#     'graphql_jwt.backends.JSONWebTokenBackend',
#     'django.contrib.auth.backends.ModelBackend',
# ]


#CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_CREDENTIALS = True
#SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'