import reflex as rx
from typing import List
from ...modelo.datos_lesing import dimensiones
from ...models import Dimensiones, Tarifas
from sqlmodel import String, asc, cast, desc, func, or_, select
from ...backend.backend import backState
import random
from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)

chip_props = {
    "radius": "full",
    "variant": "surface",
    "size": "3",
    "cursor": "pointer",
    "style": {"_hover": {"opacity": 0.75}},
}



class BasicChipsState(rx.State):
    skills: List[str] = []
    dimension_item: str =""
    selected_items: List[str] = skills[:0]

    @rx.event
    def add_selected(self, item: str):
        self.selected_items.append(item)
        self.dimension_item=self.dimension_item + item
        #print(self.selected_items)

    @rx.event
    def remove_selected(self, item: str):
        self.selected_items.remove(item)

    @rx.event
    def add_all_selected(self):
        self.selected_items = list(self.skills) 

    @rx.event
    def clear_selected(self):
        self.selected_items.clear()
        self.skills.clear()

    @rx.event
    def random_selected(self):
        self.selected_items = random.sample(
            self.skills, k=random.randint(1, len(self.skills))
        )

    @rx.event
    def llenar_dimensiones(self, tipod: str, operaciond: str):
        print(tipod)
        print(operaciond)
        self.clear_selected()
        with rx.session() as session:
            #self.skills= session.exec(select(Dimensiones.nombre).where()).all()
            self.skills= session.exec(select(Tarifas.dimension).where(
                (Tarifas.tipo == tipod)).where( Tarifas.operacion == operaciond)
                ).all()
        print(self.skills)     


def action_button(icon: str,label: str,on_click: callable) -> rx.Component:
    return rx.badge(
        rx.icon(icon, size=18),
        label,
        color_scheme="green",
        on_click=on_click,
        **chip_props,
    )


def selected_item_chip(item: str) -> rx.Component:
    return rx.badge(
        item,
        rx.icon("circle-x", size=18),
        color_scheme="green",
        **chip_props,
        on_click=BasicChipsState.remove_selected(item),
    )


def unselected_item_chip(item: str) -> rx.Component:
    return rx.cond(
        BasicChipsState.selected_items.contains(item),
        rx.fragment(),
        rx.badge(
            item,
            rx.icon("circle-plus", size=18),
            color_scheme="gray",
            **chip_props,
            on_click=BasicChipsState.add_selected(item),
        ),
    )

def allselected_item(item: str) -> rx.Component:
    return rx.badge(
            item,
            rx.icon("circle-plus", size=18),
            color_scheme="gray",
            **chip_props,
            on_click=BasicChipsState.llenar_dimensiones(item),
        )


def items_selector() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.hstack(
                rx.icon("lightbulb", size=20),
                rx.heading(
                    "Dimensiones"
                    + f" ({BasicChipsState.selected_items.length()})",
                    size="4",
                ),
                spacing="1",
                align="center",
                width="100%",
                justify_content=["end", "start"],
            ),
            # rx.hstack(
            #     action_button(
            #         "plus",
            #         "Add All",
            #         BasicChipsState.add_all_selected,
            #         "green",
            #     ),
            #     action_button(
            #         "trash",
            #         "Clear All",
            #         BasicChipsState.clear_selected,
            #         "tomato",
            #     ),
            #     action_button(
            #         "shuffle",
            #         "",
            #         BasicChipsState.random_selected,
            #         "gray",
            #     ),
            rx.hstack(
                action_button(
                    "plus",
                    "Actualizar Dimenciones",
                    BasicChipsState.llenar_dimensiones(backState.val_tipo_vehiculo, backState.val_operacion),
                ),
                spacing="2",
                justify="end",
                width="100%",
            ),
            justify="between",
            flex_direction=["column", "row"],
            align="center",
            spacing="2",
            margin_bottom="10px",
            width="100%",
        ),
        # Selected Items
        rx.flex(
            rx.foreach(
                BasicChipsState.selected_items,
                selected_item_chip,
            ),
            wrap="wrap",
            spacing="2",
            justify_content="start",
        ),
        rx.divider(),
        # Unselected Items
        rx.cond(BasicChipsState.skills.length() > 0,
            rx.flex(
                rx.foreach(
                    BasicChipsState.skills, 
                    unselected_item_chip
                ),
                wrap="wrap",
                spacing="2",
                justify_content="start",
            ),
        ),

        justify_content="start",
        align_items="start",
        width="100%",
    )