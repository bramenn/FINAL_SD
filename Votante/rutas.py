from typing import Any, Dict
from fastapi import FastAPI, APIRouter

from Votante.modelo import Votante_apoyo

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear
# PUT -> Actualizar
# DELETE -> Borrar

@router.get("/obtener_votante/{cedula}", response_model=Dict[str, Any])
def obtener_votante(cedula:str):
    """
    Esta es la ruta para obtener un votante

        votante

    """
    votante = {
        "cedula": "1225093110",
        "nombre": "Brayan Alejandro",
        "apellidos": "Herrera Amariles",
        "e-mail": "brayan.herrera@utp.edu.co",
        "telefono": "3058790290",
        "fotografia": "imagen.jpeg",
        "clave": "asdhashdi"
    }
    return votante

@router.post("/crear_votante", response_model=Dict[str, Any])
def crear_votante(votante: Votante_apoyo):
    print(
        f"cedula: {votante.cedula} \n"
        f"nombre: {votante.nombre} \n"
        f"apellidos: {votante.apellidos} \n"
        f"email: {votante.email} \n"
        f"celular: {votante.celular} \n"
        f"fotografia: {votante.fotografia} \n"
    )

    return {}

@router.put("/actualizar_votante", )
def actualizar_votante(votante: Votante_apoyo):
    print(
        f"cedula: {votante.cedula} \n"
        f"nombre: {votante.nombre} \n"
        f"apellidos: {votante.apellidos} \n"
        f"email: {votante.email} \n"
        f"celular: {votante.celular} \n"
        f"fotografia: {votante.fotografia} \n"
    )

    return {}

@router.delete("/eliminar_votante/{cedula}")
def eliminar_votante(cedula:str):

    mensaje = f"Se elimino el votante con cedula: {cedula}"

    return {"mensaje":mensaje}