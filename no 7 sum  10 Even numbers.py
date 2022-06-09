#.Write a program to print the sum of the first 10 Even numbers.
n=1
sum=0

while n<=10:
    if n%2==0:
        sum=sum+n
    n=n+1 
print(sum)
