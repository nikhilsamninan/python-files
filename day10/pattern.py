

row = 6

for i in range(row):
    for j in range(row - i):
        print("*", end=" ")
    for k in range(i):
        print(" ", end=" ")
    print("\n")

# rows = 6   
# for row in range(1, rows):

#     num = 1

#     for j in range(rows, 0, -1):

#         if j > row:

#             print("*", end=" ")

#         else:

#             print(" ", end=" ")

#             num += 1

#     print("")


# a=int(input("enter the row"))

# rows = 5

# for i in range(6):
#     for j in range(6):
#         if j > i:
#             print(" ",end="")
#         else:
#             print("*",end="  ")

#     print("", "\n")

# i = 6
# while i > 0:
#     print(" " * i)
