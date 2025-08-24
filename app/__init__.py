from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app, origins=['*'])
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marcas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    from app.routes.marcas import marcas_bp
    app.register_blueprint(marcas_bp, url_prefix='/api')
    
    @app.route('/')
    def home():
        return {'message': 'API de Marcas funcionando', 'endpoints': ['/api/marcas', '/api/health']}
    
    return app