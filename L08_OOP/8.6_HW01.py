# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/05-Object%20Oriented%20Programming/02-Object%20Oriented%20Programming%20Homework.ipynb

# Problem 1 計算兩座標的距離 & 斜率
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

#solution 1 to problem 1
class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
        #((x2-x1)的二次方+(y2-y1)的一次方)開根號   開根號相當於0.5次方

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

c1 = (3,2)
c2 = (8,10)

myline = Line(c1,c2)
print(myline.distance())
print(myline.slope())



#solution 2 to problem 1
class Line02:
    def __init__(self,coor1,coor2):
        self.x1,self.y1 = coor1
        self.x2,self.y2 = coor2

    def distance(self):
        return ((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**0.5
        #((x2-x1)的二次方+(y2-y1)的一次方)開根號   開根號相當於0.5次方

    def slope(self):
        return (self.y2-self.y1)/(self.x2-self.x1)

c1 = (3,2)#9.433981132056603
c2 = (8,10)#1.6

myline02 = Line02(c1,c2)
print(myline02.distance())
print(myline02.slope())





# Problem 2 計算圓柱體體積(volume)和表面面積
class Cylinder:
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * (self.radius)**2

    def surface_area(self):
        top = 3.14 * (self.radius**2)
        return (top*2) + (self.radius*2*3.14*self.height)
        #圓周長 = 直徑*3.14
        #圓面積 = 半徑*半徑*3.14
        #表面面積 上下兩個圓面積+ 長方形面積(半徑*2*3.14*height)

# EXAMPLE OUTPUT
mycylinder = Cylinder(2,3)
print(mycylinder.volume())#56.52
print(mycylinder.surface_area())#94.2