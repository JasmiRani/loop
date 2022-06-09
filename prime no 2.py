#.Write a program to check whether a number is prime or not.
a=int(input("enter number:- "))
count=0
b=1
while b<=a:
    if a%b==0:
        count=count+1
   0x b=b+1
if count==2:
    print("prime number")
else:
    print("no prime number")
