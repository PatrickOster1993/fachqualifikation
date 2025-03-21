# Aufgabe 12 2D-Listen
# Erstellen Sie eine 4×4-Liste (= 4 Zeilen u. 4 Spalten) mit zufälligen Zahlen zwischen 1 und 9.
# Implementieren Sie danach folgende Funktionen:
# 1. Geben Sie die Liste in einer schönen Tabellenform auf der Konsole aus.
# 2. Berechnen Sie die Summe aller Zahlen.
# 3. Finden Sie die größte Zahl in der Liste sowie deren Indizes.

liste = [
    [4, 5, 1, 6],
    [7, 3, 6, 9],
    [1, 8, 5, 6],
    [4, 7, 3, 2]
]

maxarray2d = 0
maxarray = 0

for i in range(len(liste)):
    if maxarray < max(liste[i]):
        maxarray = max(liste[i])
    if maxarray > maxarray2d:
        maxarray2d = maxarray
print(maxarray2d)