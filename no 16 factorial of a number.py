#.Write a program to print the factorial of a number accepted by the user.
i=0
a=int(input("enter number:"))
factorial=1
while a>i:
    factorial=factorial*a
    a=a-1
print("factortorial number is:",factorial)
