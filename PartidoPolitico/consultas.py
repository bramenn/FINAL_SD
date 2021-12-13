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


def obtener_partido_politico_por_nit(nit: str):
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
    if not obtener_partido_politico_por_nit(partido_politico.nit):
        # se crea la variable partido_politico_db basados en el modelo PartidoPolitico
        print(partido_politico.nit)
        print(partido_politico.nombre)
        print(partido_politico.direccion)
        print(partido_politico.foto_oficial)
        print(partido_politico.telefono)
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
    if obtener_partido_politico_por_nit(nit):
        try:
            db.session.query(PartidoPolitico).filter(
                PartidoPolitico.nit == nit
            ).delete()
            db.session.commit()
            return {"result": f"Eliminación del partido_politico {nit} correcta"}
        except:
            return {"result": f"Eliminación del partido_politico {nit} incorrecta"}
    else:
        return {"result": f"El nit {nit} no existe"}
