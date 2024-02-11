---
title: App Structure
parent: Technical Docs
nav_order: 1
---

{: .label }
Ömer Öztürk

# App structure
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>


## 1. Einleitung
Diese Dokumentation bietet eine strukturelle Übersicht der PerformFit-App, um einen klaren Leitfaden für die Navigation und Funktionalität der App aus der Perspektive der Nutzerstruktur zu geben.

## 2. Datenbankarchitektur und Benutzerregistrierung
Die Datenbankarchitektur umfasst ein User-Modell, welches die E-Mail-Adresse, den gewünschten Benutzernamen und das verschlüsselte Passwort speichert. Dieses Modell unterstützt den Registrierungsprozess, indem es neue Nutzer dazu auffordert, diese Informationen bereitzustellen:

<pre lang="no-highlight"><code>
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    gewicht = db.Column(db.Float, nullable=True)
    zielgewicht = db.Column(db.Float, nullable=True)

</code></pre>

## 3 Login-Prozess

Authentifizierungssystem und Login-View-Konfiguration
Ein wesentlicher Bestandteil der App-Struktur ist das Authentifizierungssystem, das durch Flask-Login verwaltet wird. Flask-Login bietet eine einfache Schnittstelle für das Handling von Benutzersitzungen. Ein kritischer Punkt in der Konfiguration von Flask-Login ist die Definition von login_view, die angibt, welche Route geladen wird, wenn nicht-authentifizierte Benutzer auf eine Route zugreifen möchten, die eine Anmeldung erfordert.


<pre lang="no-highlight"><code>```python
def function():
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

</code></pre>

LoginManager(): Erstellt eine Instanz von Flask-Login's LoginManager, der für das Session-Management zuständig ist.
init_app(app): Initialisiert den LoginManager mit der Flask-Anwendung. Dies ermöglicht es Flask-Login, mit der Anwendungsinstanz zu interagieren.
login_view = 'login': Legt fest, dass Benutzer zur Route mit dem Endpunkt login umgeleitet werden, wenn sie versuchen, auf eine geschützte Seite zuzugreifen, ohne eingeloggt zu sein. Dies ist ein kritischer Aspekt der Benutzerführung und Sicherheit, da es sicherstellt, dass nur authentifizierte Benutzer Zugriff auf bestimmte Bereiche der Anwendung haben.

<pre lang="no-highlight"><code>```python
def function():

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return "Falscher Benutzername oder Passwort"
    return render_template('login.html')

</code></pre>

Es wird geprüft, ob die Kombination aus Benutzername und Passwort in der Datenbank existiert.
login_user(user): Bei erfolgreicher Überprüfung wird der Benutzer eingeloggt.
Weiterleitung: Authentifizierte Benutzer werden zum Dashboard weitergeleitet, während bei einem Fehler eine entsprechende Nachricht ausgegeben wird.

## 3. Fragekatalog-Implementierung
Nach der Registrierung interagiert der Benutzer mit dem User-Modell durch einen Fragekatalog, der das aktuelle Gewicht und das Zielgewicht erfasst. Dies wird durch zusätzliche Attribute im User-Modell reflektiert, die mit den entsprechenden Benutzerdaten besetzt werden:

<pre lang="no-highlight"><code>```python
def function():
class User(db.Model):
    # ...
    current_weight = db.Column(db.Float)
    goal_weight = db.Column(db.Float)


</code></pre>

## 4. Dashboard-Struktur
Das Dashboard ist als zentrale Anlaufstelle nach dem Login konzipiert und bietet Schnellzugriff auf Hauptfunktionen wie den Workoutplan und den Fortschrittstracker. Dies wird durch eine spezifische Route und zugehörige View-Funktion in Flask ermöglicht:

<pre lang="no-highlight"><code>```python
def function():
   
@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    # Logik für die Anzeige des Dashboards


</code></pre>

## 5. Workoutplan-Architektur
Die Workoutplan-Funktion ermöglicht es Benutzern, ihre Trainingsdaten einzugeben. Dies könnte durch ein spezifisches Modell für Workouts unterstützt werden, welches mit dem Benutzermodell verknüpft ist, dabei sind Informationen wie der Tag der Übung, die Art der Übung, Wiederholungen, Sätze und eine Notiz über das Workout von Wichtigkeit und wird dies im Bereich Workout erfasst:

<pre lang="no-highlight"><code>```python
def function():
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    exercise = db.Column(db.String(100))
    repetitions = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    notes = db.Column(db.Text)

</code></pre>


## 6. Fortschrittstracker-Struktur
Der Fortschrittstracker ist durch das Progress-Modell realisiert, das eine visuelle Darstellung des Trainingsfortschritts ermöglicht. Es wird durch eine GET-Route bedient, die das entsprechende Template mit Daten versorgt:

<pre lang="no-highlight"><code>```python
def function():
class Progress(db.Model):
    ...
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    workout_completed = db.Column(db.Boolean)
    slept_well = db.Column(db.Boolean)
    ...

</code></pre>

Dieses Modell speichert Daten zu jedem Workout und der Schlafqualität der Nutzer. Es wird jeden Tag aktualisiert, um den Fortschritt zu verfolgen.