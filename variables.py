x = 1_000_000
y = 1
z = x + y
print("Ergebnis z =", z)

print("#############")

#String
name = "Murat"
print(len(name))

hex_zahl = 0xABCD
print("Hexadezimal:", hex_zahl) # Default Hexadezimal umwandlung
print("Hexadezimal:", hex(hex_zahl)) # Hexadezimal Anzeige

oct_zahl = 0o1
print("Oktalzahl:", oct_zahl) # Default Oktalzahl umwandlung
print("Oktalzahl:", oct(oct_zahl)) # Oktalzahl Anzeige

dez_zahl = 11
print("Binärzahl: ", bin(dez_zahl)) # Dezimal zu Binär umwandlung

# Typen Check
print("Typ:", type(3)) # INT
print("Typ:", type("hallo")) # STRING
print("Typ:", type(True)) # BOOL
print("Typ:", type(3.14)) # FLOAT
print("Typ:", type(None)) # NONETYPE

# ID Checken
i = 5
n = 3
print(id(i) - id(n))

# Variablenbezeichnungen (prozedural)
test = 3
my_variable = 5

## Konstanten
PI = 3.14
SSH_KEY = "SDLSLFLGLSDGLLG"

# mehrere Variablen in einer Zeile deklarieren
x, y = 3, 5
print(f"Mehrere Variablen in 1 Zeile deklariert: {x}, {y}")

# Simple Verwendung für dieses sof. "Ideom".
x, y = y, x
print(f"Zahlen vertauscht: {x}, {y}")