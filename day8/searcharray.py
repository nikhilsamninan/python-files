a = [1,2,3,4,5,6]
n = int(input("Enter the search item"))
for i in a:
    
    if(i==n):
        print(n," is in list")
        break
else:
    print("Not in list")    

# print(n in a)
