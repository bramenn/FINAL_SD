from Candidato.modelo import Candidato
import db

def obtener_candidatos_db():
    """
    Obtener todos los votantes
    query:
        select * from candidato;
    """
    candidato = db.session.query(Candidato).all()
    return candidato

def obtener_candidato_por_cedula(cedula:str):
    candidato = db.session.query(Candidato).where(Candidato.cedula==cedula).first()

    if not candidato:
        return None

    votante_dict = {
            "cedula": candidato.cedula,
            "nombre": candidato.nombre,
            "apellidos": candidato.apellidos,
            "email": candidato.email,
            "celular": candidato.celular,
            "fotografia": candidato.fotografia,
        }
    return candidato_dict