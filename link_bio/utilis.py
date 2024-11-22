import reflex as rx

#comun

def lang()-> rx.Component:
    return rx.script("document.documentElemt.lang='es'")

preview = "/imagen/arcCPK.jpg"
_meta = [
     {"name": "og:type", "content": "website"},
     {"name": "og:imagen", "content": preview},
]

#index
index_title = "CPK | Costo por Kilometro"
index_description = ""
index_preview = "/imagen/logoCPK.jpg"

index_meta = [
        {"name": "og:title", "content": index_title},
        {"name": "og:description", "content": index_description},
 ]

index_meta.extend(_meta)