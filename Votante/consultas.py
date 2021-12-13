from strgen import StringGenerator as SG

from Votante.modelo import Votante, Votante_apoyo
import db


def obtener_votantes_db():
    """
    Obtener todos los votantes
    query:
        select * from votante;
    """
    votante = db.session.query(Votante).all()
    return votante


def obtener_votante_por_cedula(cedula: str):
    votante = db.session.query(Votante).where(Votante.cedula == cedula).first()

    if not votante:
        return None

    votante_dict = {
        "cedula": votante.cedula,
        "nombre": votante.nombre,
        "apellidos": votante.apellidos,
        "email": votante.email,
        "celular": votante.celular,
        "fotografia": votante.fotografia,
        "password": votante.password,
        "edad": votante.edad,
    }
    return votante_dict


def generar_password():
    password = SG(r"[\w]{8}").render()
    return password


def crear_votante_query(votante: Votante_apoyo):
    # Esto solo se hace aqui para generar la contraseña del votante
    pwd = generar_password()

    # se crea la variable votante_db basados en el modelo Votante
    votante_db = Votante(
        cedula=votante.cedula,
        nombre=votante.nombre,
        apellidos=votante.apellidos,
        email=votante.email,
        celular=votante.celular,
        fotografia=votante.fotografia,
        password=pwd,
        edad=votante.edad,
    )

    try:  # Si la insercion sale bien nos dice "El votante se ha creado"
        db.session.add(votante_db)
        db.session.commit()
        return "El votante se ha creado"
    except:  # Si no sale bien nos dice "No se ha creado el votante"
        return "No se ha creado el votante"

def eliminar_votante_query(cedula: str):
    if obtener_votante_por_cedula(cedula):
        try:
            db.session.query(Votante).filter(Votante.cedula == cedula).delete()
            db.session.commit()
            return {"result": f"Eliminación del votante {cedula} correcta"}
        except:
            return {"result": f"Eliminación del votante {cedula} incorrecta"}
    else:
        return {"result": f"La cedula {cedula} no existe"}
