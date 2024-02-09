---
title: Reference
parent: Technical Docs
nav_order: 4
---

{: .label }
Ömer Öztürk

# Reference documentation
{: .no_toc }



<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## User Management

### `register()`

**Route:** `/register/`

**Methods:** `POST` 

**Purpose:** Registriere einen neuen Benutzer mit den angegebenen Details.

**Sample output:**

Weiterleitung zum 'fragenkatalog' bei erfolgreicher Registrierung.


`return redirect(url_for('fragenkatalog'))`


Bei Misserfolg aufgrund eines bereits existierenden Benutzernamens oder E-Mail-Adresse:


`return render_template('registration.html', error_message=error_message)`



### `login()`

**Route:** `/login/`

**Methoden:**  `POST` 

**Purpose:** Zweck: Melde einen vorhandenen Benutzer mit ihrem Benutzernamen und Passwort an.

Weiterleitung zum 'dashboard' bei erfolgreicher Anmeldung.


`return redirect(url_for('dashboard'))` 


Bei Misserfolg aufgrund falscher Anmeldeinformationen:

` return "Falscher Benutzername oder Passwort"` 


` logout()` 
Route: ` /logout/` 

Methoden: GET

Zweck: Meldet den aktuellen Benutzer ab.

Weiterleitung zur 'index' nach der Abmeldung.

` return redirect(url_for('index'))` 



---

##  Dashboard

**Route:** `dashboard()`

**Methods:** `GET` `POST`

**Purpose:** Zeige das Dashboard des Benutzers mit ihrem Fortschritt, Trainingsplänen und anderen relevanten Informationen an.

**Sample output:**


` return render_template('dashboard.html')` 

---

## Fortschrittsverfolgung

**Route:** `/fortschritt/`

**Methods:** `GET` `POST`

**Purpose:** Verfolge den Fortschritt des Benutzers über die Zeit, einschließlich Gewichtsänderungen, abgeschlossener Workouts und Schlafqualität.

**Sample output:**

Rendert das 'fortschritt.html' Template mit visuellen Darstellungen der Fortschrittsdaten des Benutzers.

` return render_template('fortschritt.html', ` 
                      `  user=user, ` 
                    ` entfernung_zum_ziel=entfernung_zum_ziel, ` 
                       ` slept_well_data=slept_well_data, ` 
                       ` workout_data=workout_data) ` 


---

##  Workout-Verwaltung

### `workout_plan()`

**Route:** `/workoutplan/`

**Methods:** `GET` `POST`

**Purpose:** Verwalte die Trainingspläne des Benutzers, einschließlich Hinzufügen, Bearbeiten und Löschen von Workouts.

**Sample output:**

Rendert das 'workoutplan.html' Template mit den vorhandenen Workouts des Benutzers und ermöglicht CRUD-Operationen.


` return render_template('workoutplan.html', trainings=trainings, training_days=training_days)` 


---

##  Workout-Verwaltung

### `trainingsinhalt()`

**Route:** `/trainingsinhalt/<string:day>/<string:training_name>`

**Methods:** `GET` 

**Purpose:** Ruft die Details einer bestimmten Trainingssitzung ab und zeigt sie an.

**Sample output:**

Rendert das 'trainingsinhalt.html' Template mit den Details der ausgewählten Trainingssitzung.


` return render_template('trainingsinhalt.html', day=day, training_name=training_name, trainingsinhalte=trainingsinhalte, training_day_id=training_day.id)` 

---

##  Workout-Verwaltung

### `add_training_and_day()`

**Route:** `/workoutplan/add/`

**Methods:** `POST` 

**Purpose:** Füge ein neues Training und einen Trainingstag hinzu.

**Sample output:**

Weiterleitung zum 'workout_plan' nach Hinzufügen des Trainings und des Trainingstages.


` return redirect (url_for('workout_plan'))` 


### ` delete_training_or_day()` 

**Route:** ` /workoutplan/delete/` 

**Methods:** `POST`

**Purpose:** Lösche ein spezifisches Training oder einen Trainingstag.

**Sample output:**

Weiterleitung zum 'workout_plan' nach dem Löschen des Trainings oder des Trainingstages.


` return redirect(url_for('workout_plan'))` 


**Route:** ` add_trainingsinhalt()` 

**Methods:** `POST`

**Purpose:** Füge neue Trainingsinhalte zu einem Trainingstag hinzu.

**Sample output:**

Nach erfolgreichem Hinzufügen Weiterleitung zur 'trainingsinhalt' Seite.


` return redirect(url_for('trainingsinhalt', day=day, training_name=training_name))` 


Bei einem Fehler wird eine Fehlermeldung angezeigt und der Benutzer zur vorherigen Seite zurückgeleitet.


` flash(f'Fehler beim Hinzufügen der Übung: {e}', 'danger')` 
` return redirect(request.referrer)` 


### ` remove_trainingsinhalt()` 

**Route:** ` /remove_trainingsinhalt/<int:inhalt_id>/` 

**Methods:** `POST`

**Purpose:** Entferne spezifische Trainingsinhalte eines Trainingstages.

Nach dem Entfernen Weiterleitung zur vorherigen Seite.

` return redirect(request.referrer)` 


