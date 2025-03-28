arr2 = [
    [1, 5, 23, 6, 7, 9],
    [3, 6, 0, 1, 2, 3, 4],
    [1, 6, 78, 0, 0, 2]
]

 
arr2_elem_23 = arr2[0][2]  
arr1 = arr2[0]  


print(arr1)
print(arr2_elem_23)


for array in arr2:

      for elem in array:
print(element, end=' ')
print()

print("#############################")

for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        print(arr2[i][j], end=' ')
        print()

print("#############################")
         
for i in range(len(arr2)):
 for j in range(len(arr2[i])):
         if arr2[i][j] == 0:
                arr2[i][j] = 1
else:
                arr2[i][j] = 0
print(arr2[i][j], end=' ')
