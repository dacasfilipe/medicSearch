from .settings import *
DEBUG = True
#chave secreta
SECRET_KEY = 'dafasfsafa'
#conectar no banco sqlite3
DATABASES = {
    'default':{
        'ENGINE':'django.db.bacends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#conectar no banco mysql
# DATABASES = {
#     'default':{
#         'ENGINE':'django.db.backends.mysql',
#         'NAME':'medicdb',
#         'USER':'root',
#         'PASSWORD':'root',
#         'HOST':'localhost',
#         'PORT':'3306',
#     }
# }

ALLOWED_HOSTS = ['localhost','127.0.0.1']