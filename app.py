from flask import render_template, request, redirect, url_for
from werkzeug.security import check_password_hash
from db import app, db, User

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
        workout_completed = 'workout' in request.form
        slept_well = 'sleep' in request.form
        print(f"Workout completed: {workout_completed}, Slept well: {slept_well}")
        return redirect(url_for('dashboard'))
    
    return render_template('dashboard.html')

# Anwendungsstartpunkt
if __name__ == '__main__':
    app.run(debug=True)
