import reflex as rx
from decouple import config

DATABASE_URL = config("DATABASE_URL")

config = rx.Config(
    app_name="link_bio",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://cpkm.com.co"
    ],
    db_url= DATABASE_URL
)