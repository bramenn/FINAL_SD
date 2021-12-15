from PartidoPolitico.modelo import PartidoPolitico, PartidoPolitico_apoyo
import db


def obtener_partidos_politicos_db():
    """
    Obtener todos los partidos politicos
    query:
        select * from partido_politico;
    """
    partido_politico = db.session.query(PartidoPolitico).all()
    return partido_politico

def obtener_partidos_politicos_ascendente_db():
    """se obtienen los partidos politicos ordenados descendentemente por nombre"""
    partido_politico = db.session.query(PartidoPolitico).order_by(PartidoPolitico.nombre.asc()).all()
    return partido_politico


def obtener_partido_politico_por_nit(nit: str):
    """se obtiene un partido politico por nit"""
    partido_politico = (
        db.session.query(PartidoPolitico).where(PartidoPolitico.nit == nit).first()
    )

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


def crear_partido_politico_query(partido_politico: PartidoPolitico_apoyo):
    """se crea un partido politico"""
    if not obtener_partido_politico_por_nit(partido_politico.nit):
        # se crea la variable partido_politico_db basados en el modelo PartidoPolitico
        partido_politico_db = PartidoPolitico(
            nit=partido_politico.nit,
            nombre=partido_politico.nombre,
            direccion=partido_politico.direccion,
            foto_oficial=partido_politico.foto_oficial,
            telefono=partido_politico.telefono,
        )

        try:  # Si la insercion sale bien nos dice "El partido_politico se ha creado"
            db.session.add(partido_politico_db)
            db.session.commit()
            return {"result":"El partido_politico se ha creado"}
        except:  # Si no sale bien nos dice "No se ha creado el partido_politico"
            return "No se ha creado el partido_politico"
    else:
        return {"result": f"El partido con {partido_politico.nit} ya existe"}

def eliminar_partido_politico_query(nit: str):
    """se elimina un partido politico filtrado por nit"""
    if obtener_partido_politico_por_nit(nit):
        try:
            db.session.query(PartidoPolitico).filter(
                PartidoPolitico.nit == nit
            ).delete()
            db.session.commit()
            return {"result": f"Eliminación del partido_politico {nit} correcta"}
        except:
            return {"result": f"Eliminación del partido_politico {nit} incorrecta ya que contiene candidatos registrados"}
    else:
        return {"result": f"El nit {nit} no existe"}

def actualizar_partido_politico_query(partido_politico: PartidoPolitico_apoyo):

    # Obtenemos el partido_politico
    partido_politico_db = obtener_partido_politico_por_nit(partido_politico.nit)

    if not partido_politico_db:
        return f"El partido_politico {partido_politico.nit} no existe y no se puede actualizar."


    # partido_politico_db["nit"] = partido_politico.nit
    partido_politico_db["nombre"] = partido_politico.nombre
    partido_politico_db["direccion"] = partido_politico.direccion
    partido_politico_db["foto_oficial"] = partido_politico.foto_oficial
    partido_politico_db["telefono"] = partido_politico.telefono

    try:
        db.session.query(PartidoPolitico).update(partido_politico_db)
        db.session.commit()
        return f"El partido_politico {partido_politico.nit} fue correctamente actualizado."
    except:
        return f"El partido_politico {partido_politico.nit} no fue actualizado por un error."

