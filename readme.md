Lenguaje de programacion: python
---

- Se crea un entorno virtual para aislar las librerias

`python -m venv venv`

- Usar el entorno virtual

`source venv/bin/activate`

- Instalacion de framework: fastapi

`pip install fastapi`

- Instalacion de depencias para fastApi:

`pip install uvicorn[standard]`

- Instalacion Pydantic (para validacion de datos)

`python -m pip install pydantic`

- Instalacion connector Mysql

`python -m pip install PyMySQL `

- Instalacion libreria para lectura de archivos .env

`pip install python-dotenv`

- Exportar lista de dependencias en archivo 'requirements.txt'

`pip freeze > requirements.txt`