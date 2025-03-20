obstsorten = []

obstsorten.append("Kiwi")

obstsorten[1] = "mango"

obstsorten.pop

if "Banane" in obstsorten:
    obstsorten.remove("Banane")

obstsorten.reverse()

print(len(obstsorten))

obstsorten2 = obstsorten.copy()

print(obstsorten, obstsorten2, id(obstsorten), id(obstsorten2))

