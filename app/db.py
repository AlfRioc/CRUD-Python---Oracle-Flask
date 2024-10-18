import cx_Oracle
from flask import current_app

def get_oracle_connection():
    dsn = current_app.config['ORACLE_DSN']
    connection = cx_Oracle.connect(
        user=current_app.config['ORACLE_USER'],
        password=current_app.config['ORACLE_PASSWORD'],
        dsn=dsn
    )
    return connection
