from dotenv import dotenv_values

env_vars = dotenv_values()

STORAGES = {
    "default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"},
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
AWS_S3_ENDPOINT_URL = env_vars.get("LIARA_ENDPOINT")
AWS_STORAGE_BUCKET_NAME = env_vars.get("LIARA_BUCKET_NAME")
AWS_S3_ACCESS_KEY_ID = env_vars.get("LIARA_ACCESS_KEY")
AWS_S3_SECRET_ACCESS_KEY = env_vars.get("LIARA_SECRET_KEY")