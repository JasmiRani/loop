#.Write a program to find the product of the digits of a number accepted from the user.
a=int(input("enter number: "))
product=1
while a>0:
    product=product*(a%10)
    a=a//10
print(product)
