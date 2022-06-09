#.Write a program to find the sum of the digits of a number accepted from the user.
a=int(input("enter number: "))
sum=0
while a>0:
    sum=sum+a%10
    a=a//10
print("sum of num is",sum)
