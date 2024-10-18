from flask import Flask, jsonify
import cx_Oracle

app = Flask(__name__)

# Configurar la conexión a Oracle
def get_oracle_connection():
    # Aquí debes ajustar los parámetros de conexión según tu configuración de Oracle XE
    dsn = cx_Oracle.makedsn('localhost', 1521, service_name='XE')  # Reemplaza 'localhost' con la IP/hostname de Oracle XE si es necesario
    connection = cx_Oracle.connect(user='system', password='123456', dsn=dsn)
    return connection

@app.route('/')
def index():
    try:
        # Obtener la conexión
        connection = get_oracle_connection()
        cursor = connection.cursor()

        # Ejecutar una consulta de prueba
        cursor.execute("SELECT 'Hello from Oracle DB!' AS greeting FROM dual")
        result = cursor.fetchone()

        # Cerrar la conexión y el cursor
        cursor.close()
        connection.close()

        return jsonify({'message': result[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
