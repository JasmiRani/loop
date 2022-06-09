#340.Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return
#20.
a=int(input("enter number:-"))
b=int(input("enter number:-"))
i=1
c=a+b
while i<2:
    if c>=15 and c<=20:
        print("return 20")
    else:
        print(" not return 20")
    i=i+1
    
