########### Aufgabe 12 ############
import random 

myarray = []

for i in range (4): # geht 4 mal durch
    inner_myarray = [] # erstellt ein leeres array
    for j in range (4): # geht 4 mal durch
        inner_myarray.append(random.randint(1,9)) # fügt eine zufällige zahl zwischen 1 und 9 hinzu
    myarray.append(inner_myarray) # fügt das array inner_myarray zum array myarray hinzu
print (myarray)


for i in range (len(myarray)): # geht durch die zeilen
    arr1 = myarray[i] # speichert die zeile in arr1
    for j in range (len(arr1)): # geht durch die spalten
        print (arr1[j], end=" ") # gibt die elemente der zeile aus
    print () # gibt eine neue zeile aus

summe = sum(myarray[0]) + sum(myarray[1]) + sum(myarray[2]) # sum() addiert die elemente eines arrays
print (summe) 

# nochmal in schöner
summe = 0

for i in range (len(myarray)): # geht durch die zeilen
    arr1 = myarray[i] # speichert die zeile in arr1
    for j in range (len(arr1)): # geht durch die spalten
        summe += arr1[j] # addiert die elemente der zeile
print (summe)

grösste_zahl = 0

for i in range (len(myarray)): # geht durch die zeilen
    arr1 = myarray[i] # speichert die zeile in arr1
    for j in range (len(arr1)): # geht durch die spalten
        if grösste_zahl < arr1[j]: # wenn die grösste zahl kleiner als das element ist
            grösste_zahl = arr1[j] # dann ist das element die grösste zahl
print (grösste_zahl)

print ("#################")

########### Aufgabe 13 ############

# tictactoe = [
#     [" ", " ", " "], 
#     [" ", " ", " "], 
#     [" ", " ", " "]
#     ]                   # erstellt ein 3x3 array manuell

tictactoe = []

def tictactoe_erstellen(): # erstellt eine funktion
    for i in range (3): # geht 3 mal durch
        inner_tictactoe = [] # erstellt ein leeres array
        for j in range (3): # geht 3 mal durch
            inner_tictactoe.append(" ") # fügt ein leeres feld hinzu
        tictactoe.append(inner_tictactoe) # fügt das array inner_tictactoe zum array tictactoe hinzu
    return tictactoe # gibt das array tictactoe zurück

tictactoe_erstellen() # erstellt das array tictactoe weil es erst erstellt werden muss
print (tictactoe) # gibt das array tictactoe aus


while True:
    
    while True:
        print ("wo willst du das X Setzen?")
        x = (input("Zeile 1, 2 oder 3: "))
        if x != "1" and x != "2" and x != "3": # wenn x nicht 1, 2 oder 3 ist
            print ("Falsche Eingabe") # dann ist die eingabe falsch
        elif tictactoe[int(x)-1][int(y)-1] != " ": # wenn das feld nicht leer ist
            print ("Feld ist schon belegt") # dann ist das feld schon belegt
        else:
            break

    while True:
        y = (input("Spalte 1, 2 oder 3: "))
        if y != "1" and y != "2" and y != "3": # wenn y nicht 1, 2 oder 3 ist
            print ("Falsche Eingabe") # dann ist die eingabe falsch
        elif tictactoe[int(x)-1][int(y)-1] != " ": # wenn das feld nicht leer ist
            print ("Feld ist schon belegt") # dann ist das feld schon belegt
        else:
            break

    tictactoe[int(x)-1][int(y)-1] = "X" # setzt das X an die gewünschte stelle
    
    for i in range (len(tictactoe)): # geht durch die zeilen
        arr1 = tictactoe[i] # speichert die zeile in arr1
        for j in range (len(arr1)): # geht durch die spalten
            print (arr1[j], end=" ") # gibt die elemente der zeile aus
        print () # gibt eine neue zeile aus

    if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X": # wenn die erste zeile voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[1][0] == "X" and tictactoe[1][1] == "X" and tictactoe[1][2] == "X": # wenn die zweite zeile voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[2][0] == "X" and tictactoe[2][1] == "X" and tictactoe[2][2] == "X": # wenn die dritte zeile voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[0][0] == "X" and tictactoe[1][0] == "X" and tictactoe[2][0] == "X": # wenn die erste spalte voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[0][1] == "X" and tictactoe[1][1] == "X" and tictactoe[2][1] == "X": # wenn die zweite spalte voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[0][2] == "X" and tictactoe[1][2] == "X" and tictactoe[2][2] == "X": # wenn die dritte spalte voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[0][0] == "X" and tictactoe[1][1] == "X" and tictactoe[2][2] == "X": # wenn die erste diagonale voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[0][2] == "X" and tictactoe[1][1] == "X" and tictactoe[2][0] == "X": # wenn die zweite diagonale voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[0][0] != " " and tictactoe[0][1] != " " and tictactoe[0][2] != " " and tictactoe[1][0] != " " and tictactoe[1][1] != " " and tictactoe[1][2] != " " and tictactoe[2][0] != " " and tictactoe[2][1] != " " and tictactoe[2][2] != " ":
        print ("Unentschieden")
        break

    while True:
        print ("wo willst du das O Setzen?")
        x = (input("Zeile 1, 2 oder 3: "))
        if x != "1" and x != "2" and x != "3": # wenn x nicht 1, 2 oder 3 ist
            print ("Falsche Eingabe") # dann ist die eingabe falsch
        elif tictactoe[int(x)-1][int(y)-1] != " ": # wenn das feld nicht leer ist
            print ("Feld ist schon belegt") # dann ist das feld schon belegt
        else:
            break

    while True:
        y = (input("Spalte 1, 2 oder 3: "))
        if y != "1" and y != "2" and y != "3": # wenn y nicht 1, 2 oder 3 ist
            print ("Falsche Eingabe") # dann ist die eingabe falsch
        elif tictactoe[int(x)-1][int(y)-1] != " ": # wenn das feld nicht leer ist
            print ("Feld ist schon belegt") # dann ist das feld schon belegt
        else:
            break

    tictactoe[int(x)-1][int(y)-1] = "O" # setzt das X an die gewünschte stelle
    
    for i in range (len(tictactoe)): # geht durch die zeilen
        arr1 = tictactoe[i] # speichert die zeile in arr1
        for j in range (len(arr1)): # geht durch die spalten
            print (arr1[j], end=" ") # gibt die elemente der zeile aus
        print () # gibt eine neue zeile aus

    if tictactoe[0][0] == "O" and tictactoe[0][1] == "O" and tictactoe[0][2] == "O": # wenn die erste zeile voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[1][0] == "O" and tictactoe[1][1] == "O" and tictactoe[1][2] == "O": # wenn die zweite zeile voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[2][0] == "O" and tictactoe[2][1] == "O" and tictactoe[2][2] == "O": # wenn die dritte zeile voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[0][0] == "O" and tictactoe[1][0] == "O" and tictactoe[2][0] == "O": # wenn die erste spalte voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[0][1] == "O" and tictactoe[1][1] == "O" and tictactoe[2][1] == "O": # wenn die zweite spalte voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[0][2] == "O" and tictactoe[1][2] == "O" and tictactoe[2][2] == "O": # wenn die dritte spalte voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[0][0] == "O" and tictactoe[1][1] == "O" and tictactoe[2][2] == "O": # wenn die erste diagonale voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[0][2] == "O" and tictactoe[1][1] == "O" and tictactoe[2][0] == "O": # wenn die zweite diagonale voll ist
        print ("Du hast gewonnen")
        break
    if tictactoe[0][0] != " " and tictactoe[0][1] != " " and tictactoe[0][2] != " " and tictactoe[1][0] != " " and tictactoe[1][1] != " " and tictactoe[1][2] != " " and tictactoe[2][0] != " " and tictactoe[2][1] != " " and tictactoe[2][2] != " ":
        print ("Unentschieden")
        break


########### Aufgabe 14 ############

