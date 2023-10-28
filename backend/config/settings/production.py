from .base import *

logger.info("Production Configs Running")

REST_FRAMEWORK.update(
    {
        "DEFAULT_RENDERER_CLASSES": "rest_framework.renderers.JSONRenderer",
    }
)
ALLOWED_HOSTS = ["*"]

DEBUG = True