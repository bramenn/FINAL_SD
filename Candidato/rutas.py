from typing import Any, Dict
from fastapi import FastAPI, APIRouter

from Candidato.modelo import Candidato_apoyo
from Candidato.consultas import *

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear
# PUT -> Actualizar
# DELETE -> Borrar

@router.get("/obtener_candidatos", response_model=Dict[str, Any])
def obtener_candidatos():
    candidatos = obtener_candidatos_db()
    diccionario_candidatos = {}
    for candidato in candidato:
        candidato_item = {
            "cedula": candidato.cedula,
            "nombre": candidato.nombre,
            "apellidos": candidato.apellidos,
            "celular": candidato.celular,
            "email": candidato.email,
            "fotografia": candidato.fotografia,
        }

        diccionario_candidatos[candidato.cedula] = candidatos_item

    return diccionario_candidatos

@router.get("/obtener_candidato/{cedula}", response_model=Dict[str, Any])
def obtener_candidato(cedula:str):
    """
    Esta es la ruta para obtener un candidato

        candidato

    """

    candidato = obtener_candidato_por_cedula(cedula=cedula)
    return candidato


@router.post("/crear_candidato", response_model=Dict[str, Any])
def crear_candidato(candidato: Candidato_apoyo):
    print(
        f"cedula: {candidato.cedula} \n"
        f"nombre: {candidato.nombre} \n"
        f"apellidos: {candidato.apellidos} \n"
        f"celular: {candidato.celular} \n"
        f"email: {candidato.email} \n"
        f"fotografia: {candidato.fotografia} \n"
    )

    return {}

@router.put("/actualizar_candidato", )
def actualizar_candidato(candidato: Candidato_apoyo):
    print(
        f"cedula: {candidato.cedula} \n"
        f"nombre: {candidato.nombre} \n"
        f"apellidos: {candidato.apellidos} \n"
        f"celular: {candidato.celular} \n"
        f"email: {candidato.email} \n"
        f"fotografia: {candidato.fotografia} \n"
    )

    return {}

@router.delete("/eliminar_candidato/{cedula}")
def eliminar_candidato(cedula:str):

    mensaje = f"Se elimino el candidato con cedula: {cedula}"

    return {"mensaje":mensaje}