from typing import Any, Dict
from fastapi import FastAPI, APIRouter

from Candidato.modelo import Candidato_apoyo
from Candidato.consultas import *

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear
# PUT -> Actualizar
# DELETE -> Borrar


@router.get("/obtener_candidatos", response_model=Dict[str, Any])
def obtener_candidatos():
    """Esta ruta obtiene todos los candidatos registrados"""
    candidatos = obtener_candidatos_db()
    diccionario_candidatos = {}
    for candidato in candidatos:
        candidato_item = {
            "nombre": candidato.nombre,
            "apellidos": candidato.apellidos,
            "celular": candidato.celular,
            "email": candidato.email,
            "fotografia": candidato.fotografia,
            "nit_partido_politico": candidato.nit_partido_politico,
            "codigo_eleccion": candidato.codigo_eleccion,
        }

        diccionario_candidatos[candidato.cedula] = candidato_item

    return diccionario_candidatos


@router.get("/obtener_candidato/{cedula}", response_model=Dict[str, Any])
def obtener_candidato(cedula: str):
    """ Esta es la ruta obtiene un candidato con el numero de la cedula"""

    candidato = obtener_candidato_por_cedula(cedula=cedula)
    return candidato


@router.post("/crear_candidato", response_model=Dict[str, Any])
def crear_candidato(candidato: Candidato_apoyo):
    """Esta ruta crea un candidato"""

    # Llamamos una funcion para crear un candidato
    result = crear_candidato_query(candidato)

    return {"result": result}


@router.put(
    "/actualizar_candidato",
)
def actualizar_candidato(candidato: Candidato_apoyo):
    print(
        f"cedula: {candidato.cedula} \n"
        f"nombre: {candidato.nombre} \n"
        f"apellidos: {candidato.apellidos} \n"
        f"celular: {candidato.celular} \n"
        f"email: {candidato.email} \n"
        f"fotografia: {candidato.fotografia} \n"
    )

    return {}


@router.delete("/eliminar_candidato/{cedula}")
def eliminar_candidato(cedula: str):
    """Esta ruta elimina un candidato con el numero de la cedula"""
    msg = eliminar_candidato_query(cedula)

    return msg
