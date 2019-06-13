import dj_database_url
from task_creator.utils import get_dot_env

ENV = get_dot_env()
DEBUG = True

DATABASES = {"default": dj_database_url.config(conn_max_age=500)}


EMAIL_HOST = "in-v3.mailjet.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = ENV.str("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = ENV.str("EMAIL_HOST_PASSWORD")

