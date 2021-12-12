from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger
import db
from sqlalchemy import Column, Integer, Boolean, String
from pydantic import BaseModel


from Votante.modelo import Votante

## MODELO RELACIONADO CON LA BD
class Voto(db.Base):
    """Este modelo define los atributos de la tabla voto y sus tipos de dato"""

    __tablename__ = "voto"
    id = Column("id", String(255), primary_key=True, unique=True, index=True)
    fecha_eleccion = Column("fecha_eleccion", BigInteger)
    cedula_votante = Column(String(255), ForeignKey("votante.cedula"))
    cedula_candidato = Column(String(255), ForeignKey("candidato.cedula"))
    # many-to-one side remains, see tip below
    votante = relationship("Votante", back_populates="voto")


## MODELO PARA RECIBIR INFORMACION DE UNA PETICION
class Voto_apoyo(BaseModel):
    cedula_votante: str
    cedula_candidato: str
    fecha_eleccion: int
