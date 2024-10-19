from flask import Blueprint, jsonify, request
from .models import Persona

main = Blueprint('main', __name__)

# Ruta para obtener todas las personas
@main.route('/api/personas', methods=['GET'])
def get_personas():
    try:
        personas = Persona.get_all()
        return jsonify([persona.to_dict() for persona in personas])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para obtener una persona por ID
@main.route('/api/personas/<int:id>', methods=['GET'])
def get_persona(id):
    try:
        persona = Persona.get_by_id(id)
        if persona:
            return jsonify(persona.to_dict())
        else:
            return jsonify({'error': 'Persona no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para crear una nueva persona
@main.route('/api/personas', methods=['POST'])
def create_persona():
    try:
        data = request.get_json()
        nueva_persona = Persona(nombre=data['nombre'], edad=data['edad'], correo=data['correo'])
        nueva_persona.save()
        return jsonify(nueva_persona.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para actualizar una persona existente
@main.route('/api/personas/<int:id>', methods=['PUT'])
def update_persona(id):
    try:
        persona = Persona.get_by_id(id)
        if not persona:
            return jsonify({'error': 'Persona no encontrada'}), 404
        
        data = request.get_json()
        persona.nombre = data['nombre']
        persona.edad = data['edad']
        persona.correo = data['correo']
        persona.update()
        
        return jsonify(persona.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para eliminar una persona
@main.route('/api/personas/<int:id>', methods=['DELETE'])
def delete_persona(id):
    try:
        persona = Persona.get_by_id(id)
        if not persona:
            return jsonify({'error': 'Persona no encontrada'}), 404
        
        persona.delete()
        return jsonify({'message': 'Persona eliminada correctamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500