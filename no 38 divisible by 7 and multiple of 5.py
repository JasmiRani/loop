#38.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and
#2700 (both included).
i=1500
a=2700
while i<=a:
    if i%5==0 and i%7==0:
        print(i,"divisible by 5 and 7")
    else:
        print("not divisible by 5 and 7")
    i=i+1
        
