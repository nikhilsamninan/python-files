def number(a,b):
    if(a%2==0 and b%2==0):
        print(min(a,b))
        # if(a>b):
        #     print (b)
        # else:
        #     print (a)     
    elif(a%2!=0 and b%2!=0):
        print(max(a,b))
        # if(a>b):
        #     print (a)
        # else:
        #     print (b)
    else:
        print(max(a,b))
        # if(a>b):
        #     print (a)
        # else:
        #     print (b)


a = int(input("Enter the 1st number"))
b = int(input("Enter the 2nd number"))
number(a,b)
