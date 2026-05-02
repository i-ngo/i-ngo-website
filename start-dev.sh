#!/bin/sh
uv run uvicorn config.wsgi:application --host 0.0.0.0 --port 8000
