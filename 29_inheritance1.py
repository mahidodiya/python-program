class mymath:
    def getpi(self):
        return 3.14
    def getsquare(self,num):
        square=num*num
        return square
    
class circle(mymath):
    def __init__(self,radius):
        self.radius=radius
    def getarea(self):
        pi=super().getpi()
        square=super().getsquare(self.radius)
        area=pi*square
        return area

class ciylnder(mymath):
    def __init__(self,radius,height):
         self.radius = radius 
         self.height = height 
    def getLateralSurface(self): 
        temp = 2 * super().getpi() * self.radius * self.height
        return temp 
r=int(input("Enter radius:")) 
h=int(input("Enter height:"))   
c1=ciylnder(r,h)
area1=c1.getLateralSurface()
print("cylinder surface area = ",area1)

r=int(input("Enter radius:"))
c2=circle(r)
area2=c2.getarea()
print("circle area = ",area2)

