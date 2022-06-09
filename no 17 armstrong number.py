#17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is
#equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)
a=input("enter number:-")
i=0
sum=0
while i<len(a):
    b=a[i]
    c=(int(b)**3)
    sum=c+sum
    i=i+1
if int(a)==sum:
    print("its armstrong number")
else:
    print("its not arm stron number")
