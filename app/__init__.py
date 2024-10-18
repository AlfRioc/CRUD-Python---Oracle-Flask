from flask import Flask
import cx_Oracle
from .routes import main

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['ORACLE_USER'] = 'db272'
    app.config['ORACLE_PASSWORD'] = 'password123'
    app.config['ORACLE_DSN'] = cx_Oracle.makedsn('localhost', 1521, service_name='XEPDB1')

    # Registrar los blueprints
    app.register_blueprint(main)

    return app
