num=int(input("enter the number"))
i=2
for x in range(i,num):
    if(num%x==0):
        print("It is not a prime")    
        break
    else:
        i+=1
else:
    print("It  is a prime number")

             

