import db
from sqlalchemy import Column, Integer, Boolean, String

class Votante(db.Base):
    """Este modelo define los atributos de la tabla votante y sus tipos de dato"""
    __tablename__ = "votante"
    cedula = Column("cedula", Integer, primary_key=True, unique=True, index=True)
    nombre = Column("nombre", String(255))
    apellidos = Column("apellidos", String(255))
    email = Column("email", String(255))
    celular = Column("celular", String(255))
    fotografia = Column("fotografia", String(255))
    password = Column("password", String(255))
    eliminado = Column("eliminado", Boolean, default=False)