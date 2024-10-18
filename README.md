# Flask CRUD - Gestión de Personas

Este proyecto es una aplicación CRUD (Crear, Leer, Actualizar, Eliminar) simple construida con Flask. Permite gestionar personas, incluyendo la creación, visualización, actualización y eliminación de registros.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalados los siguientes elementos:

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
  Python es el lenguaje de programación utilizado para construir el proyecto. Se requiere la versión 3.7 o superior.
  - [Descargar Python](https://www.python.org/downloads/)

- ![Oracle Database](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)  
  La aplicación utiliza una base de datos Oracle para el almacenamiento de datos.
  - [Descargar Oracle Database 21c Express Edition](https://www.oracle.com/database/technologies/xe-downloads.html)

### Recomendaciones

- Desinstalar si tiene alguna version mas antigua de oracle
- Al instalar oracle recordar la contraseña, caso contrario desintalar e instalar nuevamente
- Si tiene el siguente problema `error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/`

    ![Visual Studio](https://img.shields.io/badge/Visual%20Studio%20Tools-5C2D91?style=for-the-badge&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPgo8c3ZnIHdpZHRoPSI4MDBweCIgaGVpZ2h0PSI4MDBweCIgdmlld0JveD0iLTAuMDggMCA2Ny4wMTIgNjcuMDEyIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOmNjPSJodHRwOi8vY3JlYXRpdmVjb21tb25zLm9yZy9ucyMiIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxtZXRhZGF0YT4KICAgICAgICA8cmRmOlJERj4KICAgICAgICAgICAgPGNjOldvcms+CiAgICAgICAgICAgICAgICA8ZGM6c3ViamVjdD4KICAgICAgICAgICAgICAgICAgICBNaXNjZWxsYW5lb3VzCiAgICAgICAgICAgICAgICA8L2RjOnN1YmplY3Q+CiAgICAgICAgICAgICAgICA8ZGM6aWRlbnRpZmllcj4KICAgICAgICAgICAgICAgICAgICB2aXN1YWwtc3R1ZGlvLW9ubGluZQogICAgICAgICAgICAgICAgPC9kYzppZGVudGlmaWVyPgogICAgICAgICAgICAgICAgPGRjOnRpdGxlPgogICAgICAgICAgICAgICAgICAgIFZpc3VhbCBTdHVkaW8gT25saW5lCiAgICAgICAgICAgICAgICA8L2RjOnRpdGxlPgogICAgICAgICAgICAgICAgPGRjOmZvcm1hdD4KICAgICAgICAgICAgICAgICAgICBpbWFnZS9zdmcreG1sCiAgICAgICAgICAgICAgICA8L2RjOmZvcm1hdD4KICAgICAgICAgICAgICAgIDxkYzpwdWJsaXNoZXI+CiAgICAgICAgICAgICAgICAgICAgQW1pZG8gTGltaXRlZAogICAgICAgICAgICAgICAgPC9kYzpwdWJsaXNoZXI+CiAgICAgICAgICAgICAgICA8ZGM6Y3JlYXRvcj4KICAgICAgICAgICAgICAgICAgICBSaWNoYXJkIFNsYXRlcgogICAgICAgICAgICAgICAgPC9kYzpjcmVhdG9yPgogICAgICAgICAgICAgICAgPGRjOnR5cGUgcmRmOnJlc291cmNlPSJodHRwOi8vcHVybC5vcmcvZGMvZGNtaXR5cGUvU3RpbGxJbWFnZSIvPgogICAgICAgICAgICA8L2NjOldvcms+CiAgICAgICAgPC9yZGY6UkRGPgogICAgPC9tZXRhZGF0YT4KICAgIDxwYXRoIGQ9Im0gMzg4LjA1NjYxLDQ1Ni4xMjY0NyAxNi41NjEyNCw2LjY4NjMgdiA1My42Mzc0IGwgLTE2LjcxNTc0LDYuNjg4MiAtMjYuNTkwNjYsLTI2LjQzOTkgLTE2Ljg2NjUxLDEzLjA2OTEgLTYuNjg2MjgsLTMuMzQzMSB2IC0zMy41ODQxIGwgNi42ODYyOCwtMy4xOTA1IDE2Ljg2NjUxLDEzLjIxOTkgMjYuNzQ1MTYsLTI2Ljc0MzMgeiBtIC00My42MTE2NywyMy41NTI4IHYgMjAuMzYyMyBsIDEwLjAyOTQ1LC0xMC4zMzI4IC0xMC4wMjk0NSwtMTAuMDI5NSB6IG0gMjYuMTM2NDcsMTAuMDI5NSAxNy4zMjI1NiwxMy42Nzc4IHYgLTI3LjM1NTcgbCAtMTcuMzIyNTYsMTMuNjc3OSB6IiBmaWxsPSIjZmZmIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMzM3Ljc1OSAtNDU2LjEyNikiLz4KPC9zdmc+) Instalar los packetes C++ build tools [Descargar Visual Studio Tools](https://visualstudio.microsoft.com/downloads/)
- Al momento de instalar Oracle, Ejecutar el archivo `Oracle Database 21c Express Edition` primero, luego ejecutar `setup`

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/Troy8203/projectBase-Oracle
   ```

2. **Navega al directorio del proyecto:**

   ```bash
   cd projectBase-Oracle
   ```

3. **Configura un entorno virtual:**

   Es una buena práctica crear un entorno virtual para gestionar las dependencias de tu proyecto.

   ```bash
   python -m venv venv
   ```

4. **Activa el entorno virtual:**

   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Instala los paquetes de Python requeridos:**

   Instala las dependencias necesarias que se encuentran en el archivo `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

6. **Configura la conexión a la base de datos:**

   Crea un archivo `.env` en el directorio raíz del proyecto para almacenar tus credenciales de la base de datos Oracle y detalles de conexión.

   Ejemplo de archivo `.env`:
   ```env
   ORACLE_USERNAME=tu_usuario
   ORACLE_PASSWORD=tu_contraseña
   ORACLE_DSN=tu_dsn_base_de_datos
   ```

7. **Ejecuta la aplicación:**

   Una vez que todo esté configurado, puedes ejecutar el servidor de desarrollo de Flask:

   ```bash
   flask run
   ```

   La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Uso

Una vez que el servidor esté en funcionamiento, puedes acceder a las siguientes funcionalidades CRUD a través de un navegador web o herramienta de API (por ejemplo, Postman):

- **Crear** una nueva persona
- **Leer** o ver los registros de personas
- **Actualizar** un registro de persona existente
- **Eliminar** una persona

## Estructura del Proyecto

```
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates/
│       └── *.html
├── instance/
│   └── config.py
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
```

- `app/`: Contiene la lógica de la aplicación, incluyendo rutas y modelos.
- `instance/`: Se utiliza para almacenar la configuración local, como la URI de la base de datos.
- `templates/`: Plantillas HTML para renderizar el front-end de la aplicación.