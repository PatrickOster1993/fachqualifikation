import random 

def linearesuche (liste, wert): # sucht nach einem Wert in einer Liste
    for index in range (len(liste)): # geht durch die Liste
        if liste[index] == wert: # wenn der Wert gefunden wurde
            return index   # gibt die Position zurück
    return "Wert nicht gefunden" # z.B bei Python ist das None


meine_liste = []

for _ in range (10): # 10 mal
    meine_liste.append(random.randint(1,10))# fügt eine zufällige Zahl zwischen 1 und 10 hinzu

print (meine_liste)# meine zufällige Liste
print (linearesuche(meine_liste, 5)) # Suche nach der nummer 5, auf welcher Position ist sie?