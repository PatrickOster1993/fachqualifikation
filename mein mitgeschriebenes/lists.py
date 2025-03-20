
a=[3,7,1,2] # liste mit 4 int elementen
b=["a","b","c"] # liste mit 3 string elementen

a.append(1) # fügt der liste a das element 1 hinzu
print(a) # gibt die liste a aus

print (a[0]) # gibt das erste element der liste aus


x=1
y=2

y=3 # überschreibt den wert von y
y+=1 # erhöht den wert von y um 1

print (f"speicher von x: {id(x)} speicher von y: {id(y)}") # gibt die speicheradressen von x und y aus

print (f"Liste: {a} Adresse: {id(a)}") # gibt die liste a und die speicheradresse von a aus
a.append (0) # fügt der liste a das element 0 hinzu
print (f"Liste: {a} Adresse: {id(a)}") # gibt die liste a und die speicheradresse von a aus
print (f"Liste: {b} Adresse: {id(b)}") # gibt die liste b und die speicheradresse von b aus
print (id(a) - id(b)) # gibt die differenz der speicheradressen von a und b aus

c=b 
print (f"Liste b: {b}") # gibt die liste b aus
print (f"Liste c: {c}") # gibt die liste c aus
print ("################") # trennt die ausgaben
c.append("g") # fügt der liste c das element "g" hinzu

print (f"Liste b: {b}") # gibt die liste b aus
print (f"Liste c: {c}") # gibt die liste c aus
# b und c zeigen auf die gleiche speicheradresse, deshalb wird die liste b auch verändert
# wenn vorher c= b.copy() gemacht wird, dann wird die liste b nicht verändert

print ([1,2,3] == [1,2,3]) # vergleicht die listen und gibt true aus, wenn sie gleich sind
print ([1,2,3] < [1,2,3,4]) # vergleicht die listen und gibt true aus, wenn die erste liste kleiner ist

d= ["a", "b", "c", "g"]

d=c

print (f"wert von c: {c} Adresse von c: {id(c)}") # gibt die liste c und die speicheradresse von c aus
print (c==d) # vergleicht die listen und gibt true aus, wenn sie gleich sind
print (f"wert von d: {d} adresse von d: {id(d)}") # gibt die liste d und die speicheradresse von d aus
print (c is d) # vergleicht die speicheradressen und gibt true aus, wenn sie gleich sind
# bei == wird der inhalt verglichen und bei "is" die speicheradresse

print ("################")
print ("a" in d) # gibt true aus, wenn "a" in der liste d ist
print ("z" in d) # gibt true aus, wenn "z" in der liste d ist

if "a" in d:                           # wenn "a" in der liste d ist
    print ("a ist in der liste")       # wird der text ausgegeben
else:                                  # sonst
    print ("a ist nicht in der liste") # wird der text ausgegeben

i = 0

while i < 10: # solange i kleiner als 10 ist, das ist eine kopfgesteuerte schleife
    print (i) # wird i ausgegeben
    i += 1 # i wird um 1 erhöht

i=0

for i in range(10): # solange i kleiner als 10 ist, das ist eine fußgesteuerte schleife
    print (i) # wird i ausgegeben und um 1 erhöht weil range(10) von 0 bis 9 geht

# eine kopfgesteuerte schleife (while) muss nicht einmal durchlaufen werden, wenn die bedingung nicht erfüllt ist
# eine kopfgesteuerte schleife (while) wird durch eine bedingung gesteuert, eine fußgesteuerte (for) schleife durch eine zählvariable
# eine fußgesteuerte schleife (for) wird mindestens einmal durchlaufen, selbst wenn die bedingung nicht erfüllt ist

while True: # unendliche schleife
    print (i) # gibt i aus
    i+= 1 # erhöht i um 1
    if i > 0: # wenn i größer als 0 ist
        break # wird die schleife beendet
# das ist eine fußgesteuerte schleife über while, weil sie durch die zählvariable i gesteuert wird


mylist = ["hallo", "ich", "bin", "eine", "liste"]
i=0


while i < len(mylist): # solange i kleiner als die länge der liste ist
    print (mylist[i]) # wird das element an der stelle i ausgegeben
    i += 1 # i wird um 1 erhöht
# das gibt die liste aus


i=len(mylist)-1 # i wird auf die länge der liste minus 1 gesetzt um das letzte element auszugeben
while i >= 0: # solange i größer oder gleich 0 ist
    print (mylist[i]) # wird das element an der stelle i ausgegeben
    i -= 1 # i wird um 1 verringert
# das gibt die liste rückwärts aus

newlist = [1,2,3,4]

#################vergiss nicht das die zählung bei 0 beginnt####################

newlist.append(5) # fügt der liste das element 5 hinzu
print (newlist) # gibt die liste aus

newlist.pop # entfernt das letzte element der liste
print (newlist) # gibt die liste aus

newlist.pop (2) # entfernt das element an der stelle 2
print (newlist) # gibt die liste aus

newlist.insert(1,10) # fügt an der stelle 1 das element 10 ein
print (newlist) # gibt die liste aus

newlist.reverse() # dreht die liste um
print (newlist) # gibt die liste aus

newlist.remove(10) # entfernt das element 10 aus der liste, falls es doppelt vorkommt wird nur das erste entfernt
print (newlist) # gibt die liste aus

print (newlist[2]) # gibt das element an der stelle 2 aus
print (newlist[-1]) # gibt das letzte element aus
print (newlist[1:3]) # gibt die elemente von der stelle 1 bis 3 aus
print (newlist[:2]) # gibt die elemente von der stelle 0 bis 2 aus
print (newlist[2:]) # gibt die elemente von der stelle 2 bis zum ende aus
print (newlist.index(3)) # gibt die stelle des elements 3 aus
print (newlist.count(3)) # gibt die anzahl des elements 3 aus



newlist.clear() # löscht die liste 
del newlist # löscht die liste, unterschied zu clear ist das del die liste komplett löscht und clear nur die elemente entfernt

