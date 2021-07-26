from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def deploy_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'prueba tecnica'
 
    db.init_app(app)
    
    from .views import views
    from .add_producto import add_producto
    from .inventarios import inventarios
        
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(add_producto, url_prefix = '/')
    app.register_blueprint(inventarios, url_prefix = '/')

    return app
    
