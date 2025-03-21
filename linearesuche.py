# Lineare Suche funktioniert auch bei unsortierten Listen
# Wir suchen einen bestimmten Wert aus einer gegebenen Liste

import random

def linearesuche(liste, wert):
    for index in range(len(liste)):
        if liste[index] == wert:
            return index
    return "Kein Index gefunden!" # z. B. bei Python!

# Liste erstellen:
meine_liste = []

# Liste initialisieren (Zufallswerte) = unsortierte Liste
for _ in range(10):
    meine_liste.append(random.randint(1, 10))
print("Unsortierte Liste:")
print(meine_liste)

# Suche starten (Wir wollen den Index des Wertes haben, falls vorhanden!)
print("Index:", linearesuche(meine_liste, 5))