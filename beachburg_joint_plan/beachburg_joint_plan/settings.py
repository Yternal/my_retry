from pathlib import Path

from environ import Env
from loguru import logger

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

# Path
logger.add(
    sink="logs/{time:YYYY-MM-DD}.log",
    rotation="00:00",
    retention="3 days",
    compression="gz",
    encoding="utf-8",
    enqueue=True
)

# Env

assert (env_file_path := BASE_DIR / 'develop.env' if DEBUG else BASE_DIR / 'produce.env').is_file(), '缺少环境变量文件'
logger.info(f'环境变量:{env_file_path.name}')
env = Env(
    daily_push_template_id=(str, ''),  # 每日推送模版id
    daily_push_subscription_num_app_id=(str, ''),       # 每日推送测试订阅号app_id
    daily_push_subscription_num_app_secret=(str, ''),   # 每日推送测试订阅号app_secret
    daily_push_subscription_wife_open_id=(str, ''),     # 每日推送老婆账号open_id
    daily_push_subscription_mine_open_id=(str, ''),     # 每日推送自己账号open_id
)

Env.read_env(env_file=str(env_file_path))

SECRET_KEY = 'django-insecure-xh6#i#ltb_p&u5f06((u7+=by2vq_+bmiz#c_5p=-)8d#pdgkz'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'beachburg_joint_plan.urls'

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

WSGI_APPLICATION = 'beachburg_joint_plan.wsgi.application'

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

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#