import reflex as rx
from typing import List

chip_props = {
    "radius": "full",
    "variant": "surface",
    "size": "3",
    "cursor": "pointer",
    "style": {"_hover": {"opacity": 0.75}},
}

def campos_leasing(titulo: str, sel_campo: List, nombre: str, on_change: callable) -> rx.Component:
    return rx.flex(
        rx.badge(titulo, variant="solid", high_contrast=True),                
        rx.select(
            sel_campo,
            name=nombre,
            required=True,
            on_change=on_change,
        ),
        width="100%",
        flex_direction=["column", "row", "column"],
    )


def campo_input(titulo: str, placehol: str, nombre: str, tipo: str, max: int) -> rx.Component:
    return rx.flex(
        rx.badge(titulo, variant="solid", high_contrast=True),
        rx.input(
            placeholder=placehol,
            name=nombre,
            type= tipo,
            max_length = max,
            required=True,
        #on_blur="",
        ),
        width="100%",
        flex_direction=["column", "row", "column"],
    )

def campo_input_blur(titulo: str, placehol: str, nombre: str,on_blur: callable) -> rx.Component:
    return rx.flex(
        rx.badge(titulo, variant="solid", high_contrast=True),
        rx.input(
            placeholder=placehol,
            name=nombre,
            on_blur=on_blur,
            required=True,
        #on_blur="",
        ),
        width="100%",
        flex_direction=["column", "row", "column"],
    )

def campo_input_cal(titulo: str, placehol: str, nombre: str, tipo: str, valor: str) -> rx.Component:
    return rx.flex(
        rx.badge(titulo, variant="solid", high_contrast=True),
        rx.input(
            placeholder=placehol,
            name=nombre,
            type= tipo,
            value=valor,
            disabled=True,
        #on_blur="",
        ),
        width="100%",
        flex_direction=["column", "row", "column"],
    )

def campo_check(titulo: str, nombre: str, on_change: callable) -> rx.Component:
    return rx.flex(
        
        rx.checkbox(
            rx.badge(titulo, variant="solid", high_contrast=True),
            on_change=on_change,
            name=nombre,
            ),
            
        width="100%",
        flex_direction=["column", "row", "column"],
    )

def campo_switch(titulo: str, nombre: str, on_change: callable) -> rx.Component:
    return rx.badge(
        rx.switch(on_change=on_change, name=nombre),
        titulo,
        color_scheme="green",
        **chip_props,
    )

def campo_switch_doble(titulo1: str, titulo2: str, nombre: str, on_change: callable) -> rx.Component:
    return rx.badge(
        titulo1,
        rx.switch(on_change=on_change, name=nombre),
        titulo2,
        color_scheme="green",
        **chip_props,
    )

def editor_example(contenido: str): 
    return rx.vstack(
        rx.editor( 
            set_contents=contenido,
           set_options=rx.EditorOptions(
                button_list=[
                    ["fullScreen", "showBlocks", "codeView"],
                    ["preview", "print"],
                ]
           )
        ), 
        rx.box( 
            rx.html(contenido), 
            border="1px dashed #ccc",  
            border_radius="4px", 
            width="100%", 
        ), 
    ) 


def action_button(icon: str,label: str,on_click: callable) -> rx.Component:
    return rx.badge(
        rx.icon(icon, size=18),
        label,
        color_scheme="green",
        on_click=on_click,
        **chip_props,
    )

def action_link2(icon: str,label: str,href2: str) -> rx.Component:
    return rx.badge(
        rx.icon(icon, size=18),
        rx.link(
            label,
            href=href2,
        ),
        color_scheme="green",
        **chip_props,
    )    


def info_button(icon: str,label: str) -> rx.Component:
    return rx.badge(
        rx.icon(icon, size=18),
        rx.text(label),
        color_scheme="green",
        **chip_props,
    )

def button_link(icon: str,label: str, link: str) -> rx.Component:
    return rx.button(
        rx.box(
            rx.flex(
                rx.icon(icon, size=20),
                rx.text(label),
                spacing="1",
                direction="row",
            ),
            width="100%",
            justify="center",
            align="center",       
        ),
        cursor= "pointer",
        border="full",
        border_color="green",
        background_color="white",
        color="green",
        on_click=link,
        width="50hv",
)

def empresa_datos(on_submit: callable) -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Actualizar Datos", size="4"),
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title(
                "Actualizar Datos Empresa",
            ),
           
            rx.form(
                rx.flex(
                    rx.input(
                        placeholder="NIT - RUT", name="nitrut"
                    ),
                     rx.input(
                        placeholder="nombre empresa", name="nombre_empresa"
                    ),
                     rx.input(
                        placeholder="Representante Legal", name="representante"
                    ),
                    
                    rx.flex(
                        rx.alert_dialog.cancel(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.alert_dialog.action(
                            rx.button(
                                "Actualizar", type="submit"
                            ),
                        ),
                        spacing="3",
                        justify="center",
                    ),
                    direction="column",
                    spacing="4",
                ),
                on_submit=on_submit,
                reset_on_submit=False,
            ),
            max_width="450px",
        ),
    )

color = "rgb(107,99,246)"

def seleccionar_imagen(icon: str,label: str) -> rx.Component:
    """La vista principal."""
    return rx.upload(
            rx.vstack(
                rx.badge(
                    rx.icon(icon, size=18),
                    label,
                    color_scheme="green",
                    **chip_props,
                ),
            ),
            id="upload1",
            max_files=1,
            border=f"1px dotted {color}",
            padding="5em",
        )

