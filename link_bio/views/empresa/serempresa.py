import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.serempresainfo import serempresainfo
from ...components.serempresainfo import serempresaValores
from ...components.serempresainfo import serempresaObjetivos
from link_bio.components.title import title


def serempresa() -> rx.Component:
    return rx.container(
        serempresainfo(
            "Costo por Kilometro SAS",
            "Es una empresa dedicada a la gestión y venta de neumáticos procurando para nuestros clientes la mejor relación costo/beneficio del mercado.",
            ""
        ),
        serempresainfo(
            "LEMA",
            "Una nueva forma de moverse",
            ""
        ),
        serempresainfo(
            "Misión",
            "Costo por Kilometro es una empresa comercializadora de productos y servicios destinados al mantenimiento preventivo y correctivo de vehículos.  Con la calidad, oportunidad, seguridad y cumplimiento necesario para lograr la satisfacción de nuestros clientes.",
            "imagen/mision.jpg"
        ),
        serempresainfo(
            "Visión",
            "En el 2030 ser reconocidos como una empresa rentable con ventas de $300.000 USD/año que ofrece productos y servicios de calidad que se ajustan a las necesidades del transporte en Colombia.",
            "imagen/somos.jpg"
        ),
        serempresaValores(
            "Valores",
            "imagen/somos.jpg"
        ),
        serempresainfo(
            "Política de Calidad",
            "CPK Costo por Kilómetro SAS  se dedicará  a prestar servicios de mantenimiento automotriz seguros y confiables,  comprometiéndose a mejorar continuamente para buscar siempre la satisfacción de sus clientes y la seguridad en sus vehículos.",
            ""
        ),
         serempresaObjetivos(
            "Objetivos de Calidad",
            "imagen/somos.jpg"
        ),
    )