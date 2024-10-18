from .db import get_oracle_connection

class Persona:
    def __init__(self, id, nombre, edad, correo):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    @staticmethod
    def get_all(app):
        connection = get_oracle_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, nombre, edad, correo FROM personas")
        rows = cursor.fetchall()
        personas = [Persona(*row) for row in rows]
        cursor.close()
        connection.close()
        return personas

    @staticmethod
    def get_by_id(app, id):
        connection = get_oracle_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, nombre, edad, correo FROM personas WHERE id = :id", {'id': id})
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        if row:
            return Persona(*row)
        return None

    @staticmethod
    def create(app, nombre, edad, correo):
        connection = get_oracle_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO personas (nombre, edad, correo) 
            VALUES (:nombre, :edad, :correo)
        """, {'nombre': nombre, 'edad': edad, 'correo': correo})
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def update(app, id, nombre, edad, correo):
        connection = get_oracle_connection()
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE personas SET nombre = :nombre, edad = :edad, correo = :correo 
            WHERE id = :id
        """, {'nombre': nombre, 'edad': edad, 'correo': correo, 'id': id})
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(app, id):
        connection = get_oracle_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM personas WHERE id = :id", {'id': id})
        connection.commit()
        cursor.close()
        connection.close()
