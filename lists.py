# Komplexere / Zusammengesetzte Datentypen: Schwerpunkt Listen (="Array")

# Einfache Liste
a = [3, 7, 1, 2]
b = ["a", "b", "c"]
print(a)
print(b)

# Ein Element der List hinzufügen
a.append(6)
print(a)

# Auf Element innerhalb der Liste über Index zugreifen:
print(a[0]) # 1. Element = Index 0

# Verhalten des Speichers
x = 1
y = 2
print(f"Speicheradresse von X:{id(x)} Speicheradresse von y:{id(y)}")

# Jetzt bei Listen
print(f"Liste a: {a} Adresse a: {id(a)}")
a.append(0)
print(f"Liste a: {a} Adresse a: {id(a)}")
print(f"Liste b: {b} Adresse b: {id(b)}")
print(id(a) - id(b))

## Referenzieren
c = ['d', 'e', 'f']
print(f"Liste b: {b}")
print(f"Liste c: {c}")

c = b
c.append('g')

print(f"Liste b: {b}")
print(f"Liste c: {c}")

d = ['a', 'b', 'c', 'g']
print(f"Speicheradresse von c: {id(c)}")
print(f"Speicheradresse von d: {id(d)}")
print(c == d) # True Weil Identisch
print(c is d) # False Weil verschiedene Speicheradressen

d = c # Weist auf den selben Speicher zu 

print(f"Speicheradresse von c: {id(c)}")
print(f"Speicheradresse von d: {id(d)}")
print(c == d) # True Weil Identisch
print(c is d) # True Weil durch d=c auf den selben Speicher zugewiesen wird

# in-Operator (Prüft ob das Element vorhanden ist in der Liste)
print('############')
print('a' in d)
print('z' in d)

if 'a' in d:
    print("a befindet sich in d-Liste!")
else:
    print("Kein a in d-Liste vorhanden!")

# Listenelemente in einer Schleife durchlaufen
i = 0
while i < 10: # Kopfgesteuerte While Schleife
    print(i)
    i += 1 # i = i + 1 --> ++1

i = 0
while True: # Endlos Schleife # Fußgesteuerte While Schleife
    print(i)
    i += 1
    if i >= 10:
        break

# Jetzt auf Listen / Arrays angewandt
meine_liste = ["Hallo","ich","heisse","Murat"]

i = 0
while i < len(meine_liste):
    print(meine_liste[i])
    i += 1

# Reverse
i = len(meine_liste) - 1
while i >= 0:
    print(meine_liste[i])
    i -= 1

# Flexible Verwendung von Listen

hey = [3, "hallo", True]
print(hey)
print(type(hey)) # class = list

# for-Schleife mit vielen Ausprägungen
for i in range(0, len(meine_liste)):
    print(meine_liste[i])

# oder viel kompakter
for inhalt in meine_liste:
    print(inhalt)

# Weitere wichtige Grundlagen bzgl. Arrays / Listen

neue_liste = [1, 2, 3, 4]

## Letzes Element der liste entfernen

neue_liste.pop() # Entfernt die Position aus dem Index
print(neue_liste)

## Elemente an beliebiger Stelle hinzufügen

neue_liste.insert(1, 10) # (index, einZufügendeZahl)
print(neue_liste)

neue_liste.remove(10) # Entfernt den Wert aus der Liste
print(neue_liste)

kopierte_liste = neue_liste.copy() # Kopiert eine Liste

neue_liste.reverse() # Dreht die Liste um
print(neue_liste)

# Auf das erste und letzte Element der Liste zugreifen
print(neue_liste[0]) # Erstes Element
print(neue_liste[-1]) # Auf das Letzte Element der Liste zugreifen
print(neue_liste[1]) # Auf das zweite Element der Liste zugreifen
print(neue_liste[-2]) # Auf das vorletzte Element der Liste zugreifen

# Einen Abschnitt der Liste Printen
teil_liste = neue_liste[1:3]
print(teil_liste)

# Löschen einer Liste
print(neue_liste)
del neue_liste

