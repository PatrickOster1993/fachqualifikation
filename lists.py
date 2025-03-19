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