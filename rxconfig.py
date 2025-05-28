import reflex as rx
from decouple import config

DATABASE_URL = config("DATABASE_URL")
#DATABASE_URL = config("DATABASE_URL_TEST")

config = rx.Config(
    app_name="link_bio",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://cpkm.com.co"
    ],
    db_url= DATABASE_URL,
    show_built_with_reflex=False,
    plugins=[]
)