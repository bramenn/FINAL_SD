from sqlalchemy.sql.sqltypes import Boolean
from Candidato.modelo import Candidato, Candidato_apoyo
from PartidoPolitico.consultas import *
from Eleccion.consultas import *
import db


def obtener_candidatos_db():
    """
    Obtener todos los candidatos
    query:
        select * from candidato;
    """
    candidato = db.session.query(Candidato).all()
    return candidato


def obtener_candidato_por_cedula(cedula: str):
    """se obtiene un candidato con el numero de la cedula"""
    candidato = db.session.query(Candidato).where(Candidato.cedula == cedula).first()

    if not candidato:
        return None

    candidato_dict = {
        "cedula": candidato.cedula,
        "nombre": candidato.nombre,
        "apellidos": candidato.apellidos,
        "email": candidato.email,
        "celular": candidato.celular,
        "fotografia": candidato.fotografia,
        "nit_partido_politico": candidato.nit_partido_politico,
        "codigo_eleccion": candidato.codigo_eleccion,
    }
    return candidato_dict


def obtener_candidato_por_codigo_eleccion(codigo_eleccion: str):  # TODO CORREGIR A PLURAL
    """se obtiene un candidato con el numero de la codigo_eleccion"""
    candidatos = (
        db.session.query(Candidato).where(Candidato.codigo_eleccion == codigo_eleccion).all()
    )

    if not candidatos:
        return None

    return candidatos


def obtener_candidatos_por_fecha_query(fecha_eleccion: str):
    eleccion = obtener_eleccion_por_fecha(fecha_eleccion)

    if not eleccion:
        return None

    candidatos = (
        db.session.query(Candidato).where(Candidato.codigo_eleccion == eleccion.codigo)
    ).all()

    if not candidatos:
        return None


    return candidatos


def candidado_ya_existe_en_eleccion(cedula: str, codigo_eleccion: str, aux: Boolean = False):
    """Verifica si un candidato x ya existe e una eleccion y"""
    candidato = (
        db.session.query(Candidato)
        .where(Candidato.cedula == cedula)
        .where(Candidato.codigo_eleccion == codigo_eleccion)
    ).first()

    if not candidato:
        return False

    candidato_dict = {
        "id_candidato": candidato.id_candidato,
        "cedula": candidato.cedula,
        "nombre": candidato.nombre,
        "apellidos": candidato.apellidos,
        "email": candidato.email,
        "celular": candidato.celular,
        "fotografia": candidato.fotografia,
        "nit_partido_politico": candidato.nit_partido_politico,
        "codigo_eleccion": candidato.codigo_eleccion,
    }

    if aux:
        return candidato_dict

    return True


def crear_candidato_query(candidato: Candidato_apoyo):
    """se crea un candidato"""
    response_candidato_eleccion = candidado_ya_existe_en_eleccion(
        candidato.cedula, candidato.codigo_eleccion
    )
    if not response_candidato_eleccion:
        # se crea la variable candidato_bd basados en el modelo candidato
        candidato_bd = Candidato(
            cedula=candidato.cedula,
            nombre=candidato.nombre,
            apellidos=candidato.apellidos,
            email=candidato.email,
            celular=candidato.celular,
            fotografia=candidato.fotografia,
            nit_partido_politico=candidato.nit_partido_politico,
            codigo_eleccion=candidato.codigo_eleccion,
        )

        try:  # Si la insercion sale bien nos dice "El candidato se ha creado"
            db.session.add(candidato_bd)
            db.session.commit()
            return "El candidato se ha creado"
        except:  # Si no sale bien nos dice "No se ha creado el candidato"
            return "No se ha creado el candidato"
    else:
        return f"El candidato con {candidato.cedula} ya existe para esa eleccion {candidato.codigo_eleccion}"


def eliminar_candidato_query(cedula: str):
    """se elimina un candidato con el numero de la cedula"""
    if obtener_candidato_por_cedula(cedula):
        try:
            db.session.query(Candidato).filter(Candidato.cedula == cedula).delete()
            db.session.commit()
            return {"result": f"Eliminación del candidato {cedula} correcta"}
        except:
            return {"result": f"Eliminación del candidato {cedula} incorrecta"}
    else:
        return {"result": f"La cedula {cedula} no existe"}


def actualizar_candidato_query(candidato: Candidato_apoyo):

    # Obtenemos el candidato
    candidato_db = obtener_candidato_por_cedula(candidato.cedula)
    partido_politico_db = obtener_partido_politico_por_nit(candidato.nit_partido_politico)
    eleccion_db = obtener_eleccion_por_codigo(candidato.codigo_eleccion)

    if not candidato_db:
        return f"El candidato {candidato.cedula} no existe y no se puede actualizar."

    if not partido_politico_db:
        return f"El partido politico {candidato.nit_partido_politico} no existe y no se puede actualizar."

    if not eleccion_db:
        return f"La eleccion {candidato.codigo_eleccion} no existe y no se puede actualizar."

    # candidato_db["cedula"] = candidato.cedula
    candidato_db["nombre"] = candidato.nombre
    candidato_db["apellidos"] = candidato.apellidos
    candidato_db["email"] = candidato.email
    candidato_db["celular"] = candidato.celular
    candidato_db["fotografia"] = candidato.fotografia
    candidato_db["nit_partido_politico"] = candidato.nit_partido_politico
    candidato_db["codigo_eleccion"] = candidato.codigo_eleccion

    try:
        db.session.query(Candidato).update(candidato_db)
        db.session.commit()
        return f"El candidato {candidato.cedula} fue correctamente actualizado."
    except:
        return f"El candidato {candidato.cedula} no fue actualizado por un error."
