import requests
import json


def obtener_votantes():
    url = "http://localhost:8000/v1/votante/obtener_votantes"
    resp = requests.get(url)

    votantes = json.loads(resp.content)

    print("Imprimiendoa todos los votantes:")
    for votante_cedula in votantes:
        votante_info = votantes[votante_cedula]
        print(
            "-------------------------------------------------------------------------------------"
            "-------------------------------------------------------------------------------------"
            f"\n Cedula: {votante_cedula}"
            f"\t Nombre: {votante_info.get('nombre')}"
            f"\t Apellidos: {votante_info.get('apellidos')}"
            f"\t Email: {votante_info.get('email')}"
            f"\t Celular: {votante_info.get('celular')}"
            f"\t Fotografia: {votante_info.get('fotografia')}"
            f"\t Contraseña: {votante_info.get('password')}"
        )

def obtener_candidatos():
    url = "http://localhost:8000/v1/candidato/obtener_candidatos"
    resp = requests.get(url)

    candidatos = json.loads(resp.content)

    print("Imprimiendoa todos los candidatos:")
    for candidato_cedula in candidatos:
        candidato_info = candidatos[candidato_cedula]
        print(
            "-------------------------------------------------------------------------------------"
            "-------------------------------------------------------------------------------------"
            f"\n Cedula: {candidato_cedula}"
            f"\t Nombre: {candidato_info.get('nombre')}"
            f"\t Apellidos: {candidato_info.get('apellidos')}"
            f"\t Email: {candidato_info.get('email')}"
            f"\t Celular: {candidato_info.get('celular')}"
            f"\t Fotografia: {candidato_info.get('fotografia')}"
            f"\t nit_partido_politico: {candidato_info.get('nit_partido_politico')}"
        )

def obtener_partidos_politicos():
    url = "http://localhost:8000/v1/partido_politico/obtener_partidos_politicos"
    resp = requests.get(url)

    partidos_politicos = json.loads(resp.content)

    print("Imprimiendoa todos los partidos_politicos:")
    for partido_politico_nit in partidos_politicos:
        partido_politico_info = partidos_politicos[partido_politico_nit]
        print(
            "-------------------------------------------------------------------------------------"
            "-------------------------------------------------------------------------------------"
            f"\n nit: {partido_politico_nit}"
            f"\t Nombre: {votante_info.get('nombre')}"
            f"\t direccion: {votante_info.get('direccion')}"
            f"\t foto_oficial: {votante_info.get('foto_oficial')}"
            f"\t telefono: {votante_info.get('telefono')}"
        )

def obtener_elecciones():
    url = "http://localhost:8000/v1/eleccion/obtener_elecciones"
    resp = requests.get(url)

    elecciones = json.loads(resp.content)

    print("Imprimiendoa todas las elecciones:")
    for eleccion_codigo in elecciones:
        eleccion_info = elecciones[eleccion_codigo]
        print(
            "-------------------------------------------------------------------------------------"
            "-------------------------------------------------------------------------------------"
            f"\n codigo: {eleccion_codigo}"
            f"\t fecha_inicio: {eleccion.get('fecha_inicio')}"
            f"\t fecha_fin: {eleccion.get('fecha_fin')}"
            f"\t nombre: {eleccion.get('nombre')}"
            f"\t descripcion: {eleccion.get('descripcion')}"
        )

while True:
    print("VOTANTE\n" 
        "1-  Obtener todos los votantes\n" 
        "2-  Obtener todos los candidatos\n" 
        "3-  Obtener todos los partidos_politicos\n" 
        "4-  Obtener todas las elecciones\n"
        "10- Salir\n")

    opt = int(input("Igrese una opcion: "))

    if opt == 1:
        obtener_votantes()
    elif opt == 2:
        obtener_candidatos()
    elif opt == 3:
        obtener_partidos_politicos()
    elif opt == 4:
        obtener_elecciones()
    elif opt == 10:
        break
    else:
        print("Opcion incorrecta!!")

