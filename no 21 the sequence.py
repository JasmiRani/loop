#21. Write a python program to sum the sequence:
#1 + 1/1! + 1/2! + 1/3! + …….. + 1/n!
i=0
b=1
sum=1
a=int(input("enter number:-"))
while i<=a:
    sum=sum+i
    i=i+1
    print(b,"+",b,"/",i,"!","+",end="")
print(sum)
