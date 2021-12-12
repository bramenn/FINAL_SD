from datetime import datetime
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


def obtener_eleccion_por_fecha(fecha: int):
    fecha_fin = fecha + 86399
    try:
        eleccion = (
            db.session.query(Eleccion)
            .where(Eleccion.fecha_inicio >= fecha)
            .where(Eleccion.fecha_inicio <= fecha_fin)
        ).first()
    except:
        return {"result":"No se encontro ninguna eleccion para esta fecha"}

    if not eleccion:
        return {"result":"No se encontro ninguna eleccion para esta fecha"}

    eleccion_dict = {
        "codigo": eleccion.codigo,
        "fecha_inicio": datetime.fromtimestamp(eleccion.fecha_inicio),
        "fecha_fin": datetime.fromtimestamp(eleccion.fecha_fin),
        "nombre": eleccion.nombre,
        "descripcion": eleccion.descripcion,
    }
    return eleccion_dict
