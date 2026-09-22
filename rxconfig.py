import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin
from reflex.plugins import RadixThemesPlugin
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
    backend_host="0.0.0.0",
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.TailwindV4Plugin(),
        RadixThemesPlugin(
            theme=rx.theme(
                appearance="light",
                has_background=True,
                radius="large",
                accent_color="lime"
            )
        )
    ],
    disable_plugins =[SitemapPlugin],
)