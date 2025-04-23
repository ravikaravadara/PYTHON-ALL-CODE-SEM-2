#Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line.

x1=int(input("Enter x1 coordinate : "))
y1=int(input("Enter y1 coordinate : "))
x2=int(input("Enter x2 coordinate : "))
y2=int(input("Enter y2 coordinate : "))
x3=int(input("Enter x3 coordinate : "))
y3=int(input("Enter y3 coordinate : "))

slope1=(y2-y1)/(x2-x1)
slope2=(y3-y2)/(x3-x2)

if(slope1==slope2):
    print("Given Coordinates are in straight line")
else:
    print("Given Coordinates are not in straight line")
