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
def obtener_partidos_politicos():
    """Esta ruta obtiene todos los partidos politicos """
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

@router.get("/obtener_partidos_politicos_ascendente", response_model=Dict[str, Any])
def obtener_partidos_politicos_ascendente():
    """Esta ruta obtiene todos los partidos politicos de forma ascendente"""
    partidos_politicos = obtener_partidos_politicos_ascendente_db()
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
    """Esta ruta obtiene un partido_politico por el numero del nit"""
    partido_politico = obtener_partido_politico_por_nit(nit=nit)
    return partido_politico


@router.post("/crear_partido_politico", response_model=Dict[str, Any])
def crear_partido_politico(partido_politico: PartidoPolitico_apoyo):
    """Esta ruta crea un partido politico"""

    # Llamamos una funcion para crear un partido politico
    result = crear_partido_politico_query(partido_politico)

    return result


@router.put("/actualizar_partido_politico",)
def actualizar_partido_politico(partido_politico: PartidoPolitico_apoyo):
    msg = actualizar_partido_politico_query(partido_politico)

    return {"result": msg}


@router.delete("/eliminar_partido_politico/{nit}")
def eliminar_partido_politico(nit: str):
    """Esta ruta elimina un parido politico por el numero del nit"""

    msg = eliminar_partido_politico_query(nit)

    return msg
