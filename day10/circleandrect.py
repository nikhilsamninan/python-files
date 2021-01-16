class Area:
    def area(self,l = None,b = None):
        if l!=None and b!=None:
            print("Area of rect",l * b)
        elif l!=None:
            print("Area of circle",3.14 * l ** 2)    
a = Area()
a.area(4,5)
a.area(4)



