# Este es el archivo principal de todo el programa
# Aqui vamos a definir el servidor de uvicorn
# Este servidor nos permitira hacerle consultas a la api
# Aqui importamos todas las rutas que va encontrar uvicorn
# uvicorn las podra hacer visibles a consultas de cualquier persona (cliente)

from fastapi import FastAPI
import uvicorn

# Se importan todas las rutas
from Voto import rutas as rutas_voto
from Votante import rutas as rutas_votante
from Candidato import rutas as rutas_candidato
from Eleccion import rutas as rutas_eleccion
from PartidoPolitico import rutas as rutas_partido_politico

# Se importan los modelos
from Voto import modelo
from Votante import modelo
from Candidato import modelo
from Eleccion import modelo
from PartidoPolitico import modelo

# Se importa la configuracion de la bd
import db

# Se crea la aplicacion de FastApi
app = FastAPI()

# Se importan las rutas de la API:

# Ruta de votante
app.include_router(rutas_votante.router, prefix="/v1/votante", tags=["votantes"])

# # Ruta de partido_politico
app.include_router(
    rutas_partido_politico.router,
    prefix="/v1/partido_politico",
    tags=["partidos_politicos"],
)

# # Ruta de eleccion
app.include_router(rutas_eleccion.router, prefix="/v1/eleccion", tags=["elecciones"])

# # Ruta de candidato
app.include_router(rutas_candidato.router, prefix="/v1/candidato", tags=["candidatos"])

# # Ruta de voto
app.include_router(rutas_voto.router, prefix="/v1/voto", tags=["votos"])

# Aqui se corre el programa
if __name__ == "__main__":

    # Corre las migraciones de la bd
    # print("Corriendo migraciones de la bd")
    db.Base.metadata.create_all(db.conn)

    # Corre el servidor de uvicorn para la api
    uvicorn.run(app="main:app", reload=True)
