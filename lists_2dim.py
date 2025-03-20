array2d = [
    [1,5,23,6,7,9],
    [3,6,0,1,3,4],
    [1,6,78,0,0,2]
]

array2d_elem_2 = array2d[0][2]

print(array2d_elem_2)

print("############################################")

for array in array2d:
    for element in array:
        print(element, end=' ')
    print()

print("############################################")

for i in range(len(array2d)):
    for j in range(len(array2d[i])):
        print(array2d[i][j], end=' ')
    print()