class student():
    def __init__(self,x,y,z):
        self.id = x
        self.name = y
        self.age = z
    def getdetails(self):
        print(self.id,self.name,self.age)
    def change_value(self,y):
        self.name = y
    # def check_att(self)

e1 = student(1,'sara',10)
e2 = student(2,'Jose',20)
e1.getdetails()
e2.getdetails()
e2.change_value('cris')
e2.getdetails()
print(hasattr(e2, 'place'))
if hasattr(e2, 'place')!= True:
    setattr(e2,'place','haripad')
    print(getattr(e2,'place'))
    















# class Student:  
#     def __init__(self, name, id, age):  
#         self.name = name  
#         self.id = id  
#         self.age = age  
  
#     # creates the object of the class Student  
# s = Student("John", 101, 22)  
  
# # prints the attribute name of the object s  
# print(getattr(s, 'name'))  
  
# # reset the value of attribute age to 23  
# setattr(s, "age", 23)  
  
# # prints the modified value of age  
# print(getattr(s, 'age'))  
  
# # prints true if the student contains the attribute with name id  
  
# print(hasattr(s, 'id'))  
# # deletes the attribute age  
# delattr(s, 'age')  
  
# # this will give an error since the attribute age has been deleted  
# print(s.age)  