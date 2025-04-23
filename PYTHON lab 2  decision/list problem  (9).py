#Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.

ang1=int(input("Enter Angle 1 : "))
ang2=int(input("Enter Angle 2 : "))
ang3=int(input("Enter Angle 3 : "))
sum= ang1 + ang2 + ang3
if(sum==180):
    print("Traingle is valid ")
else:
    print("Traingle is not valid")
