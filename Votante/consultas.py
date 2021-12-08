from Votante.modelo import Votante, Votante_apoyo
import db

def obtener_votantes_db():
    """
    Obtener todos los votantes
    query:
        select * from votante;
    """
    votante = db.session.query(Votante).all()
    return votante

def obtener_votante_por_cedula(cedula:str):
    votante = db.session.query(Votante).where(Votante.cedula==cedula).first()

    if not votante:
        return None

    votante_dict = {
            "cedula": votante.cedula,
            "nombre": votante.nombre,
            "apellidos": votante.apellidos,
            "email": votante.email,
            "celular": votante.celular,
            "fotografia": votante.fotografia,
            "password": votante.password,
        }
    return votante_dict