n=int(input("How many numbers"))
i=0
sum=0
while(i<n):
    a=(input("enter the number"))
    if(a=="q"):
        break
    else:
        sum=sum+int(a)
        i=i+1
avg=sum/i
print(avg)         

    
    
    
   

