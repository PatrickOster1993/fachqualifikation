print("Herzlich Wilkommen bei Mattijn seine Hausaufgaben!!")
print("Wir haben gestern 5 Aufgaben bekommen:")
print("Aufgabe 1: Dokumentation")
print("Aufgabe 2: Konsolenausgabe")
print("Aufgabe 3: Variablen und Operatoren")
print("Aufgabe 4: Bit-Operatoren")
print("Aufgabe 5: if-Bedingungen")
print("")
print("Welche Aufgabe möchten Sie sehen:")

check = "y"

while check == "y":
    eingabe = input("Geben Sie bitte ein Zahl von 1 bis 5 ein: ")
    int_eingabe = int(eingabe)
    if int_eingabe <= 0:
        print("Die Zahl darf nicht 0 oder negativ sein.")
    elif int_eingabe > 5:
        print("Die Zahl darf nicht größer sein als 5.")
    elif int_eingabe == 1:
        print("Sehe print.py für die Inline Dokumentation")
        print("Möchten Sie noch ein andere Aufgabe sehen?")
        check = input("Drucken sie (y) um fort zu fahren oder ein andere Taste für Exit: ")
        if check != "y":
            print("Vielen Dank und bis Morgen")
            exit()
    elif int_eingabe == 2:
        print("Sie haben sich für die Konsolenausgabe entschieden.")
        name = input("Geben Sie bitte Ihre Name ein: ")
        alter = input("Und wie alt sind Sie? ")
        lieblingsessen = input("Was essen sie am liebsten? ")
        print(f"Hallo {name}, freut mich Ihnen kennen zu lernen. Sagen Sie mal: Wie oft haben Sie in {alter} Jahre schon {lieblingsessen} gegessen?")
        print("Möchten Sie noch ein andere Aufgabe sehen?")
        check = input("Drucken sie (y) um fort zu fahren oder ein andere Taste für Exit: ")
        if check != "y":
            print("Vielen Dank und bis Morgen")
            exit()
    elif int_eingabe == 3:
        print("Sie haben sich für die Temperaturumrechner entschieden.")
        print("Mochten Sie (1) von Normal nach Fahrenheit, oder")
        print("Mochten Sie (2) von Fahrenheit nach Normal")
        tempcheck = input("Wählen Sie 1 oder 2: ")
        int_tempcheck = int(tempcheck)
        if int_tempcheck == 1:
            Celsius = int(input("Geben Sie die Temperatur in Celsius ein: "))
            Fahrenheit = 1.8 * Celsius + 32
            print(f"{Celsius} grad Celsius ist {Fahrenheit} grad Fahrenheit")
            print("Möchten Sie noch ein andere Aufgabe machen?")
            check = input("Drucken sie (y) um fort zu fahren oder ein andere Taste für Exit: ")
            if check != "y":
                print("Vielen Dank und bis Morgen")
                exit()
        elif int_tempcheck == 2:
            Fahrenheit = int(input("Geben Sie die Temperatur in Fahrenheit ein: "))
            Celsius = (Fahrenheit - 32) / 1.8
            print(f"{Fahrenheit} grad Fahrenheit ist {Celsius} grad Celsius")
            print("Möchten Sie noch ein andere Aufgabe machen?")
            check = input("Drucken sie (y) um fort zu fahren oder ein andere Taste für Exit: ")
            if check != "y":
                print("Vielen Dank und bis Morgen")
                exit()
        else:
            tempcheck = int(input("Wählen Sie 1 oder 2: "))
    elif int_eingabe == 4:
        print("Sie haben sich für die Bit-Operatoren entschieden.")
        print("Wir definieren jetzt 2 variablen:")
        print("a = 0b1101")
        print("b = 0b1011")
        a = 0b1101
        b = 0b1011
        print("Mochten Sie (1) das Bitweise UND berechnen?")
        print("Mochten Sie (2) das Bitweise ODER berechnen?")
        print("Mochten Sie (3) das Bitweise XOR berechnen?")
        operator = int(input("Wählen Sie 1, 2 oder 3: "))
        if operator == 1:
            ergebnis = bin(a & b)
            print(f"Die UND berechnung von a und b ist: {ergebnis}")
            print("Möchten Sie noch ein andere Aufgabe machen?")
            check = input("Drucken sie (y) um fort zu fahren oder ein andere Taste für Exit: ")
            if check != "y":
                print("Vielen Dank und bis Morgen")
                exit()
        elif operator == 2:
            ergebnis = bin(a | b)
            print(f"Die ODER berechnung von a und b ist: {ergebnis}")
            print("Möchten Sie noch ein andere Aufgabe machen?")
            check = input("Drucken sie (y) um fort zu fahren oder ein andere Taste für Exit: ")
            if check != "y":
                print("Vielen Dank und bis Morgen")
                exit()
        elif operator == 3:
            ergebnis = bin(a ^ b)
            print(f"Die XOR berechnung von a und b ist: {ergebnis}")
            print("Möchten Sie noch ein andere Aufgabe machen?")
            check = input("Drucken sie (y) um fort zu fahren oder ein andere Taste für Exit: ")
            if check != "y":
                print("Vielen Dank und bis Morgen")
                exit()
        else:
            operator = int(input("Wählen Sie 1, 2 oder 3: "))
    elif int_eingabe == 5:
        print("Sie haben sich für die if-Bedingungen entschieden.")
        userinput = int(input("Denken Sie sich bitte ein Zahl aus: "))
        if userinput < 0:
            print("Die Zahl ist negativ.")
        elif userinput == 0:
            print("Die Zahl ist null.")
        else:
            if userinput % 2 == 0:
                print("Die Zahl ist positiv und gerade.")
            else:
                if userinput > 100:
                    print("Die Zahl ist positiv, ungerade und größer als 100.")
                else:
                    print("Die Zahl ist positiv und ungerade")
        if userinput > 1:
            for i in range(2, userinput):
                if userinput % i == 0:
                    break
            else:
                print("Zusätzlich ist die Zahl eine Primzahl!!")
        print("Möchten Sie noch ein andere Aufgabe machen?")
        check = input("Drucken sie (y) um fort zu fahren oder ein andere Taste für Exit: ")
        if check != "y":
            print("Vielen Dank und bis Morgen")
            exit()
        
            

