# Aufgabe 5 if-Bedingungen
# Schreiben Sie ein Python-Programm, das eine Zahl vom Benutzer einliest und folgende Prüfungen
# durchführt:
# 1. Falls die Zahl negativ ist → "Die Zahl ist negativ.“
# 2. Falls die Zahl 0 ist → "Die Zahl ist null.“
# 3. Falls die Zahl positiv und gerade ist → "Die Zahl ist positiv und gerade.“
# 4. Falls die Zahl positiv und ungerade ist, dann:
# (1) Falls die Zahl größer als 100 ist → "Die Zahl ist positiv, ungerade und größer als 100.“
# (2) Ansonsten → "Die Zahl ist positiv und ungerade.“
# 5. Bonus: Prüfen Sie, ob die Zahl eine Primzahl ist (s. https://de.wikipedia.org/wiki/
# Primzahl)! Falls ja, ergänzen Sie die Ausgabe um: "Zusätzlich ist die Zahl eine Primzahl!“

test = int(input("Zu prüfende Zahl: "))

if test < 0:
    print("Die Zahl ist negativ")
if test == 0:
    print("die Zahl ist Null")
if test > 0 and test % 2 == 0:
    print("Die zahl ist positiv und gerade.")
if test > 0 and test % 2 == 1:
    if test > 100:
        print("Die Zahl ist größer als 100, positiv und ungerade.")
    else:
        print("Die Zahl ist positiv und ungerade.")
if test > 1:
    for i in range(2, test):
        if (test % i) == 0:
            print("die zahl ist KEINE primzahl.")
            break
    else:
        print("die zahl ist eine primzahl.")
