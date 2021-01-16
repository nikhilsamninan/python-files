a = {1,2,3,10,4}
# print("maximum",max(a))
# print("minimum",min(a))
s = 0
for i in a:
    if i>s:
        s = i
print("max :",s)
for i in a:
    if i<s:
        s = i     
print("min :",s)   
