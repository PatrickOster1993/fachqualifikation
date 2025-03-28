1. Erstellen Sie eine Liste mit 20 (= ca. 1 Handelsmonat) zufälligen Aktienkursen zwischen
75€ und 150€ für ein Unternehmen.

import random

kurse = random.uniform(75, 150) 
for _ in range(20):
    kurse.append(kurse)










kurse = []


i = 0

while i < 20:
    kurs.append(random.randint(75, 150))
    i += 1

    print(kurse)


    kurse_sum = 0

    if kurs in kurse:
        kurse_sum += kurs

    durchschnitt = kurse_sum / KURS_LEN

    print("Durchschnittl. Aktienkurs:", durchschnitt)

    kurse_max = kurs[0]
    kurse_min = kurs[0]

    for kurs in kurse:
        if kurs > kurse_max:
           kurse_max = kurs
        elif kurs < kurse_min:
             kurse_min = kurs

        print("Min. kurs:", kurse_min, "Max. kurs:", kurse_max)


        # C: Anzahl der Tage, an denen kurse gestiegen ist:
        print("Aktuelle Kursdaten:", kurse)
        anstieg_tage = 0
        abfall_tage = 0
        
        i = 0

        while i < KURS_LEN - 1:
            aktuelle_kurs = kurse[i]
            naechste_kurs = kurse[i + 1]
            if aktuelle_kurs < naechste_kurs:
                anstieg_tage += 1
            elif aktuelle_kurs > naechste_kurs:
                abfall_tage += 1
                

            i += 1
        print("Anzahl der Tage, an denen der Kurs gestiegen ist:", anstieg_tage)

        for i in range(1, KURSE_LEN):
            if kurse[i] > kurse[i - 1]:
                abfall_tage += 1

        print("Anzahl der Tage, an denen der Kurs gefallen ist:", abfall_tage)

i = 0

max_anstieg_tag = 0
max_anstieg = 0

while i < (KURS_LEN - 1):
    aktuelle_kurs = kurse[i]
    naechste_kurs = kurse[i + 1]
    aktuelle_ansteig = naechste_kurs - aktuelle_kurs
    if aktuelle_ansteig > max_anstiegs_tag:
        max_anstieg = aktuelle_ansteig
        max_anstiegs_tag = i + 1
    i += 1

    print("Max. Anstiegstag:", max_anstiegs_tag)

    monats_anstieg = kurse[-1] - kurse[0]
    print("Monatsanstieg:", monats_anstieg)