import sentry_sdk
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from src.emails.router import router as email_router
from src.newsletter.router import router as newsletter_router
from src.config import settings
app = FastAPI()
app.include_router(email_router)
app.include_router(newsletter_router)



sentry_sdk.init(
    dsn=settings.SENTRY_URL,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
app.add_middleware(SentryAsgiMiddleware)