from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
import db
from sqlalchemy import Column, Integer, Boolean, String
from pydantic import BaseModel

from Voto.modelo import Voto


class Candidato(db.Base):
    """Este modelo define los atributos de la tabla candidato y sus tipos de dato"""

    __tablename__ = "candidato"
    id_candidato = Column("id_candidato", String(255), primary_key=True, unique=True)
    cedula = Column("cedula", String(255), index=True)
    nombre = Column("nombre", String(255))
    apellidos = Column("apellidos", String(255))
    celular = Column("celular", String(255))
    email = Column("email", String(255))
    fotografia = Column("fotografia", String(255))
    nit_partido_politico = Column(String(255), ForeignKey("partido_politico.nit"))
    codigo_eleccion = Column(String(255), ForeignKey("eleccion.codigo"), unique=True)
    voto = relationship("Voto")


## MODELO PARA RECIBIR INFORMACION DE UNA PETICION
class Candidato_apoyo(BaseModel):
    cedula: str
    nombre: str
    apellidos: str
    celular: str
    email: str
    fotografia: str
    nit_partido_politico: str
    codigo_eleccion: str
