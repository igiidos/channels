from .common import *
import dj_database_url



DEBUG = True

ALLOWED_HOSTS = ['*']

db_from_env = dj_database_url.config(env='DATABASE_URL', conn_max_age=500)

# 기존 DATABASES
DATABASES['default'].update(db_from_env)


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('subwaychannels.herokuapp.com', 6379)],
        },
    },
}