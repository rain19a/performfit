---
title: User Evaluation
nav_order: 4
---

{: .label }
Ömer Öztürk

# User evaluation
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Reaktion von Fehlermeldungen der Registrierungsseite

### Meta
{: .no_toc }
Status
: Done

Updated
: 02-02-2024

### Goal
{: .no_toc }
Das Ziel dieser Bewertung war es, die Wirksamkeit und Benutzerfreundlichkeit des Registrierungsprozesses zu überprüfen, um sicherzustellen, dass Nutzer ohne Hindernisse ein Konto erstellen können.

### Method
{: .no_toc }
Eine Code-Inspektion und ein simulierter Durchlauf des Registrierungsvorgangs wurden durchgeführt. Kubilay hat den Registrierungsprozess mehrmals durchgespielt, um mögliche Fehlerquellen und Unklarheiten im Prozess zu identifizieren.

### Results
{: .no_toc }
Die Überprüfung zeigte, dass der Prozess im Großen und Ganzen klar und einfach zu befolgen ist. Allerdings sind die Fehlermeldungen bezüglich der E-Mail-Adresse nicht immer präzise. Insbesondere fehlt eine klare Anweisung oder Rückmeldung, wenn Nutzer eine inkorrekte E-Mail-Formatierung verwenden. 

Was zu Verwirrung führen und die Registrierung unnötig verkomplizieren kann. Zudem wurde festgestellt, dass es keine deutlichen Hinweise zu den Passwortanforderungen gibt, was die Sicherheit der Konten beeinträchtigen und zu Frustration bei den Nutzern führen kann, wenn ihre Passwörter bei der Erstanmeldung abgelehnt werden.

### Implications
{: .no_toc }
Basierend auf diesen Erkenntnissen wird dringend empfohlen, die Fehlermeldungen zu verbessern, insbesondere durch die Einführung klarer Hinweise zur korrekten E-Mail-Formatierung. Ein Formatierungscheck sollte implementiert werden, der in Echtzeit Feedback gibt, sobald das E-Mail-Feld den Fokus verliert. 

Dies würde Nutzern sofortige Rückmeldung geben und die Benutzererfahrung erheblich verbessern. Ebenso sollten klare Richtlinien und Anforderungen für die Passworterstellung direkt auf der Registrierungsseite angezeigt werden, um die Nutzer über die Sicherheitsanforderungen aufzuklären. Diese Änderungen könnten dazu beitragen, die Abbruchrate zu verringern und die allgemeine Zufriedenheit und Sicherheit der Nutzer zu erhöhen.

---

## 02: Passwortwiederherstellung im LoginProzes

### Meta
{: .no_toc }
Status
: Obsolete

Updated
: 20-01-2024

### Goal
{: .no_toc }
Das Ziel war es, die Effizienz und Sicherheit des Login-Prozesses zu bewerten, mit einem besonderen Fokus auf Benutzererfahrung und Datensicherheit.

### Method
{: .no_toc }
Ich habe eine systematische Überprüfung des Login-Codes und eine Reihe von Tests durchgeführt, um die Authentifizierung unter verschiedenen Bedingungen zu überprüfen, einschließlich falscher Passwörter und Benutzernamen.


### Results
{: .no_toc }
Der Login-Prozess funktioniert zuverlässig und schließt Sicherheitslücken, wie das Auslesen von Passwörtern, aus. Es fehlt jedoch eine Funktion zur Passwortwiederherstellung, was ein Problem für Nutzer darstellen kann, die ihre Anmeldedaten vergessen.

Allerdings wurde diese Methode im Rahmen dieses Webprojekts nicht angewandt, da das Fehlen von Testnutzern die Anwendung dieser Methode nicht sinnvoll erscheinen lässt und sie für unsere Zwecke nicht erforderlich ist.


### Implications
{: .no_toc }
Es wird vorgeschlagen, eine Passwortwiederherstellungsfunktion zu implementieren, um die Benutzererfahrung zu verbessern. Dies würde auch die Sicherheit der Nutzerkonten erhöhen, da Nutzer weniger geneigt sein könnten, einfache, leicht zu merkende Passwörter zu verwenden. 


---

## 03: Einfache Dashboard-Interaktion 


### Meta
{: .no_toc }
Status
: Done

Updated
: 09-02-2024

### Goal
{: .no_toc }
Die Evaluation des Dashboards zielte darauf ab, die Benutzerfreundlichkeit und die Effektivität der präsentierten Daten zu analysieren.

### Method
{: .no_toc }
Für diese Bewertung wurde dies im Dashboards durchgeführt, um zu bestimmen, wie intuitiv die Benutzerschnittstelle ist und wie schnell Nutzer die benötigten Informationen finden können.


### Results
{: .no_toc }
Das Dashboard ist  einfach organisiert und bietet schnellen Zugriff auf die wichtigsten Funktionen wie Fortschrittstracker und Workoutplan. Allerdings könnten die visuellen Elemente zur Darstellung des Fortschritts verbessert werden, um die Klarheit zu erhöhen.


### Implications
{: .no_toc }
Eine Überarbeitung des Dashboard-Designs mit klareren visuellen Fortschrittsindikatoren und einer intuitiveren Anordnung der Benutzerelemente könnte die Nutzererfahrung signifikant verbessern und haben daher die dies durch eine Weiterleitung auf den Fortschrrittstracker erweitert.

---


## 04: Gridgraphen des Fortschritt- und Schlafstrackers   


### Meta
{: .no_toc }
Status
: Done

Updated
: 09-02-2024

### Goal
{: .no_toc }
Die Evaluation der Fortschrittstracker-Funktionalität hatte zum Ziel, die Wirksamkeit und Nutzerfreundlichkeit dieser Komponente in der PerformFit-App zu beurteilen. Im Fokus stand dabei insbesondere, wie gut die App es den Nutzern ermöglicht, ihren Trainingsfortschritt visuell zu erfassen und zu verfolgen.

### Method
{: .no_toc }
In Ermangelung von Testnutzern wurde eine interne Prüfung sowohl des Schlaf- als auch des Workout-Fortschrittstrackers durchgeführt. Diese Prüfung umfasste eine detaillierte Analyse der Benutzeroberfläche und des Datenflusses für beide Tracker, um zu bewerten, wie Informationen präsentiert werden und wie intuitiv die Interaktion mit den Fortschrittstrackern ist. 

Es wurde speziell untersucht, wie aktuell die in den Trackern dargestellten Informationen sind und wie diese Informationen die Motivation der Nutzer beeinflussen könnten.

### Results
{: .no_toc }
Die interne Untersuchung zeigte, dass der Fortschrittstracker für Workouts und Schlaf jeweils eine effektive und motivierende Darstellung des Nutzerfortschritts bietet, mit einer spezifischen Farbkodierung: Abgeschlossene Workouts werden in Grün und die erzielte Schlafqualität in Blau dargestellt. 

Diese Farbkodierung erleichtert es den Nutzern, ihren Fortschritt in beiden Bereichen auf einen Blick zu erfassen und motiviert zur Fortsetzung ihrer Bemühungen. Es wurde jedoch festgestellt, dass die Aktualisierung der Daten in beiden Trackern nicht immer in Echtzeit erfolgt, was zu einer verzögerten Darstellung führen kann.

### Implications
{: .no_toc }
Die Erkenntnisse legen nahe, dass eine Optimierung der Datenaktualisierung in beiden Fortschrittstrackern notwendig ist, um eine zeitnahe und genaue Darstellung des Fortschritts zu gewährleisten.

Die Einführung von Fortschrittsmeilensteinen mit spezifischen Belohnungen oder Anerkennungen für das Erreichen von Zielen im Bereich Training und Schlaf könnte eine wirksame Methode sein, um Motivation zu schaffen.

---

## 05: Workoutplan-Funktionalität
   
### Meta
{: .no_toc }
Status
: Done

Updated
: 09-02-2024

### Goal
{: .no_toc }
Das Ziel der Evaluation war es, die Funktionalität und Benutzerfreundlichkeit der Workoutplan-Komponente der PerformFit-App zu beurteilen, einschließlich der Einfachheit der Dateneingabe und der Personalisierung der Trainingspläne.


### Method
{: .no_toc }
Da keine echten Nutzer zur Verfügung standen, wurde eine interne Überprüfung durchgeführt. Dabei wurden verschiedene Szenarien durchgespielt, um die Benutzerführung und die logische Struktur der Trainingsplaneingabe zu bewerten.

Zusätzlich wurde der zugrunde liegende Code analysiert, um sicherzustellen, dass die Daten korrekt verarbeitet und gespeichert werden.

### Results
{: .no_toc }
Die interne Überprüfung ergab, dass die Eingabe von Trainingsdaten intuitiv und die Benutzeroberfläche klar gestaltet ist. Nutzer können problemlos Details wie Gewicht, Übung, Wiederholungen und Sätze eingeben.

Die Personalisierung basiert auf den eingegebenen Nutzerdaten und passt sich entsprechend deren Fortschritt an. Ein potenzieller Engpass könnte die mangelnde Flexibilität bei der Anpassung der Trainingspläne sein, wenn Nutzer ihre Ziele ändern oder spezielle Anforderungen haben.


### Implications
{: .no_toc }
Basierend auf dieser Bewertung wird empfohlen, weitere Anpassungsoptionen für den Trainingsplan einzuführen, um eine höhere Flexibilität zu gewährleisten. Dies könnte durch erweiterte Nutzereingaben oder durch adaptive Algorithmen erreicht werden, die auf Änderungen in den Benutzerzielen reagieren. 

Des Weiteren sollte in Betracht gezogen werden, zusätzliche Unterstützung für Nutzer zu implementieren, die möglicherweise Hilfe bei der korrekten Ausführung von Übungen benötigen, etwa durch Video-Tutorials oder integrierte Beschreibungen.
