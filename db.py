from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask import Flask

# Flask-Anwendung erstellen
app = Flask(__name__)

# Konfiguration der Datenbank
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Datenbankinstanz erstellen
db = SQLAlchemy(app)

# Datenbankmodell für die Benutzer
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    # Methode zum Setzen des Passwort-Hashes
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

# Datenbanktabellen erstellen
with app.app_context():
    db.create_all()
