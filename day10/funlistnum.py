# def num_list(l):
#     a = 1
#     b = 1
#     access=1
#     print(l)
#     for i in l:
#         if(a == 0):
#             if(i==0):
#                 a = 1
#                 b = 0
    
#         elif(b == 0):
#             if(i==7):
#                 access=0
#                 print("True")

#         elif(i==0):
#             a = 0
#     if(access == 1):
#         print("false")
def num_list(l):
    wan_list=[0,0,7]
    org_list=[]
    for i in l:
        if(i == 0 or i == 7):
            org_list.append(i)
    if(wan_list == org_list):
        print("true")
    else:
        print("false")
    



l=[1,2,3,7,0,0]
num_list(l)


