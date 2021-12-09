import requests
import json


def obtener_votantes():
    url = "http://localhost:8000/v1/votante/obtener_votantes"
    resp = requests.get(url)

    votantes = json.loads(resp.content)

    print("Imprimiendoa todos los votantes:")
    for votante_cedula in votantes:
        vontante_info = votantes[votante_cedula]
        print(
            "-------------------------------------------------------------------------------------"
            "-------------------------------------------------------------------------------------"
            f"\nCedula: {votante_cedula}"
            f"\t Nombre: {vontante_info.get('nombre')}"
            f"\t Apellidos: {vontante_info.get('apellidos')}"
            f"\t Email: {vontante_info.get('email')}"
            f"\t Celular: {vontante_info.get('celular')}"
            f"\t Fotografia: {vontante_info.get('fotografia')}"
            f"\t Contraseña: {vontante_info.get('password')}"
        )


while True:
    print("VOTANTE\n" "1-  Obtener todos los votantes\n" "10- Salir\n")

    opt = int(input("Igrese una opcion: "))

    if opt == 1:
        obtener_votantes()
    elif opt == 10:
        break
    else:
        print("Opcion incorrecta!!")
