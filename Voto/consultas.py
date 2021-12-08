from Voto.modelo import Voto
import db

def obtener_votos_db():
    """
    Obtener todos los votos
    query:
        select * from voto;
    """
    voto = db.session.query(Voto).all()
    return voto

def obtener_votos_por_cedula_candidato(cedula_candidato:str):
    votos = db.session.query(Voto).where(Voto.cedula_candidato==cedula_candidato)

    if not votos:
        return None

    return votos

def obtener_votos_por_cedula_votante(cedula_votante:str):
    votos = db.session.query(Voto).where(Voto.cedula_votante==cedula_votante)

    if not votos:
        return None

    return votos

# TERMINAR FECHA ELECCION COMO TIMESTAMP -- UTILIZANDO LA LIBRERIA DATETIME Y DATETIME.TIMESTAMP
def obtener_votos_por_fecha_eleccion(fecha_eleccion:str):
    votos = db.session.query(Voto).where(Voto.fecha_eleccion==fecha_eleccion)

    if not votos:
        return None

    return votos