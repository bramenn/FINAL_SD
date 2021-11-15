from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/votante/obtener_votante")
def obtener_votante():
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