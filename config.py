import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
THREADS_PER_PAGE = 2

LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "main.log")

LOG_MAX_BYTES = 1000000
LOG_BACKUP_COUNT = 15

SECRET_KEY = "somesecretkey"