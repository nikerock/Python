x=10
y=5
z=5
if(x>y and x>z and y>z):
    print("x is greater",x)
    print("y is greater then z")
elif(x>y and x>y and z>y):
    print("x is greater",x)
    print("z is greater then y")
elif(x>y and x>z and y==z):
    print("x is greater",x)
    print("y and z are equal")
elif(y>x and y>z and x>z):
    print("y is greater",y)
    print("x is greater then z")
elif(y>x and y>z and z>x):
    print("x is greater",x)
    print("z is greater then x")
elif(y>x and y>z and x==z):
    print("x is greater",x)
    print("x and z are equal")
elif(z>x and z>y and x>y):
    print("z is greater",z)
    print("X is greater then y")
elif(z>x and z>y and y>x):
    print("x is greater",x)
    print("y is greater then x")
elif(z>x and z>y and y==x):
    print("x is greater",x)
    print("y and z are equal")
else:
    print("All are equal",x,y,z)