from typing import Any, Dict
from fastapi import FastAPI, APIRouter

from Eleccion.modelo import Eleccion_apoyo

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear

@router.get("/obtener_eleccion/{fecha}", response_model=Dict[str, Any])
def obtener_eleccion(fecha:str):
    eleccion = {
        "codigo": "",
        "fecha": "",
        "hora_inicio": "",
        "hora_fin": "",
        "nombre": "",
        "descripcion": "",
    }
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