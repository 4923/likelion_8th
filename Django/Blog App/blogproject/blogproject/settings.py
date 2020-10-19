from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rx4##k1_e3q!xaj2ud4m7s2%yk%m)!)s9&f0#^zdh@!@)*!+a1'
# 404 page 안나오는 에러
#  'You're seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.' 
# SECURITY WARNING: don't run with debug turned on in production!

### DEBUG가 True면 개발자모드, False면 배포모드
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = '*'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'handlerpage',
    'portfolio.apps.PortfolioConfig',
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

ROOT_URLCONF = 'blogproject.urls'

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

WSGI_APPLICATION = 'blogproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# < STATIC >
STATIC_URL = '/static/'
# static file 경로 적는 부분
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'portfolio','static')
]
# static이 모일 위치: django에서 static 모으는 기능 제공함
STATIC_ROOT = os.path.join(BASE_DIR,'static')
  # 위 STATICFILES_DIRS, STATIC_ROOT 작업 종료 후 python manage.py collectstatic 명령어로 static 모으기
  # 이제 blogproject 안에 static 폴더가 생겼을테니까, template에 가서 {% load static %} 사용하면 static을 template에 불러오게 됨 (여기서는 portfolio.html)

# < Media >
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')