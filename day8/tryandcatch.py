# num = [1,2]
# print(num[2])
# try:
#     age = int(input("Enter your age"))
#     print(age)
# except ValueError:
#     print("You didn't input a valid age")
# else:
#     print("Hai")

# try:
#     age = int(input("Enter your age"))
#     k = 10/age
#     print(k)
# except ValueError as x:
#     print("Not valid age")
#     print(x)
#     print(type(x))   
# try:
#     age = int(input("enter your age"))
# except ValueError:
#     print("Invalid Input")
# y =  10
# print(y)

# try:
#     age = int(input("Enter your age"))
#     k = 10/age
#     print(k)
# except ZeroDivisionError as x:
#     print("Not valid age")
#     print(x)
#     print(type(x))   
# except ValueError as x:
#     print("you entered invalid data type")
#     print(x)
#     print(type(x))     

# try:
#     for i in ['a','b','c']:
#         print (i**2)
# except TypeError as x:
#     print(x)
#     print(type(x))
try:
    x = int (input())
    y = 0
    z = x/y
except ZeroDivisionError as x:
    print(x)
    print(type(x))
except ValueError as x:
    print(x)
    print(type(x))    




