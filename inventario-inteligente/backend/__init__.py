from flask import Flask
from flask_mysqldb import MySQL
from config import Config

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mysql.init_app(app)
    
    from routes import productos_bp
    app.register_blueprint(productos_bp)
    
    return app
