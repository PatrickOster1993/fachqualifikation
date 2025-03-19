# komplexe datentypen

a = [42,7,1,2,4]
b = ["a","b","c"]
print(a)
print(b)

# Element hinzuzufügen
a.append(6)
print(a)

# auf Element via Index zugreifen.
print(a[0]) # liste fängt an mit index 0 -> lijst met 4 elementen zijn index 0 t/m 3

x = 1
y = 2

print("Speicheradresse von x:", id(x), "Speicheradresse von y:", id(y)) # id() is waar de variable word opgeslagen in het interne geheugen hier verschil 32 bit -> 4 byte (int)
# liste kriegen 159552 bits in beispiel herr Oster -> genoeg vrije ruimte voor append!!

# Referenzieren

c = ["d", "e", "f"]