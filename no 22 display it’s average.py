#22. Write a program to accept 10 numbers from the user and display it’s average
i=1
sum=0
while i<=10:
    a=int(input("enter number"))
    sum=sum+a
    i=i+1
average=sum//10
print(average)
