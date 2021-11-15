import db
from sqlalchemy import Column, Integer, Text, Boolean, String, ForeignKey, Float

class Votante(db.Base):
    __tablename__ = "votante"
    id = Column(Integer, primary_key=True, index=True)
    cedula = Column("cedula", Integer, unique=True, index=True)
    nombre = Column("nombre", String(255))
    apelldos = Column("apelldos", String(255))
    email = Column("email", String(255))
    telefono = Column("telefono", String(255))
    fotografia = Column("fotografia", String(255))
    password = Column("password", String(255))