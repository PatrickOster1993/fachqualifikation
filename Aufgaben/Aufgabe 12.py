import random

# 1. Erstelle eine 4x4 Liste mit zufälligen Zahlen zwischen 1 und 9
matrix = []
for zeile in range(4):
    reihe = []
    for spalte in range(4):
        zahl = random.randint(1, 9)
        reihe.append(zahl)
    matrix.append(reihe)

# 2. Gib die Liste schön formatiert aus
print("Zufällige 4x4-Liste:")
for reihe in matrix:
    for zahl in reihe:
        print(zahl, end=" ")
    print()

# 3. Berechne die Summe aller Zahlen
gesamtsumme = 0
for reihe in matrix:
    for zahl in reihe:
        gesamtsumme += zahl
print(f"\nGesamtsumme aller Zahlen: {gesamtsumme}")

# 4. Finde die größte Zahl und alle Positionen davon
max_wert = matrix[0][0]
pos_max = []
for zeile in range(4):
    for spalte in range(4):
        if matrix[zeile][spalte] > max_wert:
            max_wert = matrix[zeile][spalte]
            pos_max = [(zeile+1, spalte+1)] #bessere verständlich da wir ja bei 1 anfangen aber das array bei 0
        elif matrix[zeile][spalte] == max_wert:
            pos_max.append((zeile+1, spalte+1)) #bessere verständlich da wir ja bei 1 anfangen aber das array bei 0

print(f"\nGrößter Wert: {max_wert} an Position(en): {pos_max}")
print(f"Anzahl der Positionen mit größtem Wert: {len(pos_max)}")

# 5. Zeige die größten Werte jeder einzelnen Zeile
print("\nGrößte Werte jeder Zeile:")
for zeile in range(4):
    max_zeile = matrix[zeile][0]
    for spalte in range(1, 4):
        if matrix[zeile][spalte] > max_zeile:
            max_zeile = matrix[zeile][spalte]
    print(f"Zeile {zeile}: Größter Wert = {max_zeile}")