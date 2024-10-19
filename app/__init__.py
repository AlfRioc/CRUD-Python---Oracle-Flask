from flask import Flask
import cx_Oracle
from .routes import main
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configurar la clave secreta desde el archivo .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Configurar la base de datos Oracle desde el archivo .env
    app.config['ORACLE_USER'] = os.getenv('ORACLE_USER')
    app.config['ORACLE_PASSWORD'] = os.getenv('ORACLE_PASSWORD')
    app.config['ORACLE_DSN'] = cx_Oracle.makedsn(
        os.getenv('ORACLE_HOST'), 
        os.getenv('ORACLE_PORT'), 
        service_name=os.getenv('ORACLE_SERVICE_NAME')
    )

    # Registrar los blueprints
    app.register_blueprint(main)

    return app