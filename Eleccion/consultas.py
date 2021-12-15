from datetime import datetime
from os import error
from Eleccion.modelo import Eleccion, Eleccion_apoyo
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


def obtener_elecciones_db_fecha_descendente():
    """
    Obtener todas las eleciones
    query:
        select * from eleccion;
    """
    eleccions = db.session.query(Eleccion).order_by(Eleccion.fecha_eleccion.desc()).all()
    if not eleccions:
        return None
    return eleccions


def obtener_eleccion_por_fecha(fecha: str):
    """Se obtiene una eleccion por fecha"""
    eleccion_fecha = datetime.strptime(fecha, "%d-%m-%Y")
    try:
        eleccion = (
            db.session.query(Eleccion).where(Eleccion.fecha_eleccion == eleccion_fecha)
        ).first()
    except:
        return {"result": "Error buscando eleccion"}

    if not eleccion:
        return None

    eleccion_dict = {
        "codigo": eleccion.codigo,
        "fecha_eleccion": eleccion.fecha_eleccion,
        "hora_inicio": eleccion.hora_inicio,
        "hora_fin": eleccion.hora_fin,
        "nombre": eleccion.nombre,
        "descripcion": eleccion.descripcion,
    }
    return eleccion_dict


def obtener_eleccion_por_codigo(codigo: str):
    """Se obtiene una eleccion por codigo"""
    try:
        eleccion = (db.session.query(Eleccion).where(Eleccion.codigo == codigo)).first()
    except:
        return {"result": "Error buscando eleccion"}

    if not eleccion:
        return None

    eleccion_dict = {
        "codigo": eleccion.codigo,
        "fecha_eleccion": eleccion.fecha_eleccion,
        "hora_inicio": eleccion.hora_inicio,
        "hora_fin": eleccion.hora_fin,
        "nombre": eleccion.nombre,
        "descripcion": eleccion.descripcion,
    }
    return eleccion_dict


def crear_eleccion_query(eleccion: Eleccion_apoyo):

    # ponemos la fecha eleccion en el formato esperado por la bd
    eleccion_fecha = datetime.strptime(eleccion.fecha_eleccion, "%d-%m-%Y")

    if not (eleccion_fecha.day > datetime.now().day - 1):
        return f"No se puede crear esta eleccion porque la fecha {eleccion.fecha_eleccion} ya paso"
    # Verificamos que la eleccion no exista
    eleccion_en_db_fecha = obtener_eleccion_por_fecha(eleccion.fecha_eleccion)
    eleccion_en_db_codigo = obtener_eleccion_por_codigo(eleccion.codigo)

    if not (eleccion_en_db_fecha or eleccion_en_db_codigo):
        # Condicion para que la hora no sea fuera del formato de 24h
        if 23 >= eleccion.hora_inicio >= 0 and 23 >= eleccion.hora_fin >= 0:
            eleccion_db = Eleccion(
                codigo=eleccion.codigo,
                fecha_eleccion=eleccion_fecha,
                hora_inicio=eleccion.hora_inicio,
                hora_fin=eleccion.hora_fin,
                nombre=eleccion.nombre,
                descripcion=eleccion.descripcion,
            )
            try:  # Si la insercion sale bien nos dice "El votante se ha creado"
                db.session.add(eleccion_db)
                db.session.commit()
                return "La eleccion se ha creado"
            except error:  # Si no sale bien nos dice "No se ha creado el votante"
                return "La eleccion no se ha creado {error}"
        else:
            return "La eleccion no se ha creado, porque envio una hora invalida"
    else:
        return f"La eleccion con fecha {eleccion_fecha} ó codigo {eleccion.codigo} ya existe"
