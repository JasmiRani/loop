#15. Write a program to print the Fibonacci series till n terms (Accept n from user)
i=1
a=0
b=1
c=0
print(a,b,end=",")
while i<=10:
    c=a+b
    a=b
    b=c
    print(c,end=",")
    i=i+1
