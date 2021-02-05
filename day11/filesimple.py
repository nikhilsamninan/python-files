k = open("simplefile.txt",'r+')
for i in range(5):
    print(k.readline())

k.close()
