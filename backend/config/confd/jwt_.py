from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=900),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
}
