













import random


def print_spielfeld(spielfeld):
    for zeile in spielfeld:
        for spalte in zeile:
            print(spalte, end="")
        print()


def init_spielfeld():
    spielfeld = []
    for _ in range(10):
        zeilen = []
        for _ in range(100):
            zeilen.append('.')
        spielfeld.append(zeilen)
    return spielfeld

def setze_schlange(spielfeld, schlange):
    x1 = schlange[0][0]
    y1 = schlange[0][1]
    x2 = schlange[1][0]
    y2 = schlange[1][1]

    spielfeld[x1][y1] = ''
    spielfeld[x2][y2] = ''
    return spielfeld

def bewege_schlange(spielfeld, schlange, richtung):

    kopf_zeile = schlange[0][0]
    kopf_spalte = schlange[0][1]
    schwanz_zeile = schlange[1][0]
    schwanz_spalte = schlange[1][1]
    spielfeld[kopf_zeile][kopf_spalte] = '.'
    spielfeld[schwanz_zeile][schwanz_spalte] = '.'
    spielfeld[kopf_zeile][kopf_spalte] = ''
    spielfeld[schwanz_zeile][schwanz_spalte] = ''
    spielfeld[kopf_zeile][kopf_spalte] = ''
    spielfeld[schwanz_zeile][schwanz_spalte] = ''
    spielfeld[kopf_zeile][kopf_spalte] = ''
    spielfeld[schwanz_zeile][schwanz_spalte] = ''
    spielfeld[kopf_zeile][kopf_spalte] = ''

    head = schlange[0]
    tail = schlange[1]

    if richtung == 'w':
        schlange[kopf_zeile] -= 1
        schlange[schwanz_zeile] = kopf_zeile
        schlange[schwanz_spalte] = kopf_spalte
        spielfeld[schwanz_zeile][schwanz_spalte] = '.'
        spielfeld[tail[0]][tail[1]] = '.'
        spielfeld[head[0]][head[1]] = ''
        spielfeld[tail[0]][tail[1]] = ''
        spielfeld[head[0]][head[1]] = ''

        print("schlange vorher:", schlange)
        schlange[0][1] -= 1
        schlange[1] = head
        spielfeld[tail[0]][tail[1]] = '.'
    elif richtung == 's':
        schlange[0][0] += 1
        schlange[1] = head
        spielfeld[tail[0]][tail[1]] = '.'
    elif richtung == 'a':
        schlange[0][1] -= 1
        schlange[1] = head
        spielfeld[tail[0]][tail[1]] = '.'
    elif richtung == 'd':
        schlange[0][1] += 1
        schlange[1] = head
        spielfeld[tail[0]][tail[1]] = '.'
    elif richtung == 'b':
        schlange[0][0] -= 1
        schlange[1] = head
        spielfeld[tail[0]][tail[1]] = '.'

        print("schlange nachher:", schlange)

    return {"spielfeld": spielfeld, "schlange": schlange}

def essen_erreicht(schlange, essen):
    
    schlangenkopf = schlange[0]
    if schlangenkopf == essen:
        return True
    return False
        
mein_spielfeld = init_spielfeld()

meine_schlange = [[5, 4], [5, 5]]
mein_essen = []

  

setze_schlange(mein_spielfeld, meine_schlange)


while True:
    x = random.randint(0, 9)
    y = random.randint(0, 9)

    if mein_spielfeld[x][y] is not '':
        mein_spielfeld[x][y] = ''
        mein_essen.append(x)
        mein_essen.append(y)
        break

print_spielfeld(mein_spielfeld)
print("Essen:", mein_essen)




# Ntzereingaben (= Steuerung der Schlange)
richtung = input("Bitte Richtung eingeben (wasd): ")
# w = nach oben bewegen
# s = nach unten bewegen
# a = nach links bewegen
# d = nach rechts bewegen

bewegte_schlange = bewege_schlange(mein_spielfeld, meine_schlange, richtung)
neues_spielfeld = bewegte_schlange["spielfeld"]
neue_schlange = bewegte_schlange["schlange"]
print_spielfeld(neues_spielfeld)




