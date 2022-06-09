#.Write a program to display all even numbers that fall between two numbers (exclusive both numbers)
#.entered by the user
c=int(input("enter first number: "))
a=int(input("enter second number: "))
while c<a:
    if c%2==0:
        print(c)
    c=c+1
