
def tictactoe_erstellen(): # erstellt eine funktion
    for i in range (3): # geht 3 mal durch
        inner_tictactoe = [] # erstellt ein leeres array
        for j in range (3): # geht 3 mal durch
            inner_tictactoe.append(" ") # fügt ein leeres feld hinzu
        tictactoe.append(inner_tictactoe) # fügt das array inner_tictactoe zum array tictactoe hinzu
    return tictactoe # gibt das array tictactoe zurück

def setzenzeile():
    while True:
        print ("wo willst du dein Zeichen Setzen?")
        zeile = int((input("Zeile 1, 2 oder 3: ")))
        if zeile != 1 and zeile != 2 and zeile != 3: # wenn x nicht 1, 2 oder 3 ist
            print ("Falsche Eingabe") # dann ist die eingabe falsch
        else:
            return (zeile)

def setzenspalte():
    while True:
        spalte = int(input(("Spalte 1, 2 oder 3: ")))
        if spalte != 1 and spalte != 2 and spalte != 3: # wenn y nicht 1, 2 oder 3 ist
            print ("Falsche Eingabe") # dann ist die eingabe falsch
        else:
            return (spalte)

def prüfenleer(zeile, spalte, xoro):
    if tictactoe[zeile-1][spalte-1] != " ":
        print ("Feld ist schon belegt")
        return False
    else:
        tictactoe[zeile-1][spalte-1] = xoro
        return True

def feld():
    for i in range (len(tictactoe)): # geht durch die zeilen
        arr1 = tictactoe[i] # speichert die zeile in arr1
        for j in range (len(arr1)): # geht durch die spalten
            print (arr1[j], end=" ") # gibt die elemente der zeile aus
        print () # gibt eine neue zeile aus

def siegesprüfung(xoro):
    if tictactoe[0][0] == xoro and tictactoe[0][1] == xoro and tictactoe[0][2] == xoro:
        gewonnen = True
        return(gewonnen)
    elif tictactoe[1][0] == xoro and tictactoe[1][1] == xoro and tictactoe[1][2] == xoro:
        gewonnen = True
        return(gewonnen)
    elif tictactoe[2][0] == xoro and tictactoe[2][1] == xoro and tictactoe[2][2] == xoro:
        gewonnen = True
        return(gewonnen)
    elif tictactoe[0][0] == xoro and tictactoe[1][0] == xoro and tictactoe[2][0] == xoro:
        gewonnen = True
        return(gewonnen)
    elif tictactoe[0][1] == xoro and tictactoe[1][1] == xoro and tictactoe[2][1] == xoro:
        gewonnen = True
        return(gewonnen)
    elif tictactoe[0][2] == xoro and tictactoe[1][2] == xoro and tictactoe[2][2] == xoro:
        gewonnen = True
        return(gewonnen)
    elif tictactoe[0][0] == xoro and tictactoe[1][1] == xoro and tictactoe[2][2] == xoro: 
        gewonnen = True
        return(gewonnen)
    elif tictactoe[0][2] == xoro and tictactoe[1][1] == xoro and tictactoe[2][0] == xoro: 
        gewonnen = True
        return(gewonnen)
    
def prüfenvoll():
    for i in range(len(tictactoe)):
        for j in range(len(tictactoe[i])):
            if tictactoe[i][j] == " ":
                return False
    return True

def xoro():
    if spielerzug==True:
        return("X")
    else:
        return("O")
    


spielerzug = True
tictactoe = []
tictactoe_erstellen() # erstellt das array tictactoe weil es erst erstellt werden muss

while True:
    feld()
    zeichen = xoro()
    while True:    
        zeile = setzenzeile()
        spalte = setzenspalte()
        if prüfenleer(zeile, spalte, zeichen):
            break
    
    if prüfenvoll():
        feld()
        print ("Feld ist voll")
        break
    
    if siegesprüfung(zeichen):
        feld()
        print (f"{zeichen} hat gewonnen!")
        break

    spielerzug = not spielerzug






# while True:
    
#     while True:
#         print ("wo willst du dein Zeichen Setzen?")
#         x = (input("Zeile 1, 2 oder 3: "))
#         if x != "1" and x != "2" and x != "3": # wenn x nicht 1, 2 oder 3 ist
#             print ("Falsche Eingabe") # dann ist die eingabe falsch
#         elif tictactoe[int(x)-1][int(y)-1] != " ": # wenn das feld nicht leer ist
#             print ("Feld ist schon belegt") # dann ist das feld schon belegt
#         else:
#             break

#     while True:
#         y = (input("Spalte 1, 2 oder 3: "))
#         if y != "1" and y != "2" and y != "3": # wenn y nicht 1, 2 oder 3 ist
#             print ("Falsche Eingabe") # dann ist die eingabe falsch
#         elif tictactoe[int(x)-1][int(y)-1] != " ": # wenn das feld nicht leer ist
#             print ("Feld ist schon belegt") # dann ist das feld schon belegt
#         else:
#             break

#     tictactoe[int(x)-1][int(y)-1] = "X" # setzt das X an die gewünschte stelle
    
#     for i in range (len(tictactoe)): # geht durch die zeilen
#         arr1 = tictactoe[i] # speichert die zeile in arr1
#         for j in range (len(arr1)): # geht durch die spalten
#             print (arr1[j], end=" ") # gibt die elemente der zeile aus
#         print () # gibt eine neue zeile aus

#     if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X": # wenn die erste zeile voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[1][0] == "X" and tictactoe[1][1] == "X" and tictactoe[1][2] == "X": # wenn die zweite zeile voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[2][0] == "X" and tictactoe[2][1] == "X" and tictactoe[2][2] == "X": # wenn die dritte zeile voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[0][0] == "X" and tictactoe[1][0] == "X" and tictactoe[2][0] == "X": # wenn die erste spalte voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[0][1] == "X" and tictactoe[1][1] == "X" and tictactoe[2][1] == "X": # wenn die zweite spalte voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[0][2] == "X" and tictactoe[1][2] == "X" and tictactoe[2][2] == "X": # wenn die dritte spalte voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[0][0] == "X" and tictactoe[1][1] == "X" and tictactoe[2][2] == "X": # wenn die erste diagonale voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[0][2] == "X" and tictactoe[1][1] == "X" and tictactoe[2][0] == "X": # wenn die zweite diagonale voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[0][0] != " " and tictactoe[0][1] != " " and tictactoe[0][2] != " " and tictactoe[1][0] != " " and tictactoe[1][1] != " " and tictactoe[1][2] != " " and tictactoe[2][0] != " " and tictactoe[2][1] != " " and tictactoe[2][2] != " ":
#         print ("Unentschieden")
#         break

#     while True:
#         print ("wo willst du das O Setzen?")
#         x = (input("Zeile 1, 2 oder 3: "))
#         if x != "1" and x != "2" and x != "3": # wenn x nicht 1, 2 oder 3 ist
#             print ("Falsche Eingabe") # dann ist die eingabe falsch
#         elif tictactoe[int(x)-1][int(y)-1] != " ": # wenn das feld nicht leer ist
#             print ("Feld ist schon belegt") # dann ist das feld schon belegt
#         else:
#             break

#     while True:
#         y = (input("Spalte 1, 2 oder 3: "))
#         if y != "1" and y != "2" and y != "3": # wenn y nicht 1, 2 oder 3 ist
#             print ("Falsche Eingabe") # dann ist die eingabe falsch
#         elif tictactoe[int(x)-1][int(y)-1] != " ": # wenn das feld nicht leer ist
#             print ("Feld ist schon belegt") # dann ist das feld schon belegt
#         else:
#             break

#     tictactoe[int(x)-1][int(y)-1] = "O" # setzt das X an die gewünschte stelle
    
#     for i in range (len(tictactoe)): # geht durch die zeilen
#         arr1 = tictactoe[i] # speichert die zeile in arr1
#         for j in range (len(arr1)): # geht durch die spalten
#             print (arr1[j], end=" ") # gibt die elemente der zeile aus
#         print () # gibt eine neue zeile aus

#     if tictactoe[0][0] == "O" and tictactoe[0][1] == "O" and tictactoe[0][2] == "O": # wenn die erste zeile voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[1][0] == "O" and tictactoe[1][1] == "O" and tictactoe[1][2] == "O": # wenn die zweite zeile voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[2][0] == "O" and tictactoe[2][1] == "O" and tictactoe[2][2] == "O": # wenn die dritte zeile voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[0][0] == "O" and tictactoe[1][0] == "O" and tictactoe[2][0] == "O": # wenn die erste spalte voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[0][1] == "O" and tictactoe[1][1] == "O" and tictactoe[2][1] == "O": # wenn die zweite spalte voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[0][2] == "O" and tictactoe[1][2] == "O" and tictactoe[2][2] == "O": # wenn die dritte spalte voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[0][0] == "O" and tictactoe[1][1] == "O" and tictactoe[2][2] == "O": # wenn die erste diagonale voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[0][2] == "O" and tictactoe[1][1] == "O" and tictactoe[2][0] == "O": # wenn die zweite diagonale voll ist
#         print ("Du hast gewonnen")
#         break
#     if tictactoe[0][0] != " " and tictactoe[0][1] != " " and tictactoe[0][2] != " " and tictactoe[1][0] != " " and tictactoe[1][1] != " " and tictactoe[1][2] != " " and tictactoe[2][0] != " " and tictactoe[2][1] != " " and tictactoe[2][2] != " ":
#         print ("Unentschieden")
#         break