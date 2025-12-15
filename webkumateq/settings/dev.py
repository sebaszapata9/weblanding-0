# tu_proyecto/settings/dev.py
from .base import *
import os

DEBUG = True
# debug en true permite visualizar errores detallados en el navegador

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# DB simple en dev (SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# En dev Django sirve estáticos desde aquí (tu carpeta /static)
STATICFILES_DIRS = [BASE_DIR / "static"]

"""STATICFILES_DIRS para servir assets sin collectstatic."""



# Emails a consola para no spamearte
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
