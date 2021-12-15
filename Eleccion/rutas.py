from datetime import datetime
from typing import Any, Dict
from fastapi import FastAPI, APIRouter

from Eleccion.modelo import Eleccion_apoyo
from Eleccion.consultas import *

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear


@router.get("/obtener_elecciones", response_model=Dict[str, Any])
def obtener_elecciones():
    """Esta ruta obtiene todas las elecciones"""
    elecciones = obtener_elecciones_db()
    if elecciones:
        diccionario_elecciones = {}
        for eleccion in elecciones:
            eleccion_item = {
                "fecha_eleccion": eleccion.fecha_eleccion,
                "fecha_inicio": eleccion.hora_inicio,
                "fecha_fin": eleccion.hora_fin,
                "nombre": eleccion.nombre,
                "descripcion": eleccion.descripcion,
            }

            diccionario_elecciones[eleccion.codigo] = eleccion_item

        return diccionario_elecciones
    return {"result": "No se encontraron elecciones"}

@router.get("/obtener_elecciones_descendente", response_model=Dict[str, Any])
def obtener_elecciones():
    """Esta ruta obtiene todas las elecciones"""
    elecciones = obtener_elecciones_db_fecha_descendente()
    if elecciones:
        diccionario_elecciones = {}
        for eleccion in elecciones:
            eleccion_item = {
                "fecha_eleccion": eleccion.fecha_eleccion,
                "fecha_inicio": eleccion.hora_inicio,
                "fecha_fin": eleccion.hora_fin,
                "nombre": eleccion.nombre,
                "descripcion": eleccion.descripcion,
            }

            diccionario_elecciones[eleccion.codigo] = eleccion_item

        return diccionario_elecciones
    return {"result": "No se encontraron elecciones"}


@router.get("/obtener_eleccion/{fecha}", response_model=Dict[str, Any])
def obtener_eleccion(fecha: str):
    """Esta ruta obtiene una elccion por fecha {"%d-%m-%Y"}"""
    eleccion = obtener_eleccion_por_fecha(fecha)
    return eleccion


@router.post("/crear_eleccion", response_model=Dict[str, Any])
def crear_eleccion(eleccion: Eleccion_apoyo):
    """Esta ruta crea una eleccion"""
    result = crear_eleccion_query(eleccion)
    return {"result": result}
