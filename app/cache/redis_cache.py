import json 
import redis
import os
from app.core.config import settings
from dotenv import load_dotenv 
load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")

redis_client = redis.StrictRedis.from_url(REDIS_URL, decode_responses = True)

def get_cached_predicion(key: str):
    value = redis_client.get(key)

    if value:
        return json.loads(value)

    return None

def set_cache_prediction(key: str, value: dict, expiry: int = 3600):
    redis_client.setex(key, expiry, json.dumps(value))