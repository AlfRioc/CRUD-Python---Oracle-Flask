from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app  # Importar current_app
from .models import Persona

main = Blueprint('main', __name__)

# Leer todas las personas
@main.route('/')
def index():
    personas = Persona.get_all(app=current_app)  # current_app es necesario aquí
    return render_template('index.html', personas=personas)

# Crear una nueva persona
@main.route('/personas/nueva', methods=['GET', 'POST'])
def create_persona():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        correo = request.form['correo']
        Persona.create(app=current_app, nombre=nombre, edad=edad, correo=correo)
        flash('Persona creada con éxito')
        return redirect(url_for('main.index'))
    return render_template('create_persona.html')

# Actualizar una persona
@main.route('/personas/editar/<int:id>', methods=['GET', 'POST'])
def update_persona(id):
    persona = Persona.get_by_id(app=current_app, id=id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        correo = request.form['correo']
        Persona.update(app=current_app, id=id, nombre=nombre, edad=edad, correo=correo)
        flash('Persona actualizada con éxito')
        return redirect(url_for('main.index'))
    return render_template('update_persona.html', persona=persona)

# Eliminar una persona
@main.route('/personas/eliminar/<int:id>')
def delete_persona(id):
    Persona.delete(app=current_app, id=id)
    flash('Persona eliminada con éxito')
    return redirect(url_for('main.index'))
