import redis

config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}

conn = redis.StrictRedis(**config)

QUIT = False
LIMIT = 10000000
