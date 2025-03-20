# 1. Erstellt eine Liste mit den gegebenen Temperaturen
temperaturen = [15, 18, 20, 22, 17, 19, 21]

# 2. Errechnet den durchschnitt der Temperaturen
average_temp = sum(temperaturen) / len(temperaturen)
print(f"Durchschnittstemperatur: {average_temp:.2f}°C")

# 3. Findet die Höchste und Niedrigste Temperatur und gibt sie aus
max_temp = max(temperaturen)
min_temp = min(temperaturen)
print(f"Höchste Temperatur: {max_temp}°C")
print(f"Niedrigste Temperatur: {min_temp}°C")

# 4. Ersetzt alle Temperaturen die niedrieger sind als 18 mit 18 Grad
temperaturen = [temp if temp >= 18 else 18 for temp in temperaturen]
print(f"Liste nach Ersetzung der Werte unter 18°C: {temperaturen}")

# 5. Tauscht die Temeratur des ersten Tages mit dem Letzen
temperaturen[0], temperaturen[-1] = temperaturen[-1], temperaturen[0]
print(f"Liste nach dem Tausch des ersten und letzten Tages: {temperaturen}")