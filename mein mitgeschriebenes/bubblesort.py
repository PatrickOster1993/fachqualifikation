import random

def bubblesort (liste): # sortiert eine Liste nach dem Bubble Sort Algorithmus
    for i in range (len(liste)): # geht durch die Liste
        for j in range (len(liste)-i -1): # nimmt die Länge der Liste und zieht i ab weil die letzten i Elemente schon sortiert sind
            print (i,j) # gibt i und j aus damit man sieht wie der Algorithmus funktioniert
            if liste [j+1] < liste [j]: # wenn das nächste Element kleiner ist als das aktuelle
                liste[j], liste[j+1] = liste[j+1], liste[j] # dann tausche die beiden Elemente
    return liste

meine_liste = []

for i in range (10):    
    meine_liste.append(random.randint(1,100))

print (meine_liste)
print (bubblesort(meine_liste))

