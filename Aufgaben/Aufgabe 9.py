# 1. Erstellt eine Liste mit den gegebenen Temperaturen
temperatures = [15, 18, 20, 22, 17, 19, 21]

# 2. Errechnet den durchschnitt der Temperaturen
average_temp = sum(temperatures) / len(temperatures)
print(f"Durchschnittstemperatur: {average_temp:.2f}°C")

# 3. Findet die Höchste und Niedrigste Temperatur und gibt sie aus
max_temp = max(temperatures)
min_temp = min(temperatures)
print(f"Höchste Temperatur: {max_temp}°C")
print(f"Niedrigste Temperatur: {min_temp}°C")

# 4. Ersetzt alle Temperaturen die niedrieger sind als 18 mit 18 Grad
temperatures = [temp if temp >= 18 else 18 for temp in temperatures]
print("Liste nach Ersetzung der Werte unter 18°C:", temperatures)

# 5. Tauscht die Temeratur des ersten Tages mit dem Letzen
temperatures[0], temperatures[-1] = temperatures[-1], temperatures[0]
print("Liste nach dem Tausch des ersten und letzten Tages:", temperatures)