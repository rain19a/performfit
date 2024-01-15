---
title: App Structure
parent: Technical Docs
nav_order: 1
---

{: .label }
[Ömer Öztürk]

# [App structure, incl. context]
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>


Inhaltsverzeichnis

1. Einleitung
2. Value Proposition
3. App-Struktur
- App-Verhalten
- Datenmodell
- Framework
- UML-Diagramm
4. Designentscheidungen
5. Nutzerbewertung
6. Erreichte und verfehlte Ziele
7. Verbesserungsvorschläge für das nächste Mal
8. Peer-Review
9. Zusammenfassung des individuellen Beitrags
10. Literaturverzeichnis
11. Abbildungsverzeichnis




3.1 App - Verhalten

# Einleitung
Diese Dokumentation bietet eine Übersicht über den User Flow innerhalb der PerformFit-App. Sie soll neuen Entwicklern, Designern und Produktmanagern einen klaren Leitfaden für die Navigation und Funktionalität der App aus Nutzersicht geben.

# Registrierungs- und Login-Prozess
Registrierung
Neue Nutzer durchlaufen einen Registrierungsprozess, bei dem sie aufgefordert werden, folgende Informationen bereitzustellen:

E-Mail-Adresse
Gewünschter Benutzername
Passwort

Bestehende Nutzer melden sich mit ihrem Benutzernamen und Passwort an. Alternativ ist ein Gastzugang ohne Registrierung möglich.

# Initialer Fragekatalog
Nach erfolgreicher Registrierung werden neue Nutzer durch einen Fragekatalog geleitet, der dazu dient, das Fitnessniveau zu erfassen und individuelle Ziele zu setzen. Die Fragen beinhalten:

Fitnesserfahrung (Anfänger/Fortgeschrittener)
Aktuelles Gewicht
Zielgewicht

# Dashboard
Das Dashboard ist die zentrale Anlaufstelle für Nutzer nach dem Login. Es enthält:

Schnellzugriff auf Hauptfunktionen wie Workoutplan und Fortschrittstracker

# Workoutplan
Nutzer erhalten basierend auf ihrem initialen Fragekatalog personalisierte Trainingspläne. Innerhalb der Trainingsplan-Funktion können Nutzer:

Ihre Trainingsdaten eingeben, einschließlich Gewicht, Übung, Wiederholungen, Sätze und Notizen für jede Übung.
Ihre Trainingsfortschritte überprüfen und aktualisieren.

# Fortschrittstracker
Der Fortschrittstracker bietet eine visuelle Darstellung des Trainingsfortschritts mit einem Gitterdiagramm, in dem:

Abgeschlossene Workouts in Grün markiert werden.
Nicht abgeschlossene Workouts in Grau erscheinen.
Die Erfassung der Workouts erfolgt durch eine einfache Ja/Nein-Abfrage, um die Nutzerinteraktion zu erleichtern und eine genaue Nachverfolgung zu gewährleisten.


Diese Dokumentation soll eine klare und präzise Beschreibung des User Flows in der PerformFit-App bieten und die Navigation sowie die Hauptfunktionen für das Team verständlich machen.
