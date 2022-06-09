#26. Write a program to print the following series till n terms.
#2 , 22 , 222 , 2222 _ _ _ _ _ n terms
a=int(input("enter number"))
i=1
b=2
while i<=a:
    print(str(b)*i,end=",")
    i=i+1
    
