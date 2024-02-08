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

class WorkoutDay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    day_name = db.Column(db.String(50), nullable=False)
    user = db.relationship('User', backref=db.backref('workout_days', lazy=True))

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_day_id = db.Column(db.Integer, db.ForeignKey('workout_day.id'), nullable=False)
    exercise_name = db.Column(db.String(100), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    repetitions = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    workout_day = db.relationship('WorkoutDay', backref=db.backref('workouts', lazy=True))


