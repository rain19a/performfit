---
title: App Behavior
parent: Technical Docs
nav_order: 2
---

{: .label }
Ömer Öztürk

# App behavior
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>


## 1. Einleitung
Diese Dokumentation konzentriert sich auf das Verhalten der PerformFit-App, indem sie detailliert beschreibt, wie die App auf Benutzerinteraktionen reagiert und welche Prozesse im Hintergrund ablaufen. Ziel ist es, einen tiefgreifenden Einblick in die Funktionsweise der App aus Nutzersicht zu geben.

## 2. Registrierungs- und Login-Prozess
Registrierung
Benutzeraktion: Der Nutzer gibt seine E-Mail-Adresse, einen gewünschten Benutzernamen und ein Passwort auf der Registrierungsseite ein.
Systemreaktion: Die App überprüft die Einzigartigkeit von E-Mail-Adresse und Benutzername in der Datenbank. Bei Erfolg wird der neue Benutzer gespeichert, das Passwort verschlüsselt und der Benutzer wird automatisch eingeloggt.
Feedback: Der Nutzer erhält eine Bestätigung der erfolgreichen Registrierung oder eine Fehlermeldung, falls die E-Mail/Benutzername bereits verwendet werden.

Login
Benutzeraktion: Bestehende Nutzer geben ihren Benutzernamen und ihr Passwort ein.
Systemreaktion: Die App prüft die Anmeldeinformationen gegen die Datenbank. Bei Übereinstimmung wird eine Session erstellt.
Feedback: Der Nutzer wird zum Dashboard weitergeleitet oder erhält bei Fehlern eine entsprechende Meldung.

## 3. Initialer Fragekatalog
Benutzeraktion: Neue Nutzer beantworten Fragen zu ihrer Fitnesserfahrung, aktuellem Gewicht und Zielgewicht.
Systemreaktion: Die Antworten werden im Benutzerprofil gespeichert und unter dem Fortschrittstracker angezeigt.

## 4. Dashboard
Übersicht: Das Dashboard dient als zentrale Anlaufstelle und bietet Schnellzugriff auf den Workoutplan und dem Fortschrittstracker.
Interaktion: Nutzer können ihre täglichen Aktivitäten einsehen, Workouts planen und ihren Fortschritt verfolgen.
Anpassung: Das Dashboard passt sich dynamisch an die gespeicherten Benutzerdaten und deren Fortschritte an.

## 5. Workoutplan
Erstellung: Basierend auf dem initialen Fragekatalog und fortlaufenden Eingaben wie z.b akutelles Gewicht und Zielgewicht speichert er diese im Fortschrittstracker ab.
Eingabe: Nutzer tragen Daten zu ihren Workouts ein, inklusive Übungen, Wiederholungen, Sätze und Notizen.
Aktualisierung: Die App aktualisiert den Fortschritt und passt den Trainingsplan entsprechend an.

## 6. Fortschrittstracker
Visualisierung: Der Fortschrittstracker bietet eine graphische Darstellung des Trainingsfortschritts, markiert abgeschlossene Workouts in Grün und Bezug auf die Schlafqualität in Blau.
Interaktion: Die Erfassung der Workouts und der Schlafqualität erfolgt über das Auswählen der Checkbox im Dashboard.
Feedback: Nutzer erhalten ein sofortiges visuelles Feedback zu ihrem Trainingsfortschritt.