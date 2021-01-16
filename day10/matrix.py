r = int(input("Enter the no of rows"))
c = int(input("Enter the no of columns"))

matrix=[]
print("Enter the enteries")

for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)

# matrix = [[1,2,3],[2,3,4]]

for i in  matrix:
    for j in i:
        print(j,end=" ")
    print()
        
        



