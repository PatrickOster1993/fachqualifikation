#Ein Spieler steuert eine Schlange in einem 10×10-Spielfeld. Ziel ist es, Essen zu fressen ohne
#gegen die Wände oder sich selbst zu stoßen. Die Schlange wächst mit jeder Mahlzeit. Folgende Implementierungen sind vorzunehmen:

    #Erstellen Sie ein 10×10-Spielfeld mit '.' für leere Felder.
    #Die Schlange startet mit einer Länge von 2 Feldern und wird durch 'S' dargestellt. Platzieren Sie zufällig ein Essen auf dem Spielfeld.

#Der Spieler gibt Bewegungen ein:
    #- W (hoch), S (runter), A (links), D (rechts).
    #- Die Schlange bewegt sich in die gewählte Richtung.
#- Falls sie das Essen erreicht, wächst sie.

#Regeln für das Spiel:
#- Die Schlange kann sich nicht durch Wände bewegen (führt zum Game Over).
#- Wenn die Schlange sich selbst berührt, verliert der Spieler.
#- Nach dem Fressen erscheint das nächste Essen an einer zufälligen Position.
#Nach jedem Zug wird das Spielfeld aktualisiert und ausgegeben. Das Spiel endet, wenn:
#- Die Schlange gegen eine Wand oder sich selbst stößt (= verloren).
#- Optional: Der Spieler eine bestimmte Länge (z. B. 10 Felder) erreicht (= gewonnen).

import random

def print_spielfeld(spielfeld):
    for zeile in spielfeld:
        for spalte in zeile:
            print(spalte, end = "")
        print()

def init_spielfeld():
    spielfeld = []
    for _ in range(10):
        zeile = []
        for _ in range(10):
            zeile.append(" . ")
        spielfeld.append(zeile)
    return spielfeld

def setze_schlange(spielfeld, schlange):
    #                    Kopf   Schwanz
    # meine_schlange = [[5, 4], [5, 5]]
    kopf_zeile = schlange[0][0]
    kopf_spalte = schlange[0][1]
    schwanz_zeile = schlange[1][0]
    schwanz_spalte = schlange[1][1]

    spielfeld[kopf_zeile][kopf_spalte] = ' S '
    spielfeld[schwanz_zeile][schwanz_spalte] = ' S '

def bewege_schlange(spielfeld, schlange, richtung):
    #                    Kopf   Schwanz
    # meine_schlange = [[5, 4], [5, 5]]
    print("Schlange vorher: ", schlange)
    kopf_zeile = schlange[0][0]
    kopf_spalte = schlange[0][1]
    schwanz_zeile = schlange[1][0]
    schwanz_spalte = schlange[1][1]

    if richtung == 'w':
        schlange[0][0] -= 1

    elif richtung == 's':
        schlange[0][0] += 1

    elif richtung == 'a':
        schlange[0][1] -= 1

    elif richtung == 'd':
        schlange[0][1] += 1

    schlange[1][0] = kopf_zeile
    schlange[1][1] = kopf_spalte

    kopf_zeile_neu = schlange[0][0]
    kopf_spalte_neu = schlange[0][1]
    schwanz_zeile_neu = schlange[1][0]
    schwanz_spalte_neu = schlange[1][1]

    spielfeld[kopf_zeile_neu][kopf_spalte_neu] = ' S '
    spielfeld[schwanz_zeile_neu][schwanz_spalte_neu] = ' S '
    spielfeld[schwanz_zeile][schwanz_spalte] = ' . '

    print("Schlange nachher: ", schlange)
        
    return {"spielfeld": spielfeld, "schlange": schlange}

def essen_erreicht(schlange, essen):
    # Gib True zurück, wenn Indizes von Schlangenkopf == Indizes von essen
    schlangenkopf = schlange[0]
    if schlangenkopf == essen:
        return True
    return False

mein_spielfeld = init_spielfeld()
# print_spielfeld(mein_spielfeld)

meine_schlange = [[5, 4], [5, 5]]
mein_essen = []

setze_schlange(mein_spielfeld, meine_schlange)

while(True):
    x = random.randint(0, 9)
    y = random.randint(0, 9)

    if mein_spielfeld[x][y] is not ' S ':
        mein_spielfeld[x][y] = ' O '
        mein_essen.append(x)
        mein_essen.append(y)
        break

print_spielfeld(mein_spielfeld)

# Nutzereingaben (= Steuerung der Schlange)
meine_richtung = input("Bitte Richtung eingeben (wasd): ")
# w = nach oben bewegen
# s = nach unten bewegen
# a = nach links bewegen
# d = nach rechts bewegen

bewegte_schlange = bewege_schlange(mein_spielfeld, meine_schlange, meine_richtung)
neue_schlange = bewegte_schlange["schlange"]
neues_spielfeld = bewegte_schlange["spielfeld"]
setze_schlange(neues_spielfeld, neue_schlange)

if essen_erreicht(neue_schlange, mein_essen):
    pass
    # füge der Schlange ein weiteres Körperteil hinzu...

print_spielfeld(neues_spielfeld)





