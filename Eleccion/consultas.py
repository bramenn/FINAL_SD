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
        "fecha_inicio": eleccion.hora_inicio,
        "fecha_fin": eleccion.hora_fin,
        "nombre": eleccion.nombre,
        "descripcion": eleccion.descripcion,
    }
    return eleccion_dict


def crear_eleccion_query(eleccion: Eleccion_apoyo):

    # ponemos la fecha eleccion en el formato esperado por la bd
    eleccion_fecha = datetime.strptime(eleccion.fecha_eleccion, "%d-%m-%Y")

    # Verificamos que la eleecion no exista
    eleccion_en_db = obtener_eleccion_por_fecha(eleccion.fecha_eleccion)
    print(eleccion_en_db)
    if not eleccion_en_db:
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
                return {"result": "La eleccion se ha creado"}
            except error:  # Si no sale bien nos dice "No se ha creado el votante"
                return {"result": "La eleccion no se ha creado {error}"}
        else:
            return {"result": "La eleccion no se ha creado, porque envio una hora invalida"}
    else:
        return {"result": f"La eleccion con fecha {eleccion_fecha}  ya existe"}
