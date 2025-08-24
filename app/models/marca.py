from app import db
from datetime import datetime

class Marca(db.Model):
    __tablename__ = 'marcas'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(20), default='Pendiente')
    propietario = db.Column(db.String(100), nullable=False)
    numero_registro = db.Column(db.String(50), unique=True)
    
    def __init__(self, nombre, descripcion, categoria, propietario, estado='Pendiente'):
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.propietario = propietario
        self.estado = estado
        self.numero_registro = self.generar_numero_registro()
    
    def generar_numero_registro(self):
        ultima_marca = Marca.query.order_by(Marca.id.desc()).first()
        if ultima_marca and ultima_marca.numero_registro:
            try:
                ultimo_numero = int(ultima_marca.numero_registro.split('-')[1])
                nuevo_numero = ultimo_numero + 1
            except (IndexError, ValueError):
                nuevo_numero = 1
        else:
            nuevo_numero = 1
        return f"MR-{nuevo_numero}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'categoria': self.categoria,
            'fechaRegistro': self.fecha_registro.isoformat() if self.fecha_registro else None,
            'estado': self.estado,
            'propietario': self.propietario,
            'numeroRegistro': self.numero_registro
        }