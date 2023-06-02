from core.settings.base import *
import os

ALLOWED_HOSTS = ["*"]
DEBUG = False
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
