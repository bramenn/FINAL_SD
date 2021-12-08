from Eleccion.modelo import Eleccion
import db

def obtener_elecciones_db():
    """
    Obtener todas las eleciones
    query:
        select * from eleccion;
    """
    eleccion = db.session.query(Eleccion).all()
    return eleccion

def obtener_eleccion_por_codigo(codigo:str):
    eleccion = db.session.query(Eleccion).where(Eleccion.codigo==codigo).first()

    if not eleccion:
        return None

    eleccion_dict = {
            "codigo": eleccion.codigo,
            "fecha": eleccion.fecha,
            "hora_inicio": eleccion.hora_inicio,
            "hora_fin": eleccion.hora_fin,
            "nombre": eleccion.nombre,
            "descripcion": eleccion.descripcion,
        }
    return eleccion_dict
