+++
title = "Regelbasierter Chatbot"
translationKey = "rule-based"
description = "Ein regelbasierter Chatbot interagiert mit Nutzern, indem er vordefinierten Regeln und Skripten folgt und auf bestimmte Schlüsselwörter oder Button-Auswahlen ohne KI-Lernen reagiert."
keywords = [
  "regelbasierter Chatbot",
  "Chatbot",
  "Entscheidungsbaum",
  "Automatisierung",
  "Kundensupport"
]
category = "KI-Chatbot & Automatisierung"
type = "glossary"
date = 2025-12-05
lastmod = 2025-12-05
draft = false
url = "/internal/glossary/Rule-Based-Chatbot/"

+++
## Was ist ein regelbasierter Chatbot?

Ein **regelbasierter Chatbot** ist eine Art Konversationssoftware, die mit Nutzern anhand eines Satzes vordefinierter Regeln, Skripte oder Entscheidungsbäume interagiert. Anstatt künstliche Intelligenz oder maschinelles Lernen zu verwenden, reagiert er auf bestimmte Schlüsselwörter, Phrasen oder Button-Auswahlen. Diese Bots können nicht improvisieren oder aus Benutzerdaten „lernen“; ihr Verhalten wird vollständig durch ihre anfängliche Programmierung bestimmt.

- **Andere Bezeichnungen:** Entscheidungsbaum-Bots, Skript-Bots, Menü-Bots.  
- **Keine „echte“ KI:** Regelbasierte Bots nutzen kein maschinelles Lernen oder NLP wie KI-basierte Bots. Sie führen einfache Automatisierung aus, kein intelligentes Verständnis.  
- **Vorhersehbarkeit:** Jede mögliche Interaktion ist im Voraus festgelegt. Wenn der Nutzer von diesen Pfaden abweicht, gibt der Bot eine generische Antwort oder bietet eine Weiterleitung an einen Menschen an.
## Wie funktionieren regelbasierte Chatbots?

Regelbasierte Chatbots funktionieren wie interaktive Flussdiagramme oder Entscheidungsbäume. Ihr Betrieb wird durch ein einfaches Konzept gesteuert: **„Wenn der Nutzer X sagt, antworte mit Y.“** Jedes Nutzereingabe wird einer Regel zugeordnet, die eine entsprechende Antwort auslöst.

### Zentrale Komponenten

- **Trigger:**  
  Bestimmte Wörter, Phrasen oder Aktionen, die die Reaktion des Bots auslösen. Beispielsweise erkennt der Bot „Bestellstatus“ als Trigger, wenn der Nutzer das eintippt.

- **Regeln/Logik:**  
  Bedingte Anweisungen (if/then-Logik), die festlegen, wie der Bot auf Trigger reagiert. Beispiel: „Wenn der Nutzer nach Öffnungszeiten fragt, zeige die Zeiten an.“

- **Vordefinierte Antworten:**  
  Vorgefertigte Antworten (Text, Links, Buttons), die der Bot als Reaktion auf Trigger liefert.

- **Fallbacks:**  
  Standardantworten, wenn der Bot die Nutzereingabe keiner Regel zuordnen kann. Oft ist dies eine höfliche Fehlermeldung oder das Angebot, an einen menschlichen Agenten weiterzuleiten.

- **Kein Lernen:**  
  Die Fähigkeiten des Bots entwickeln sich nicht weiter. Jede Verhaltensänderung erfordert eine manuelle Anpassung und Regelaktualisierung.
### Schritt-für-Schritt-Beispiel

**Szenario: Online-Shop-Chatbot**

1. **Nutzer öffnet den Chat:**  
   Bot zeigt an: „Hallo! Wie kann ich Ihnen helfen? (Bestellstatus, Rückgaben, FAQ)“

2. **Nutzer tippt „Bestellstatus“:**  
   Bot: „Bitte geben Sie Ihre Bestellnummer ein.“

3. **Nutzer gibt Bestellnummer ein:**  
   Bot: Sucht die Bestellung in der Datenbank und liefert Tracking-Informationen.

4. **Nutzer fragt nach einem Produkt, das nicht im Skript ist:**  
   Bot: „Entschuldigung, dabei kann ich nicht helfen. Möchten Sie mit einem menschlichen Agenten sprechen?“

Jeder Schritt, einschließlich Folgefragen und möglicher Nutzer-Umwege, ist im Voraus festgelegt. Es gibt keine Improvisation oder dynamisches Verständnis; wenn die Nutzerabsicht nicht vorhergesehen wurde, kann der Bot nicht helfen.

### Visualisierung: Regelbasierter Chatbot als Flussdiagramm

Ein regelbasierter Chatbot lässt sich am besten als verzweigtes Flussdiagramm darstellen:

- Jede Box steht für eine mögliche Nutzereingabe oder Bot-Antwort.
- Pfeile zeigen den Verlauf des Gesprächs je nach Nutzerwahl.
- Endpunkte führen zu Fallback-Nachrichten oder einer Eskalation.

[Siehe Beispiel-Entscheidungsbaum von HeroThemes](https://herothemes.com/blog/rule-based-chatbots/#how-do-rule-based-chatbots-work)

## Arten regelbasierter Chatbots

Regelbasierte Chatbots lassen sich nach Interaktionsstil, Komplexität und Anwendungsfall kategorisieren:

### Buttonbasierte (Menü-)Chatbots

- Nutzer interagieren über klickbare Buttons oder Menüs. Jede Auswahl löst eine neue Option oder Information aus.
- Ideal für einfache, transaktionale Interaktionen wie Reservierungen, Öffnungszeiten oder Support-Themen.
- **Beispiel:** Einfacher Restaurant-Buchungsbot.

### Schlüsselwortbasierte Chatbots

- Der Bot achtet auf bestimmte Schlüsselwörter oder -phrasen in der Nutzereingabe.
- Ordnet Eingaben Regeln zu, um vorgefertigte Antworten zu liefern.
- Etwas flexibler als Button-Bots, aber weiterhin auf erkannte Wörter beschränkt.
- **Beispiel:** „Rückerstattung“, „Rückgaberecht“, „Öffnungszeiten“.

### Datenabfrage-Chatbots

- Führen Nutzer durch Formulare, die als Fragenreihe präsentiert werden.
- Einsatz für Leadgenerierung, Umfragen, Terminvereinbarungen.
- Oft Kombination aus Button- und Texteingabe-Logik.

### Entscheidungsbaum-Chatbots

- Komplex verzweigte Gesprächsflüsse, oft erstellt mit visuellen Drag-and-drop-Editoren.
- Jede Nutzerantwort grenzt die Möglichkeiten ein und führt zur Lösung.
- Häufig im Kundensupport und bei Problemlösungen im Einsatz.

### Quiz-/Fragebogen-Chatbots

- Für interaktive Umfragen, Quizze oder Produktempfehlungen.
- Typischerweise buttonbasiert oder mit einfacher Texterkennung.
- **Beispiel:** Lead-Qualifizierungsquiz auf SaaS/B2B-Websites.
## Technische Umsetzung

Entwickler setzen regelbasierte Chatbots mit einfacher Programmierlogik, Mustererkennung und teils simplen NLP-Bibliotheken für Tokenisierung oder reguläre Ausdrücke um.

### Mustererkennung & Bedingungslogik

- **Mustererkennung:**  
  Der Bot vergleicht Nutzereingaben mit vordefinierten Mustern (oft reguläre Ausdrücke).
- **If/then/else-Logik:**  
  Für jedes erkannte Muster liefert der Bot die zugeordnete Antwort.

> „Wenn Eingabe ‚hi|hallo|hey‘ entspricht, antworte mit ‚Hallo! Wie kann ich Ihnen helfen?‘“

**Mustererkennung ist der Kern:** Egal wie ausgefeilt das Interface ist, jeder regelbasierte Bot besteht letztlich aus Ein-/Ausgabe-Paaren, meist als switch/case-Anweisungen, Dictionaries oder Lookup-Tabellen im Code umgesetzt.
### Beispiel: Einfacher regelbasierter Chatbot in Python

Ein klassisches Beispiel nutzt Pythons NLTK-Bibliothek für einfache Mustererkennung und Antwortlogik:

```python
import nltk
import re
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?"]],
    [r"my name is (.*)", ["Hello %1! How can I assist you today?"]],
    [r"(.*) your name?", ["I am your friendly chatbot!"]],
    [r"how are you?", ["I'm just a bot, but I'm doing well. How about you?"]],
    [r"bye|exit", ["Goodbye! Have a great day!"]],
    [r"(.*)", ["I'm sorry, I didn't understand that. Could you rephrase?"]]
]

class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)
    def respond(self, user_input):
        return self.chat.respond(user_input)

chatbot = RuleBasedChatbot(pairs)

def chat_with_bot():
    print("Hello, I am your chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

chat_with_bot()
```
### Best Practices für Entwickler

- **Regeln übersichtlich halten:** Klarer, wartbarer Code oder visuelle Flow-Editoren nutzen.
- **Nutzereingaben antizipieren:** Möglichst viele realistische Gesprächspfade abbilden.
- **Reguläre Ausdrücke für Mustererkennung:** Um Schreibvarianten und Formulierungen abzudecken.
- **Robuste Fallbacks implementieren:** Immer eine Standardantwort für unerkannte Eingaben vorsehen.
- **Eskalation einplanen:** Übergabe an menschliche Agenten ermöglichen, wenn nötig.
- **Umfangreich testen:** Echte Gespräche simulieren und Regeln für bessere Abdeckung anpassen.

**Weiterführende Literatur:**  
- [Codecademy: Rule-Based Chatbots Cheat Sheet](https://www.codecademy.com/learn/rule-based-chatbots/modules/rule-based-chatbots/cheatsheet)

## Vorteile regelbasierter Chatbots

Regelbasierte Chatbots sind weiterhin beliebt, da sie mehrere praktische Vorteile bieten:

1. **Einfach & schnell umsetzbar:**  
   Visuelle Drag-and-drop-Editoren und einfache Logik machen die Einrichtung auch für Nicht-Entwickler zugänglich. Ein Basis-Bot ist in wenigen Stunden einsatzbereit.

2. **Kostengünstig:**  
   Kein teures KI-Training, keine großen Datensätze oder externe Verarbeitung nötig. Viele Plattformen bieten kostenlose oder günstige Tarife.

3. **Volle Kontrolle über Antworten:**  
   Jede Antwort ist vorformuliert und markenkonform. Keine Überraschungen oder Abweichungen vom Skript.

4. **Zuverlässig & sicher:**  
   Vorhersehbares Verhalten und minimales Risiko für Datenlecks. Verarbeitung bleibt auf Ihren Servern oder vertrauenswürdigen Plattformen.

5. **Ideal für Routineaufgaben & FAQs:**  
   Automatisiert wiederkehrende Anfragen (Öffnungszeiten, Standorte, Statusabfragen, Formulare) mit nahezu sofortigen Antworten.

6. **Einfache Integration:**  
   Kann für Echtzeitabfragen (z. B. Bestellstatus, Terminfenster) an Datenbanken oder APIs angebunden werden.

7. **Geringer Wartungsaufwand (bei statischem Inhalt):**  
   Für Unternehmen mit seltenen Änderungen ist die Wartung minimal.
## Grenzen regelbasierter Chatbots

Regelbasierte Bots haben klare Grenzen—diese zu kennen ist entscheidend für gutes Design:

1. **Begrenztes Verständnis:**  
   Bots können nur auf Eingaben reagieren, die vordefinierten Regeln entsprechen. Falschschreibungen, Mehrdeutigkeiten oder unerwartete Fragen bringen den Ablauf durcheinander.

2. **Roboterhaft & geskriptet:**  
   Fühlt sich an wie ein Telefonmenü, nicht wie ein natürliches Gespräch.

3. **Kein Lernen oder Anpassung:**  
   Verbessern sich nicht durch Nutzung. Alle Updates müssen manuell erfolgen.

4. **Schwache Fehlerbehandlung:**  
   Schwierigkeiten mit Tippfehlern, Slang oder komplexen Nutzeranliegen.

5. **Schwer skalierbar bei Komplexität:**  
   Mit wachsender Regelzahl wird Wartung aufwändig und fehleranfällig.

6. **Potenzial für Nutzerfrust:**  
   Wenn der Bot das Anliegen nicht abdeckt oder zu viele Klicks nötig sind, leidet das Erlebnis.

7. **Hoher Wartungsaufwand bei dynamischem Inhalt:**  
   Wenn sich Inhalte oft ändern, ist Skriptanpassung arbeitsintensiv.
## Praktische Beispiele & Anwendungsfälle

Regelbasierte Chatbots werden branchenübergreifend für Routine- und Massenvorgänge eingesetzt:

### eCommerce-Support-Bot  
- **Beispiel:** [H&M Virtual Assistant](https://herothemes.com/blog/rule-based-chatbots/#rule-based-chatbot-examples)  
- Beantwortet FAQs wie Bestellstatus, Rückgaben, Öffnungszeiten über Menüs.
- Leitet bei Anfragen außerhalb des Skripts an Support/Menschen weiter.

### Airline-FAQ & Self-Service  
- **Beispiel:** [Lufthansas Elisa](https://herothemes.com/blog/rule-based-chatbots/#rule-based-chatbot-examples)  
- Unterstützt bei Stornierungen, Rückerstattungen und COVID-19-Infos per Entscheidungsbaum.

### Banking-Assistant  
- Beantwortet Kontofragen, Filialinfos und einfache Transaktionen.
- Komplexe oder sensible Anliegen werden an Menschen weitergegeben.

### Restaurant-Reservierungsbot  
- Bucht Tische, zeigt Speisekarten und Öffnungszeiten—alles per Menüauswahl.

### Leadgenerierungs-Chatbot  
- Qualifiziert Leads auf B2B-Seiten mit geskripteten Abläufen („Wie groß ist Ihr Unternehmen?“).

### Interner Helpdesk (HR/IT)  
- Automatisiert Anfragen zu Formularen, Richtlinien oder Passwort-Resets.

### Weitere Branchen  
- Gesundheitswesen (Terminvereinbarung)  
- Reisen (Hotel-/Aktivitätsbuchungen)  
- Einzelhandel (Rückgaben, Garantieinfos)  
## Vergleich: Regelbasierter Chatbot vs. KI-Chatbot

| **Aspekt**           | **Regelbasierter Chatbot**                                     | **KI-basierter Chatbot**                                      |
|----------------------|---------------------------------------------------------------|--------------------------------------------------------------|
| **Ansatz**           | Vordefinierte Skripte/Entscheidungsbäume                      | Maschinelles Lernen & NLP ([Natural Language Processing](/en/glossary/natural-language-processing--nlp-/))         |
| **Lernen**           | Kein Selbstlernen; statisch                                   | Lernt aus Daten; passt sich an                               |
| **Eingabeverarbeitung** | Schlüsselwortabgleich/Buttons; geringe freie Texteingabe | Versteht Absicht, Synonyme, Tippfehler; robuste Sprachverarbeitung |
| **Gesprächsfluss**   | Linear, vorhersehbar, „menüartig“                            | Dynamisch, kontextbezogen, mehrstufige Dialoge               |
| **Antwortflexibilität** | Fest, geskriptet                                       | Generativ oder kontextbasiert; menschlicher                  |
| **Einrichtung & Kosten** | Schnell, günstig, oft ohne Code                        | Höhere Kosten, Einrichtung & Training nötig                  |
| **Ideal für**        | FAQs, Routinetasks, Leadformulare                             | Komplexe Anfragen, große Themenvielfalt                      |
| **Wartung**          | Manuelle Regelupdates                                        | Laufende Daten-/Trainingspflege                              |
| **Skalierbarkeit**   | Begrenzt durch Regelkomplexität                              | Besser für Vielfalt & Skalierung geeignet                    |
| **Nutzererlebnis**   | Vorhersehbar, transparent, aber starr                        | Natürlich, flexibel, teils unvorhersehbar                    |
| **Fehlerbehandlung** | Nur Fallback oder Eskalation                                 | Kann nachfragen, umformulieren oder Neues versuchen          |
## Wann sollte man regelbasierte Chatbots einsetzen?

Regelbasierte Chatbots sind die richtige Wahl, wenn:

- Nutzeranfragen **vorhersehbar und wiederkehrend** sind (Öffnungszeiten, Reservierungen, Bestellstatus).
- Sie **volle Kontrolle** über jede Antwort (z. B. für Compliance oder Markenauftritt) benötigen.
- Budget oder technische Ressourcen begrenzt sind—diese Bots sind günstig und schnell startklar.
- Sie **schnell launchen** wollen (MVPs, Pilotprojekte, zeitlich begrenzte Kampagnen).
- **Keine großen Datensätze** für KI-Training vorhanden sind.
- **Zuverlässigkeit und Sicherheit** entscheidend sind (keine externe Datenverarbeitung).

**Tipp:** Erwarten Ihre Nutzer offenere, „menschliche“ Gespräche oder ist Ihr Use Case komplex, könnte eine hybride oder KI-basierte Lösung nötig sein.
## Wie baut man einen regelbasierten Chatbot?

**Schritt-für-Schritt-Vorgehen:**

1. **Häufige Anfragen sammeln:**  
   Die wichtigsten Nutzerfragen oder Aufgaben für die Automatisierung identifizieren.

2. **Gesprächsfluss gestalten:**  
   Gesprächspfade mit Flowchart-Tools oder visuellen Editoren abbilden.

3. **Regeln schreiben:**  
   Trigger (Schlüsselwörter/Buttons) und die zugehörigen Antworten definieren.

4. **Fallbacks festlegen:**  
   Bestimmen, was bei nicht erkannten Eingaben geschieht (eskalieren, Hilfe anzeigen etc.).

5. **Testen & optimieren:**  
   Echte Gespräche simulieren und Regeln für Abdeckung und Genauigkeit anpassen.

6. **Mit Systemen integrieren (falls nötig):**  
   Für dynamische Daten (Bestellungen, Termine) Anbindung an interne APIs oder Datenbanken.

7. **Veröffentlichen & überwachen:**  
   Live gehen, Lücken beobachten und Regeln bei Bedarf aktualisieren.

**Beliebte Plattformen:**  
- [Chatfuel](https://chat