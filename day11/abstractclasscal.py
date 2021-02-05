from abc import ABC, abstractmethod
class Calculator(ABC):
    @abstractmethod
    def cal_fun(self,a,b):
        pass
class Addition(Calculator):
    def cal_fun(self,x,y):
        self.a = x
        self.b = y
        print(self.a + self.b)
class subtraction(Calculator):
    def cal_fun(self,x,y):
        self.a = x
        self.b = y
        print(self.a - self.b)
class division(Calculator):
    def cal_fun(self,x,y):
        self.a = x
        self.b = y
        print(self.a / self.b)
class multiplication(Calculator):
    def cal_fun(self,x,y):
        self.a = x
        self.b = y
        print(self.a * self.b)

a = int(input("Enter the 1st number"))

b = int(input("Enter the 2nd number"))
a1 = Addition()
a1.cal_fun(a,b)
b1 = subtraction()
b1.cal_fun(a,b)
c1 = division()
c1.cal_fun(a,b)
d1 = multiplication()
c1.cal_fun(a,b)