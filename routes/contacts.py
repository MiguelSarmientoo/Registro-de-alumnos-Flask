from flask import Blueprint, render_template, request, redirect, url_for
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def index():
    contact_list = Contact.query.all()
    return render_template('index.html', contacts=contact_list)

@contacts.route('/new', methods=['POST'])
def add_contact():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    carrera = request.form['carrera']
    pais = request.form['pais']

    new_contact = Contact(nombre, apellido, telefono, carrera, pais)
    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for('contacts.index'))

@contacts.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    if request.method == "POST":
        contact = Contact.query.get(id)
        contact.nombre = request.form['nombre']
        contact.apellido = request.form['apellido']
        contact.telefono = request.form['telefono']
        contact.carrera = request.form['carrera']
        contact.pais = request.form['pais']

        db.session.commit()
        return redirect(url_for('contacts.index'))

    contact = Contact.query.get(id)
    return render_template('update.html', contact=contact)

@contacts.route('/delete/<id>')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    return redirect(url_for('contacts.index'))

@contacts.route('/about')
def about():
    return render_template('add.html')
