from typing import Any, Dict
from fastapi import FastAPI, APIRouter

from Votante.modelo import Votante_apoyo
from Votante.consultas import *

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear
# PUT -> Actualizar
# DELETE -> Borrar

# ok
@router.get("/obtener_votantes", response_model=Dict[str, Any])
def obtener_votantes():
    """se crea la ruta para obtener todos los votantes"""
    votantes = obtener_votantes_db()
    diccionario_votantes = {}
    for votante in votantes:
        votante_item = {
            "nombre": votante.nombre,
            "apellidos": votante.apellidos,
            "email": votante.email,
            "celular": votante.celular,
            "fotografia": votante.fotografia,
            "password": votante.password,
            "edad": votante.edad,
        }

        diccionario_votantes[votante.cedula] = votante_item

    return diccionario_votantes

@router.get("/obtener_votantes_mayores_18", response_model=Dict[str, Any])
def obtener_votantes_mayores_18():
    """se crea la ruta para obtener todos los votantes mayores a 18"""
    votantes = obtener_votantes_mayores_18_db()
    diccionario_votantes = {}
    for votante in votantes:
        votante_item = {
            "nombre": votante.nombre,
            "apellidos": votante.apellidos,
            "email": votante.email,
            "celular": votante.celular,
            "fotografia": votante.fotografia,
            "password": votante.password,
            "edad": votante.edad,
        }

        diccionario_votantes[votante.cedula] = votante_item

    return diccionario_votantes

@router.get("/obtener_votantes_entre_18_27", response_model=Dict[str, Any])
def obtener_votantes_entre_18_27():
    """se crea la ruta para obtener todos los votantes con edades entre 18 y 27"""
    votantes = obtener_votantes_entre_18_27_db()
    diccionario_votantes = {}
    if votantes:
        for votante in votantes:
            votante_item = {
                "nombre": votante.nombre,
                "apellidos": votante.apellidos,
                "email": votante.email,
                "celular": votante.celular,
                "fotografia": votante.fotografia,
                "password": votante.password,
                "edad": votante.edad,
            }

            diccionario_votantes[votante.cedula] = votante_item

        return diccionario_votantes
    else:
        return {"result": "error"}

@router.get("/obtener_promedio_edad_votantes", response_model=Dict[str, Any])
def obtener_promedio_edad_votantes():
    """se crea la ruta para obtener los votantes con edad mayor a el promedio
    de las edades de todos los votantes"""
    votantes = obtener_promedio_edad_votantes_db()
    diccionario_votantes = {}
    if votantes:
        for votante in votantes:
            votante_item = {
                "nombre": votante.nombre,
                "apellidos": votante.apellidos,
                "email": votante.email,
                "celular": votante.celular,
                "fotografia": votante.fotografia,
                "password": votante.password,
                "edad": votante.edad,
            }

            diccionario_votantes[votante.cedula] = votante_item

        return diccionario_votantes
    else:
        return {"result": "error"}



# ok
@router.get("/obtener_votante/{cedula}", response_model=Dict[str, Any])
def obtener_votante(cedula: str):
    """se crea la ruta para obtener un votante por cedula"""

    votante = obtener_votante_por_cedula(cedula=cedula)
    return votante


# ok
@router.post("/crear_votante", response_model=Dict[str, Any])
def crear_votante(votante: Votante_apoyo):
    """se crea la ruta para crear un votante"""

    # Llamamos una funcion para crear un votante
    result = crear_votante_query(votante)

    return {"result": result}


@router.put("/actualizar_votante",)
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
def eliminar_votante(cedula: str):
    """se crea la ruta para eliminar un votante filtrado por cedula"""

    msg = eliminar_votante_query(cedula)

    return msg
