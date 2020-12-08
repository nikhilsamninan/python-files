n=int(input("Enter a number"))
sum=0
p=n
while n>0:
    b=n%10
    sum=sum+b**3
    n=n//10
if sum==p:
    print("It is an Amstrong Number")
else:
    print("It is Not an Amstrong Number")
