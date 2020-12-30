l={"Tuna Salad": 450,"Mixed Fried rice": 120,"briyani": 9}
item = input("Enter the item : ")
if(item in l):

    print("item in list")
    delivery = int(input("overnight delivery 0=no,1=yes"))
    if(delivery == 1):
        s = l[item]
        if(s<10):
            shipping = 2 + 5
            total = s + shipping  
        elif(s>10):
            shipping = 3 + 5
            total = s + shipping  
            
    else:
        s = l[item]
        if(s<10):
            shipping = 2 
            total = s + shipping
        elif(s>10):
            shipping = 3 
            total = s + shipping
    print("invoice")
    print("item price: ",s)
    print("Shipping Charge: ",shipping)
    print("Total:",total)

else:
    print("item not in list")    
    

    


















# if(item in l):
#     s = l[item]
#     if(s<10):
#         total = s + 2
#         print("item price",total) 
#         delivery = int(input("overnight delivery 0=no,1=yes"))
#         if(delivery == 1):
#             total = total + 5
#             print("invoice")
#             print(s)
#             print(total)   
#         else:
#             print("Overnight delivery charge avoided")
#     elif(s>10):
#         total = s + 3
#         print(total) 
#         delivery = int(input("overnight delivery 0=no,1=yes"))
#         if(delivery == 1):
#             total = total + 5
#             print("invoice")

        #     print(total)   
        # else:
        #     print("Overnight delivery charge avoided")
            
    