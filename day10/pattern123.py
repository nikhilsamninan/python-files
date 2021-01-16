a=int(input("enter the row"))

s=1
for i in range(1,a):
    for j in range(1,i+1):
        print(s,end="")
    s=s+1 
    print(" ")

   