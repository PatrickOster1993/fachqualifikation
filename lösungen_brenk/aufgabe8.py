fruits = ["apple", "banana", "pineapple", "cherry", "grapefruit"]
print(fruits)
fruits.append("kiwi")
print(fruits)
fruits[1] = "mango"
print(fruits)
fruits.pop()
print(fruits)
try:
    fruits.remove("banana")
    print(fruits)
except:
    print("There's no banana in the list.")
fruits.reverse()
print(fruits)
print(len(fruits))
fruits2 = fruits.copy()
print(f"{fruits} + {id(fruits)}")
print(f"{fruits2} + {id(fruits2)}")
