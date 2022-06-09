#19. Write a program to add first n terms of the following series using a while loop :
#1/1! + 1/2! + 1/3! + …….. + 1/n!
i=1
b=1
n=int(input("enter number:-"))
while i<=n:
    print(b,"/",i,"!","+",end=",")
    i=i+1
