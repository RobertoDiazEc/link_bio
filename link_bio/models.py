import reflex as rx
import sqlalchemy

from typing import List, Optional
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
    ciudad: str = Field(nullable=False)
    username: str = Field(nullable=False, index=True)
    password: str = Field(nullable=False)
    estado: str = Field(default="AC", max_length=2)
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )
    nitrut: Optional[str] = None
    nombre_empresa: Optional[str] = None
    representante: Optional[str] = None
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

class Tipo_Vehiculo(rx.Model, table=True):
    """A table of tipo_vehiculo."""
    nombre: str = Field(nullable=False, index=True, unique=True)
    valor: Optional[int] = None
    estado: str = Field(default="AC", max_length=2)
    tarifatipo: List['Tarifas'] = Relationship(back_populates='tipo_vehiculos')


class Servicio(rx.Model, table=True):
    """A table of servicios.""" 
    name: str = Field(nullable=False, unique=True)
    valor: Optional[int] = None
    estado: str = Field(default="AC", max_length=2)  

class Sector(rx.Model, table=True):
    nombre: str = Field(nullable=False, unique=True)
    valor: Optional[int] = None
    estado: str = Field(default="AC", max_length=2)      

class Operacion(rx.Model, table=True):
    nombre: str = Field(nullable=False, index=True)
    valor: Optional[int] = None
    estado: str = Field(default="AC", max_length=2)
    tarifaoperacion: List['Tarifas'] = Relationship(back_populates='operacions')

class Dimensiones(rx.Model, table=True):
    nombre: str = Field(nullable=False, index=True, unique=True)
    valor: Optional[int] = None
    estado: str = Field(default="AC", max_length=2)
    tarifadimension: List['Tarifas'] = Relationship(back_populates='dimensioness')       

class Config_Empresa(rx.Model, table=True):
    nombre: str = Field(nullable=False)
    direccion: str
    nit: Optional[int] = None
    representante: str
    por_iva: Optional[int] = None
    email: str
    moneda: str
    server_email: str
    stm_email: str
    pop_email: str
    administrador: str
    estado: str = Field(default="AC", max_length=2)

class Tarifas(rx.Model, table=True):
    """A table of tarifas."""
    tipo: str = Field(nullable=False, index=True)
    operacion: str = Field(nullable=False, index=True)
    dimension: str = Field(nullable=False, index=True)
    valor: float = Field(default=0)
    estado: str = Field(default="AC", max_length=2)
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
        back_populates="tarifasu"
    )
    dimension_id: int = Field(default=None, foreign_key='dimensiones.id')
    dimensioness: Dimensiones = Relationship(back_populates='tarifadimension')
    operacion_id: int = Field(default=None, foreign_key='operacion.id')
    operacions: Operacion = Relationship(back_populates='tarifaoperacion')
    tipo_id: int = Field(default=None, foreign_key='tipo_vehiculo.id')
    tipo_vehiculos: Tipo_Vehiculo = Relationship(back_populates='tarifatipo')


class LeasingCli(rx.Model, table=True):
    """A table of clientes."""
    placa: str = Field(nullable=False, max_length=6)
    tipo: str = Field(nullable=False)
    servicio: str = Field(nullable=False)
    operacion: str = Field(nullable=False)
    sector: str = Field(nullable=False)
    ruta: str = Field(nullable=False)
    kilometros: int = Field(default=0)
    dimension: str = Field(nullable=False)
    precio_cal: float = Field(default=0)
    leasing: float = Field(default=0)
    username: str = Field(nullable=False, index=True)
    estado: str = Field(default="AC", max_length=2)
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    ) 
    imagenplaca: Optional[str] = None 
    usersesion_id: int = Field(default=None, foreign_key='usersesion.id')
    usersesionl: UserSesion = Relationship(back_populates='leasingclis')
    tarifa_id: int = Field(default=None, foreign_key='tarifas.id')
    tarifasu: Tarifas = Relationship(back_populates='leasingclis')
   
    
class Contactos(rx.Model, table=True):
    nombres: str = Field(nullable=False, index=True)
    correo: str = Field(nullable=False, unique=True)
    titulo: str = Field(nullable=False)
    mesaje: str = Field(nullable=False)
    estado: str = Field(default="AC", max_length=2)
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    ) 

