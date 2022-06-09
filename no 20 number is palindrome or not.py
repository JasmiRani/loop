#20. Write a program to check whether a number is palindrome or not.
a=int(input("enter number:-"))
i=a
b=0
while a>0:
    b=(b*10)+a%10
    a=a//10
if i==b:
    print("number is palindrome")
else:
    print("number is not palindrome")

