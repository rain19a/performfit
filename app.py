from flask import render_template, request, redirect, url_for
from werkzeug.security import check_password_hash
from db import app, db, User
from flask import jsonify
from db import app, db, User, Progress
from datetime import timedelta
from datetime import date
from flask_login import login_user, login_required, logout_user, current_user


# Route für die Registrierungsseite
@app.route('/register', methods=['GET', 'POST'])
def register():
    error_message = None

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
            login_user(user)  # Loggt den Benutzer ein
            return redirect(url_for('dashboard'))
        else:
            return "Falscher Benutzername oder Passwort"

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
    gewicht = request.form.get('gewicht')
    zielgewicht = request.form.get('zielgewicht')
    return redirect(url_for('dashboard'))

# Route für Dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        user_id = 1  # Ersetzen Sie dies mit der tatsächlichen Benutzer-ID
        workout_completed = 'workout' in request.form
        slept_well = 'sleep' in request.form

        # Überprüfen, ob bereits ein Eintrag für heute existiert
        today_progress = Progress.query.filter_by(user_id=user_id, date=date.today()).first()

        # Aktualisieren oder neuen Eintrag erstellen
        if today_progress:
            today_progress.workout_completed = workout_completed
            today_progress.slept_well = slept_well
        else:
            new_progress = Progress(
                user_id=user_id, 
                date=date.today(), 
                workout_completed=workout_completed, 
                slept_well=slept_well
            )
            db.session.add(new_progress)

        db.session.commit()

        return redirect(url_for('dashboard'))
    
    return render_template('dashboard.html')




@app.route('/fortschritt')
def fortschritt():
    # Hier sollte die Benutzer-ID aus der Sitzung oder dem Login-Manager geholt werden
    # Zum Beispiel (hier pseudocode, abhängig von Ihrer Authentifizierungsimplementierung):
    # user_id = session['user_id'] oder user_id = current_user.id
    user_id = 1  # Diese Zeile dient nur als Platzhalter

    start_date = date.today() - timedelta(days=364)
    
    progress_data = Progress.query.filter(
        Progress.user_id == user_id,
        Progress.date >= start_date
    ).order_by(Progress.date.asc()).all()
    
    if not progress_data:
        # Hier können Sie entscheiden, ob Sie eine Fehlermeldung oder leere Listen zurückgeben
        error_message = "Keine Fortschrittsdaten verfügbar."
        return render_template('fortschritt.html', error_message=error_message)

    # Vorbereiten der Daten für die Darstellung im Grid
    slept_well_data = [{'date': p.date.strftime('%Y-%m-%d'), 'value': p.slept_well} for p in progress_data]
    workout_data = [{'date': p.date.strftime('%Y-%m-%d'), 'value': p.workout_completed} for p in progress_data]
    
    # Daten an die HTML-Vorlage senden
    return render_template('fortschritt.html', slept_well_data=slept_well_data, workout_data=workout_data)









# Anwendungsstartpunkt
if __name__ == '__main__':
    app.run(debug=True)
