from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '$!iahgbz$9!!)(r2wif9novg3ywl+#4*y134=@zcgf&d-qiwu7'

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'timescale',
]

ROOT_URLCONF = 'monitor.urls'

DATABASES = {
    "default": {
        "ENGINE": "timescale.db.backends.postgis",
        "HOST": os.environ.get("POSTGRES_HOST"),
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
    },
}
