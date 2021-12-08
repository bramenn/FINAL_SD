from typing import Any, Dict
from fastapi import FastAPI, APIRouter

from Candidato.modelo import Candidato_apoyo
from Candidato.consultas import *

router = APIRouter()

# GET -> Buscar
# POST -> Insersion -  Crear
# PUT -> Actualizar
# DELETE -> Borrar

@router.get("/obtener_votantes", response_model=Dict[str, Any])
def obtener_votantes():
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
        }

        diccionario_votantes[votante.cedula] = votante_item

    return diccionario_votantes

@router.get("/obtener_candidato/{cedula}", response_model=Dict[str, Any])
def obtener_candidato(cedula:str):
    candidato = {
        "cedula": "",
        "nombre": "",
        "apellidos": "",
        "celular": "",
        "e-mail": "",
        "fotografia": "",
    }
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