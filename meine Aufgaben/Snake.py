import random

feld = []
def Felderstellen():
    for i in range (10): 
        inner_tictactoe = [] 
        for j in range (10): 
            inner_tictactoe.append("X") 
        feld.append(inner_tictactoe) 
    feld [5][4],feld[5][5] = "S", "S"
    return feld 

def essen():
    while True:
        snackz = random.randint(0,9)
        snacks = random.randint(0,9)
        if feld[snackz][snacks] is not "S":
            feld[snackz][snacks] = "O"
            break

def pfeld():    
    for i in range (len(feld)):
        arr1 = feld[i] 
        for j in range (len(arr1)): 
            print (arr1[j], end=" ") 
        print () 

Felderstellen()
essen()
pfeld()

taste=None

input (taste)
if taste == "w":
    pass