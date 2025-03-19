# Aufgabe 6 Dokumentation
# Ziehen Sie sich nochmals den im heutigen Unterricht geschriebenen Code zu Gemüte und erstellen
# Sie sich eine Zusammenfassung, welche die wichtigsten, heute behandelten Kerninhalte umfasst.


#####################################################################################################

# Listen

# Methode	                Beschreibung
# list.append(x)	        Fügt x am Ende der Liste hinzu
# list.insert(i, x)	        Fügt x an Index i ein
# list.extend(iterable)	    Fügt eine andere Liste oder Iterable hinzu
# list.remove(x)	        Entfernt das erste Vorkommen von x
# list.pop(i)         	    Entfernt und gibt das Element an Index i zurück
# list.clear()	            Entfernt alle Elemente aus der Liste
# list.index(x)       	    Gibt den Index des ersten Vorkommens von x zurück
# list.count(x)       	    Gibt die Anzahl der Vorkommen von x zurück
# list.sort()         	    Sortiert die Liste aufsteigend
# list.reverse()      	    Kehrt die Reihenfolge der Liste um
# list.copy()         	    Erstellt eine flache Kopie der Liste


# 1. Erstellen einer Liste
my_list = [1, 2, 3, 4, 5]  # Eine einfache Liste mit Zahlen
empty_list = []  # Leere Liste
mixed_list = [1, "Hallo", 3.14, True]  # Liste mit verschiedenen Datentypen

# 2. Zugriff auf Elemente
print(my_list[0])   # Erstes Element (Index 0)
print(my_list[-1])  # Letztes Element
print(my_list[1:4]) # Slicing: [Start:Ende] -> [2, 3, 4]
print(my_list[:3])  # Die ersten drei Elemente
print(my_list[::2]) # Jedes zweite Element


# 3. Liste bearbeiten
my_list[2] = 99  # Ändert das dritte Element


my_list.append(6)  # Fügt 6 am Ende hinzu
my_list.insert(2, 42)  # Fügt 42 an Index 2 ein
my_list.extend([7, 8, 9])  # Mehrere Elemente hinzufügen


my_list.remove(3)  # Entfernt das erste Vorkommen von 3
popped = my_list.pop()  # Entfernt und gibt das letzte Element zurück
popped_at_index = my_list.pop(1)  # Entfernt Element an Index 1
del my_list[0]  # Löscht das erste Element
my_list.clear()  # Leert die gesamte Liste


# 4. Listen durchlaufen (Schleifen)
for item in my_list:
    print(item)

for index, value in enumerate(my_list):
    print(f"Index {index}: {value}")

# 5. Listenlänge
length = len(my_list)  # Anzahl der Elemente in der Liste

# 6. Sortieren und Umkehren
my_list.sort()  # Sortiert die Liste aufsteigend
my_list.sort(reverse=True)  # Sortiert die Liste absteigend
sorted_list = sorted(my_list)  # Erstellt eine sortierte Kopie
my_list.reverse()  # Kehrt die Reihenfolge der Liste um


# 7. Prüfen, ob ein Element in der Liste ist
if 3 in my_list:
    print("3 ist in der Liste")


# 8. Zählen von Elementen
count = my_list.count(2)  # Zählt, wie oft die 2 vorkommt

# 9. Index eines Elements finden
index = my_list.index(4)  # Gibt den Index des ersten Vorkommens von 4 zurück


# 10. Listen kopieren
copy_list = my_list.copy()  # Erstellt eine Kopie
copy_list = my_list[:]  # Alternative Methode
import copy
deep_copy = copy.deepcopy(my_list)  # Falls verschachtelte Listen enthalten sind


# 11. Listen kombinieren (Zusammenfügen)
new_list = my_list + [10, 11, 12]  # Verbindet zwei Listen

################################################################################################################

# Schleifen

# Befehl	            Bedeutung
# for	                Iteriert über eine Sequenz (Liste, String, etc.)
# while	            Wiederholt Code, solange eine Bedingung erfüllt ist
# range               (start, stop, step)	Erzeugt eine Zahlenfolge für for-Schleifen
# break	            Beendet die Schleife sofort
# continue	        Springt zur nächsten Iteration
# else                nach Schleife	Wird ausgeführt, wenn die Schleife nicht durch break beendet wurde
# enumerate()	        Gibt Index und Wert in einer for-Schleife zurück
# zip()	            Kombiniert mehrere Listen und iteriert gleichzeitig darüber
# reversed()	        Durchläuft eine Sequenz rückwärts
# List Comprehension	Kompakte Möglichkeit, Listen zu erstellen


# 1. for-Schleife (iterative Schleife)
# Die for-Schleife wird verwendet, um über iterierbare Objekte wie Listen, Tupel, Strings oder Dictionaries zu laufen.

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

word = "Python"

for char in word:
    print(char)


# 2. while-Schleife (bedingte Schleife)
# Die while-Schleife wird so lange ausgeführt, bis eine bestimmte Bedingung False wird.

x = 0
while x < 5:
    print(x)
    x += 1

# 3. range() (Zahlenbereiche in Schleifen)
# Die Funktion range(start, stop, step) erzeugt eine Sequenz von Zahlen und wird oft in for-Schleifen verwendet.

for i in range(5):
    print(i)  # Gibt 0, 1, 2, 3, 4 aus

for i in range(2, 6):
    print(i)  # Gibt 2, 3, 4, 5 aus

for i in range(0, 10, 2):
    print(i)  # Gibt 0, 2, 4, 6, 8 aus

for i in range(10, 0, -2):
    print(i)  # Gibt 10, 8, 6, 4, 2 aus

# 4. break (Schleife vorzeitig beenden)
# Mit break kann eine Schleife vorzeitig abgebrochen werden.

x = 0
while x < 10:
    if x == 5:
        break  # Beendet die Schleife, wenn x == 5
    print(x)
    x += 1

for num in range(10):
    if num == 5:
        break  # Beendet die Schleife, wenn num == 5
    print(num)


# 5. continue (Nächste Iteration überspringen)
# Mit continue wird die aktuelle Iteration übersprungen, und die Schleife fährt mit der nächsten fort.

for num in range(5):
    if num == 2:
        continue  # Springt zur nächsten Iteration, wenn num == 2
    print(num)

# 6. else nach einer Schleife
# Die else-Klausel wird ausgeführt, wenn die Schleife normal beendet wird (d. h. nicht durch break unterbrochen wird).

for num in range(3):
    print(num)
else:
    print("Schleife normal beendet")

# 7. enumerate() (Index und Wert in for-Schleifen)
# enumerate() gibt sowohl den Index als auch den Wert eines iterierbaren Objekts zurück.

fruits = ["Apfel", "Banane", "Kirsche"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 8. zip() (Mehrere Listen gleichzeitig durchlaufen)
# zip() kombiniert zwei oder mehr Listen und gibt Tupel zurück.

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} ist {age} Jahre alt")

# 9. reversed() (Schleife rückwärts)
# Mit reversed() kann eine Liste oder range() rückwärts durchlaufen werden.

for num in reversed(range(5)):
    print(num)

# 10. List Comprehensions (Schleifen in einer Zeile)
# List Comprehensions sind eine kurze, elegante Art, Listen mit Schleifen zu erstellen.

squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]


#######################################################################################
# Methoden

# 1. Methoden definieren (def)
# Methoden werden mit def definiert und können Parameter haben.

def greet(name):
    return f"Hallo, {name}!"

print(greet("Alice"))  # Ausgabe: Hallo, Alice!

# Beispiel: Methode mit Standardwerten

def greet(name="Gast"):
    return f"Hallo, {name}!"

print(greet())         # Ausgabe: Hallo, Gast!
print(greet("Bob"))    # Ausgabe: Hallo, Bob!

#####################################################################################
#Noch nicht gemacht aber wichtig!

# 2. Klassenmethoden (self)
# In Klassen sind Methoden an Objekte gebunden und benötigen self, um auf Instanzvariablen zuzugreifen.

class Person:
    def __init__(self, name):
        self.name = name  # Instanzvariable

    def greet(self):
        return f"Hallo, mein Name ist {self.name}."

p = Person("Alice")
print(p.greet())  # Ausgabe: Hallo, mein Name ist Alice.


# 3. Statische Methoden (@staticmethod)
# Statische Methoden sind unabhängig von Instanzvariablen und brauchen kein self.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))  # Ausgabe: 8


# 4. Klassenmethoden (@classmethod)
# Klassenmethoden greifen mit cls auf die Klasse zu.
class Counter:
    count = 0  # Klassenvariable

    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count

print(Counter.increment())  # Ausgabe: 1
print(Counter.increment())  # Ausgabe: 2

# 5. *args (Variable Anzahl an Argumenten)
# *args ermöglicht, beliebig viele Argumente als Tupel zu übergeben.

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))  # Ausgabe: 10


# 6. **kwargs (Keyword-Argumente)
# **kwargs ermöglicht, beliebig viele benannte Argumente als Dictionary zu übergeben.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Berlin")


# 7. Methodenüberladung mit Standardwerten
# Python unterstützt keine echte Methodenüberladung, aber Standardwerte oder *args/**kwargs können genutzt werden.

def greet(name="Gast", greeting="Hallo"):
    return f"{greeting}, {name}!"

print(greet())                # Ausgabe: Hallo, Gast!
print(greet("Alice"))         # Ausgabe: Hallo, Alice!
print(greet("Bob", "Hi"))     # Ausgabe: Hi, Bob!


# 8. Lambda-Funktionen (Anonyme Methoden)
# Lambda-Funktionen sind kurze, anonyme Methoden, die für einfache Operationen nützlich sind.

add = lambda a, b: a + b
print(add(3, 5))  # Ausgabe: 8

# Beispiel: Lambda in sorted()

names = ["Alice", "Bob", "Charlie"]
names.sort(key=lambda name: len(name))
print(names)  # Ausgabe: ['Bob', 'Alice', 'Charlie']


# 9. Rekursive Methoden
# Eine Methode kann sich selbst aufrufen (Rekursion), z. B. zur Berechnung der Fakultät.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Ausgabe: 120


# 10. Methoden-Dekoratoren
# Dekoratoren sind Funktionen, die eine Methode modifizieren, ohne sie zu ändern.

