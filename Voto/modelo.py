import db
from sqlalchemy import Column, Integer, Boolean, String
from pydantic import BaseModel

## MODELO RELACIONADO CON LA BD
class Voto(db.Base):
    """Este modelo define los atributos de la tabla voto y sus tipos de dato"""
    __tablename__ = "voto"
    id = Column("id", Integer, primary_key=True, unique=True, index=True)
    cedula_votante = Column("cedula_votante", String(255))
    cedula_candidato = Column("cedula_candidato", String(255))
    fecha_eleccion = Column("fecha_eleccion", String(255))

## MODELO PARA RECIBIR INFORMACION DE UNA PETICION
class Voto_apoyo(BaseModel):
    cedula_votante: str
    cedula_candidato: str
    fecha_eleccion: str
    