###########Aufgabe2############
name= input("was ist ihr name ")
alter = input("was ist ihr Alter ")
lieblingsessen = input("was ist ihr lieblingsessen ")
print (f"ihr name ist {name}, sie sind {alter} jahre alt und ihr lieblingsessen ist {lieblingsessen}")

###########Aufgabe3############
TemperaturC= float(input("geben sie die temperatur in celsius ein "))
TemperaturF= TemperaturC*1.8+32
print (f"die temperatur in fahrenheit ist {TemperaturF}")

###########Aufgabe4############
a= 0b1101
b= 0b1011

c= a & b #bitweise und
d= a | b #bitweise oder
e= a ^ b #bitweise exklusiv oder

if c%2==0:
    print ("c ist gerade")
else:
    print ("c ist ungerade")
        
#dezimal
print (c, d, e)
#binär
print (bin(c), bin(d), bin(e))

###########Aufgabe5############

eingabe = int(input("geben sie eine zahl ein "))
if eingabe<0:
    print ("die zahl ist negativ")

if eingabe==0:
    print ("die zahl ist 0")

if eingabe>0 and eingabe%2==0:
    print ("die zahl ist positiv und gerade")

if eingabe>0 and eingabe%2!=0:
    if eingabe>100:
        print ("die zahl ist positiv und ungerade und größer als 100")
    else: 
        print ("die zahl ist positiv und ungerade")

if eingabe>1:
    for i in range(2, eingabe):
        if (eingabe % i) == 0:
            print("die zahl ist keine primzahl")
            break
    else:
        print("die zahl ist eine primzahl")