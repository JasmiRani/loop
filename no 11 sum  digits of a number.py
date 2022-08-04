#.Write a program to find the sum of the digits of a number accepted from the user.
a=int(input("enter number: "))
i=0
sum=0
while i<len(a):
    sum=sum+int(a[i])
    i=i+1
print("sum of num is",sum)
