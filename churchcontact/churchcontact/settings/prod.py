from churchcontact.settings.base import * 

DEBUG = False

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = ""
EMAIL_PORT = 587
EMAIL_HOST_USER = "test@host.com"
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
