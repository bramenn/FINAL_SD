from datetime import datetime
from typing import Any, Dict
from fastapi import FastAPI, APIRouter
from Candidato.consultas import obtener_candidato_por_id
from Eleccion.consultas import obtener_eleccion_por_fecha
from Voto.consultas import (
    crear_voto_query,
    obtener_resultados_eleccion,
    obtener_votos_por_cedula_votante,
)

from Voto.modelo import Voto_apoyo

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear


@router.get("/obtener_votos_votante/{cedula}", response_model=Dict[str, Any])
def obtener_votos_votante(cedula: str):
    """Esta ruta obtiene los votos generados de un votante"""
    votos = obtener_votos_por_cedula_votante(cedula)

    if not votos:
        return {"result": "No hay votos para este votante {cedula}"}

    diccionario_votos = {}
    for voto in votos:
        candidato = obtener_candidato_por_id(voto.id_candidato)
        eleccion = obtener_eleccion_por_fecha(datetime.strftime(voto.fecha_eleccion, "%d-%m-%Y"))
        votante_item = {
            "cedula_votante": voto.cedula_votante,
            "eleccion": eleccion,
            "candidato": candidato,
        }

        diccionario_votos[voto.id] = votante_item

    return diccionario_votos


@router.get("/obtener_voto_candidato/{cedula}", response_model=Dict[str, Any])
def obtener_voto_candidato(cedula: str):
    """Esta ruta obtiene los votos recibidos de un candidato"""
    voto = {"cedula_votante": "", "cedula_candidato": "", "fecha_eleccion": ""}
    return voto


@router.get("/obtener_voto_fecha/{fecha}", response_model=Dict[str, Any])
def obtener_voto_fecha(fecha: str):
    """Esta ruta obtiene los votos generados un una fecha determinada"""
    voto = {"cedula_votante": "", "cedula_candidato": "", "fecha_eleccion": ""}
    return voto


@router.get("/obtener_resultados_fecha/{fecha}", response_model=Dict[str, Any])
def obtener_resultados_fecha(fecha: str):
    """Esta ruta obtiene los votos generados un una fecha determinada"""
    result = obtener_resultados_eleccion(fecha)
    return {f"result": result}


@router.post("/crear_voto", response_model=Dict[str, Any])
def crear_voto(voto: Voto_apoyo):
    """Esta ruta crea un voto"""
    result = crear_voto_query(voto)

    return {"result": result}
