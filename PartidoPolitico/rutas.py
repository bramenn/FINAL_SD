from typing import Any, Dict
from fastapi import FastAPI, APIRouter

from PartidoPolitico.modelo import PartidoPolitico_apoyo

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear
# PUT -> Actualizar
# DELETE -> Borrar

@router.get("/obtener_partido_politico/{NIT}", response_model=Dict[str, Any])
def obtener_partido_politico(NIT:str):
    partido_politico = {
        "NIT": "",
        "nombre": "",
        "direccion": " ",
        "foto_oficial": "imagen.jpeg",
        "telefono": "3057890290"
    }
    return partido_politico

@router.post("/crear_partido_politico", response_model=Dict[str, Any])
def crear_partido_politico (partido_politico: PartidoPolitico_apoyo):
    print(
        f"NIT: {partido_politico.NIT} \n"
        f"nombre: {partido_politico.nombre} \n"
        f"direccion: {partido_politico.direccion} \n"
        f"foto_oficial: {partido_politico.foto_oficial} \n"
        f"telefono: {partido_politico.telefono} \n"
    )

    return {}

@router.put("/actualizar_partido_politico", )
def actualizar_partido_politico(partido_politico: PartidoPolitico_apoyo):
    print(
        f"NIT: {partido_politico.NIT} \n"
        f"nombre: {partido_politico.nombre} \n"
        f"direccion: {partido_politico.direccion} \n"
        f"foto_oficial: {partido_politico.foto_oficial} \n"
        f"telefono: {partido_politico.telefono} \n"
    )

    return {}

@router.delete("/eliminar_partido_politico/{NIT}")
def eliminar_partido_politico(NIT:str):

    mensaje = f"Se elimino el partido_politico con NIT: {NIT}"

    return {"mensaje":mensaje}