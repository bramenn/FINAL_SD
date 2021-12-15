from typing import Any, Dict
from fastapi import FastAPI, APIRouter
from Voto.consultas import crear_voto_query, obtener_resultados_eleccion

from Voto.modelo import Voto_apoyo

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear


@router.get("/obtener_voto_votante/{cedula}", response_model=Dict[str, Any])
def obtener_voto_votante(cedula: str):
    """Esta ruta obtiene los votos generados de un votante"""
    voto = {"cedula_votante": "", "cedula_candidato": "", "fecha_eleccion": ""}
    return voto


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

    return {"result":result}
