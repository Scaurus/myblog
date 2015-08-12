
from settings import * 
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

#EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'r.zhuravskiy@gmail.com'
EMAIL_USE_TLS = 'TRUE'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'r.scaurus@gmail.com'
EMAIL_HOST_PASSWORD = 'Osdim5smexk'
EMAIL_PORT = 587