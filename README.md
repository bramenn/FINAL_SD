# Estos son los pasos para poder correr el proyecto

## Simplemente siga los pasos

---
**(OPCIONAL)** Haga esto **SOLO** si no tiene postgres instalado en su maquina (linux)

    sudo apt-get install postgresql

**Pronto para Windows 😉 ...**

---

**(REQUERIDO)** Para instalar los requerimientos ejecute esto en su terminal.

    pip install -r requirements.txt



**(REQUERIDO)** Crear un rol de la bd:

    CREATE ROLE sd_final CREATEDB CREATEROLE LOGIN PASSWORD 'sd_final';

**(REQUERIDO)** Crear la bd:

    CREATE DATABASE votaciones ENCODING 'UTF8' LC_COLLATE='C' LC_CTYPE='C' template=template0 OWNER sd_final;

---
Para correr el programa haga:

    python main.py

    ó

    python3 main.py


# (∩｀-´)⊃━☆ﾟ.*･｡ﾟ