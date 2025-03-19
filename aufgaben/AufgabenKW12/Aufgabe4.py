# Aufgabe 4 Bit-Operatoren
# Schreiben Sie ein Python-Programm, das zwei binäre Zahlen vergleicht: Definieren Sie a = 0b1101
# und b = 0b1011, berechnen Sie das bitweise UND, das bitweise ODER und das bitweise XOR (=
# Exklusives ODER) dieser beiden Zahlen. Prüfen Sie auch, ob das Ergebnis des bitweisen UND eine
# ungerade Dezimalzahl ist und geben Sie die Ergebnisse in binärer und dezimaler Form aus.

a = 0b1101
b = 0b1011

print("UND: ", bin(a&b), "bzw.", (a&b))
print("ODER: ", bin(a|b))
print("XOR: ", bin(a^b))