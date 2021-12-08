from sqlalchemy.sql.schema import ForeignKey
import db
from sqlalchemy import Column, Integer, Boolean, String
from pydantic import BaseModel

## MODELO RELACIONADO CON LA BD
class Eleccion(db.Base):
    """Este modelo define los atributos de la tabla eleccion y sus tipos de dato"""
    __tablename__ = "eleccion"
    codigo = Column("codigo", String(255), primary_key=True, unique=True, index=True)
    fecha_inicio = Column("fecha_inicio", Integer, unique=True)
    fecha_fin = Column("fecha_fin", Integer, unique=True)
    nombre = Column("nombre", String(255))
    descripcion = Column("descripcion", String(255))
    cedula_candidato = Column(String(255), ForeignKey("candidato.cedula"))

## MODELO PARA RECIBIR INFORMACION DE UNA PETICION
class Eleccion_apoyo(BaseModel):
    codigo: str
    fecha_inicio: int
    fecha_fin: int
    nombre: str
    descripcion: str
