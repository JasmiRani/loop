#39.Write a Python program to guess a number between 1 to 9
i=1
a=int(input("enter number"))
while i<=9:
    if i==a:
        print("guess number is between 1 to 9")
        break
    i=i+1
else:
    print("guess number is not between 1 to 9")
