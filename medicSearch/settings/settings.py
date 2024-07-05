from pathlib import Path
LANGUAGE_CODE='pt-br'
TIME_ZONE = 'America/Sao_Paulo'
import os
STATIC_URL = '/static'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
ALLOWED_HOSTS = ['localhost','127.0.0.1']