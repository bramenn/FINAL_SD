from sqlalchemy.orm import relationship
import db
from sqlalchemy import Column, Integer, Boolean, String
from pydantic import BaseModel

## MODELO RELACIONADO CON LA BD
class Votante(db.Base):
    """Este modelo define los atributos de la tabla votante y sus tipos de dato"""

    __tablename__ = "votante"
    cedula = Column("cedula", String(255), primary_key=True, unique=True, index=True)
    nombre = Column("nombre", String(255))
    apellidos = Column("apellidos", String(255))
    email = Column("email", String(255))
    celular = Column("celular", String(255))
    fotografia = Column("fotografia", String(255))
    password = Column("password", String(255))
    voto = relationship("Voto", back_populates="votante", uselist=False)


## MODELO PARA RECIBIR INFORMACION DE UNA PETICION
class Votante_apoyo(BaseModel):
    cedula: str
    nombre: str
    apellidos: str
    email: str
    celular: str
    fotografia: str
    password: str
