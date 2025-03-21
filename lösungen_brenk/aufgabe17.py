products = [["Laptop", 1200], ["Smartphone", 800], ["Tablet", 500], ["Monitor", 300], ["Maus", 50]]

def bubblesort(list, direction):
    for i in range(len(list)):
        changed = False
        for j in range(len(list) - i - 1):
            if direction == "up":
                if list[j + 1][1] < list[j][1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    changed = True
            if direction == "down":
                if list[j + 1][1] > list[j][1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    changed = True
        if not changed:
            break

    print(list)

bubblesort(products, "up")
bubblesort(products, "down")

def linearsearch(list, value):
    for index in range(len(list)):
        if list[index][0] == value:
            return index
    return "Kein Index gefunden!"

index = linearsearch(products, "Hallo")
if type(index) == int: 
    print(products[index][0] + ": " + str(products[index][1]) +"€")
else:
    print(index)

def add_product(products):
    name = input("Please enter a product name.")
    price = int(input("Please enter a product price."))
    products.append([name, price])
    bubblesort(products, "down")

products = add_product(products)