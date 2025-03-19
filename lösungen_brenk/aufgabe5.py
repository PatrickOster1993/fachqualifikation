number = int(input("Enter a number: "))

if number < 0:
    print("The number is negative.")
elif number == 0:
    print("The number is zero.")
elif number > 0 and number % 2 == 0:
    print("The number is positive and even.")
else:
    if number > 100:
        print("The number is positive and odd and greater than 100.")
    else:
        print("The number is positive and odd.")