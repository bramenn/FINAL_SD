from datetime import datetime
from Eleccion.modelo import Eleccion
import db


def obtener_elecciones_db():
    """
    Obtener todas las eleciones
    query:
        select * from eleccion;
    """
    eleccions = db.session.query(Eleccion).all()
    if not eleccions:
        return None
    return eleccions


def obtener_eleccion_por_fecha(fecha: int):
    fecha_fin = fecha + 86399
    try:
        eleccion = (
            db.session.query(Eleccion)
            .where(Eleccion.fecha_inicio >= fecha)
            .where(Eleccion.fecha_inicio <= fecha_fin)
        ).first()
    except:
        return {"result":"Error buscando eleccion"}

    if not eleccion:
        return {"result":"No se encontro ninguna eleccion para esta fecha"}

    eleccion_dict = {
        "codigo": eleccion.codigo,
        "fecha_inicio": datetime.fromtimestamp(eleccion.fecha_inicio),
        "fecha_fin": datetime.fromtimestamp(eleccion.fecha_fin),
        "nombre": eleccion.nombre,
        "descripcion": eleccion.descripcion,
    }
    print(eleccion_dict)
    return eleccion_dict
