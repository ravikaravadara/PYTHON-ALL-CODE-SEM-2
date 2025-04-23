#Print largest and smallest values out of three

a=input("Enter value of a : ")
b=input("Enter value of b : ")
c=input("Enter value of c : ")
if(a>b):
    if(a>c):
        print("Largest number is : ", a)
    else:
        print("Largest number is : ", c)
else:
    if(b>c):
        print("Largest number is : ", b)
    else:
        print("Largest number is : ", c)

if(a>b):
    if(b>c):
        print("Smallest number is : ", c)
    else:
        print("Smallest number is : ", b)
else:
    if(a>c):
        print("Smallest number is : ", c)
    else:
        print("Smallest number is : ", a)
       
