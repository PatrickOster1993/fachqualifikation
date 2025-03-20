############Aufgabe 7############

for x in range (1, 101):
    if x%3 == 0 and x%5 == 0:
        print ("fizzbuzz")
    elif x%3 == 0:
        print ("fizz")
    elif x%5 == 0:
        print ("buzz")
    else:
        print (x)
        

#schöner mit KI
# for x in range (101):
#     print (f"{'fizz' if x%3 == 0 else ''}{'buzz' if x%5 == 0 else ''}" or x)

# #oder 
# for x in range (101):
#     print ("fizz"*(x%3==0) + "buzz"*(x%5==0) or x)

############Aufgabe 8############

mylist = ["apfel", "birne", "kirsche", "banane", "pflaume"]

mylist.append("kiwi")
print (mylist)

mylist.insert(2, "mango")
print (mylist)

mylist.pop()
print (mylist)

if "banane" in mylist:
    mylist.remove("banane")
    print (mylist)


mylist.reverse()
print (mylist)


print (len(mylist))

mylist2 = mylist.copy()
print (f"liste1: {mylist} id: {id(mylist)} and liste2: {mylist2} id: {id(mylist2)}")

############Aufgabe 9############

temp = [15, 18, 20, 22, 17, 19, 21]

print (f"durchschnitt: {sum(temp)/len(temp):.2f}")

print (f"max: {max(temp)} min: {min(temp)}")


temp = [15, 18, 20, 22, 17, 19, 21]
for i in range (len(temp)):
    if temp[i] < 18:
        temp[i] = 18
print (temp)

k= temp[0]
temp[0] = temp[-1]
temp[-1] = k
print (temp)

############Aufgabe 10############
import random

aktien = random.sample(range(75, 150), 20)
print (aktien)

print (f"durchschnitt: {sum(aktien)/len(aktien):.2f}")
print (f"max: {max(aktien)} min: {min(aktien)}")

tage_gestiegen = 0
tage_gesunken = 0

for i in range (1, len(aktien)):
    if aktien[i] > aktien[i-1]:
        tage_gestiegen += 1
print (f"tage gestiegen: {tage_gestiegen}")

for i in range (1, len(aktien)):
    if aktien[i] < aktien[i-1]:
        tage_gesunken += 1
print (f"tage gesunken: {tage_gesunken}")

höchster_tag = 0
anstieg = 0
höchster_anstieg = 0  

for i in range (1, len(aktien)):
    if aktien[i] > aktien[i-1]:
        anstieg = aktien[i] - (aktien[i-1])
        if anstieg > höchster_anstieg:
            höchster_anstieg = anstieg
            höchster_tag = i+1

print (f"höchster tag: {höchster_tag} anstieg: {höchster_anstieg}")

gesamter_anstieg = 0

for i in range (1, len(aktien)):
    if aktien[i] > aktien[i-1]:
        anstieg = aktien[i] - (aktien[i-1])
        gesamter_anstieg += anstieg
print (f"gesamter anstieg: {gesamter_anstieg}")