"""
ASGI config for nipik project.
"""

import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup(set_prefix=False)

django_wsgi_app = get_wsgi_application()

from a2wsgi import WSGIMiddleware
from fastapi import FastAPI

from api.routers.contact import router as contact_router

fastapi_app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
fastapi_app.include_router(contact_router, prefix="/api")
fastapi_app.mount("/", WSGIMiddleware(django_wsgi_app))

application = fastapi_app
