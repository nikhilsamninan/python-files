class employee():   
    k="hai"
    def __init__(self,x,y,z):   #default method or function
        self.name = x            #called in every class
        self.dept = y
        self.job = z
        
    def getdetails(self):
        print(self.name,self.dept,self.job)
    def addnew(self,p,q,r):
        self.name = p           
        self.dept = q 
        self.job = r
    # print(k)

    
e1 = employee('Ram','HR','TL')   #here we create objects
e2 = employee('Sam','SE','PM')
e1.getdetails()
e2.getdetails()
# del e2              #to delete the object
e2.getdetails()
e1.addnew('nikhil','SE','HR')
e1.getdetails()
print(e1.k)
# notes

# two varibles
# -> instance varible
# -> static varible(class varible)

# 3 methods
# -> instance method  as instance variable
# -> static method    as add function only no parameter is passed
# -->class method     as class variable 

