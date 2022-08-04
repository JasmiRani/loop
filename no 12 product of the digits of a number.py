#.Write a program to find the product of the digits of a number accepted from the user.
a=input("enter number: ")
i=0
product=1
while i<len(a):
    product=product*int(a[i])
    i=i+1
print("product of the digits of a number is",product)
