from core.settings.base import *
import os

ALLOWED_HOSTS = ["*"]
DEBUG = False
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = os.path.join(BASE_DIR, "static")
