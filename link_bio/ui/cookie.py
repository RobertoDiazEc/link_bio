import reflex as rx
import asyncio

import link_bio.constants  as Constants
from ..views.links.timecookies import live_progress


class LocalStorageState(rx.State):
    # local storage that automatically updates in other states across tabs
    autcookie: str = rx.LocalStorage("",sync= True)
    arribaobajo ="1"
    posisionabs= "static"
    opened: int = 0
    ocultartiempo: bool = True
    botoncookie: bool = False
    value: int = 0

    @rx.event
    def dialog_open(self):
        self.opened = 1
        self.autcookie="T"

    @rx.event
    def on_load(self):
        if self.autcookie == "":
            self.opened = 0
            self.botoncookie = True
            self.arribaobajo="1001"
            self.posisionabs= "fixed"
            self.ocultartiempo = True
        else:
            self.arribaobajo="1" 
            self.posisionabs= "static"
            self.botoncookie = False   
 
    @rx.event
    def dialog_salir(self):
        self.opened = 0
        self.autcookie=""
        self.ocultartiempo= False
        self.start_progress

    @rx.event()
    def start_progress(self):
        while self.value < 500:
           self.value += 1
        self.ocultartiempo= True            
       


def alert_dialog2(opened=False) -> rx.Component:
    
    if opened == 1:
        return rx.window_alert("Gracias por Preferirnos!")
    else: 
        return  rx.center(
            rx.cond(
                LocalStorageState.ocultartiempo,
                rx.box(
                    
                    rx.container(
                        # rx.image(
                        #     src=Constants.CPK_LOGO, 
                        #     width="60%", 
                        #     height="25%",
                        # ),
                        rx.heading("Politica de Uso de Cookies", size="3"),
                        rx.text(""" Utilizamos cookies para mejorar tu experiencia en nuestro sitio web. Al continuar navegando en este sitio, aceptas el uso de cookies. Puedes obtener más información en nuestra [Política de Privacidad](#). """), 
                        rx.accordion.root(
                            rx.accordion.item(
                                header="Más Información",
                                content="""Estos cookies son necesarias para asegurar el funcionamiento básico del Site o para suministrar un servicio solicitado por el usuario y no se pueden desactivar. Permiten, por ejemplo, identificar la sesión, acceder a partes de acceso restringido, utilizar elementos de seguridad durante la navegación, etc.""",
                            ),
                            collapsible=True,
                            type="multiple",
                            variant="soft",
                            color_scheme="blue",
                        ),
                        rx.flex(
                            rx.button(
                                "Aceptar",
                                on_click=LocalStorageState.dialog_open,
                                width="50%",
                                variant="soft", 
                            ),
                            rx.button(
                                "Rechazar",
                                on_click=LocalStorageState.dialog_salir,
                                width="50%", 
                                variant="soft",
                            ),
                            spacing="2",
                            flex_direction=["column", "row", "row"],
                            padding="12px",
                        ),
                        padding="12px",
                        border_radius="25px",
                        #as_child=True,
                    ),
                    
                    border_radius="10px",
                    background_color="var(--gray-2)",
                    padding="3em",
                    position=rx.cond(LocalStorageState.autcookie == "",
                                "fixed",
                                "static"
                    ),
                    bottom="10px",
                    z_index=LocalStorageState.arribaobajo,
                    width="80%",
                    overflow="auto"  
                # style={"position": "fixed",
                #            "bottom": "10px", 
                #            "right": "20px", 
                #            "z-index": "1000"}
                ),
                rx.box(
                    rx.hstack(
                        rx.progress(value=LocalStorageState.value, duration="15000"),
                        rx.button(
                            "Exit", on_click=LocalStorageState.start_progress,
                            width="15%", 
                            variant="soft",
                        ),
                        width="100%",
                    ),
                    border_radius="10px",
                    #background_color="var(--gray-2)",
                    padding="1em",
                    position="fixed",
                    bottom="10px",
                    z_index=LocalStorageState.arribaobajo,
                    width="80%",
                    overflow="auto"  
            ),
        ),          
    )