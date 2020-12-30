n=int(input("Enter The Number"))
while(n>0):

    if(n%5==0 and n%6==0):
        print("true")
    else:
        print("false")    
    if(n%5==0 or n%6==0):
        print("true")
    else:
        print("false")    
    if(n%5!=0 or n%6!=0):
        print("true")
    else:
        print("false")    
    break
