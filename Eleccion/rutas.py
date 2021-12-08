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
    elecciones = obtener_elecciones_db()

    # CONVERTIMOS LA FECHAS GUARDADAS EN FECHAS HUMANAS

    diccionario_elecciones = {}
    for eleccion in elecciones:
        eleccion.fecha_inicio = datetime.fromtimestamp(eleccion.fecha_inicio)
        eleccion.fecha_fin = datetime.fromtimestamp(eleccion.fecha_fin)
        eleccion_item = {
            "fecha_inicio": eleccion.fecha_inicio,
            "fecha_fin": eleccion.fecha_fin,
            "nombre": eleccion.nombre,
            "descripcion": eleccion.descripcion,
        }

        diccionario_elecciones[eleccion.codigo] = eleccion_item

    return diccionario_elecciones

# NO ANDA
@router.get("/obtener_eleccion/{fecha}", response_model=Dict[str, Any])
def obtener_eleccion(fecha: str):
    # date_time = datetime.strptime(fecha, "%d/%m/%Y %H:%M:%S")
    # Formateamos la fecha entrante en dia/mes/año
    date_time = datetime.strptime(fecha, "%d-%m-%Y")
    # Convertimos la fecha en timestamp
    fecha = datetime.timestamp(date_time)
    eleccion = obtener_eleccion_por_fecha(fecha)
    return eleccion


@router.post("/crear_eleccion", response_model=Dict[str, Any])
def crear_eleccion(eleccion: Eleccion_apoyo):
    print(
        f"codigo: {eleccion.codigo} \n"
        f"fecha: {eleccion.fecha} \n"
        f"hora_inicio: {eleccion.hora_inicio} \n"
        f"hora_fin: {eleccion.hora_fin} \n"
        f"nombre: {eleccion.nombre} \n"
        f"descripcion: {eleccion.descripcion} \n"
    )

    return {}
