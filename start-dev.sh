#!/bin/sh
gunicorn config.asgi_wsgi:application -k uvicorn.workers.UvicornWorker -w 2 -b 0.0.0.0:8000
