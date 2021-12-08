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
    eleccion = (
        db.session.query(Eleccion)
        .filter(Eleccion.fecha_inicio >= fecha)
        .filter(Eleccion.fecha_inicio <= fecha_fin)
    )

    if not eleccion:
        return None

    eleccion_dict = {
        "codigo": eleccion.codigo,
        "fecha_inicio": eleccion.fecha_inicio,
        "fecha_fin": eleccion.fecha_fin,
        "nombre": eleccion.nombre,
        "descripcion": eleccion.descripcion,
    }
    return eleccion_dict
