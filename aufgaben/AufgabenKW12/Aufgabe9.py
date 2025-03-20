temp = [15, 18, 20, 22, 17, 19, 21]

gesamt = 0
for i in range(0, len(temp)):
    gesamt += temp[i]

durchschnitt = gesamt / len(temp)

print(durchschnitt)


print(max(temp), min(temp))

for i in range(0, len(temp)):
    if temp[i] < 18:
        temp[i] = 18

print(temp)

last = temp[len(temp)-1]
first = temp[0]

temp[0] = last
temp[len(temp)-1] = first

print(temp)