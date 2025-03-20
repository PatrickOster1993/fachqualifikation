import random

numbers = []
for _ in range(4):
    inner_numbers = []
    for _ in range(4):
        inner_numbers.append(random.randint(1, 9))
    numbers.append(inner_numbers)

# Alternative: matrix = [[random.randint(1, 9) for _ in range(4)] for _ in range(4)]

print("-----------")
for i in range(4):
    print("|", end=" ")
    for j in range(4):
        print(numbers[i][j], end=" ")
    print("|", end=" ")
    print()
print("-----------")

sum = 0
for i in range(len(numbers)):
    for number in numbers[i]:
        sum += number

print(f"Sum of all numbers: {sum}")

biggest_number = numbers[0][0]
for i in range(len(numbers)):
    for number in numbers[i]:
        if number > biggest_number:
            biggest_number = number

print(biggest_number)