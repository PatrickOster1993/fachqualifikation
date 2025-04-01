array= [2,8,6,5,4,1]
i=1
counter =0
while True:
    if i==6 and counter==0:
        break
    if i==6:
        i=1
        counter=0
    if array[i]<array[i-1]:
        array[i],array[i-1]=array[i-1],array[i]
        counter+=1
    i+=1
    print (i)
    print (array)
