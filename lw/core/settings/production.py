from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('SECRET_KEY', '')

try:
    from .local import *
except ImportError:
    pass
