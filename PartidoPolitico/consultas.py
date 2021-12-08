from PartidoPolitico.modelo import PartidoPolitico
import db

def obtener_partidos_politicos_db():
    """
    Obtener todos los partidos politicos
    query:
        select * from partido_politico;
    """
    partido_politico = db.session.query(PartidoPolitico).all()
    return partido_politico

def obtener_partido_politico_por_nit(nit:str):
    partido_politico = db.session.query(PartidoPolitico).where(PartidoPolitico.nit==nit).first()

    if not partido_politico:
        return None

    partido_politico_dict = {
            "nit": partido_politico.nit,
            "nombre": partido_politico.nombre,
            "direccion": partido_politico.direccion,
            "foto_oficial": partido_politico.foto_oficial,
            "telefono": partido_politico.telefono,
        }
    return partido_politico_dict