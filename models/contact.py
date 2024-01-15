from utils.db import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    telefono = db.Column(db.String(15))
    carrera = db.Column(db.String(100))
    pais = db.Column(db.String(100))

    def __init__(self, nombre, apellido, telefono, carrera, pais):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.carrera = carrera
        self.pais = pais
