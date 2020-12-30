k=open("phone_Book.txt",'a+')
name=input("Enter the Name")
roll_no=int(input("Enter the Roll No"))
ph_no=(input("Enter the phone number"))
dict_value={"name":[],"roll_no":[],"phone_number":[] }
dict_value["name"].append(name)
dict_value["roll_no"].append(roll_no)
dict_value["phone_number"].append(ph_no)

p = str(dict_value)
k.write(eval(p))

k.close()