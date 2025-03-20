array2d = [ # 2 Dimensionales-Array
    [1,5,23,6,7,9],
    [3,6,0,1,3,4],
    [1,6,78,0,0,2]
]

array2d_elem_2 = array2d[0][2]  # 23

print(array2d_elem_2) # 23

for array in array2d: # geht durch die zeilen
    #print (array)
    for element in array: # geht durch die elemente
        print (element, end=" ") # gibt die elemente aus
    print () # gibt eine neue zeile aus


print("#################")

#for i in range (len(array2d)):
#    for j in range (len(array2d[i])):
#        print (array2d[i][j], end=" ")
#    print ()

for i in range (len(array2d)): # geht durch die zeilen
    arr1 = array2d[i] # speichert die zeile in arr1
    for j in range (len(arr1)): # geht durch die spalten
        print (arr1[j], end=" ") # gibt die elemente der zeile aus
    print ()

print("#################")

