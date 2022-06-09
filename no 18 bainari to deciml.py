#18. Write a program to convert binary to decimal.
binary=int(input("enyer number:-"))
i=0
d=0
while binary!=0:
    rem=binary%10
    binary=binary//10
    d=d+rem*i
    i=i*2
print("decimal number is=",d)
    
    
