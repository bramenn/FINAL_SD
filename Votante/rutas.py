from typing import Any, Dict
from fastapi import FastAPI, APIRouter

from Votante.modelo import Votante_apoyo
from Votante.consultas import *

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear
# PUT -> Actualizar
# DELETE -> Borrar

@router.get("/obtener_vontantes", response_model=Dict[str, Any])
def obtener_vontantes():
    votantes = obtener_votantes()
    diccionario_votantes = {}
    for votante in votantes:
        votante_item = {
            "nombre": votante.nombre,
            "apellidos": votante.apellidos,
            "email": votante.email,
            "celular": votante.celular,
            "fotografia": votante.fotografia,
            "password": votante.password,
        }

        diccionario_votantes[votante.cedula] = votante_item

    return diccionario_votantes

@router.get("/obtener_votante/{cedula}", response_model=Dict[str, Any])
def obtener_votante(cedula:str):
    """
    Esta es la ruta para obtener un votante

        votante

    """
    votante = obtener_votante_por_cedula(cedula=cedula)
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