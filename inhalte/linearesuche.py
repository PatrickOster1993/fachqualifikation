# Lineare Suche funktion


import random

def linearesuchen(liste, wert):
    for index in range(len(liste)):
         if liste[index] == wert:
             return index
         return "kein Index gefunden!" # z. B. bei Python!

# Liste erstellen:
meine_liste = []

# Liste initialisieren (Zufallswerte) = unsortirte Liste
for i in range(10):
    meine_liste.append(random.randint(0, 50))
print("Unsortierte Liste:")
print(meine_liste)

# Suche starten (Wir wollen den index des Wertes haben falls er existiert