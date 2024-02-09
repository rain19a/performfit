---
title: Design Decisions
nav_order: 3
---

{: .label }
Ömer Öztürk

# Design decisions
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>


---

## 01.Datenbankdesign für Workout-Informationen

### Meta
{: .no_toc }

- **Status:** Fertig - Entschieden
- **Aktualisiert am:** 11.01.2024

### Problemstellung
{: .no_toc }
Beim Entwurf unserer Workout-Datenbank galt es zu bestimmen, welche essenziellen Informationen zur Unterstützung unserer Nutzer erforderlich sind, ohne überflüssige Daten zu erheben. Die Herausforderung lag darin, eine ausgewogene Lösung zu finden, die sowohl nützlich als auch benutzerfreundlich ist.

### Entscheidung
{: .no_toc }
Nach gründlicher Beratung wurde entschieden, sich auf die Erfassung der Kernelemente eines Workouts zu konzentrieren: die durchgeführten Übungen, Anzahl der Wiederholungen und Sätze. Informationen zur Dauer und Intensität werden den Nutzern überlassen und können in einem optionalen Notizfeld festgehalten werden.

### Betrachtete Optionen
{: .no_toc }
- **Pro:**
  - Ermöglicht genaues Tracking von Workouts.
  - Wesentlich für die Messung des Fortschritts und Anpassung der Trainingspläne.
- **Contra:**
  - Kann für Anfänger oder Gelegenheitsnutzer überfordernd sein.
  - Erwartet präzise Angaben von den Nutzern.

### Umsetzung
{: .no_toc }
Basierend auf der Abwägung von Vor- und Nachteilen wurde beschlossen, die Attribute Dauer und Intensität nicht in die Hauptdatenbankstruktur aufzunehmen.

---

## 02.Gridgraph-Visualisierung für Workout-Fortschritt

### Meta
{: .no_toc }

- **Status:** - Entschieden
- **Aktualisiert am:** 11.01.2024

### Problemstellung
{: .no_toc }
Es wurde eine visuelle Methode benötigt, um den Fortschritt im Workout-Programm auf motivierende und ansprechende Weise darzustellen.

### Entscheidung
{: .no_toc }

Die Wahl fiel auf die Einführung einer Gridgraph-Visualisierung mit Farben und Symbolen, um einen direkten Überblick über den Fortschritt zu ermöglichen und zugleich motivierend zu wirken.

### Betrachtete Optionen
{: .no_toc }
- **Nur Zahlen und Tabellen:**
  - **Vorteil:** Sehr präzise.
  - **Nachteil:** Kann als monoton empfunden werden und wenig motivieren.
- **Gridgraph mit Farben und Symbolen:**
  - **Vorteil:** Visuell ansprechend und intuitiv.
  - **Nachteil:** Kann bei längerer Nutzung eintönig wirken und Herausforderungen bei Updates darstellen.
- **Mix aus beidem:**
  - **Vorteil:** Vereint Genauigkeit mit visueller Attraktivität.
  - **Nachteil:** Technisch anspruchsvoll in der Umsetzung.

### Umsetzung
{: .no_toc }
Um die Komplexität zu reduzieren und den Überblick zu bewahren, wurde eine einfache Ja/Nein-Funktion implementiert, die es Nutzern ermöglicht, Fortschritte einfach zu markieren und den Gridgraph übersichtlich zu halten.

---

## 03. Auswahl des Bootstrap-Frameworks für eine bessere Benutzeroberfläche

### Meta
{: .no_toc }
- **Status:** Fertig - Entschieden
- **Aktualisiert am:** 05.02.2024

### Problemstellung
{: .no_toc }
Die Auswahl eines Frontend-Frameworks war entscheidend, um unseren Nutzern eine ansprechende und intuitive Benutzeroberfläche zu bieten. Wir benötigten ein Framework, das sowohl flexibel als auch mächtig ist, um unsere Designvisionen umzusetzen.

### Entscheidung
{: .no_toc }
Nach der Bewertung mehrerer Optionen haben wir uns für Bootstrap entschieden. Bootstrap bietet eine umfangreiche Sammlung vordefinierter Komponenten, die nicht nur die Entwicklung beschleunigen, sondern auch sicherstellen, dass die Anwendung auf verschiedenen Geräten gut aussieht und funktioniert. Es wurde als die beste Wahl angesehen, um unsere ästhetischen Anforderungen zu erfüllen und die Benutzererfahrung zu verbessern.

### Betrachtete Optionen
{: .no_toc }
- **Material Design:**
  - **Vorteil:** Modernes und konsistentes Design.
  - **Nachteil:** Möglicherweise weniger Anpassungsfähigkeit für spezifische Designanforderungen.
- **Foundation:**
  - **Vorteil:** Flexibles Grid-System und anpassungsfähige Komponenten.
  - **Nachteil:** Steilere Lernkurve im Vergleich zu Bootstrap.
- **Bootstrap:**
  - **Vorteil:** Weit verbreitet, reaktionsfähig und intuitiv.
  - **Nachteil:** Standard-Bootstrap-Themen können zu ähnlich aussehenden Websites führen.

### Umsetzung
{: .no_toc }
Bootstrap wurde in unser Entwicklungsworkflow integriert, um die Benutzeroberfläche zu standardisieren und zu verfeinern. Zusätzlich wurde ein Theme angepasst, um ein einzigartiges Aussehen zu gewährleisten, das sich von Standard-Bootstrap-Designs unterscheidet.


---


## 04. Gestaltung der Startseite mit Bild

### Meta
{: .no_toc }
- **Status:** Fertig - Entschieden
- **Aktualisiert am:** 14.12.2023

### Problemstellung
{: .no_toc }
Die Gestaltung der Startseite ist kritisch für den ersten Eindruck der Nutzer. Es galt zu entscheiden, ob die Startseite direkt mit einem Login beginnen oder mit einem einladenden Bild, um die Nutzer willkommen zu heißen.

### Entscheidung
{: .no_toc }
Es wurde entschieden, die Startseite mit einem Bild zu gestalten, um eine einladende Atmosphäre zu schaffen. Dies soll helfen, die Nutzer positiv zu stimmen und ihr Interesse an der Plattform zu wecken, bevor sie aufgefordert werden, sich anzumelden oder zu registrieren.

### Betrachtete Optionen
{: .no_toc }
- **Startseite mit Login:**
  - **Vorteil:** Schneller Zugriff auf Benutzerkonten.
  - **Nachteil:** Kann als unfreundlich oder geschäftsmäßig wahrgenommen werden.
- **Startseite mit Bild:**
  - **Vorteil:** Schafft eine einladende und warme Erstbegegnung.
  - **Nachteil:** Verzögert möglicherweise den Zugang zu Benutzerfunktionen.

### Umsetzung
{: .no_toc }
Die Startseite wird ein ansprechendes, thematisch passendes Bild anzeigen, das die Kernbotschaft der Plattform visuell vermittelt. Die Option zum Login oder zur Registrierung wird dezent, aber deutlich sichtbar platziert.

---

## 05. Dashboard als Startpunkt nach dem Login

### Meta
{: .no_toc }
- **Status:** Fertig - Entschieden
- **Aktualisiert am:** 17.01.2024

### Problemstellung
{: .no_toc }
Nach dem Login muss entschieden werden, welche Seite den Nutzern als erstes präsentiert wird. Die Wahl stand zwischen dem Fortschrittstracker, dem Dashboard und dem Workoutplan.

### Entscheidung
{: .no_toc }
Das Dashboard wird als erste Seite nach dem Login festgelegt. Dies wurde entschieden, da die Nutzer hier ihre Einträge machen, die dann auf dem Fortschrittstracker zu sehen sind. Somit ist das Dashboard der zentrale Anlaufpunkt für die Nutzeraktivitäten.

### Betrachtete Optionen
{: .no_toc }
- **Fortschrittstracker als Startseite:**
  - **Vorteil:** Fokus auf die Überwachung der Fortschritte.
  - **Nachteil:** Weniger Kontext für neue Einträge oder Überblick.
- **Dashboard:**
  - **Vorteil:** Zentraler Anlaufpunkt für alle Nutzeraktivitäten.
  - **Nachteil:** Könnte überladen wirken, wenn nicht gut strukturiert.
- **Workoutplan:**
  - **Vorteil:** Direkter Start in die Trainingsplanung.
  - **Nachteil:** Vernachlässigt andere wichtige Aspekte wie Fortschrittsüberwachung.

### Umsetzung
{: .no_toc }
Das Dashboard wird so gestaltet, dass es eine Übersicht der letzten Aktivitäten sowie schnellen Zugriff auf die wichtigsten Funktionen bietet. Ein klar strukturiertes Layout soll dabei helfen, Überladung zu vermeiden.

---

