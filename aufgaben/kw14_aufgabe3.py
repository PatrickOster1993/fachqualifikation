# Aufgabe 3 Rekursion
# Überprüfen Sie alle bisherigen, innerhalb der Fachqualifikation behandelten, Übungsaufgaben und
# identifizieren Sie jene, die einen iterativen Lösungsansatz verwenden. Schreiben Sie anschließend
# die betreffenden Lösungen so um, dass stattdessen ein rekursiver Ansatz verfolgt wird.

# -*- coding: utf-8 -*-

# Identifikation von iterativen Lösungen und Umwandlung in rekursive Lösungen:

# Beispiel 1: Berechnung der Fakultät
# Iterative Lösung:
def fakultaet_iterativ(n):
    ergebnis = 1
    for i in range(1, n + 1):
        ergebnis *= i
    return ergebnis

# Rekursive Lösung:
def fakultaet_rekursiv(n):
    if n == 1:
        return 1
    return n * fakultaet_rekursiv(n - 1)

# Beispiel 2: Summe aller Zahlen von 1 bis n
# Iterative Lösung:
def summe_iterativ(n):
    ergebnis = 0
    for i in range(1, n + 1):
        ergebnis += i
    return ergebnis

# Rekursive Lösung:
def summe_rekursiv(n):
    if n == 1:
        return 1
    return n + summe_rekursiv(n - 1)

# Beispiel 3: Fibonacci-Folge
# Iterative Lösung:
def fibonacci_iterativ(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Rekursive Lösung:
def fibonacci_rekursiv(n):
    if n <= 1:
        return n
    return fibonacci_rekursiv(n - 1) + fibonacci_rekursiv(n - 2)

# Beispiel 4: Palindrom-Überprüfung
# Iterative Lösung:
def ist_palindrom_iterativ(wort):
    return wort == wort[::-1]

# Rekursive Lösung:
def ist_palindrom_rekursiv(wort):
    if len(wort) <= 1:
        return True
    if wort[0] != wort[-1]:
        return False
    return ist_palindrom_rekursiv(wort[1:-1])
