zahl = int(input("Bitte gebe eine Zahl ein: "))

ist_gerade = zahl % 2 == 0


if zahl < 0:
    print("Die Zahl ist negativ.")

if zahl == 0:
    print("Die Zahl ist null.")

if zahl > 0 and ist_gerade:
    print("Die Zahl ist positiv und gerade")

if zahl > 0 and not ist_gerade:
    if zahl > 100:
        print("Die Zahl ist positiv, ungerade und größer als 100")
    else:
        print("Die Zahl ist positiv und ungerade")

#Bonus Primezahl

def is_prime(zahl):
    for i in range(2,zahl):
        print("Index", i, "//", "Rest:", zahl%i)
        if (zahl%i) == 0:
            return False
    return True

if  is_prime(zahl):
    print("Es ist eine Primzahl")