#Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) )

r=int(input("Enter the radius of circle:"))
x=int(input("Enter the x coordinate of center of circle:"))
y=int(input("Enter the y coordinate of center of circle:"))
x1=int(input("Enter the x coordinate of point:"))
y1=int(input("Enter the y coordinate of point:"))

result=((x1-x)**2)+((y1-y)**2)

if(result<(r**2)):
    print("Given point is in the circle")
elif(result==(r**2)):
    print("Given point is on the circle")
else:
    print("Given point is outside of the circle")
    
    
