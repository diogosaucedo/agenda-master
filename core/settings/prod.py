from core.settings.base import *


ALLOWED_HOSTS = ["*"]
DEBUG = False
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
