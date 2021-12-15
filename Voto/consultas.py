from datetime import datetime
from Candidato.consultas import candidado_ya_existe_en_eleccion, obtener_candidato_por_cedula
from Eleccion.consultas import obtener_eleccion_por_fecha
from Votante.consultas import obtener_votante_por_cedula
from Votante.modelo import Votante_apoyo
from Voto.modelo import Voto
import db


def obtener_votos_db():
    """
    Obtener todos los votos
    query:
        select * from voto;
    """
    voto = db.session.query(Voto).all()
    return voto


def obtener_votos_por_cedula_candidato(cedula_candidato: str):
    """Se obtienen todos los votos obtenidos de un candidato por su cedula"""
    votos = db.session.query(Voto).where(Voto.cedula_candidato == cedula_candidato)

    if not votos:
        return None

    return votos


def obtener_votos_por_cedula_votante(cedula_votante: str):
    """Se obtienen todos los votos generados de un votante por su cedula"""
    votos = db.session.query(Voto).where(Voto.cedula_votante == cedula_votante)

    if not votos:
        return None

    return votos


# TERMINAR FECHA ELECCION COMO TIMESTAMP -- UTILIZANDO LA LIBRERIA DATETIME Y DATETIME.TIMESTAMP
def obtener_votos_por_fecha_eleccion(fecha_eleccion: str):
    """se obtienen todos los votos de una eleccion por fecha"""
    votos = db.session.query(Voto).where(Voto.fecha_eleccion == fecha_eleccion)

    if not votos:
        return None

    return votos


def crear_voto_query(voto: Votante_apoyo):

    # Volvemos la fecha en el format apropido
    eleccion_fecha = datetime.strptime(voto.fecha_eleccion, "%d-%m-%Y")
    # Buscamos si la eleccion existe
    eleccion = obtener_eleccion_por_fecha(voto.fecha_eleccion)
    if not eleccion:
        return f"La eleccion del {voto.fecha_eleccion} no existe"

    # Buscamos si el candidato existe para la elecion
    candidato = candidado_ya_existe_en_eleccion(voto.cedula_candidato, eleccion.get("codigo"), True)

    if not candidato:
        return f"El candidato {voto.cedula_candidato} de la eleccion {eleccion.get('codigo')} no existe"

    # buscamos que el votante exista
    votante = obtener_votante_por_cedula(voto.cedula_votante)
    if not votante:
        return f"El votante {voto.cedula_votante} no existe"

    # Creamos el voto
    voto_db = Voto(
        fecha_eleccion=eleccion_fecha,
        cedula_votante=voto.cedula_votante,
        id_candidato=candidato.get("id_candidato"),
    )

    # Validar que la password enviada es correcta
    if voto.password == votante.get("password"):
        # TODO CREAR IF PARA EVITAR VARIAS VECES LOS VOTOS
        try:  # Si la insercion sale bien nos dice "El voto se ha creado"
            db.session.add(voto_db)
            db.session.commit()
            return "El voto fue registrado"
        except:  # Si no sale bien nos dice "No se ha creado el voto"
            return "No se ha creado el voto"
    else:
        return f"La contraseña no coincide"
