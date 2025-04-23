#Given the length and breadth of a rectangle, write a program to find whether the are of the rectangle is greater than its perimeter

l=int(input("Enter Lenght of rectangle : "))
b=int(input("Enter breadth of rectangle : "))
area=l*b
perimeter=2*(l+b)
if(area>perimeter):
    print("Area of rectangle Greater than it's perimeter")
else:
    print("Area of rectangle greater than it's perimeter")
