# Collapsi: Inoffizielle Regelsammlung

[Deutsch](README.de.md) · [English](README.md) · [Français](README.fr.md) · [Español](README.es.md)

Dieses Repository enthält eine **inoffizielle** mehrsprachige Regelsammlung für [Collapsi](https://riffleshuffleandroll.itch.io/collapsi), das abstrakte Strategiespiel von **Mark S. Ball** von Riffle Shuffle & Roll.

Die aktuelle Veröffentlichung, die **Collapsi Revival Edition**, dokumentiert sowohl Mark S. Balls aktualisierten Aufbau mit Buben für das normale Spiel zu zweit als auch den früheren Aufbau mit Jokern. Sie enthält außerdem optionale **Wiederbelebungsvarianten** von **Johann Duscher (a.k.a. Jonny Dee)**. Diese basieren weiterhin auf dem Joker-Aufbau und lassen kollabierte Karten auf verschiedene kontrollierte Arten ins Spiel zurückkehren. Das Projekt ist unabhängig und keine offizielle Veröffentlichung von Mark S. Ball.

## Originalreferenz und aktuelle Veröffentlichung

Das herunterladbare Originalregelwerk bezeichnet sich als **Collapsi v1.3.1**, zuletzt aktualisiert am 9. Juli 2025. Es verwendet zwei Buben als Startkarten; jeder Bube erlaubt als Eröffnungszug genau ein Feld. Diese inoffizielle Veröffentlichung dokumentiert den aktualisierten Aufbau neben dem früheren Joker-Aufbau, bei dem eine Zugweite von 1, 2, 3 oder 4 Feldern gewählt wird. Die Wiederbelebungsvarianten basieren weiterhin auf dem Joker-Aufbau. Andere Erklärungen auf dem [YouTube-Kanal von Riffle Shuffle & Roll](https://www.youtube.com/@riffleshuffleandroll) können andere Entwicklungsstände des Originalspiels zeigen; dieses Repository leitet daraus keine offizielle Versionsnummer ab.

## Spielanleitungen

| Sprache | Markdown | PDF |
| --- | --- | --- |
| Deutsch | [Online lesen](docs/de/rules.md) | [PDF herunterladen](output/pdf/collapsi-rules-de.pdf) |
| English | [Read online](docs/en/rules.md) | [Download PDF](output/pdf/collapsi-rules-en.pdf) |
| Français | [Lire en ligne](docs/fr/rules.md) | [Télécharger le PDF](output/pdf/collapsi-rules-fr.pdf) |
| Español | [Leer en línea](docs/es/rules.md) | [Descargar PDF](output/pdf/collapsi-rules-es.pdf) |

Die Stammdatei `README.md` ist englisch, weil GitHub genau diese Datei automatisch anzeigt. Jedes README und jede Anleitung beginnt mit einem kompakten Sprachwechsler; die deutsche Fassung ist dadurch mit einem Klick erreichbar.

## Versionierung

Diese Regelsammlung verwendet eine **eigene semantische Version** und einen Editionsnamen. Die aktuelle Veröffentlichung ist die **Collapsi Revival Edition**, Version **1.0.1**. Bei kompatiblen Patch-Releases bleibt der Editionsname bestehen; Releases mit neuen Varianten erhalten einen neuen Namen. Releases und Git-Tags verwenden `edition-vMAJOR.MINOR.PATCH`, zum Beispiel `edition-v1.0.1`. Die Schritte für eine Veröffentlichung stehen in der englischen [Release-Checkliste](RELEASE.md).

Diese Nummer bezeichnet ausschließlich diese inoffizielle Regelsammlung. Sie ist bewusst unabhängig von unbekannten oder später geänderten Versionen des Originalregelwerks und darf nicht als offizielle Collapsi-Version dargestellt werden. Die Kompatibilität zu einer bestimmten Originalfassung gehört stattdessen in die Release Notes.

## Repository-Struktur

```text
docs/<sprache>/rules.md      Übersetzte Markdown-Quellen
output/pdf/                 Erzeugte PDFs
assets/fonts/               Mitgelieferte Fonts für stabiles Layout
scripts/build_pdfs.py       Ein Build für alle Sprachen
.github/workflows/          Automatische PDF-Prüfung
```

Sprachverzeichnisse verwenden kurze, kleingeschriebene, BCP-47-kompatible Kennungen wie `en`, `de`, `fr` oder `pt-br`. Nur übersetzte Texte liegen unter `docs/<sprache>/`. Fonts, Build-Logik, Lizenzierung, Hinweise für Mitwirkende und Workflows bleiben sprachunabhängig im Stammverzeichnis.

## PDFs erzeugen

Die PDF-Pipeline verwendet [ReportLab](https://www.reportlab.com/opensource/). Sie vermeidet eine LaTeX-Installation und native HTML-Renderer-Abhängigkeiten, unterstützt aber eingebettete Fonts, kontrollierte Seitenumbrüche, Seitenzahlen, Links und PDF-Metadaten.

```sh
uv sync --locked
uv run python scripts/build_pdfs.py
```

Festgeschriebene Abhängigkeiten, ein gemeinsamer Renderer, mitgelieferte Noto-Sans-Fonts, feste Release-Metadaten und stabile Dateinamen sorgen für reproduzierbare Builds. Der GitHub-Actions-Workflow baut jede Sprache neu, weist auf veraltete eingecheckte PDFs hin und stellt die PDFs zusätzlich als Workflow-Artefakt bereit.

## Lizenz und Namensnennung

Johann Duschers eigene Texte und Wiederbelebungsbeiträge stehen unter [CC BY-NC-SA 4.0](LICENSE.md). Damit sind Wiederverwendung und Bearbeitung erlaubt, jedoch keine kommerzielle Nutzung; Bearbeitungen müssen unter derselben Lizenz stehen. Jede verbreitete Regelfassung soll kostenlos zugänglich bleiben. Collapsi selbst und Mark S. Ball zuzuordnende Inhalte unterliegen weiterhin dessen Rechten und werden von diesem Repository nicht neu lizenziert.

Bei Varianten, die von diesen Wiederbelebungsregeln abgeleitet sind, sollen Mark S. Ball und Johann Duscher genannt bleiben. Varianten ohne Verwendung oder Ableitung der Wiederbelebungsregeln benötigen keine Namensnennung Johann Duschers. Den genauen Geltungsbereich beschreibt [LICENSE.md](LICENSE.md); Rollen sind in [CONTRIBUTORS.md](CONTRIBUTORS.md) dokumentiert.

## Übersetzungen beitragen

Weitere Übersetzungen sind willkommen. Die Checkliste in [CONTRIBUTING.md](CONTRIBUTING.md) erklärt, wie eine Sprache ohne duplizierte Build-Konfiguration ergänzt wird.
