# l=open("open.txt",'w+')
# k=l.write("hai")
# print (k)
# l.close

l = open(r"D:\phythonclassfiles\forcheck.txt",'r+')
l.write("Nikhil Sam Ninan \nHaripad")
l.seek(0)
s=l.read()
print(s)
l.close

# l = open(r"D:\phythonclassfiles\forcheck.txt",'w+')
# l.write("Nikhil Sam Ninan \nHaripad")
# l.seek(0)
# s=l.read()
# print(s)
# l.close

# l = open(r"D:\phythonclassfiles\forcheck.txt",'a+')
# l.write("Nikhil Sam Ninan \nHaripad")
# l.seek(0)
# s=l.read()
# print(s)
# l.close