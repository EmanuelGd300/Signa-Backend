def validate_marca_data(data):
    errors = {}
    
    if not data.get('nombre', '').strip():
        errors['nombre'] = 'El nombre es requerido'
    elif len(data['nombre'].strip()) < 2:
        errors['nombre'] = 'El nombre debe tener al menos 2 caracteres'
    
    if not data.get('descripcion', '').strip():
        errors['descripcion'] = 'La descripción es requerida'
    elif len(data['descripcion'].strip()) < 10:
        errors['descripcion'] = 'La descripción debe tener al menos 10 caracteres'
    
    if not data.get('categoria', '').strip():
        errors['categoria'] = 'La categoría es requerida'
    
    if not data.get('propietario', '').strip():
        errors['propietario'] = 'El propietario es requerido'
    elif len(data['propietario'].strip()) < 2:
        errors['propietario'] = 'El propietario debe tener al menos 2 caracteres'
    
    return errors