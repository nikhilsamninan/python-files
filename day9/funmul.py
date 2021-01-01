# def multipication(a,b):
#     s = a * b
#     return(s)
# def add(d,f):
    
#     s = a + b
#     return(s)

# a = int(input("enter the 1st value"))
# b = int(input("enter the 2nd value"))
# p = add(a,b)
# q = multipication(a,b)
# print (p)
# print (q)

def mul(*num):
    # p = int(num)
    s = 1
    for i in num:
        s = s * i
    return (s)
   

k = mul(3,4,5)     
print(k)    