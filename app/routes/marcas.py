from flask import Blueprint, request, jsonify
from app import db
from app.models.marca import Marca
from app.utils.validators import validate_marca_data

marcas_bp = Blueprint('marcas', __name__)

@marcas_bp.route('/marcas', methods=['GET'])
def get_marcas():
    try:
        marcas = Marca.query.all()
        return jsonify([marca.to_dict() for marca in marcas]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@marcas_bp.route('/marcas/<int:marca_id>', methods=['GET'])
def get_marca(marca_id):
    try:
        marca = Marca.query.get_or_404(marca_id)
        return jsonify(marca.to_dict()), 200
    except Exception as e:
        return jsonify({'error': 'Marca no encontrada'}), 404

@marcas_bp.route('/marcas', methods=['POST'])
def create_marca():
    try:
        data = request.get_json()
        
        errors = validate_marca_data(data)
        if errors:
            return jsonify({'errors': errors}), 400
        
        marca = Marca(
            nombre=data['nombre'].strip(),
            descripcion=data['descripcion'].strip(),
            categoria=data['categoria'].strip(),
            propietario=data['propietario'].strip()
        )
        
        db.session.add(marca)
        db.session.commit()
        
        return jsonify(marca.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@marcas_bp.route('/marcas/<int:marca_id>', methods=['PUT'])
def update_marca(marca_id):
    try:
        marca = Marca.query.get_or_404(marca_id)
        data = request.get_json()
        
        errors = validate_marca_data(data)
        if errors:
            return jsonify({'errors': errors}), 400
        
        marca.nombre = data['nombre'].strip()
        marca.descripcion = data['descripcion'].strip()
        marca.categoria = data['categoria'].strip()
        marca.propietario = data['propietario'].strip()
        marca.estado = data.get('estado', marca.estado)
        
        db.session.commit()
        
        return jsonify(marca.to_dict()), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@marcas_bp.route('/marcas/<int:marca_id>', methods=['DELETE'])
def delete_marca(marca_id):
    try:
        marca = Marca.query.get_or_404(marca_id)
        
        db.session.delete(marca)
        db.session.commit()
        
        return jsonify({'message': 'Marca eliminada correctamente'}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@marcas_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK', 'message': 'API funcionando correctamente'}), 200