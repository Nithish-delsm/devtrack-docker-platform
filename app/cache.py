import json
import os

import redis

_client = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=6379,
    password=os.environ["REDIS_PASSWORD"],
    decode_responses=True,
    socket_connect_timeout=2,
    socket_timeout=2,
)

TASKS_KEY = "tasks:all"
TTL_SECONDS = 60


def cache_get(key):
    """Return (value, redis_ok). value is None on a miss."""
    try:
        raw = _client.get(key)
        return (json.loads(raw) if raw is not None else None), True
    except redis.RedisError:
        return None, False


def cache_set(key, value, ttl=TTL_SECONDS):
    try:
        _client.set(key, json.dumps(value), ex=ttl)
    except redis.RedisError:
        pass


def cache_delete(key):
    try:
        _client.delete(key)
    except redis.RedisError:
        pass
