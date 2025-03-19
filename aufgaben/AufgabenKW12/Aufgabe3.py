# Aufgabe 3 Variablen und Operatoren
# Schreiben Sie ein Programm, das eine als Variable hinterlegte Temperatur in Celsius in Fahrenheit
# umrechnet und dann anschließend das Ergebnis in der Konsole ausgibt. Die Umrechnungsformel
# lautet wie folgt:
# mit F: Temperatur in Fahrenheit; sowie C: Temperatur in Celsius

input = float(input("Geben Sie die Temperatur ein (°C): "))
print("Temperatur in °F: ", (input*1.8)+32)