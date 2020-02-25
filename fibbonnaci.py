num = int(input('Enter the number : '))
a=0
z=1
x=0
print( a ,"\n", z )
for i in range(num-2):
    x = a + z
    a = z
    z = x
    print(x)