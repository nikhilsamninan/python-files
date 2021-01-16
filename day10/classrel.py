# class Point:
#     r = 'red' #here constant variable set as red for r then used in prgm
#     def __init__(self,x,y):# here __init__ is magic method to call the value as set attributes
#         self.x = x
#         self.y = y  
#     def draw(self): #self to access the parameter
#         print(f"the parameter are {self.x} and {self.y}")


# p1 = Point(1,2) #here the point parameter is passed to the class and here object is defined
# p2 = Point(3,4)
# p1.draw() #here call the function(method) from the classs # self to be to call
# p2.draw()
# print(p1.r) # here point as red be called that red r is fixed in above function call
# print(isinstance(p1,Point)) #to check the instances as p1 in the point classs
# p1.z=10
# print(p1.z) #here dinamically assign the variable
# Point.r = "yelow"
# print(p1.r) # as to change the constant assigned value here red changes to yellow


# #class mths v intce mthds
# Point = Point(0,0)

# class Point:
#     default_color ="red"  here red is class variables

#     def __init__(self,x,y):# here __init__ is magic method to call the value as set attributes
#         self.x = x    #instant method
#         self.y = y    #here x and y are instant variables
#         pass

#     @classmethod       #class method
#     def Zero(cls):
#         return cls(0,0)
#     @staticmethod
#     def sum(a,b):
#         return a+b    #here static method defined


# p3 = Point.Zero()
# print(p3.x) #here the class method is defined then that is called in this case

    

# p5 = Point(5,6)
# k=p5.sum(4,6)
# print(k)
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y 
# p7 = Point(1,2)
# p8 = Point(1,2)
# print(p7==p8) #here false apperad


# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y 
#     def __eq__(self,x):
#         return self.x==x.x and self.y==x.y
# p7 = Point(1,2)
# p8 = Point(1,2)
# print(p7==p8) #here true appered as we define the eq(another magic method) function


# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y 
#     def __eq__(self,x):
#         return self.x==x.x and self.y==x.y
# p7 = Point(1,2)
# p8 = Point(1,2)
# p9 = p7+p8
# print(p9) # here add doesnot work so apply another magic method

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y 
#     def __eq__(self,x):
#         return self.x==x.x and self.y==x.y
#     def __add__(self,other):
#         return Point(self.x+other.x,self.y+other.y)
# p7 = Point(1,2)
# p8 = Point(1,2)
# p9 = p7+p8
# print(p9.y) # here call as .xor y as to get the value



#--------inheritence------------

# class Animal:
#     def eat(self):
#         print("eat")
# class Mammal(Animal):
#     def walk(self):
#         print("walk")
# class Fish(Animal):
#     def swim(self):
#         print("swim")

# f1=Fish()  #here inherit from one class to another as Animal is parent class and its eat is used by all other classs
# f1.eat()



# class Animal:
#     def __init__(self):
#         self.age=1
#     def eat(self):
#         print("eat")
# class Mammal(Animal):
#     def walk(self):
#         print("walk")
# class Fish(Animal):
#     def __init__(self):
#         # self.age = 2
#         self.weight=5
#     def swim(self):
#         print("swim")

# f1=Fish()  
# f1.eat()
# print(f1.age)  #here method and attribute can inherit
# print(f1.age)

# print(issubclass(Mammal,Animal)) # here sub class be checked by issubclass then print true
# print(issubclass(Animal,Mammal)) # here sub class be checked by issubclass then print false
# print(issubclass(Mammal,object)) # here is true as the all class is under object class


# class Animal:
#     def __init__(self):
#         self.age=1
#     def eat(self):
#         print("eat")
# class Mammal(Animal):
#     def walk(self):
#         print("walk")
# class Fish(Animal):
#     def __init__(self): # here to access the __init class of the parent class
#         super().__init__()  #multi level inheritence
#         self.weight=5   
#     def swim(self):
#         print("swim")
# f1=Fish()
# print(f1.age)
# print(f1.weight)

#note: it first check the first ancestor class

#-------------------------------#

# first call left side parent
#method resolution order
# c(a,b) a constructor be called



