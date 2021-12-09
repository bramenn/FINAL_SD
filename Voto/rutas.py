from typing import Any, Dict
from fastapi import FastAPI, APIRouter

from Voto.modelo import Voto_apoyo

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear


@router.get("/obtener_voto_votante/{cedula}", response_model=Dict[str, Any])
def obtener_voto_votante(cedula: str):
    voto = {"cedula_votante": "", "cedula_candidato": "", "fecha_eleccion": ""}
    return voto


@router.get("/obtener_voto_candidato/{cedula}", response_model=Dict[str, Any])
def obtener_voto_candidato(cedula: str):
    voto = {"cedula_votante": "", "cedula_candidato": "", "fecha_eleccion": ""}
    return voto


@router.get("/obtener_voto_fecha/{fecha}", response_model=Dict[str, Any])
def obtener_voto_fecha(fecha: str):
    voto = {"cedula_votante": "", "cedula_candidato": "", "fecha_eleccion": ""}
    return voto


@router.post("/crear_voto", response_model=Dict[str, Any])
def crear_voto(voto: Voto_apoyo):
    print(
        f"cedula_votante: {voto.cedula_votante} \n"
        f"cedula_candidato: {voto.cedula_candidato} \n"
        f"fecha_eleccion: {voto.fecha_eleccion} \n"
    )

    return {}
