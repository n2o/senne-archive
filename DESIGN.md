---
name: Senne-Archiv
description: Das digitale Archiv der Naturschutz-Stiftung Senne als Herbarsammlung aus Belegbögen, Etiketten und grünen Mappen.
colors:
  folder: "#226c36"
  folder-dark: "#1b5a2c"
  folder-text: "#e3efe5"
  stamp: "#7a2e55"
  tape: "#d8ccb0"
  sheet: "#f2f2ec"
  ink: "#1d1f1c"
  soft: "#4a4d47"
  rule: "#c4c4b8"
  white: "#ffffff"
typography:
  display:
    fontFamily: "Spectral, Georgia, serif"
    fontSize: "clamp(2.25rem, 5vw, 3.5rem)"
    fontWeight: 600
    lineHeight: 1.2
  headline:
    fontFamily: "Spectral, Georgia, serif"
    fontSize: "clamp(1.75rem, 3.6vw, 2.625rem)"
    fontWeight: 600
    lineHeight: 1.2
  section:
    fontFamily: "Spectral, Georgia, serif"
    fontSize: "1.375rem"
    fontWeight: 600
    lineHeight: 1.2
  title:
    fontFamily: "Spectral, Georgia, serif"
    fontSize: "1.25rem"
    fontWeight: 500
    lineHeight: 1.3
  lead:
    fontFamily: "Spectral, Georgia, serif"
    fontSize: "1.25rem"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Spectral, Georgia, serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
    fontFeature: "lnum"
  small-caps:
    fontFamily: "Spectral SC, Spectral, Georgia, serif"
    fontSize: "0.9375rem"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.06em"
  plate:
    fontFamily: "IBM Plex Mono, ui-monospace, monospace"
    fontSize: "0.875rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.02em"
  label:
    fontFamily: "IBM Plex Mono, ui-monospace, monospace"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.2
  control:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 600
    lineHeight: 1
  small:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.4
rounded:
  xs: "0.15rem"
  sm: "2px"
  md: "0.5rem"
  full: "999px"
spacing:
  gutter: "clamp(1rem, 3vw, 2.5rem)"
  plate: "5.75rem"
  indent: "6.75rem"
  touch: "2.75rem"
components:
  folder-cover:
    backgroundColor: "{colors.folder}"
    textColor: "{colors.white}"
    padding: "1.25rem clamp(1rem, 3vw, 2.5rem) 1.75rem"
  search-field:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: "3rem"
    padding: "0 0.875rem"
  button-search:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    typography: "{typography.control}"
    rounded: "{rounded.sm}"
    height: "3rem"
    padding: "0 1.75rem"
  bandmark:
    backgroundColor: "{colors.folder}"
    textColor: "{colors.white}"
    rounded: "{rounded.sm}"
    padding: "0.2rem 0.55rem 0.25rem"
  decade-chip:
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: "2.75rem"
    padding: "0.55rem 0.9rem"
  decade-chip-hover:
    backgroundColor: "{colors.folder}"
    textColor: "{colors.white}"
  filter-chip:
    textColor: "{colors.folder}"
    rounded: "{rounded.sm}"
    padding: "0.2rem 0.6rem"
  page-link:
    textColor: "{colors.folder}"
    size: "2.75rem"
  page-link-current:
    backgroundColor: "{colors.folder}"
    textColor: "{colors.white}"
    size: "2.75rem"
  stamp:
    textColor: "{colors.stamp}"
    typography: "{typography.small-caps}"
    padding: "0.3rem 0.6rem 0.35rem"
  stamp-fig:
    textColor: "{colors.stamp}"
    rounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.folder}"
    textColor: "{colors.white}"
    padding: "1.25rem clamp(1rem, 3vw, 2.5rem)"
  viewer-close:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    height: "2.75rem"
    padding: "0 1rem"
---

# Design System: Senne-Archiv

## Overview

**Creative North Star: "Die Herbarsammlung"**

Das Archiv ist eine Herbarsammlung: Jeder Eintrag ist ein Beleg auf einem kühlen Bogen, mit Etikett, Inventarnummer in der Randspalte und Eingangsstempel; das Archiv als Ganzes ist eine Folge grüner Gattungsmappen, eine pro Jahrzehnt. Der Mappenkopf in Stiftungsgrün trägt das Logo wie ein aufgeklebtes Präparat unter zwei Streifen Leinenband.

Die Dichte ist die einer Sammlungsliste, nicht die eines Katalogs: Belegstreifen statt Karten, Linien statt Kästen, Etikettzeilen mit kleinen Mono-Feldnamen statt Tabellen. Der Zustand eines Belegs (Datei, Abbildungen, online, nur analog) steht als Stempel mit eigener Form am Rand, leicht schief wie von Hand gesetzt. Gelesen wird in einer Buchserife; Bedienelemente sprechen eine nüchterne Grotesk, damit Suchen und Blättern sofort als Werkzeug erkennbar sind.

Abgelehnt ist die Katalogseite aus weißer Fläche, Filterspalte und Karten mit Schatten. Abweichung vom Richtungsvertrag: Dort heißt das Feld „leg.“; gebaut ist „Autor“, weil das Publikum überwiegend aus Laien besteht und Klarheit beim Lesen vorgeht. Die Herbarwelt bleibt in Etikettlinien, Mono-Feldnamen, Stempeln und Mappen.

**Key Characteristics:**
- Kühler Belegbogen als Grund, Stiftungsgrün nur als Mappe (Kopf, Fuß, Jahrzehnt-Marke, aktueller Zustand) und als Linkfarbe.
- Inventarnummer SA-0000 in einer festen Randspalte; Etikett, Abschnitte und Titel fluchten auf einer Linie.
- Stempel in Pflaume: Zustand als Form, nicht als Farbe.
- Flach: keine Schatten, Tiefe nur durch Mappenkante, Leinenband und Linien.
- Alle Schriften selbst gehostet (OFL), keine externen Ressourcen.

## Colors

Eine gedämpfte Sammlungspalette: kühles Papier, tiefe Etiketttinte, ein Stiftungsgrün als Mappe und ein einziges Pflaume für Stempel.

### Primary
- **Stiftungsgrün / Mappengrün** (folder): Mappenkopf und Fuß als volle Fläche, Jahrzehnt-Marke, aktuelle Seite, aktiver Facettenfilter, Hover der Jahrzehnt-Chips, alle Links im Lesebereich. Verbindliche Markenfarbe der Stiftung.
- **Mappenkante** (folder-dark): ausschließlich die 7px-Kante, die Kopf und Fuß gegen den Bogen absetzt.
- **Mappen-Hellgrün** (folder-text): Feldnamen der Suche und Trefferzahlen auf grüner Fläche, wo reines Weiß zu laut wäre.

### Secondary
- **Stempel-Pflaume** (stamp): Eingangsstempel, Fokusring (3px), Text-Cursor. Sonst nirgends.

### Tertiary
- **Leinenband** (tape): die schräg geklebten Bandstreifen über Logo und Leitfoto, außerdem die Textauswahl.

### Neutral
- **Belegbogen** (sheet): Seitengrund, Suchfelder, Bildbetrachter.
- **Etiketttinte** (ink): Fließtext, Überschriften, die tragenden 1px-Linien unter Kopfzeilen und Abschnitten, der Suchknopf.
- **Bleistiftgrau** (soft): Feldnamen, Inventarnummern, Zähler, Nebentexte.
- **Etikettlinie** (rule): feine Trennlinien zwischen Belegstreifen und unter Etikettfeldern, Rahmen der Seitenzahlen.
- **Weiß** (white): Text auf grüner und schwarzer Fläche. Im Code als Literal ohne eigene Custom Property.

### Named Rules
**The Mappengrün Rule.** Grün ist Mappe oder Weg: Fläche nur für Kopf, Fuß, Jahrzehnt-Marke und aktuellen Zustand, sonst nur als Linkfarbe. Kein grüner Schmuck, keine grünen Kästen im Lesebereich.

**The Ein-Stempel-Farbe Rule.** Pflaume gehört dem Stempel, dem Fokus und dem Cursor. Stempel unterscheiden sich nie über Farbe.

## Typography

**Display Font:** Spectral (mit Georgia, serif)
**Body Font:** Spectral (mit Georgia, serif); Spectral SC für Stempel und Listenköpfe
**Label/Mono Font:** IBM Plex Mono (mit ui-monospace) für Feldnamen und Inventarnummern; Public Sans (mit system-ui) für Bedienelemente

**Character:** Eine Buchserife trägt Titel und Text wie auf einem gedruckten Etikett; Kapitälchen setzen Stempel und Rubriken, die Schreibmaschinen-Mono die Feldnamen und Nummern. Die Grotesk bleibt reines Werkzeug.

### Hierarchy
- **Display** (display): Startseiten-Titel, einmal pro Seite.
- **Headline** (headline): Titel des Belegs auf der Detailseite; Flatpage-Titel (clamp 2rem–2.75rem) und Blocktitel der Startseite (clamp 1.625rem–2.125rem) liegen in derselben Stufe.
- **Section** (section): Abschnitte der Detailseite (Dokumente, Abstract, Notizen).
- **Title** (title): Belegtitel im Streifen der Trefferliste, max. 44em breit.
- **Lead** (lead): Einleitungssätze, max. 36em.
- **Body** (body): Fließtext mit Versalziffern; Prosa max. 68ch.
- **Small Caps** (small-caps): Stempel, Facettenköpfe, Listenköpfe der Startseite; die Jahresangabe „anno 1980“ in Spectral SC 500 mit 0.05em.
- **Plate** (plate): Inventarnummer SA-0000 in der Randspalte.
- **Label** (label): Feldnamen (Autor, Jahr, Art), Suchfeld-Beschriftungen, Zähler.
- **Control** (control): Navigation, Suchknopf, „öffnen“-Aktion; Eingaben und Seitenzahlen in Public Sans 400.

### Named Rules
**The Vier-Stimmen Rule.** Spectral liest, Spectral SC stempelt, Plex Mono beschriftet, Public Sans bedient. Keine Stimme übernimmt die Rolle einer anderen.

**The Kein-dünner-Schnitt Rule.** Kein Schnitt unter 400; Fließtext nie kleiner als 1.0625rem, Mono-Beschriftungen nie kleiner als 0.8125rem.

## Layout

Ein Bogen mit Randspalte. Der Inhalt sitzt auf `.sheet` (max. 90rem, seitlicher Abstand gutter); die Inventarnummer steht in einer festen Randspalte (plate), Etikett und Abschnitte der Detailseite rücken auf die Titelkante ein (indent = plate + 1rem). Die Detailseite ist auf 72rem begrenzt, Etikett und Abschnitte auf 48rem.

- **Trefferliste:** Facettenspalte 14.5rem neben der Liste (Abstand 2.5rem). Jeder Belegstreifen ist ein vierspaltiges Raster: Jahrzehnt-Marke (5rem), Inventarnummer (plate), Titel mit Etikettzeile, Stempel rechtsbündig.
- **Etikett:** Felder als Raster `auto-fill, minmax(13rem, 1fr)`, jedes Feld eine unterstrichene Zeile.
- **Startseite:** ab 60.0625rem zweispaltig (Text 1fr, Tafeln 1.25fr); Textblöcke wechseln die Bildseite von Block zu Block, Blöcke ohne Bild setzen Überschrift und Text nebeneinander statt eine Hälfte leer zu lassen.
- **Bis 60rem:** Facetten werden zwei waagerecht scrollbare Chip-Reihen über der Liste.
- **Bis 40rem:** kompakter Mappenkopf (Logo 5.25rem neben dem Namen, Stichwort und Suchknopf in einer Zeile, Autorfeld darunter); Belegstreifen stapeln Marke + Nummer, Titel, Stempel; die Einrückung fällt auf 0.
- **Rhythmus:** Streifen 0.75rem vertikal, Abschnitte 2.25rem, Startseiten-Blöcke 4rem mit Linie.

**The Randspalte Rule.** Die Inventarnummer hat ihre eigene Spalte; alles, was zum Beleg gehört, fluchtet auf die Titelkante daneben.

**The Neue-Mappe Rule.** Ein neues Jahrzehnt beginnt eine neue Mappe: grüne Jahrzehnt-Marke und eine 2px grüne Oberlinie statt der feinen Etikettlinie.

## Elevation & Depth

Das System ist flach; es gibt keinen einzigen `box-shadow`. Tiefe entsteht aus Material: die 7px dunklere Mappenkante unter dem Kopf und über dem Fuß, die schräg geklebten Leinenband-Streifen über Logo und Leitfoto, die 1px-Linien in Tinte (Kopfzeilen) und Etikettgrau (Streifen, Felder). Einzige Ebene ist der Bildbetrachter: ein natives `<dialog>` auf Bogengrund über einem Tintenschleier (82 %).

**The Flacher-Bogen Rule.** Nichts schwebt. Wo etwas hervortreten soll, wird es geklebt, gestempelt oder unterstrichen, nie beschattet.

**The Leinenband Rule.** Leinenband hält, was aufgezogen ist: das Logo auf der Mappe und das Leitfoto auf dem Bogen, je zwei Streifen gegenläufig um 4–8° gedreht. Es schmückt keinen Text und keine Bedienelemente.

## Shapes

Fast rechtwinklig. Bedienelemente, Chips und Marken haben 2px Ecken (sm). Rundungen gibt es nur als Bedeutung: der runde Stempel (full) für Abbildungen, der asymmetrisch gerundete Stempel (0.5rem 0.15rem) für Online-Verweise. Linien sind das tragende Formmittel; Inhalte stehen nie in gefüllten Kästen.

**The Stempelform Rule.** Der Zustand eines Belegs ist die Form seines Stempels: Doppelrahmen (3px double) für Dateien wie PDF, rund für Abbildungen, asymmetrisch gerundet für online, gestrichelt für „nur analog“. Jeder Stempel hat einen festen Grundwinkel (−3° bis 2.5°) plus einen Neigungsversatz je Beleg (−2° bis 2°).

## Components

### Buttons
Schwer und eindeutig, wie ein Stempelkissen.
- **Shape:** fast eckig (2px).
- **Suchknopf:** Etiketttinte mit weißer Public Sans 600, 3rem hoch, seitlich 1.75rem. Hover dunkelt auf Schwarz ab.
- **Schließen im Bildbetrachter:** Tinte mit Weiß, oben rechts, 2.75rem hoch.
- **Focus:** 3px Fokusring in Pflaume mit 3px Abstand; auf grüner Mappe weiß.

### Chips
- **Jahrzehnt-Chips (Startseite):** 1px Tintenrahmen, 2px Ecken, mindestens 2.75rem hoch, Zahl in Mono-Grau. Hover füllt mit Mappengrün, Text weiß, Zahl hellgrün.
- **Aktive Filter:** 1px grüner Rahmen, grüner Text, 2px Ecken.
- **Facetten mobil:** Rahmen in Etikettlinie; aktiv mit grüner Fläche und weißem Text.

### Inputs / Fields
- **Style:** randlose Felder auf Belegbogen in der grünen Mappe, 2px Ecken, 3rem hoch, Public Sans 400; Beschriftung darüber in Plex Mono 500 0.8125rem, hellgrün.
- **Focus:** weißer 3px Ring (auf grüner Fläche).
- Autorauswahl ist ein natives `<select>`.

### Navigation
- **Hauptnavigation:** Public Sans 600 in Weiß auf der Mappe; aktiv und Hover mit 2px weißer Unterkante.
- **Facetten (Desktop):** Liste mit kurzem Tintenstrich (0.875rem × 1px) vor jedem Eintrag, Zahl rechts in Mono; aktiv wird der Strich zum 1.375rem × 3px grünen Balken und der Text grün und 600.
- **Seitenzahlen:** 2.75rem Quadrate, 1px Etikettlinie, grüner Text; aktuelle Seite grün gefüllt.
- **Fuß:** grüne Mappe mit 7px Kante oben, weiße Links in Public Sans.

### Belegstreifen (Signature)
Ein Eintrag der Trefferliste: Jahrzehnt-Marke (grün gefüllt, nur beim ersten Beleg eines Jahrzehnts), Inventarnummer in Plex Mono, Titel in Spectral 500 als grüner Link, darunter die Etikettzeile mit Feldern als unterstrichene Paare aus Mono-Feldname und Wert, rechts die Stempel. Getrennt durch 1px Etikettlinie, bei neuem Jahrzehnt durch 2px Grün.

### Etikett (Signature)
Die Angaben der Detailseite als Definitionsliste: Mono-Feldname über dem Wert, jedes Feld auf einer 1px Etikettlinie, eingerückt auf die Titelkante.

### Dokumentzeile (Signature)
Der Weg zur Datei: Stempel (z. B. PDF), Dateiname, rechts die Aktion „öffnen“ in grüner Public Sans 600; abgeschlossen von einer 1px Tintenlinie. Hover unterstreicht Name und Aktion.

### Stempel (Signature)
Spectral SC 600, 0.06em Laufweite, Pflaume, Rahmen nach der Stempelform-Regel; im Belegkopf vergrößert auf 1.375rem.

### Tafeln (Startseite)
Stiftungsfotos als Raster 2fr/1fr, das Leitfoto über zwei Zeilen und mit zwei Leinenband-Streifen aufgezogen. Bilder öffnen im Bildbetrachter (`<dialog>`, Einblendung 0.35s, bei reduzierter Bewegung ohne Animation).

## Do's and Don'ts

### Do:
- **Do** Zustände als Stempelform ausdrücken (Doppelrahmen, rund, asymmetrisch, gestrichelt), immer in Pflaume.
- **Do** Inhalte mit Linien gliedern: 1px Tinte unter Kopfzeilen, 1px Etikettlinie zwischen Streifen und Feldern, 2px Grün für eine neue Mappe.
- **Do** Feldnamen klein in Plex Mono über oder vor den Wert setzen, als unterstrichene Etikettzeile.
- **Do** die Inventarnummer in die Randspalte (5.75rem) setzen und Zugehöriges auf die Titelkante einrücken.
- **Do** Touch-Ziele mindestens 2.75rem hoch halten und den 3px Fokusring in Pflaume (auf Grün weiß) erhalten.
- **Do** Schriften selbst hosten; keine Laufzeit-Ressourcen von Dritten.

### Don't:
- **Don't** Schatten verwenden, weder auf Karten noch auf Bedienelementen.
- **Don't** Belege als Karten oder Inhalte in gefüllte Kästen setzen; Rahmen gibt es nur an Stempeln, Chips, Seitenzahlen und Filtern.
- **Don't** Stempel über Farbe unterscheiden oder Pflaume außerhalb von Stempel, Fokus und Cursor einsetzen.
- **Don't** Mappengrün als Schmuckfläche im Lesebereich einsetzen.
- **Don't** Schriftschnitte unter 400 verwenden.
- **Don't** Leinenband auf Text oder Bedienelemente kleben; es hält nur Logo und Leitfoto.
- **Don't** das Stiftungslogo verändern oder nachzeichnen.
