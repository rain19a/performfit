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