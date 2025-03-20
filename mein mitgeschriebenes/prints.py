
hallo = "Hallo"
name = input ("dein name: ")
name = (hallo + " " + name)# " " für ein leerzeichen, parameter ändert man nicht direkt weil bad practice

a = 5
print("Meine zahl ist", a, sep="#", end=" ") # wird automatisch ein leerzeichen eingefügt
#sep für ein anderes zeichen als leerzeichen
#end für ein anderes zeichen als ein zeilenumbruch 

print("Meine zahl ist" + "5")# "+" für ein zusammen schreiben ohne leerzeichen

#print (f"blabla") f macht es einfacher weil alles danach als string interpretiert wird, {} für eine variable

exit()