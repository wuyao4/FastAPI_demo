import dramatiq
from app.config import Config
from dramatiq.middleware import Retries
from dramatiq.brokers.redis import RedisBroker

retries = Retries(max_retries=3)
redis_broker = RedisBroker(url=Config.REDIS_URL)
redis_broker.add_middleware(retries)
dramatiq.set_broker(redis_broker)
