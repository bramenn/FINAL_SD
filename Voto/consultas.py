from datetime import datetime
from Candidato.consultas import candidado_ya_existe_en_eleccion, obtener_candidato_por_cedula, obtener_candidato_por_codigo_eleccion
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
    votos = db.session.query(Voto).where(Voto.cedula_candidato == cedula_candidato).first()

    if not votos:
        return None

    return votos


def obtener_votos_por_cedula_votante(cedula_votante: str):
    """Se obtienen todos los votos generados de un votante por su cedula"""
    votos = db.session.query(Voto).where(Voto.cedula_votante == cedula_votante).first()

    if not votos:
        return None

    return votos


# TERMINAR FECHA ELECCION COMO TIMESTAMP -- UTILIZANDO LA LIBRERIA DATETIME Y DATETIME.TIMESTAMP
def obtener_votos_por_fecha_eleccion(fecha_eleccion: str):
    """se obtienen todos los votos de una eleccion por fecha"""
    votos = db.session.query(Voto).where(Voto.fecha_eleccion == fecha_eleccion).first()

    if not votos:
        return None

    return votos


def obtener_voto(fecha_eleccion: str, cedula_votante: str, id_candidato: str):
    """se obtienen todos los votos de una eleccion por fecha"""

    voto = (
        db.session.query(Voto)
        .where(Voto.fecha_eleccion == fecha_eleccion)
        .where(Voto.cedula_votante == cedula_votante)
        .where(Voto.id_candidato == id_candidato)
    ).first()

    if not voto:
        return None

    return voto

def obtener_numero_de_votos(id_candidato: str, fecha_eleccion: str):
    eleccion_fecha = datetime.strptime(fecha_eleccion, "%d-%m-%Y")
    votos = (
        db.session.query(Voto)
        .where(Voto.fecha_eleccion == eleccion_fecha)
        .where(Voto.id_candidato == id_candidato)
    ).all()

    numero_de_votos = len(votos)

    return numero_de_votos


def obtener_resultados_eleccion(fecha_eleccion: str):
    votos = obtener_votos_por_fecha_eleccion(fecha_eleccion)

    if not votos:
        return f"Para esta fecha {fecha_eleccion} no hay votaciones"

    eleccion = obtener_eleccion_por_fecha(fecha_eleccion)
    candidatos = obtener_candidato_por_codigo_eleccion(eleccion.get("codigo"))

    candidatos_dict = {}

    for candidato in candidatos:
        numero_votos = obtener_numero_de_votos(candidato.id_candidato, fecha_eleccion)
        candidato_item = {
            "nombre": candidato.nombre,
            "apellidos": candidato.apellidos,
            "celular": candidato.celular,
            "email": candidato.email,
            "fotografia": candidato.fotografia,
            "nit_partido_politico": candidato.nit_partido_politico,
            "codigo_eleccion": candidato.codigo_eleccion,
            "numero de votos": numero_votos
        }

        candidatos_dict[candidato.cedula] = candidato_item


    resultados = {
        "codigo_eleccion": eleccion.get("codigo"),
        "fecha_eleccion": eleccion.get("fecha_eleccion"),
        "nombre_eleccion": eleccion.get("nombre"),
        "descripcion_eleccion": eleccion.get("descripcion"),
        "resultados_candidatos": candidatos_dict
    }

    return resultados



def crear_voto_query(voto: Votante_apoyo):

    # Volvemos la fecha en el format apropido
    eleccion_fecha = datetime.strptime(voto.fecha_eleccion, "%d-%m-%Y")
    # Buscamos si la eleccion existe
    eleccion = obtener_eleccion_por_fecha(voto.fecha_eleccion)
    if not eleccion:
        return f"La eleccion del {voto.fecha_eleccion} no existe"

    if not (
        eleccion.get("fecha_eleccion").date() == datetime.now().date()
        and eleccion.get("hora_inicio") <= datetime.now().hour <= eleccion.get("hora_fin")
    ):
        return f"La eleccion no esta abierta."

    # Buscamos si el candidato existe para la elecion
    candidato = candidado_ya_existe_en_eleccion(
        voto.cedula_candidato, eleccion.get("codigo"), True
    )

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

    voto_existe = obtener_voto(eleccion_fecha, voto.cedula_votante, candidato.get("id_candidato"))

    if voto_existe:
        return f"El voto hecho por el votante {voto.cedula_votante} ya existe"

    # Validar que la password enviada es correcta
    if voto.password == votante.get("password"):
        try:  # Si la insercion sale bien nos dice "El voto se ha creado"
            db.session.add(voto_db)
            db.session.commit()
            return "El voto fue registrado"
        except:  # Si no sale bien nos dice "No se ha creado el voto"
            return "No se ha creado el voto"
    else:
        return f"La contraseña no coincide"
