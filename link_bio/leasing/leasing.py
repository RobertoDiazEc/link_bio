import reflex as rx


from ..backend.backend import backState
from ..styles.styles import SizeTxt
from ..views.pdfs.pdf_react import pdf_react
from ..views.leasing.dimensiones import items_selector
from ..views.leasing.campos import campos_leasing, campo_input, campo_input_blur, campo_switch_doble, button_link, action_button, campo_input_cal, seleccionar_imagen, empresa_datos
from ..ui.routes import Route
import link_bio.styles.styles  as styles
import link_bio.styles.colors as colors
from ..ui.base_page import base_page
from ..modelo.datos_lesing import tipo_Vehiculo, servicio, sector, operacion

  #,on_load= backState.check_login()         

@rx.page(route=Route.LEASING.value, title="CPK | Leasing",on_load= backState.check_login())
def leasing_page() -> rx.Component:
    mi_child=  rx.box(
        rx.desktop_only(
            rx.box(
                rx.hstack(
                    rx.hstack( 
                        rx.image( 
                            src="/logoCPK.jpg", 
                            width="4em", 
                            height="auto", 
                            border_radius="25%", 
                        ), 
                        rx.heading( 
                            "Arrendamiento",
                            size="4",
                            weight="bold", 
                            color= colors.TextoColor.LEASING
                        ),
                    ),                  
                    rx.hstack( 
                        # rx.badge(
                        #         rx.icon(tag="user-round-plus", size=32),
                        #         color_scheme="blue",
                        #         radius="full",
                        #         padding="0.65rem",
                        #     ),
                        rx.heading( f"Bienvenido {backState.user_actual.nombre}",
                            size="3",
                            weight="bold", 
                            color= colors.TextoColor.LEASING
                                ), 
                        rx.icon_button( 
                            rx.icon("log-out"), 
                            size="3", 
                            radius="full",
                            on_click=backState.logout,
                            ),
                        align_items="center"
                    ), 
                    justify="between", 
                    align_items="center", 
                ), 
                #display= "flex", 
                #bg= 
                bg= colors.Color.LEASING,
                padding="1em", 
                position="fixed",    #, absolute#"                
                top="0px", 
                z_index="1000", 
                width="100%", 
                overflow="auto",   
            ),
        ),
        rx.mobile_and_tablet(
            rx.box(
                rx.hstack(
                    rx.hstack( 
                        rx.image( 
                            src="/logoCPK.jpg", 
                            width="3em", 
                            height="auto", 
                            border_radius="25%", 
                        ), 
                        rx.heading( 
                            "Arrendamiento",
                            size="3",
                            weight="bold",
                            height="auto", 
                            color= colors.TextoColor.LEASING
                        ),
                    ),
                    rx.hstack(
                        rx.flex( 
                        # rx.badge(
                        #         rx.icon(tag="user-round-plus", size=10),
                        #         color_scheme="blue",
                        #         radius="full",
                        #         padding="0.05rem",
                        #     ),
                        rx.heading( f"Bienvenido {backState.user_actual.nombre}",
                                    size="1",
                                    weight="bold",
                                    justify="end", 
                                    color= colors.TextoColor.LEASING
                                ),
                                spacing="1",
                                flex_wrap="wrap",
                                width="100%",
                                align="end",
                                justify="end",
                                direction="column",    
                        ),         
                        rx.icon_button( 
                            rx.icon("log-out"), 
                            size="2", 
                            radius="full",
                            on_click=backState.logout,
                        ),
                        align_items="center",
                    ), 
                    justify="between", 
                    align_items="center", 
                ), 
                #display= "flex", 
                #bg= 
                background_color=colors.Color.LEASING, 
                padding="1em", 
                position="fixed", 
                top="0px", 
                z_index="1000", 
                width="100%", 
                overflow="auto",   
            ),
        ),
        rx.cond(
            backState.acceso_auth,                                
            rx.flex(
                rx.box( 
                    rx.form.root(
                        rx.flex(
                            rx.section(
                                rx.flex(
                                    campos_leasing(
                                        "Tipo Vehículo",
                                        backState.tipoVehiculoall,
                                        "tipo",
                                        backState.change_value_tipo,
                                    ),
                                    campos_leasing(
                                        "Servicio",
                                        backState.servicioall,
                                        "servicio",
                                        backState.change_value_servicio,
                                    ),
                                    campos_leasing(
                                        "Operación",
                                        backState.operacionall,
                                        "operacion",
                                        backState.change_value_operacion
                                    ),
                                    campos_leasing(
                                        "Sector",
                                        backState.sectorall,
                                        "sector",
                                        backState.change_value_sector,
                                    ),                                    
                                    margin=SizeTxt.DEFAULT.value,
                                    #direction="row",
                                    spacing="2",
                                    flex_direction=["column", "row", "row"],
                                    #flex_wrap="wrap",
                                    justify="between",
                                    margin_top="8px",
                                    padding="8px",
                                ),
                            #     padding="12px",
                            #     margin=SizeTxt.DEFAULT.value,
                            #     border_radius="20px",
                            #     background_color="#4b652a8a",
                            # ),
                            # rx.section(
                                rx.flex(
                                    campos_leasing(
                                        "Dimension",
                                        backState.dimensionesall,
                                        "dimension",
                                        backState.change_value_dimension,
                                    ),
                                    campo_input_blur(
                                        "Recorrido Km/mes",
                                        "Recorrido Mensual Promedio",
                                        "kilometros",                                        
                                        backState.set_val_kilometros,
                                    ),
                                    campo_input(
                                        "Numero de Placa",
                                        "numero de placa",
                                        "placa",
                                        "Text",
                                        6,
                                    ),
                                    
                                    
                                       
                                    margin=SizeTxt.DEFAULT.value,
                                    #direction="row",
                                    spacing="2",
                                    flex_direction=["column", "row", "row"],
                                    #flex_wrap="wrap",
                                    justify="between",
                                    margin_top="4px",
                                    padding="8px",
                                ),                                
                                rx.card(
                                    rx.flex(
                                        rx.card(
                                            campo_input_cal(
                                                "Tarifa",
                                                "Tarifa calculada",
                                                "leasing",
                                                "float",
                                                backState.calculo_tarifa,
                                            ), 
                                            action_button(
                                                "grip",
                                                "Calcular Tarifa",
                                                backState.calcular_tarifa,
                                            ),
                                            justify="center",
                                            variant="ghost",
                                            width="100%",
                                        ),
                                        rx.card(
                                            campo_input_cal(
                                                "Tarjeta de Propiedad",
                                                "Imagen tarejeta",
                                                "imagenplaca",
                                                "Text",
                                                backState.name_imagen,
                                            ),
                                             rx.callout(
                                                "Subir imagen de la Tarjeta de Propiedad antes de Procesar el Contrato",
                                                icon="info",
                                                color_scheme="blue",
                                            ),
                                        
                                        justify="center",
                                        spacing="2",
                                        variant="ghost",
                                        width="100%",
                                        ),
                                        rx.card(
                                            rx.box(
                                                rx.button(
                                                    rx.center(
                                                    rx.icon("file-text", size=20),
                                                    "Procesar Contrato", flex="1",
                                                    ),
                                                    width="100%",
                                                    radius="full",
                                                ),
                                                padding="10px",
                                                justify="center",
                                                variant="ghost",
                                                width="100%",
                                                type="submit",
                                                cursor="pointer",
                                            ),
                                            rx.cond(backState.leasing_cliente.id,
                                                action_button(
                                                    "newspaper",
                                                    f" Generar Contrato PDF {backState.leasing_cliente.id}",
                                                    backState.generar_pdfjs,
                                                    #generar_pdfjs
                                                # pdf_react,
                                                ),
                                            ),
                                            justify="center",
                                            variant="ghost",
                                            width="100%",
                                        ),
                                        padding="10px",
                                        spacing="2",
                                        flex_direction=["column", "row", "row"],
                                        width="100%",  
                                    ),
                                    padding="12px",
                                    margin=SizeTxt.DEFAULT.value,
                                    border_radius="10px",
                                    background_color="#3b3b3b",  
                                ),
                                padding="12px",
                                margin=SizeTxt.DEFAULT.value,
                                border_radius="20px",
                                background_color="#4b652a8a",
                            ),        
                            #max_width=styles.MAX_WIDTH,
                            margin=SizeTxt.DEFAULT.value,
                            direction="column",
                            #flex_direction=["column", "row", "row"],
                            spacing="4",
                            flex_wrap="wrap",
                            width="100%",
                            #height="100vh",
                            margin_top="10px",
                            padding="15px",
                        ),
                        spacing="3",      
                        width="100%",     
                        #padding="15px", 
                        #margin_bottom="0.2", 
                        on_submit=backState.grabar_leasing,
                        reset_on_submit=True, 
                    ),
                    rx.section(
                        rx.card(
                            
                            rx.accordion.root(
                                rx.accordion.item(
                                    header="Subir Tarjeta de Propiedad",
                                    content= rx.section(
                                        seleccionar_imagen(
                                            "grip",
                                            "Seleccionar Imagen",
                                        ),
                                        rx.hstack(
                                        action_button(
                                            "grip",
                                            "Subir Imagen",
                                            backState.imagen_placa(rx.upload_files(upload_id="upload1")),
                                        ),
                                        action_button(
                                            "grip",
                                            "Borrar Imagen",
                                            backState.imagen_placa_borrar(rx.upload_files(upload_id="upload1")),
                                        ),
                                        ),
                                        rx.image(
                                            src=rx.get_upload_url(backState.name_imagen)
                                        ),
                                    ),
                                    #empresa_datos(backState.actualizacliente),
                                ),                            
                                collapsible=True,
                                width="400px",
                                orientation="vertical",
                            ),

                            padding="12px",
                            variant="ghost",
                            margin=SizeTxt.DEFAULT.value,
                            border_radius="10px",  
                        ),
                        padding="12px",
                        margin=SizeTxt.DEFAULT.value,
                        border_radius="20px",
                        background_color="#4b652a8a",
                    ),        
                    spacing="2",      
                    width="100%",                    
                ),
                # rx.box(
                #     editor_example("<p>Editor content</p>"),
                # ),
                
                width="100%",
                padding_top="60px",
                display="flex",
                flex_direction=["column", "column"],
                align_items="center",
            ),
                
        ),
        #height="auto, 650px", 
    )
    return base_page(
       mi_child,
        True
    )