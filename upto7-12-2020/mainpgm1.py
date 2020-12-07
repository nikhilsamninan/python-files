password=8890
access=False
p= int(input("Enter The Password"))
if p==password:
    print("Enter to the Room")
    access=True
elif p>8885 and p<8895:
    print("Reset password\n" "Contact Admin")
else:
    print("Alert")
if access==True:
    print("Access Granted")
else:
    print("Access Denied")  