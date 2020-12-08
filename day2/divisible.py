a=int(input("Enter a Number"))
if (a%2==0):
    print(a,"Entered Number is Divisible by 2")
    if(a%5==0):
        print(a,"Entered Number is Divisible by 5")
    else:
        print(a,"Entered Number is Not Divisible by 5")
else:
    print(a,"Entered Number is Not Divisible by 2")
