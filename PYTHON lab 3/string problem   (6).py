#check whether a given number is prime, perfect, armstrong, palindrome, automorphic.

n=int(input("Enter a number to check : "))
for i in range(2, n):
    if(n%i==0):
        print("Not Prime")
        break
else:
    print("Prime")

for i in range(1, n):
    if(i*i==n):
        print("Perfect")
else:
    print("Not Prime")
    

