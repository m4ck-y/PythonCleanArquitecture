# Lenguaje de programacion: python

- Se crea un entorno virtual para aislar las librerias

`python -m venv venv`

- Usar el entorno virtual

`source venv/bin/activate`

- Exportar lista de dependencias en archivo 'requirements.txt'

`pip freeze > requirements.txt`



## Librerias Generales
-Lectura de archivos .env

`pip install python-dotenv`


## Infraestructura

#### BD
- Connector Mysql

`python -m pip install PyMySQL `

#### API-REST

- Framework: fastapi

`pip install fastapi`

- Dependencias para fastApi:

`pip install uvicorn[standard]`

- Instalacion Pydantic (para validacion de datos)

`python -m pip install pydantic`

#### Consola

`python -m pip install click`