for i in range(1,151):
    if((i%3==0) & (i%5==0)):
        print("Fuzz+Buzz")
    elif(i%3==0):
        print("Fuzz")
    elif(i%5==0):
        print("Buzz")    
    elif((i%3==0) & (i%5==0)):
        print("Fuzz+Buzz")
    else:
        print(i)