# actress-proto
Prototyp für meine eigentliche Idee einen Daily Budget Klon in Pyhton zu bauen.

## Bereits unterstützte Features
- es gibt eine gui ;-)
- simple csv-Datei aus Dateisytem auswählbar und Einträge werden in einer Datenbank abspeichert
- Ausgabe aller eingelesen Daten
- Doppler werden erkannt und herausgefiltert

## nächstes große Ding
- schickere Anzeige
- Herzchen für Schauspielerinnen als Favorit vergebar

# Developer-stuff
## Prototyping
### MVPs to be done
- logik zum Speichern von heart-ranking (0 und 1)
- generische tabelle erstellen?!

### MVPs done
- Excel-Datei umsatz.csv einlesen
- Prototyp: Datenbank erstellen und mit Inhalten füttern
- daten auslesen
- Datenbank erstellen, aber nur 1x ;-)
- Import-Tabelle ohne Logik
- Daten in gui ausgeben (plain und ohne Formatierung)
- Auswahl-Dialog Import-Datei
- importierte Datei in Liste umwandeln
- Liste in sqlite-table abspeichern
- redundanzfreie Ablage
- Anzeige Input-Feld
- gui Ausgabe in Table formatieren
- input-felder für Ranking
- primary key sqlite aufnehmen --> SELECT ROWID, * FROM...
- enumerate() bei db_auslesen() eingebaut


## dev-backlog (technische Sünden)
- clean and pretty code, OOP
- screen refreshen, wenn Änderungen
- Alter ausrechnen
- dynamische Fenstergröße
- Logging-Feld: 0 nur import, nicht verändert / 1 bestätigte Kategorie / 2 automatische vergeben, noch nicht bestätigt
- Limit beim db_auslesen() einbauen für Paging
- Menü für auslesen, auswertung, ....
- Filter bei db_auslesen() für Dinge, die noch kein Logging Feld haben (s. oben)
