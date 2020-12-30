k = open("listfile1.txt",'w+')
n=int(input("Enter the phone number"))
dict_value = {'Name':'Nikhil','Roll.no':28}
dict_value["phone_number"]=n
k.write(str(dict_value))
k.seek(0)
s = k.read()
print(type(s))
p=(eval(s))
print(p)
# p = eval(s)
# print(type(p))
k.close()
