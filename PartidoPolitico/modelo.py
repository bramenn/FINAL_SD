from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, Integer, Boolean, String
from pydantic import BaseModel

from Candidato.modelo import Candidato
import db


class PartidoPolitico(db.Base):
    """Este modelo define los atributos de la tabla partido politico y sus tipos de dato"""

    __tablename__ = "partido_politico"
    nit = Column("nit", String(255), primary_key=True, unique=True, index=True)
    nombre = Column("nombre", String(255))
    direccion = Column("direccion", String(255))
    foto_oficial = Column("foto_oficial", String(255))
    telefono = Column("telefono", String(255))
    cedula_candidato = relationship("Candidato")


## MODELO PARA RECIBIR INFORMACION DE UNA PETICION
class PartidoPolitico_apoyo(BaseModel):
    nit: str
    nombre: str
    direccion: str
    foto_oficial: str
    telefono: str
