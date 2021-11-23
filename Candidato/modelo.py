import db
from sqlalchemy import Column, Integer, Boolean, String

class Candidato(db.Base):
    """Este modelo define los atributos de la tabla candidato y sus tipos de dato"""
    __tablename__ = "candidato"
    cedula = Column("documeto de identidad", Integer, primary_key=True, unique=True, index=True)
    nombre = Column("nombre", String(255))
    apellidos = Column("apellidos", String(255))
    celular = Column("celular", String(255))
    email = Column("email", String(255))
    fotografia = Column("fotografia", String(255))
    partido_politico = Column("partido politico", String(255))