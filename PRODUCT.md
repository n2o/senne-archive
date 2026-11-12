# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
Heimatforschende, Naturschutz-Engagierte und Studierende, die Literatur, Dokumente und Bilder zur Senne (Heide- und Sandlandschaft in Ostwestfalen-Lippe) suchen. Viele kommen über Google direkt auf einen einzelnen Eintrag oder ein PDF, nicht über die Startseite. Gepflegt werden die Inhalte von ein bis zwei Ehrenamtlichen der Naturschutz-Stiftung Senne über den Django-Admin.

## Product Purpose
sennearchiv.de ist das digitale Archiv der Naturschutz-Stiftung Senne: rund 350 Einträge (Bücher, Artikel, Fotos, Dias, Tonträger u. a.) von rund 165 Autorinnen und Autoren, viele mit PDF oder Abbildungen. Erfolg heißt: Wer etwas zur Senne sucht, findet den passenden Eintrag schnell, versteht ihn und kommt an das Dokument.

## Positioning
Die einzige gebündelte, frei zugängliche Sammlung von Senne-Literatur und -Dokumenten, kuratiert von der Stiftung, die die Landschaft schützt.

## Operating Context
Suche nach Stichwörtern (Titel, Abstract, Notizen, Schlagworte) und nach Autor; Detailseite je Eintrag mit Angaben, Abstract, Anhängen und Abbildungen; Startseite mit drei redaktionellen Blöcken; Impressum und Datenschutz als Flatpages. Dateien liegen in einem privaten S3-Bucket und werden über zeitlich begrenzte, signierte Links ausgeliefert. Nicht veröffentlichte Einträge sind öffentlich unsichtbar.

## Capabilities and Constraints
- Django 5.2, serverseitig gerenderte Templates; Inhalte pflegen Ehrenamtliche selbst, also muss jedes Layout mit unvollständigen oder unsauberen Daten leben (fehlender Abstract, sehr lange Titel, Tippfehler in Feldern).
- Keine externen Ressourcen zur Laufzeit (DSGVO): Schriften und Skripte selbst hosten, keine Google Fonts, kein CDN, keine Tracker, keine Cookies für Besucher.
- Barrierefreiheit wurde auf axe 0 Verstöße gebracht und darf nicht zurückfallen.
- Entschieden: jQuery, select2 und lightbox2 werden durch Browser-Funktionen ersetzt.
- Medienarten: Artikel, Audiodatei, Buch, CD/DVD, Dia(s), Filmspule, Foto(s), Gegenstand, Kassette, Schallplatte, Schrifttum, Sonstiges, Stempel, Tonband, VHS, Videodatei.

## Brand Commitments
- Das Logo der Naturschutz-Stiftung Senne (NSS-Monogramm mit „Senne Archiv / Naturschutz Stiftung Senne“) bleibt unverändert.
- Das Stiftungsgrün bleibt (heute #299549 für Linien, #226c36 für Text und Flächen auf Weiß).
- Alles andere (Schriften, weitere Farben, Layout) ist frei, solange es zur Stiftung passt.

## Evidence on Hand
- Eigene Landschaftsfotos der Stiftung auf der Startseite: Heide im Nebel mit Eichen, Küchenschelle, Moor/Sennebach, Calluna-Heide (im Bucket unter `frontpage/`). Nur diese vorhandenen Fotos verwenden, keine fremden oder erzeugten Bilder.
- Logo nur als JPG mit Hintergrund (`frontpage/logo_senne_mit_hintergrund_w400px.jpg`); eine Vektorfassung liegt nicht vor.
- Echte Archivdaten (Titel, Autoren, Jahre, Medienarten) aus der Datenbank.

## Product Principles
1. Finden vor Gestalten: Suche und Stöbern sind der Kern, jede Seite führt schnell zum Dokument.
2. Jede Detailseite ist eine Startseite, weil Google-Besucher dort landen.
3. Einfach bleiben: wenige Seiten, wenige Bedienelemente, ohne Schulung für Ehrenamtliche pflegbar.
4. Die Landschaft ist der Grund für das Archiv; sie darf spürbar sein, ohne die Suche zu verdrängen.

## Accessibility & Inclusion
WCAG 2.1 AA (axe ohne Verstöße), auch für ältere, nicht technikaffine Besucher: gut lesbare Schriftgrößen, keine dünnen Schriftschnitte, Bedienung per Tastatur und Screenreader, Touch-Ziele ab 44 px.
