########### Aufgabe 12 ############

myarray = [
    [1,2,3,4],
    [5,6,7,8],
    [9,8,7,6]
]

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

tictactoe = [
    ["" , "" , ""],
    ["" , "" , ""],
    ["" , "" , ""]
]

