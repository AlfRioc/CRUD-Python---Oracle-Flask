from .db import get_oracle_connection

class Persona:
    def __init__(self, id=None, nombre=None, edad=None, correo=None):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    @staticmethod
    def get_all():
        connection = get_oracle_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, nombre, edad, correo FROM personas")
        rows = cursor.fetchall()
        personas = [Persona(id=row[0], nombre=row[1], edad=row[2], correo=row[3]) for row in rows]
        cursor.close()
        connection.close()
        return personas

    @staticmethod
    def get_by_id(id):
        connection = get_oracle_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, nombre, edad, correo FROM personas WHERE id = :id", {'id': id})
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        if row:
            return Persona(id=row[0], nombre=row[1], edad=row[2], correo=row[3])
        return None

    def save(self):
        connection = get_oracle_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO personas (nombre, edad, correo) VALUES (:nombre, :edad, :correo)",
            {'nombre': self.nombre, 'edad': self.edad, 'correo': self.correo}
        )
        connection.commit()
        cursor.close()
        connection.close()

    def update(self):
        connection = get_oracle_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE personas SET nombre = :nombre, edad = :edad, correo = :correo WHERE id = :id",
            {'nombre': self.nombre, 'edad': self.edad, 'correo': self.correo, 'id': self.id}
        )
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self):
        connection = get_oracle_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM personas WHERE id = :id", {'id': self.id})
        connection.commit()
        cursor.close()
        connection.close()

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'edad': self.edad,
            'correo': self.correo
        }