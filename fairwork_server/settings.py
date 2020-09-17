import os
from pathlib import Path
import django_heroku


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# SECRET_KEY="z8g799!p-!c(z_!v=%%2*c_3l7x=i1+cv8hs%d9wuuwqtfo04_"
SECRET_KEY = "mnlwxor0iu)4d&p69v03_)migrr2n9nv6ned7s$v(y6=n512vv"

ROOT_URLCONF="fairwork_server.urls"

INSTALLED_APPS=[
    "auditor.apps.AuditorConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

STATIC_URL = 'static/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, STATIC_URL),
)

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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

