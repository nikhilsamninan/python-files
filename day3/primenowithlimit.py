a= int(input("Enter the lower limit"))
b= int(input("Enter the High limit"))
print("The Prime Numbers b/w",a,"&",b,"are")
for p in range(a,b):
    i=2
    for x in range(i,p):
        if(p%x==0):  
            break
        else:
            i+=1
    else:
        
        print(p)