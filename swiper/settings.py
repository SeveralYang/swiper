"""
Django settings for swiper project.

Generated by 'django-admin startproject' using Django 1.11.15.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&xy_z3v9afo0quh@0vmh)o^l!n!827nfn3&7g)+=1v^)swi1w7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# 允许访问
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'social',
    'vip',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'common.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.middleware.AuthMiddleware'
]

ROOT_URLCONF = 'swiper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django.contrib.auth.context_processors.auth',
                # 'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'swiper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = 'medias'


# 日志配置
BASE_LOG_DIR = os.path.join(BASE_DIR, "logs")

LOGGING = {
    'version':1,
    
    'disable_existing_loggers': False,

    'formatters':{
        'simple':{
            "format" : '%(asctime)s  %(levelname)s : %(funcName)s  %(message)s' ,
            "datefmt" : "%Y-%m-%d %H:%M:%S"
        },
        'verbose':{
            "format" : ('%(asctime)s  %(levelname)s [%(process)d-%(threadName)s] ' 
                        '%(module)s.%(funcName)s line %(lineno)d  %(message)s') ,
            "datefmt" : "%Y-%m-%d %H:%M:%S"
        }
    },

    'handlers':{
        'console':{
            'class':'logging.StreamHandler',
            'level':'DEBUG' if DEBUG else 'WARNING'
        },
        'info':{
            'class':'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, "info.log"),
            'when':'D',
            'backupCount': 30,
            'formatter':'simple',
            'level':"INFO"
        },
        'error':{
            'class':'logging.handlers.TimedRotatingFileHandler',
            'filename':os.path.join(BASE_LOG_DIR,"error.log"),
            'when':'W0', # 每周一新建一个log文件
            'backupCount': 4, # 日志保留四周
            'formatter':'verbose',
            'level':"WARNING"
        }
    },

    'loggers':{
        'django':{
            'handlers':['console'],
        },
        
        'inf':{
            'handlers':['info'],
            'propagate':True,  # 是否向上一级logger实例传递日志信息
            'level':'INFO'
        },
        'err':{
            'handlers':['error'],
            'propagate':True,
            'level':'WARNING'
        }
    },

}

# 默认 django.core.cache  配置
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
#     }
# }

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PICKLE_VERSION": -1
        }
    }
}