# for i in range(10):
#     print (i+1)

# x = int(input(f"Zahl: "))
# for i in range (10):
#     y = x * (i+1) 
#     print (y)

# summe = 0
# x = int(input(f"Zahl: "))
# for i in range (x):
#     i+=1
#     q = i*i
#     summe += q 
#     print (q,summe)

# i=0
# while i < 10:
#     i+=1
#     print(i)

# i=0
# s=0
# while i < 10:
#     i+=1
#     if i<=5:
#         s+=i
#     print(i, s)

# i=0
# m=0
# while m<50:
#     i+=1
#     m= i*2
#     print (m)

# x=0
# s=0 
# i=1
# z=0
# while x >= 0:
#     x = int(input("gib eine Zahl ein:"))
#     s += x
#     z = s/i
#     i+=1 
#     print (z)

# i=0
# x=0
# p= "passwort123"
# while True:
#     x=str(input("gib Passwort ein:"))
#     if x == p:
#         print("richtig")
#         break
#     else:
#         print ("falsch")
#         i+=1
#     if i>=3:
#         print("verkackt")
#         break

# i=0
# z=10
# x = int(input("gib eine positive Zahl ein:"))

# if x>0:
#     while True:
#         i+=1
#         if x < z:
#             print (i)
#             break
#         if z <= x:
#             z= z*10
# else:
#     print("falsche eingabe") 
       

# ar= [0,1,2,3,4]
# s=0
# for i in ar:
#     s+= ar[i]
# print (s)


#Falsch
# ar= ["Max","Berta","Dieter"]
# z=0
# i=0
# x=ar[0]
# while True:
#     i-=1
#     print (ar[i])
#     if ar[i] == x:
#         break

# ar= ["alpha", "beta", "gamma"]
# length= 0
# for i in ar:
#     length+=1 
# print (length)

# i=length
# for length in ar:
#     i-=1
#     print (ar[i])

# ar=[1.2 ,2,3,4,5]
# length= 0
# for i in ar:
#     length+=1 
# print (length)

# i=0
# s=0
# for length in ar:
    
#     s+=ar[i]
#     i+=1
# print (s/length)

# import random

# ar=[]
# length=6
# i=0
# while i < length:
#     ar.append(random.randint(10,50))
#     i+=1

# print (ar)

# x=0
# for i in range(len(ar)):
#     if x < ar[i]:
#         x= ar[i]
    
# print (x)


ar= [50,20,10,15,30,25]

x=len(ar)
for i in range (len(ar)):
    for j in range(1,x):
        if ar[j]<ar[j-1]:
            ar[j], ar[j-1] = ar[j-1], ar[j]
            print (ar)
    x-=1
print (ar)

