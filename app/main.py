from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from app.bookings.router import router as booking_router
from app.hotels.router import router as hotel_router
from app.images.router import router as image_router
from app.pages.router import router as page_router
from app.settings import settings
from app.users.router import router as user_router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url(settings.REDIS_URL)
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield


app = FastAPI(lifespan=lifespan)


app.mount('/static', StaticFiles(directory='app/static'), name='static')
app.include_router(page_router)
app.include_router(user_router)
app.include_router(booking_router)
app.include_router(hotel_router)
app.include_router(image_router)


origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)
