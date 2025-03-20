temperatures = [15, 18, 20, 22, 17, 19, 21]
average_temperature = sum(temperatures) / len(temperatures)
print(f"Durchschnitt: {average_temperature:.2f}")
max_temperature = max(temperatures)
print(f"Max: {max_temperature}")
min_temperature = min(temperatures)
print(f"Min: {min_temperature}")
for i in range(len(temperatures)):
    if temperatures[i] < 18:
        temperatures[i] = 18.5
print(temperatures)

temperatures[0], temperatures[-1] = temperatures[-1], temperatures[0] # Tuple-Unpacking / Mehrfachzuweisung
print(temperatures)