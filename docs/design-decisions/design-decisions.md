---
title: Design Decisions
nav_order: 3
---

{: .label }
[Kubilay Jessa]

# [Design decisions]
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: [Datenbankdesign für Workouts]

### Meta

Status
: **Work in progress** - Decided 

Updated
: 11-01-2024

### Problem statement

[Describe the problem to be solved or the goal to be achieved. Include relevant context information.]

Beim Aufbau unserer Workout-Datenbank waren wir uns nicht sicher, welche Infos wir wirklich brauchen. Wir dachten erst an Dauer und Intensität, aber irgendwie schien das wohlmöglich zu viel vom User sein. Wir brauchten was Besseres, etwas, das unseren Nutzern wirklich hilft, ohne unnötige Daten zu sammeln.


### Decision

[Describe **which** design decision was taken for **what reason** and by **whom**.]

Okay, also haben wir uns hingesetzt und entschieden, dass wir uns auf die Basics konzentrieren: Welche Übungen, wie viele Wiederholungen und wie viele Sätze. Dauer und Intensität? Die packen wir lieber in ein optionales Notizfeld. Wir waren uns nämlich nicht sicher, wie wir "Intensität" am besten definieren sollten. Wir zusammen fanden es sinnvoller den Nutzern zu erlauben, ihre eigenen Eindrücke und Notizen dazu zu machen, anstatt zu versuchen, das irgendwie standardmäßig in die Datenbank einzubauen.

### Regarded options

[Describe any possible design decision that will solve the problem. Assess these options, e.g., via a simple pro/con list.]

Pro:
Ermöglicht präzises Tracking von Workout-Leistungen.
Wichtig für die Feststellung von Fortschritt und Anpassung des Trainings.

Contra:
Kann für Anfänger oder Gelegenheitsnutzer zu detailliert sein.
Erfordert genaue Eingaben von den Nutzern.

Nach eingehender Bewertung der Vor- und Nachteile haben wir uns entschieden, in unserer Datenbankstruktur für Workouts die Attribute Dauer und Intensität nicht aufzunehmen.

---

## 02: [Gridgraph-Visualisierung für Workout-Fortschritt]

### Meta

Status
: **Work in progress** - Decided 

Updated
: 11-01-2024

### Problem statement
Wir brauchten eine coole Art, um den Fortschritt im Workout-Programm zu zeigen. Tabellen und Zahlen sind okay, aber wir wollten etwas, das unsere Nutzer richtig motiviert und ihnen schnell zeigt, wie gut sie vorankommen.

### Decision

Also haben wir uns überlegt, eine Gridgraph-Visualisierung zu machen. Mit bunten Farben und Symbolen, damit es richtig ins Auge springt. Wir wollten, dass unsere Nutzer einen Blick drauf werfen und sofort sehen, was Sache ist - wie weit sie gekommen sind und wo sie noch was drauflegen können.


### Regarded options

Nur Zahlen und Tabellen
Vorteil: Super genau und gibt alle Details.
Nachteil: Kann langweilig sein, nicht gerade motivierend.

Gridgraph mit Farben und Symbolen
Vorteil: Sieht gut aus, macht Spaß beim Angucken.
Nachteil: Kann nach längerer Nutzung zu eintönig werden und schwierig mit der automatischen Aktualisierung der Workouts.

Mix aus beidem
Vorteil: Hat alles – die Genauigkeit und den Look.
Nachteil: Könnte echt knifflig werden, das hinzubekommen.


Lösung für die Nachteile
Um das Problem mit dem „Zu-viel-des-Guten“ und der komplizierten Umsetzung zu lösen, haben wir uns was Cleveres überlegt: Wir bauen eine einfache Ja-Nein-Funktion ein. Damit können die Nutzer ihren Fortschritt markieren, ohne dass es zu überladen wird. So bleibt der Gridgraph übersichtlich und leicht zu verstehen.

---