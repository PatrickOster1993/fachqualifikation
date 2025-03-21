from time import sleep
import random

def check2bc():
    print("Möchten Sie noch ein andere Aufgabe sehen?")
    check = input("Drucken sie (y) um fort zu fahren oder ein andere Taste für Exit: ")
    if check != "y":
        print("Vielen Dank und bis Morgen")
        exit()

check = "y"
  
print("Herzlich Wilkommen bei Mattijn seine Hausaufgaben!!")
print("Hier ist das komplett Übersicht von Fachquali KW 12.")

while check == "y":
    print("Aufgaben Dienstag")
    print()
    print("Aufgabe 1: Dokumentation")
    print("Aufgabe 2: Konsolenausgabe")
    print("Aufgabe 3: Variablen und Operatoren")
    print("Aufgabe 4: Bit-Operatoren")
    print("Aufgabe 5: if-Bedingungen")
    print()
    print("Aufgaben Mittwoch")
    print()
    print("Aufgabe 6: if-Dokumentation")
    print("Aufgabe 7: Schleifen")
    print("Aufgabe 8: Listen")
    print("Aufgabe 9: Listen und Schleifen")
    print("Aufgabe 10: Bonus * Listen und Schleifen")
    print()
    print("Aufgaben Donnerstag")
    print()
    print("Aufgabe 11: Dokumentation")
    print("Aufgabe 12: 2D - Listen")
    print("Aufgabe 13: Tic-Tac-Toe")
    print("Aufgabe 14: Registerverwaltung")
    print("")
    print("Aufgaben Freitag")
    print()
    print("Aufgabe 15: Dokumentation")
    print("Aufgabe 16: Tic-Tac-Toe")
    print("Aufgabe 17: Bubblesort & Lineare Suche")
    print("")   
    print("Welche Aufgabe möchten Sie sehen:")
    eingabe = input("Geben Sie bitte ein Zahl von 1 bis 17 ein: ")
    int_eingabe = int(eingabe)
    if int_eingabe <= 0:
        print("Die Zahl darf nicht 0 oder negativ sein.")
    elif int_eingabe > 17:
        print("Die Zahl darf nicht größer sein als 14.")
    elif int_eingabe == 1:
        print("Sehe bitte die Inline Dokumentationen")
        check2bc()
    elif int_eingabe == 2:
        print("Sie haben sich für die Konsolenausgabe entschieden.")
        name = input("Geben Sie bitte Ihre Name ein: ")
        alter = input("Und wie alt sind Sie? ")
        lieblingsessen = input("Was essen sie am liebsten? ")
        print(f"Hallo {name}, freut mich Ihnen kennen zu lernen. Sagen Sie mal: Wie oft haben Sie in {alter} Jahre schon {lieblingsessen} gegessen?")
        check2bc()
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
            check2bc()
        elif int_tempcheck == 2:
            Fahrenheit = int(input("Geben Sie die Temperatur in Fahrenheit ein: "))
            Celsius = (Fahrenheit - 32) / 1.8
            print(f"{Fahrenheit} grad Fahrenheit ist {Celsius} grad Celsius")
            check2bc()
        else:
            tempcheck = int(input("Wählen Sie 1 oder 2: "))
    elif int_eingabe == 4:
        print("Sie haben sich für die Bit-Operatoren entschieden.")
        print("Wir definieren jetzt 2 variablen:")
        a = 0b1101
        b = 0b1011
        print(a)
        print(b)
        print("Mochten Sie (1) das Bitweise UND berechnen?")
        print("Mochten Sie (2) das Bitweise ODER berechnen?")
        print("Mochten Sie (3) das Bitweise XOR berechnen?")
        operator = int(input("Wählen Sie 1, 2 oder 3: "))
        if operator == 1:
            ergebnis = bin(a & b)
            print(f"Die UND berechnung von a und b ist: {ergebnis}")
            check2bc()
        elif operator == 2:
            ergebnis = bin(a | b)
            print(f"Die ODER berechnung von a und b ist: {ergebnis}")
            check2bc()
        elif operator == 3:
            ergebnis = bin(a ^ b)
            print(f"Die XOR berechnung von a und b ist: {ergebnis}")
            check2bc()
        else:
            operator = int(input("Wählen Sie 1, 2 oder 3: "))
    elif int_eingabe == 5:
        print("Sie haben sich für die if-Bedingungen entschieden.")
        userinput = float(input("Denken Sie sich bitte ein Zahl aus: "))
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
            for i in range(2, int(userinput)):
                if userinput % i == 0:
                    break
            else:
                print("Zusätzlich ist die Zahl eine Primzahl!!")
        check2bc()
    elif int_eingabe == 6:
        print("Sehe bitte die Inline Dokumentationen")
    elif int_eingabe == 7:
        print("Für die Schleifen-Übung habe ich ein Fizz-Buzz-Spiel erstellt")
        print("Es werden die Zahlen von 1 bis 100 ausgegeben,")
        print("Hinter vielfache von 3 wird FIZZ ausgegeben.")
        print("Hinter vielfache von 5 wird BUZZ ausgegeben.")
        print("Hinter vielfache von 3 und 5 wird FIZZBUZZ ausgegeben.")
        print("READY???")
        sleep(3)
        for i in range(101):
            if i % 3 == 0 and i % 5 == 0:
                print(i, "      FIZZBUZZ")
            elif i % 3 == 0:
                print(i, "      FIZZ")
            elif i % 5 == 0:
                print(i, "      BUZZ")
            else:
                print(i)
        check2bc()
    elif int_eingabe == 8:
        print("Sie haben sich für die Listen-Übung entschieden.")
        print("Die aufgabe besteht aus 7 verschiedene manipulationen die hier nacheinander durchgeführt werden.")
        print("Aber zuerst erstellen wir eine Liste mit 5 verschiedene Obstsorten:")
        mein_obstkorb = ["Birne", "Apfel", "Banane", "Avocado", "Pfirsich"]
        print(mein_obstkorb)
        sleep(3)
        print("Manipulation 1: Füge Kiwi hinzu:  * .append()")
        mein_obstkorb.append("Kiwi")
        print(mein_obstkorb)
        sleep(2)
        print("")
        print("Manipulation 2: Füge an 2. Stelle Mango hinzu:  * .insert()")
        mein_obstkorb.insert(1,"Mango")
        print(mein_obstkorb)
        sleep(2)
        print("")
        print("Manipulation 3: Entferne das letzte Element:  * .pop()")
        mein_obstkorb.pop()
        print(mein_obstkorb)
        sleep(2)
        print("")
        print("Manipulation 4: Entferne Banane falls vorhanden:  * .remove()")
        mein_obstkorb.remove("Banane")
        print(mein_obstkorb)
        sleep(2)
        print("")
        print("Manipulation 5: Drehe die Reihenfolge der Liste um:  * .reverse()")
        mein_obstkorb.reverse()
        print(mein_obstkorb)
        sleep(2)
        print("")
        print("Manipulation 6: Gebe die Länge der Liste aus:  * len()")
        print(len(mein_obstkorb))
        sleep(2)
        print("")
        print("Manipulation 7: Erstelle ein Kopie und gebe beide inkl speicheradressen aus:     * .copy()  / id()")
        mein_kopie = mein_obstkorb.copy()
        print(f"mein_obstkorb: {mein_obstkorb}, mein_kopie: {mein_kopie}")
        print(f"mein_obstkorb: {id(mein_obstkorb)} mein_kopie: {id(mein_kopie)}")
        check2bc()
    elif int_eingabe == 9:
        print("Sie haben sich für die Listen und Schleifen-Übung entschieden.")
        print("Die aufgabe besteht aus 5 verschiedene manipulationen die hier nacheinander durchgeführt werden.")
        print("Manipulation 1: Erstelle eine Liste mit 7 Temperaturen:")
        meine_woche = [15,18,20,22,17,19,21]
        print(meine_woche)
        sleep(2)
        print("")
        print("Manipulation 2: Berechne die Durchschnitttemperatur:  * for-schleife / len()")
        total = 0
        for tag in meine_woche:
            total = total + tag
        mein_durchschnitt = total / len(meine_woche)
        print(f"Durchschnitt Temperatur ist: {mein_durchschnitt}")
        sleep(2)
        print("")
        print("Manipulation 3: Gebe die min und max aus:  * min() / max()")
        print(f"Minimum Temperatur ist:  {min(meine_woche)}")
        print(f"Maximum Temperatur ist:  {max(meine_woche)}")    
        sleep(2)
        print("")
        print("Manipulation 4: Ersetze Temperaturen unter 18 durch 18:  * for-schleife / if")
        for i in range(len(meine_woche)):
            if meine_woche[i] < 18:
                meine_woche[i] = 18
        print(meine_woche)
        sleep(2)
        print("")
        print("Manipulation 5: Tausche die Erste und Letzte Wert:  * meine_woche[0] = meine_woche[-1]")
        meine_woche[0], meine_woche[-1] = meine_woche[-1], meine_woche[0]
        print(meine_woche)
        check2bc()
    elif int_eingabe == 10:
        print("die Bonusaufgabe:")
        print("Schritt 1: Erstelle eine Liste mit 20 Werte:")
        meine_aktien = [
            112.37, 89.54, 136.82, 103.19, 127.65, 
            94.28, 148.93, 81.76, 119.40, 107.52, 
            132.18, 96.85, 141.29, 85.63, 124.97, 
            100.71, 138.46, 92.30, 146.58, 79.15
        ]
        print("Schritt 2: Berechne und gebe aus:")
        print("A: Durchschnittliche wert:      * for-schleife / len()")
        total = 0
        for tag in meine_aktien:
            total = total + tag
        mein_durchschnitt = total / len(meine_aktien)
        print(f"Durchschnittliche Wert ist: {mein_durchschnitt}")
        sleep(2)
        print("")
        print("B: Gebe die min und max aus:  * min() / max()")
        print(f"Minimum Wert ist:  {min(meine_aktien)}")
        print(f"Maximum Wert ist:  {max(meine_aktien)}")    
        sleep(2)
        print("")
        print("C & D: Gebe die Tage wo die Kurs gestiegen oder gefallen ist aus:  * while / if schleife")
        steigen = 0
        fallen = 0
        x = 0
        i = 1
        while i < len(meine_aktien):
            if meine_aktien[i] > meine_aktien[x]:
                steigen += 1
            else:
                fallen +=1
            i += 1
            x += 1
        print(f"Tage gestiegen ist: {steigen}")
        print(f"Tage gefallenen ist: {fallen}")
        sleep(2)
        print("")
        print("Schritt 3: Finde den Tag wo die Kurs am starksten gestiegen ist:  * while / if schleife")
        steigen = 0
        meiste = 0
        m = 0
        n = 1
        while n < len(meine_aktien):
            if meine_aktien[n] > meine_aktien[m]:
                steigen = meine_aktien[n] - meine_aktien[m]
                if steigen > meiste:
                    meiste = steigen
            m += 1
            n += 1
        print(f"Die größte steigung der Kurs ist: {meiste}")
        sleep(2)
        print("")
        print("Schritt 4 - 1: Differenz zwischen Index [0] und [-1] Tage wo die Kurs gestiegen oder gefallen ist aus:  * while / if schleife")
        differenz = meine_aktien[0] - meine_aktien[-1]
        print(f"Die differenz zwischen erste und letzten Tag ist: {differenz}")
        sleep(2)
        print("")
        print("Schritt 4 -2: Gebe die gesamte Steigung und gefallen ist aus:  * while / if schleife")
        steigen = 0
        fallen = 0
        x = 0
        i = 1
        while i < len(meine_aktien):
            if meine_aktien[i] > meine_aktien[x]:
                steigen += meine_aktien[i] - meine_aktien[x]
            else:
                fallen += meine_aktien[i] - meine_aktien[x]
            i += 1
            x += 1
        print(f"Die gesamte Steigung ist: {steigen}")
        print(f"Die gesamte Rückgang ist: {fallen}")
        check2bc()
    elif int_eingabe == 11:
        print("Sehe bitte die Inline Dokumentationen")
        check2bc()    
    elif int_eingabe == 12:
        print("Sie haben sich für die 2-D Listen entschieden!!")
        print("Schritt 1: Gebe 4 Zeilen mit 4 Spalten mit random Zahlen zwischen 1 und 9 aus:")
        meine_tabelle = [ [], [], [], [] ]
        for spalte in meine_tabelle:
            for i in range(4):
                spalte.append(random.randint(1, 9))
        for spalte in meine_tabelle:
            print(spalte) 
        sleep(2)
        print("Schritt 2: Jetzt mit Zwischensumme pro Zeile und Grand Total:")
        zwischensumme = 0
        total = 0
        for spalte in meine_tabelle:
            for zahl in spalte:
                zwischensumme = zwischensumme + zahl
            print(spalte, "Zwischensumme ist:", zwischensumme)
            total = total + zwischensumme
            zwischensumme = 0
            sleep(0.5)
        print("Grand Total ist:", total)
        print("Schritt 3: Was ist die hochste Zahl, und was ist seine Indizes:")
        hochste_zahl = 0
        zeile_i = []
        spalte_i = []
        i = 0
        j = 0
        for spalte in meine_tabelle:
            j = 0
            for zahl in spalte:
                if zahl > hochste_zahl:
                    hochste_zahl = zahl
                    zeile_i = [i]
                    spalte_i = [j]
                elif zahl == hochste_zahl:
                    zeile_i.append(i)
                    spalte_i.append(j)
                j+= 1
            i += 1  
        print(f"Die hochste Zahl ist: {hochste_zahl}")
        print("Bitte von oben nach unten Lesen:")
        print(f"Die Zeile Index is: {zeile_i}")
        print(f"Die Spalte Index is: {spalte_i}")
        check2bc()
    elif int_eingabe == 13 or int_eingabe == 16:
        print("Sehe print.py für die Inline Dokumentation")
        check2bc()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    elif int_eingabe == 14:
        print("Sehe print.py für die Inline Dokumentation")
        check2bc()
    elif int_eingabe == 15:
        print("Sehe print.py für die Inline Dokumentation")
        check2bc()
    elif int_eingabe == 17:
        
        def Sort(liste, reverse=False):
            for i in range(len(liste)):
                for j in range(len(liste) - i - 1):
                    if (liste[j + 1][1] > liste[j][1]) == reverse:
                        liste[j + 1], liste[j] = liste[j], liste[j + 1]
            return liste
            



        print("Herzlich Wilkommen bei MediumMarkt - Unsere Service ist nicht schlecht, aber richtig gut ist es auch nicht...")
        Products = [["Laptop", 1200], ["Smartphone", 800], ["Tablet", 500], ["Monitor", 300], ["Maus", 50]]
        print("Hauptmenu")
        print("Sie haben 3 möglichkeiten:")
        print("Für sortieren wählen sie (1)")
        print("Um ein Product zu suchen wählen sie (2)")
        print("Um ein Product hinzu zu fügen wählen sie (3)")
        menu = input("Was möchten Sie machen? ")
        try:
            int_menu = int(menu)
        except ValueError as e:
            print("Bitte ein Zahl eingeben")
        if int_menu == 1:
            print("Für sortieren von Klein nach GroßGroß nach Klein wählen sie (1)")
            print("Für sortieren von Groß nach Klein wählen sie (2)")
            h_oder_r = input("Was möchten Sie machen? ")
            try:
                int_h_oder_r = int(h_oder_r)
            except ValueError as e:
                print("Bitte ein Zahl eingeben")
            if int_h_oder_r == 1:
                Sort(Products,reverse=False)
            elif int_h_oder_r == 2:
                Sort(Products, reverse=True)
            else:
                print("Bitte 1 oder 2 auswählen!")
                print("Die sortierte producten:", Products)
        if int_menu == 2:
            print("Welches Produkt suchen Sie:")
            

            print("Die sortierte producten:", Products)
        check2bc()
