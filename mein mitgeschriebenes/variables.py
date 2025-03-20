x = 1_000_000
y = 1
z = x + y
print("ergebnis:", z)
print(f"ergebnis: {z}")# besser, weil der gesamte text nach dem "f" als string interpretiert wird

hex_zahl = 0xABCD
print(f"hex_zahl: {hex_zahl}")# hexadezimalzahl wird in dezimalzahl umgewandelt
print(f"hex_zahl: {hex(hex_zahl)}")# hexadezimalzahl wird in hexadezimalzahl angezeigt

oct_zahl = 0o1234
print(f"oct_zahl: {oct_zahl}")# oktazahl wird in dezimalzahl umgewandelt
print(f"oct_zahl: {oct(oct_zahl)}")# oktazahl wird in oktazahl angezeigt

bin_zahl = 0b1010
print(f"bin_zahl: {bin_zahl}")# binärzahl wird in dezimalzahl umgewandelt
print(f"bin_zahl: {bin(bin_zahl)}")# binärzahl wird in binärzahl angezeigt

print (len(str(3)))# str() für eine zahl in einen string umwandeln und len() für die länge des strings

print (f"typ: {type("hallo")}")# type() für den typ einer variable

x = None

print(f"typ: {type(None)}")# None ist ein spezieller typ der nichts enthält und nicht null ist um fehler zu vermeiden

i=5
n=3

print (id (i), id (n))# id() für die speicheradresse einer variable

m= 5%3

print (m)# % für den rest einer division

d= 5//3

print (d)# // für den ganzzahligen teil einer division

h= 5**3

print (h)# ** für (5 hoch 3) eine potenz

a=3 # 0000 0011
b=6 # 0000 0101
c=a&b # 0000 0001
print(c) # & für eine bitweise und verknüpfung

###############################Absichtlich falsch############################################
print (4 and 3) # gibt einfach den letzten wert aus
print (4 or 3) # gibt den ersten wert aus
##############################################################################################

print (4>5 and 5>6)# and für eine "und" verknüpfung
print (4>5 or 5>6)# or für eine "oder" verknüpfung

d= 5
e= 5
f= 6

#if ist eine wenn prüfung und else ist eine sonst prüfung

if d==e:# == für eine gleichheitsprüfung
    print ("d und e sind gleich") # wenn es True ist wird der text ausgegeben
else:
        print ("d und e sind nicht gleich") # wenn es False ist wird der text ausgegeben


if d!=f:# != für eine ungleichheitsprüfung
    print ("d und f sind nicht gleich") # wenn es True ist wird der text ausgegeben
elif d==e:# elif für eine weitere wenn prüfung
    print ("d und e sind gleich") # wenn es True ist und der obere nicht, wird der text ausgegeben
else:
    print ("d und f sind gleich")# wenn es False ist wird der text ausgegeben


zahl1 = 50
zahl2 = zahl1 << 1 # << für eine bitweise verschiebung nach links, bei binär wird die zahl um eine stelle nach links verschoben
# also 0010 wird nach 0100 verschoben wenn es binär wäre und dezimal wird es verdoppelt

print (zahl2)



exit()