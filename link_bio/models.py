import reflex as rx
import sqlalchemy

from typing import List
from sqlmodel import Field, Relationship
from datetime import datetime, timezone

def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ClienteL(rx.Model, table=True):
    """A table of clientes."""
    nombre: str = Field(nullable=False)
    apellido: str = Field(nullable=False)
    email: str = Field(nullable=False)
    celular: str = Field(nullable=False)
    username: str = Field(nullable=False, index=True)
    password: str = Field(nullable=False)
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )
    usersesions: List['UserSesion'] = Relationship(
        back_populates="clientel"
    )
    
class UserSesion(rx.Model, table=True):
    """A table of Users."""
    nombrelogin: str = Field(index=True)
    cliente_id: int = Field(default=None, foreign_key='clientel.id')
    clientel: ClienteL = Relationship(back_populates="usersesions")
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )
    update_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'onupdate': sqlalchemy.func.now(),
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )
    leasingclis: List['LeasingCli'] = Relationship(
        back_populates="usersesionl"
    )


class LeasingCli(rx.Model, table=True):
    """A table of clientes."""
    placa: str = Field(nullable=False)
    servicio: str = Field(nullable=False)
    ruta: str = Field(nullable=False)
    kilometros: int = Field(default=0)
    dimension: str = Field(nullable=False)
    precio_cal: float = Field(default=0)
    leasing: float = Field(default=0)
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )   
    usersesion_id: int = Field(default=None, foreign_key='usersesion.id')
    usersesionl: UserSesion = Relationship(back_populates='leasingclis')
