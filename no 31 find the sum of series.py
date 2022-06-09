#31. Write a program to find the sum of following series:
#1 + 2 + 6 + 24 + 120 . . . . . n terms
i=1
b=1
sum=0
a=int(input("enter number"))
while i<=a:
    b=i*b
    sum=sum+b
    i=i+1
    print(sum,end=",")

