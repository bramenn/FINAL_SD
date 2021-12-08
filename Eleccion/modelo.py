from sqlalchemy.sql.schema import ForeignKey
import db
from sqlalchemy import Column, Integer, Boolean, String
from pydantic import BaseModel

## MODELO RELACIONADO CON LA BD
class Eleccion(db.Base):
    """Este modelo define los atributos de la tabla eleccion y sus tipos de dato"""
    __tablename__ = "eleccion"
    codigo = Column("codigo", String(255), primary_key=True, unique=True, index=True)
    fecha = Column("fecha", String(255))
    hora_inicio = Column("hora_inicio", String(255))
    hora_fin = Column("hora_fin", String(255))
    nombre = Column("nombre", String(255))
    descripcion = Column("descripcion", String(255))
    cedula_candidato = Column(String(255), ForeignKey("candidato.cedula"))

## MODELO PARA RECIBIR INFORMACION DE UNA PETICION
class Eleccion_apoyo(BaseModel):
    codigo: str
    fecha: str
    hora_inicio: str
    hora_fin: str
    nombre: str
    descripcion: str
