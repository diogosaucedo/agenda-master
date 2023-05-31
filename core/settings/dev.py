from core.settings.base import *

# When DEBUG is True and ALLOWED_HOSTS is empty, the host is validated against ['.localhost', '127.0.0.1', '[::1]'].
ALLOWED_HOSTS = []
DEBUG = True
LOGGING = {
    **LOGGING,
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
        }
    },
}
