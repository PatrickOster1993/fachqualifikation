
#1
temperaturen = [15, 18, 20, 22, 17, 19, 21]
print(temperaturen)


#2
temp_sum = 0
temp_len = 0

for temp in temperaturen:
    temp_len += 1
    temp_sum += temp

    durchschnitt = temp_sum / temp_len

    print("Länge d. Liste:", temp_len)
    print("Summe d. Temperaturen:", temp_sum)
    print("Durchschnittstemperatur:", durchschnitt)


    print("Max:", min(temperaturen), "Max:", max(temperaturen))

   
    min_temp = temperaturen[0]
    max_temp = temperaturen[0]

    for temp in temperaturen:
        if temp < min_temp:
            min_temp = temp
        elif temp > max_temp:
            max_temp = temp

    print("Min:", min_temp, "Max:", max_temp)
    



    #4. Ersetzen der Temperatur 18°C durch den Wert18.
    

    i = 0

    while i < temp_len:
        temp = temperaturen[i]
        if temp  < 18:
            temperaturen[i] = 18
        i += 1

        print("Temperaturen nachher:", temperaturen)

        first_temp = temperaturen[0]
        last_temp = temperaturen[temp_len -1]
        
        temperaturen[0] = last_temp
        temperaturen[temp_len -1] = first_temp

        print("Temperaturen vertauscht:", temperaturen)

