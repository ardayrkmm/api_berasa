from flask import Flask
from config import Config
from extensi import db, migrate, bcrypt, jwt, mail
from routes.authRoute import auth_bp
from routes.jenisRoute import jenis_bp
from routes.DonasiRoute import donasi_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inisialisasi ekstensi
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    

    # Register Blueprints (Routes)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(jenis_bp, url_prefix="/api/jenis")
    app.register_blueprint(donasi_bp, url_prefix="/api/donasi")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
