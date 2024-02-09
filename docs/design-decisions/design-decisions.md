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

## Datenbankdesign für Workout-Informationen

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

## Gridgraph-Visualisierung für Workout-Fortschritt

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

## 03: Gridgraph-Visualisierung - Farbwahl


### Meta
{: .no_toc }
Status
: **Work in progress** - Decided 

Updated
: 11-01-2024

### Problem statement
{: .no_toc }


### Decision
{: .no_toc }


### Regarded options
{: .no_toc }

---

## 04: ----


### Meta
{: .no_toc }
Status
: **Work in progress** - Decided 

Updated
: 11-01-2024

### Problem statement
{: .no_toc }


### Decision
{: .no_toc }


### Regarded options
{: .no_toc }

---

## 05: ----


### Meta
{: .no_toc }
Status
: **Work in progress** - Decided 

Updated
: 11-01-2024

### Problem statement
{: .no_toc }


### Decision
{: .no_toc }


### Regarded options
{: .no_toc }
