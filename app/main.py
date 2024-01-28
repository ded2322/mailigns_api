from fastapi import FastAPI

from fastapi_cache import FastAPICache
from contextlib import asynccontextmanager
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis


from app.clients.router import router as clients_router
from app.mailing.router import router as mailing_router
from app.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}")
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(clients_router)
app.include_router(mailing_router)
