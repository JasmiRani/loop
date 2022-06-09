#32. Write a program to find the sum of following series:
#S = 1 + 4 – 9 + 16 – 25 + 36 – … … n terms
i=2
b=1
=0
a=int(input("enter number:-"))
print(b,end=",")
while i<=a:
    if i%2==0:
        b=i**2
        print("+",b,end=",")
    else:
        print("-",i**2,end=",")
    i=i+1
