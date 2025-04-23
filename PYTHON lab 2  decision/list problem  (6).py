#Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. If student secures <= 39 marks in any subject, consider him as fail. Also assigned a subject wise grade based on the following table:
#Marks Range Grade

#Absent NA
#0 – 39 F
#40 – 44 P
#45 – 49 C
#50 – 54 B
#55 – 59 B+
#60 – 69 A
#70 – 79 A+
#80 – 100 O

sub1=int(input("Enter the marks of first subject:"))
sub2=int(input("Enter the marks of second subject:"))
sub3=int(input("Enter the marks of third subject:"))

print("marks of first subject:",sub1)
print("marks of second subject:",sub2)
print("marks of third subject:",sub3)

print("Total:",sub1+sub2+sub3)
print("Avarage:",(sub1+sub2+sub3)/3)

if(sub1<=39):
    print("sub1->Fail")
    print("sub1->Grade:F")
elif(sub1<=44 & sub1>=40):
    print("sub1->Pass")
    print("sub1->Grade:P")
elif(sub1<=49 & sub1>=45):
    print("sub1->Pass")
    print("sub1->Grade:C")
elif(sub1<=54& sub1>=50):
    print("sub1->Pass")
    print("sub1->Grade:B")
elif(sub1<=59 & sub1>=55):
    print("sub1->Pass")
    print("sub1->Grade:B+")
elif(sub1<=60 & sub1>=69):
    print("sub1->Pass")
    print("sub1->Grade:A")
elif(sub1<=79 & sub1>=70):
    print("sub1->Pass")
    print("sub1->Grade:A+")
elif(sub1<=100 & sub1>=80):
    print("sub1->Pass")
    print("sub1->Grade:O")
else:
    print("sub1->Absent")
    print("sub1->Grade:NA")

if(sub2<=39):
    print("sub2->Fail")
    print("sub2->Grade:F")
elif(sub1<=44 & sub1>=40):
    print("sub2->Pass")
    print("sub2->Grade:P")
elif(sub1<=49 & sub1>=45):
    print("sub2->Pass")
    print("sub2->Grade:C")
elif(sub1<=54& sub1>=50):
    print("sub2->Pass")
    print("sub2->Grade:B")
elif(sub1<=59 & sub1>=55):
    print("sub2->Pass")
    print("sub2->Grade:B+")
elif(sub1<=60 & sub1>=69):
    print("sub2->Pass")
    print("sub2->Grade:A")
elif(sub1<=79 & sub1>=70):
    print("sub2->Pass")
    print("sub2->Grade:A+")
elif(sub1<=100 & sub1>=80):
    print("sub2->Pass")
    print("sub2->Grade:O")
else:
    print("sub2->Absent")
    print("sub2->Grade:NA")

if(sub3<=39):
    print("sub3->Fail")
    print("sub3->Grade:F")
elif(sub1<=44 & sub1>=40):
    print("sub3->Pass")
    print("sub3->Grade:P")
elif(sub1<=49 & sub1>=45):
    print("sub3->Pass")
    print("sub3->Grade:C")
elif(sub1<=54& sub1>=50):
    print("sub3->Pass")
    print("sub3->Grade:B")
elif(sub1<=59 & sub1>=55):
    print("sub3->Pass")
    print("sub3->Grade:B+")
elif(sub1<=60 & sub1>=69):
    print("sub3->Pass")
    print("sub3->Grade:A")
elif(sub1<=79 & sub1>=70):
    print("sub3->Pass")
    print("sub3->Grade:A+")
elif(sub1<=100 & sub1>=80):
    print("sub3->Pass")
    print("sub3->Grade:O")
else:
    print("sub3->Absent")
    print("sub3->Grade:NA")
