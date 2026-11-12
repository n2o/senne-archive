---
version: 1
slug: "senne-templates-base-html"
primary_target: "senne/templates/base.html"
related_targets: ["archive/templates/archive/index.html","archive/templates/archive/detail.html","frontpage/templates/frontpage/index.html","templates/flatpages/default.html"]
---

---
version: 1
slug: "senne-templates-base-html"
primary_target: "senne/templates/base.html"
related_targets: ["archive/templates/archive/index.html","archive/templates/archive/detail.html","frontpage/templates/frontpage/index.html","templates/flatpages/default.html"]
---

# Surface brief: sennearchiv.de (alle öffentlichen Seiten)

Scope: Startseite, Archivsuche/-liste, Detailseite, Flatpages (Impressum, Datenschutz). Mode: read. Build path: code-led.
Audience/job: Heimatforschende, Naturschutz-Leute, Studierende finden Senne-Literatur und kommen ans Dokument; viele landen per Google direkt auf einer Detailseite.
Entschieden: Bedienung + neuer Look; jQuery, select2, lightbox2 raus (native select/datalist, <dialog>). Archiv ohne Suchbegriff durchblätterbar, Trefferzahl, Jahr sichtbar, Medienart-Filter, Detailseite mit deutlichem Dokument-Zugang. Logo + Stiftungsgrün verbindlich. Nur vorhandene Stiftungsfotos.
Entschieden im Bau: fest chronologisch, älteste zuerst (ohne Jahr am Ende). Feldname „Autor“ statt des Herbar-Begriffs „leg.“: das Publikum ist überwiegend Laien, Klarheit im Lesebereich geht vor (mode read); die Welt bleibt in Etikett-Linien, Mono-Feldnamen, Stempeln und Mappen.

## Direction contract

THESIS: Das Archiv ist eine Herbarsammlung: jeder Eintrag ein Beleg mit Etikett, das Archiv eine Folge grüner Gattungsmappen. Verweigert wird die Katalogseite aus weißer Fläche, Filterspalte und Karten mit Schatten.

OWN-WORLD: Kühler Belegbogen #f2f2ec als Grund, Mappenkopf in Stiftungsgrün #226c36 mit Logo unter Leinenband (#d8ccb0), Etikett-Tinte #1d1f1c, Eingangsstempel in Pflaume #7a2e55. Etikettfelder als unterstrichene Zeilen mit kleinen Mono-Feldnamen (leg., Jahr, Art), Titel in einer Buchserife, Inventarnummer SA-0000 in der Randspalte, Zustand als Stempelform (Doppelrahmen PDF, rund Abbildungen, gestrichelt nur analog). Keine Kästen, keine Schatten.

STORY: Besucher sehen sofort, was die Sammlung enthält, blättern nach Jahrzehnt oder suchen, erkennen am Stempel, ob es ein Dokument gibt, und öffnen es auf der Detailseite mit einem Griff.

FIRST VIEWPORT: Grüner Mappenkopf über volle Breite: Logo links mit Leinenband, Name, Navigation rechts, darunter Stichwort- und Autorfeld mit Suchen. Darunter links Jahrzehnte und Medienart, rechts Trefferzeile „62 Treffer … Seite 1 von 4“ und Belegstreifen: Jahrzehnt + Inventarnummer in der Randspalte, Titel, Etikettzeile, Stempel rechts.

FORM: Herbarbeleg, Platz 5 der eigenen Liste (gezogen). seed:f4d75dff586c31a8

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
