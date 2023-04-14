def isRectangle(a, b, c, d):
    if (a == b and d == c) or (a == c and b == d) or (a == d and b == c):
        return True
    else:
        return False

def isTriangle(x, y, z):
    if (x + y <= z) or (x + z <= y) or (y + z <= x) :
        return True
    else:
        return False 

x, y, z = input("Enter the value for the sides of Triangle (space separated) : ").split(" ")
a, b, c, d = input("Enter the value for the sides of Rectangle (space separated) : ").split(" ")
if isTriangle(x, y, z):
    print("Valid Traingle") 
else:
    print("Invalid Triangle")

if isRectangle(a,b,c,d):
    print("Valid Rectangle") 
else:
    print("Invalid Rectangle")
