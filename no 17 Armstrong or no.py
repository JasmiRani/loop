#Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is
# equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.).
a=int(input("enter number:"))
arms=a
sum=0
while a>0:
    sum=sum+(a%10)**3
    a=a//10
if arms==sum:
    print("armstrong number")
else:
    print("not")
