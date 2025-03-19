

a = [3, 7, 1, 2]
b = ['a', 'b', 'c', 'd']






a.append(6)
print(a)

#
print(a[0])


# Verhalten des Speichers:

x = 1
y = 2

y = 3

# zunächst bei einfachen Variablen:
print("Speicheradresse von x:", id(x), "Speicheradresse von y:", id(y))

# jetzt bei Listen:
print("Liste a:", a, "Adresse a:", id(a))

a.append(0)

print("Liste a:", a, "Adresse a:", id(a))

c = ['d', 'e', 'f']

c = b

c.append('g')

print("Liste b:", b)
print("Liste c:", c)



# Vergleichsoperatoren

print([1,2,3] == [1,2,3])


#Listenelemente in einer Schleife durchlaufen:

i = 0

while i < 10:
    print(i)
    i += 1

