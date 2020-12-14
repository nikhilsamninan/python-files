num=int(input("enter the number"))
i=2
flag=0
while(i<num/2):
    if(num%i==0):
        flag= 1
        break
    else:
        i+=1
if(flag==0):
    print("It is a prime number")  
else:
    print("It is not a prime number")




    