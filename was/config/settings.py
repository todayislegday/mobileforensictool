"전체적인 셋팅"

from pathlib import Path
import os
# 베이스 경로 변수로 설정.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y54lt#$x7zqjdjkdbw#xj7+^mhdig8&v@vo(*tjt2u2=s5ucg@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =True  #DEBUG=True이면, ALLOWED_HOST는 필요없다.
             #DEBUG=False이면, ALLOWED_HOST를 반드시 설정해주어야 하고 
             # /static과 /media의 디렉토리를 웹 서버(Nginx, Apache 등)에서 설정해주어야 한다
ALLOWED_HOSTS = [] 


# Application definition

INSTALLED_APPS = [
    'app.apps.AppConfig',#모델을 앱에서 사용하기 위해서
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR /'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASE_ROUTERS = [ #여러 db를 중계
    'config.dbrouter.MultiDBRouter', 
]

path=os.path.dirname(os.path.abspath(__file__))
f = open(f"{path}/../../경로.txt", 'r')
OUTPATH=f.readlines()[1]
f.close()

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': f'{BASE_DIR}/db.sqlite3',
    },
     'contacts': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/data/com.samsung.android.providers.contacts/databases/contacts2.db',
    },
    'calllog': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/data/com.samsung.android.providers.contacts/databases/calllog.db',
    },
    'message': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/data/com.samsung.android.messaging/databases/message_content.db',
    },
     'mms': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/user_de/0/com.android.providers.telephony/databases/mmssms.db',
    },
    'map': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/data/com.samsung.cmh/databases/cmh.db',
    },
    'chrome2': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/data/com.android.chrome/app_chrome/Default/History',
    },
    'SAMINT': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/data/com.sec.android.app.sbrowser/app_sbrowser/Default/History',
    },
    'WebDowndata': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/data/com.android.providers.downloads/databases/downloads.db',
    },
    'Webint': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/data/com.android.providers.media/databases/internal.db',
    },
    'Webext': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/data/com.android.providers.media/databases/external.db',
    },
    'Appinslog': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/data/com.android.vending/databases/localappstate.db',
    },
    'Media': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/data/com.samsung.android.providers.media/databases/media.db',
    },
    'Calendar': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':f'{OUTPATH}/data/com.android.providers.calendar/databases/calendar.db',
    }

   
}


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
