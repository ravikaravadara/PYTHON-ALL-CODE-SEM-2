#Accept a year value from the user. Check whether it is a leap year or not.

year=int(input("Enter any year : "))
if(year%4==0 & year%100==0 & year%400==0):
    print("Given year is leap year");
else:
    print("Given year not leap year");

