from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, Integer, Boolean, String, BigInteger
from pydantic import BaseModel

import db
from Candidato.modelo import Candidato

## MODELO RELACIONADO CON LA BD
class Eleccion(db.Base):
    """Este modelo define los atributos de la tabla eleccion y sus tipos de dato"""

    __tablename__ = "eleccion"
    codigo = Column("codigo", String(255), primary_key=True, unique=True, index=True)
    fecha_inicio = Column("fecha_inicio", BigInteger, unique=True)
    fecha_fin = Column("fecha_fin", BigInteger, unique=True)
    nombre = Column("nombre", String(255))
    descripcion = Column("descripcion", String(255))
    candidato = relationship("Candidato")



## MODELO PARA RECIBIR INFORMACION DE UNA PETICION
class Eleccion_apoyo(BaseModel):
    codigo: str
    fecha_inicio: int
    fecha_fin: int
    nombre: str
    descripcion: str
