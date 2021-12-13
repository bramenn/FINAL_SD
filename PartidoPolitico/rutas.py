from typing import Any, Dict
from fastapi import FastAPI, APIRouter

from PartidoPolitico.modelo import PartidoPolitico_apoyo
from PartidoPolitico.consultas import *

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear
# PUT -> Actualizar
# DELETE -> Borrar


@router.get("/obtener_partidos_politicos", response_model=Dict[str, Any])
"""se crea la ruta para obtener todos los partidos politicos """
def obtener_partidos_politicos():
    partidos_politicos = obtener_partidos_politicos_db()
    diccionario_partidos_politicos = {}
    for partido_politico in partidos_politicos:
        partido_politico_item = {
            "nombre": partido_politico.nombre,
            "direccion": partido_politico.direccion,
            "foto_oficial": partido_politico.foto_oficial,
            "telefono": partido_politico.telefono,
        }

        diccionario_partidos_politicos[partido_politico.nit] = partido_politico_item

    return diccionario_partidos_politicos

@router.get("/obtener_partidos_politicos_descendente", response_model=Dict[str, Any])
def obtener_partidos_politicos_descendente():
    partidos_politicos = obtener_partidos_politicos_descendente_db()
    diccionario_partidos_politicos = {}
    for partido_politico in partidos_politicos:
        partido_politico_item = {
            "nit": partido_politico.nit,
            "direccion": partido_politico.direccion,
            "foto_oficial": partido_politico.foto_oficial,
            "telefono": partido_politico.telefono,
        }

        diccionario_partidos_politicos[partido_politico.nombre] = partido_politico_item

    return diccionario_partidos_politicos



@router.get("/obtener_partido_politico/{nit}", response_model=Dict[str, Any])
def obtener_partido_politico(nit: str):
    """
    Esta es la ruta para obtener un partido_politico

        partido_politico

    """

    partido_politico = obtener_partido_politico_por_nit(nit=nit)
    return partido_politico


@router.post("/crear_partido_politico", response_model=Dict[str, Any])
def crear_partido_politico(partido_politico: PartidoPolitico_apoyo):

    # Llamamos una funcion para crear un partido politico
    result = crear_partido_politico_query(partido_politico)

    return result


@router.put(
    "/actualizar_partido_politico",
)
def actualizar_partido_politico(partido_politico: PartidoPolitico_apoyo):
    print(
        f"nit: {partido_politico.nit} \n"
        f"nombre: {partido_politico.nombre} \n"
        f"direccion: {partido_politico.direccion} \n"
        f"foto_oficial: {partido_politico.foto_oficial} \n"
        f"telefono: {partido_politico.telefono} \n"
    )

    return {}


@router.delete("/eliminar_partido_politico/{nit}")
def eliminar_partido_politico(nit: str):

    msg = eliminar_partido_politico_query(nit)

    return msg
