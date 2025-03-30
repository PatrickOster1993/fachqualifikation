## Zusatzaufgabe 1 Snake
## Ein Spieler steuert eine Schlange in einem 10×10-Spielfeld. Ziel ist es, Essen (🍎 ) zu fressen, ohne
## gegen die Wände oder sich selbst zu stoßen. Die Schlange wächst mit jeder Mahlzeit. Folgende
## Implementierungen sind vorzunehmen:
## 1. Erstellen Sie ein 10×10-Spielfeld mit '.' für leere Felder.
## 2. Die Schlange startet mit einer Länge von 2 Feldern und wird durch 'S' dargestellt.
## 3. Platzieren Sie zufällig ein Essen auf dem Spielfeld.
## 4. Der Spieler gibt Bewegungen ein:
## - W (hoch), S (runter), A (links), D (rechts).
## - Die Schlange bewegt sich in die gewählte Richtung.
## - Falls sie das Essen erreicht, wächst sie.
## 5. Regeln für das Spiel:
## - Die Schlange kann sich nicht durch Wände bewegen (führt zum Game Over).
## - Wenn die Schlange sich selbst berührt, verliert der Spieler.
## - Nach dem Fressen erscheint das nächste Essen an einer zufälligen Position.
## 6. Nach jedem Zug wird das Spielfeld aktualisiert und ausgegeben.
## 7. Das Spiel endet, wenn:
## - Die Schlange gegen eine Wand oder sich selbst stößt (= verloren).
## - Optional: Der Spieler eine bestimmte Länge (z. B. 10 Felder) erreicht (= gewonnen).


import random

# Konstanten
SPIELFELD_GROESSE = 10
SNAKE_SYMBOL = 'S'
LEERES_FELD = '.'
ESSEN_SYMBOL = '🍎'
RICHTUNGEN = {'W': (0, -1), 'S': (0, 1), 'A': (-1, 0), 'D': (1, 0)}

# Funktion zum Initialisieren des Spielfelds
def initialisiere_spielfeld():
    spielfeld = [[LEERES_FELD for _ in range(SPIELFELD_GROESSE)] for _ in range(SPIELFELD_GROESSE)]
    return spielfeld

# Funktion zum Platzieren der Schlange
def platziere_schlange(spielfeld):
    x, y = SPIELFELD_GROESSE // 2, SPIELFELD_GROESSE // 2
    spielfeld[y][x] = SNAKE_SYMBOL
    spielfeld[y][x - 1] = SNAKE_SYMBOL
    return [(x, y), (x - 1, y)]

# Funktion zum Platzieren des Essens
def platziere_essen(spielfeld, schlange):
    while True:
        x, y = random.randint(0, SPIELFELD_GROESSE - 1), random.randint(0, SPIELFELD_GROESSE - 1)
        if spielfeld[y][x] == LEERES_FELD and (x, y) not in schlange:
            spielfeld[y][x] = ESSEN_SYMBOL
            return (x, y)

# Funktion zum Drucken des Spielfelds
def drucke_spielfeld(spielfeld):
    for reihe in spielfeld:
        print(' '.join(reihe))
    print()

# Funktion zum Aktualisieren des Spielfelds
def aktualisiere_spielfeld(spielfeld, schlange, essen, richtung):
    kopf = schlange[0]
    neuer_kopf = (kopf[0] + richtung[0], kopf[1] + richtung[1])

    # Prüfen, ob die Schlange gegen eine Wand stößt
    if (neuer_kopf[0] < 0 or neuer_kopf[0] >= SPIELFELD_GROESSE or
        neuer_kopf[1] < 0 or neuer_kopf[1] >= SPIELFELD_GROESSE):
        return False

    # Prüfen, ob die Schlange sich selbst berührt
    if neuer_kopf in schlange:
        return False

    # Schlange bewegen
    schlange.insert(0, neuer_kopf)
    spielfeld[neuer_kopf[1]][neuer_kopf[0]] = SNAKE_SYMBOL

    # Prüfen, ob das Essen erreicht wurde
    if neuer_kopf == essen:
        essen = platziere_essen(spielfeld, schlange)
    else:
        schwanz = schlange.pop()
        spielfeld[schwanz[1]][schwanz[0]] = LEERES_FELD

    return schlange, essen

# Hauptspielschleife
def spiel():
    spielfeld = initialisiere_spielfeld()
    schlange = platziere_schlange(spielfeld)
    essen = platziere_essen(spielfeld, schlange)

    drucke_spielfeld(spielfeld)

    while True:
        richtung_input = input("Bewegung (W, S, A, D): ").upper()

        if richtung_input not in RICHTUNGEN:
            print("Ungültige Eingabe! Bitte W, S, A oder D eingeben.")
            continue

        richtung = RICHTUNGEN[richtung_input]
        ergebnis = aktualisiere_spielfeld(spielfeld, schlange, essen, richtung)

        if ergebnis is False:
            print("Game Over! Deine Schlange hat sich selbst oder eine Wand berührt.")
            break
        else:
            schlange, essen = ergebnis

        drucke_spielfeld(spielfeld)

        # Optional: Prüfen, ob die Schlange eine bestimmte Länge erreicht hat
        if len(schlange) >= 10:
            print("Gewonnen! Du hast die maximale Länge erreicht.")
            break

# Spiel starten
if __name__ == "__main__":
    spiel()
