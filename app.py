from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)

# Konfiguration der Datenbank
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

# Route für die Registrierungsseite
@app.route('/register', methods=['GET', 'POST'])
def register():
    error_message = None  # Variable für Fehlermeldungen

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            error_message = "Benutzername oder E-Mail-Adresse bereits vergeben. Bitte wählen Sie einen anderen."
        else:
            user = User(name=name, email=email, username=username)
            user.set_password(password)

            try:
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('fragenkatalog'))
            except Exception as e:
                error_message = "Ein Fehler ist aufgetreten. Bitte versuchen Sie es erneut."

    return render_template('registration.html', error_message=error_message)


# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            # TODO: Hier Logik einfügen, um zu überprüfen, ob der Benutzer den Fragenkatalog ausgefüllt hat
            # Vorläufige Weiterleitung zur Startseite
            return redirect(url_for('fragenkatalog'))
        else:
            # Falscher Benutzername oder Passwort
            return "Falscher Benutzername oder Passwort"  # oder eine andere Fehlerbehandlung

    return render_template('login.html')

# Route für die Startseite
@app.route('/')
def index():
    return render_template('index.html')

# Route für den Fragekatalog
@app.route('/fragenkatalog')
def fragenkatalog():
    return render_template('fragenkatalog.html')

# Route für die Verarbeitung des Fragekatalogs
@app.route('/submit_fragenkatalog', methods=['POST'])
def submit_fragenkatalog():
    # Informationen aus dem Formular extrahieren
    gewicht = request.form.get('gewicht')
    zielgewicht = request.form.get('zielgewicht')
    # Daten verarbeiten (z.B. speichern oder auswerten)

    return redirect(url_for('index')) # Zur Index-Seite umleiten

# Anwendungsstartpunkt
if __name__ == '__main__':
    app.run(debug=True)