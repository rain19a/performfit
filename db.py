from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask import Flask
from flask_login import UserMixin
from flask_migrate import Migrate
from datetime import date


# Flask-Anwendung erstellen
app = Flask(__name__)

# Konfiguration der Datenbank
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Datenbankinstanz erstellen
db = SQLAlchemy(app)

#Aktualisierung DB
migrate = Migrate(app, db)


# Datenbankmodell für die Benutzer
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    gewicht = db.Column(db.Float, nullable=True)
    zielgewicht = db.Column(db.Float, nullable=True)
    
    # Methode zum Setzen des Passwort-Hashes
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

# Datenbanktabellen erstellen
with app.app_context():
    db.create_all()

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, default=date.today, nullable=False)
    slept_well = db.Column(db.Boolean, default=False, nullable=False)
    workout_completed = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<Progress {self.user_id} {self.date} Slept: {self.slept_well} Workout: {self.workout_completed}>'

class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class TrainingDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(10), nullable=False)  # Montag bis Sonntag
    training_id = db.Column(db.Integer, db.ForeignKey('training.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    training = db.relationship('Training', backref=db.backref('training_days', lazy=True))
    trainingsinhalte = db.relationship('TrainingInhalt', back_populates='training_day', cascade="all, delete-orphan")

class TrainingInhalt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uebungsname = db.Column(db.String(128), nullable=False)
    gewicht = db.Column(db.Float, nullable=False)
    saetze = db.Column(db.Integer, nullable=False)
    wiederholungen = db.Column(db.Integer, nullable=False)
    training_day_id = db.Column(db.Integer, db.ForeignKey('training_day.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    training_day = db.relationship('TrainingDay', back_populates='trainingsinhalte')