import math

x1 = int(input("Enter x1:") )
y1 = int(input("Enter y1:") )
x2 = int(input("Enter x2:") )
y2 = int(input("Enter y2:") )

def distance(x1,y1,x2,y2):
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

print("the distance between(",x1,",",y1,") and (",x2,",",y2,") is",round(distance(x1,y1,x2,y2),3) )

