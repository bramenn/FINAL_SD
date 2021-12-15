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

def obtener_votantes_mayores_18_db():
    """se obtienen todos los votantes mayores a 18 años"""
    votantes = db.session.query(Votante).where(Votante.edad >= 18).all()

    if not votantes:
        return None

    return votantes

def obtener_promedio_edad_votantes_db():
    """se obtiene los votantes con edades mayores a el promedio de las edades de todos los votantes"""
    lista_votantes = obtener_votantes_db()
    lista_votantes_edades = []
    promedio_edad = 0

    if lista_votantes:
        for votante in lista_votantes:
            lista_votantes_edades.append(votante.edad)
        promedio_edad = sum(lista_votantes_edades)/len(lista_votantes_edades)
        votantes = db.session.query(Votante).where(Votante.edad > promedio_edad).all()

        if not votantes:
            return None

        return votantes

    return None

def obtener_votantes_entre_18_27_db():
    """se obtienen todos los votantes con edades entre 18 y 27 años"""
    votantes = (
                db.session.query(Votante)
                .where(Votante.edad >= 18)
                .where(Votante.edad <= 27)
            ).all()

    if not votantes:
        return None

    return votantes

def obtener_votante_por_cedula(cedula: str):
    """se obtiene un votante por el numero de cedula"""
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
    """se genera la contraseña automaticamente"""
    password = SG(r"[\w]{8}").render()
    return password


def crear_votante_query(votante: Votante_apoyo):
    # Esto solo se hace aqui para generar la contraseña del votante
    pwd = generar_password()

    if not obtener_votante_por_cedula(votante.cedula):
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
    else:
        return {"result": f"El votante con {votante.cedula} ya existe"}


def eliminar_votante_query(cedula: str):
    """se elimina el votante por el numero de cedula"""
    if obtener_votante_por_cedula(cedula):
        try:
            db.session.query(Votante).filter(Votante.cedula == cedula).delete()
            db.session.commit()
            return {"result": f"Eliminación del votante {cedula} correcta"}
        except:
            return {"result": f"Eliminación del votante {cedula} incorrecta"}
    else:
        return {"result": f"La cedula {cedula} no existe"}


def actualizar_votante_query(votante: Votante_apoyo):

    # Obtenemos el votante
    votante_db = obtener_votante_por_cedula(votante.cedula)

    if not votante_db:
        return f"El votante {votante.cedula} no existe y no se puede actualizar."


    # votante_db["cedula"] = votante.cedula
    votante_db["nombre"] = votante.nombre
    votante_db["apellidos"] = votante.apellidos
    votante_db["email"] = votante.email
    votante_db["celular"] = votante.celular
    votante_db["fotografia"] = votante.fotografia
    votante_db["edad"] = votante.edad

    try:
        db.session.query(Votante).update(votante_db)
        db.session.commit()
        return f"El votante {votante.cedula} fue correctamente actualizado."
    except:
        return f"El votante {votante.celular} no fue actualizado por un error."



